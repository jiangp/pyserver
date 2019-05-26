# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pbrpc.message_pb2 as message__pb2

class GrpcfuncStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GrpcDataFunc = channel.unary_unary(
        '/ecprotobuf.Grpcfunc/GrpcDataFunc',
        request_serializer=message__pb2.EcReqHeader.SerializeToString,
        response_deserializer=message__pb2.EcResHeader.FromString,
        )


class GrpcfuncServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GrpcDataFunc(self, request, context):
    """Sends a Datafunc
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GrpcfuncServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GrpcDataFunc': grpc.unary_unary_rpc_method_handler(
          servicer.GrpcDataFunc,
          request_deserializer=message__pb2.EcReqHeader.FromString,
          response_serializer=message__pb2.EcResHeader.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ecprotobuf.Grpcfunc', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))