import grpc
from grpc_reflection.v1alpha import reflection
from concurrent import futures
import proto.compiled.customer_pb2 as customer_pb2
import proto.compiled.customer_pb2_grpc as customer_pb2_grpc



from google.protobuf import any_pb2

class CustomerServiceServicer(customer_pb2_grpc.CustomerServiceServicer):
    
    def CreateCustomer(self, request, context):
        print(f"Creating customer: {request.customer.customer_name}")
        response = customer_pb2.CreateCustomerResponse(
            operation=customer_pb2.Operation(
                operationName="CreateCustomer",
                status=customer_pb2.OperationStatus.DONE,
                response=any_pb2.Any()
            )
        )
        return response

    def UpdateCustomer(self, request, context):
        print(f"Updating customer: {request.customer.customer_id}")
        response = customer_pb2.UpdateCustomerResponse(
            operation=customer_pb2.Operation(
                operationName="UpdateCustomer",
                status=customer_pb2.OperationStatus.DONE,
                response=any_pb2.Any()
            )
        )
        return response

    def DeleteCustomer(self, request, context):
        print(f"Deleting customer: {request.customer_id}")
        response = customer_pb2.DeleteCustomerResponse(
            operation=customer_pb2.Operation(
                operationName="DeleteCustomer",
                status=customer_pb2.OperationStatus.DONE,
                response=any_pb2.Any()
            )
        )
        return response

    def GetCustomer(self, request, context):
        print(f"Fetching customer with ID: {request.value}")
        customer = customer_pb2.Customer(
            customer_id="123",
            customer_name="John Doe",
            customer_configuration=customer_pb2.CustomerConfiguration(
                config_option_1="Option 1",
                config_option_2=True,
                config_option_3=5,
                enabled_features=["Feature A", "Feature B"]
            )
        )
        return customer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_pb2_grpc.add_CustomerServiceServicer_to_server(CustomerServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server running at [::]:50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()