#!/usr/bin/python
# -*- coding: UTF-8 -*-
# main.py

import grpc, time
from pbrpc.message_pb2_grpc import GrpcfuncServicer,  add_GrpcfuncServicer_to_server
from concurrent import futures
   
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'
   

class Grpcfunc(GrpcfuncServicer):
    def DoGrpcsvr(self, request,context):
       cmd =  request.cmd
       return EcResHeader(cmd= cmd, )

def server():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GrpcfuncServicer_to_server(Grpcfunc(),grpcServer)   #add_FormatDataServicer_to_server(FormatData(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
   
if '__main__' == __name__:
    server()