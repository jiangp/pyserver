1. 定义gRPC接口，编辑message.proto文件

   ```c++
   syntax = "proto3"; //声明使用proto3语法
   
   //package ecchatting;
   
   service FormatData {
     rpc DoFormat(Data) returns (Data){}
   }
   message Data {
     int32 conversation_id = 1;
     string message = 2;
   }
   ```

2. 编译protobuf

   python -m grpc_tools.protoc --proto_path=.  --python_out=. --grpc_python_out=. message.proto

   会生成message_pb2_grpc.py和message_pb2.py两个文件

3. 实现server端

   ```python
   import grpc, time
   import message_pb2_grpc, message_pb2
   from concurrent import futures
   
   _ONE_DAY_IN_SECONDS = 60 * 60 * 24
   _HOST = 'localhost'
   _PORT = '8080'
   
   class FormatData(message_pb2_grpc.FormatDataServicer):
       def DoFormat(self, request, context):
           m_id = request.conversation_id
           question = request.message
           return message_pb2.Data(conversation_id=m_id, message=question)
       
   def server():
       grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
       message_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
       grpcServer.add_insecure_port(_HOST + ':' + _PORT)
       grpcServer.start()
       try:
           while True:
               time.sleep(_ONE_DAY_IN_SECONDS)
       except KeyboardInterrupt:
           server.stop(0)
   
   if '__main__' == __name__:
       server()
   ```

4. 实现客户端

   ```python
   from __future__ import print_function
   
   import grpc
   import message_pb2_grpc, message_pb2
   
   _HOST = 'localhost'
   _PORT = '8080'
   
   def run():
       conn = grpc.insecure_channel(_HOST + ':' + _PORT)
       client = message_pb2_grpc.FormatDataStub(channel=conn)
       response = client.Doformat(message_pb2.Data(conversation_id= 100,message='Hello'))
       print(response.conversation_id, response.message)
      
   if '__main__' == __name__:
       run()
   ```


