import sys
import datetime
import time
from concurrent import futures
import threading
import socket

import grpc

import p2p_msg_pb2
import p2p_msg_pb2_grpc

class PeerServicer(p2p_msg_pb2_grpc.PeerServicer):
    def __init__(self, username):
        self.username = username

    # this function will be called on receiving message from other peer
    def Msg(self, requestIterator, context):
        for newMsg in requestIterator:
            # print it and send response
            printMsg(newMsg)
            yield p2p_msg_pb2.Empty()

    # clients can subscribe to server's messages using this function
    def SubscribeMsg(self, request, context):
        print('User connected.')
        return listenInput(self.username)

def printMsg(msg):
    print('[' + msg.time + '] ' 
        + msg.name + ': ' + msg.text)


def listenInput(username):
    print('Starting listening user input...')
    while (True):
        msgToSend = input()
        if (len(msgToSend) == 0):
            continue
	
        timeStr = datetime.datetime.now().strftime('%H:%M:%S')

        yield p2p_msg_pb2.PeerMessage(
            name = username, 
            time = timeStr,
            text = msgToSend)

def startServer(port, username):
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=16))
        p2p_msg_pb2_grpc.add_PeerServicer_to_server(PeerServicer(username), server)
        server.add_insecure_port('[::]:' + port)
        server.start()
        print('Server started. Waiting for client to connect...')
        server.wait_for_termination()
    except:
        print('Server error occured.')

def listenServer(stub):
    try:
        rs = stub.SubscribeMsg(p2p_msg_pb2.Empty())
        for r in rs:
            printMsg(r)
    except:
        print('Error occured while listening server.')

def startSending(serverip, port, username):
    with grpc.insecure_channel(serverip + ':' + port) as channel:
        stub = p2p_msg_pb2_grpc.PeerStub(channel)
        print('Starting listening server...')
        ls = threading.Thread(target = listenServer, args = (stub,))
        ls.start()
        ers = stub.Msg(listenInput(username))       
        for r in ers:
            continue
        ls.join()

# main
if len(sys.argv) < 4:
    print('Please specify peer\'s IP, port and your name to be a client')
    print('or type \'--server\' instead of IP to be a server and a client at the same time.')
    sys.exit(0)

#print('Type \'/q\' to quit.')

isFirst = sys.argv[1] == '--server'
port = sys.argv[2]
username = sys.argv[3]

try:
    if isFirst:
        startServer(port, username)
    else:
        ip = sys.argv[1]
        startSending(ip, port, username)
except:
    print('Error occured.')
