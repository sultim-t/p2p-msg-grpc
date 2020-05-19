from __future__ import print_function

import random
import logging

import grpc

import p2p_msg_pb2
import p2p_msg_pb2_grpc


# def guide_get_one_feature(stub, point):
#     feature = stub.GetFeature(point)
#     if not feature.location:
#         print("Server returned incomplete feature")
#         return

#     if feature.name:
#         print("Feature called %s at %s" % (feature.name, feature.location))
#     else:
#         print("Found no feature at %s" % feature.location)


# def guide_get_feature(stub):
#     guide_get_one_feature(
#         stub, route_guide_pb2.Point(latitude=409146138, longitude=-746188906))
#     guide_get_one_feature(stub, route_guide_pb2.Point(latitude=0, longitude=0))


# def guide_list_features(stub):
#     rectangle = route_guide_pb2.Rectangle(
#         lo=route_guide_pb2.Point(latitude=400000000, longitude=-750000000),
#         hi=route_guide_pb2.Point(latitude=420000000, longitude=-730000000))
#     print("Looking for features between 40, -75 and 42, -73")

#     features = stub.ListFeatures(rectangle)

#     for feature in features:
#         print("Feature called %s at %s" % (feature.name, feature.location))


# def generate_route(feature_list):
#     for _ in range(0, 10):
#         random_feature = feature_list[random.randint(0, len(feature_list) - 1)]
#         print("Visiting point %s" % random_feature.location)
#         yield random_feature.location


# def guide_record_route(stub):
#     feature_list = route_guide_resources.read_route_guide_database()

#     route_iterator = generate_route(feature_list)
#     route_summary = stub.RecordRoute(route_iterator)
#     print("Finished trip with %s points " % route_summary.point_count)
#     print("Passed %s features " % route_summary.feature_count)
#     print("Travelled %s meters " % route_summary.distance)
#     print("It took %s seconds " % route_summary.elapsed_time)


def make_message(name, time, text):
    return p2p_msg_pb2.PeerMessage(name=name, time=time, text=text)


def generate_messages():
    messages = [
        make_message("Sender", 0, "Text1"),
        make_message("Sender", 1, "Text2"),
        make_message("Sender", 2, "Text3"),
    ]
    for msg in messages:
        print("Sending %s" % (msg.text))
        yield msg


def send(stub):
    stub.Send(generate_messages())


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = p2p_msg_pb2_grpc.PeerStub(channel)
        send(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
