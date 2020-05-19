from concurrent import futures
import time
import math
import logging

import grpc

import p2p_msg_pb2
import p2p_msg_pb2_grpc

class CustomPeerServicer(p2p_msg_pb2_grpc.PeerServicer):

    def Send(self, request_iterator, context):
        for new_msg in request_iterator:
            print("[time: %d, from: %s]: %s" % (new_msg.time, new_msg.name, new_msg.text))
            yield new_msg


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    p2p_msg_pb2_grpc.add_PeerServicer_to_server(CustomPeerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
