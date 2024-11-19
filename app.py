from flask import Flask, request, jsonify
from google.protobuf.json_format import ParseDict, MessageToDict
import proto.compiled.customer_pb2 as customer_pb2
import proto.compiled.customer_pb2_grpc as customer_pb2_grpc
from google.protobuf import any_pb2
from google.protobuf.wrappers_pb2 import StringValue

app = Flask(__name__)

# Helper function to convert JSON to ProtoBuf using ParseDict
def json_to_proto(json_data, proto_class):
    proto_message = proto_class()
    ParseDict(json_data, proto_message)
    return proto_message

# Helper function to convert ProtoBuf to JSON using MessageToDict
def proto_to_json(proto_message):
    return MessageToDict(proto_message, preserving_proto_field_name=True)

@app.route('/create_customer', methods=['POST'])
def create_customer():
    # Parse incoming JSON request into ProtoBuf
    json_data = request.get_json()
    create_request = json_to_proto(json_data, customer_pb2.CreateCustomerRequest)

    # Process the customer creation (simplified logic for demonstration)
    customer = create_request.customer
    print(f"Creating customer: {customer.customer_name}")

    # Prepare the response in ProtoBuf format
    operation = customer_pb2.Operation(
        operationName="CreateCustomer",
        status=customer_pb2.OperationStatus.DONE,
        response=any_pb2.Any()  # Add any relevant response data
    )
    response = customer_pb2.CreateCustomerResponse(operation=operation)

    # Convert ProtoBuf response to JSON
    response_json = proto_to_json(response)

    return jsonify(response_json)

@app.route('/update_customer', methods=['POST'])
def update_customer():
    # Parse incoming JSON request into ProtoBuf
    json_data = request.get_json()
    update_request = json_to_proto(json_data, customer_pb2.UpdateCustomerRequest)

    # Process the customer update (simplified logic for demonstration)
    print(f"Updating customer: {update_request.customer_id}")

    # Prepare the response in ProtoBuf format
    operation = customer_pb2.Operation(
        operationName="UpdateCustomer",
        status=customer_pb2.OperationStatus.DONE,
        response=any_pb2.Any()  # Add any relevant response data
    )
    response = customer_pb2.UpdateCustomerResponse(operation=operation)

    # Convert ProtoBuf response to JSON
    response_json = proto_to_json(response)

    return jsonify(response_json)

@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    # Parse incoming JSON request into ProtoBuf
    json_data = request.get_json()
    delete_request = json_to_proto(json_data, customer_pb2.DeleteCustomerRequest)

    # Process the customer deletion (simplified logic for demonstration)
    print(f"Deleting customer: {delete_request.customer_id}")

    # Prepare the response in ProtoBuf format
    operation = customer_pb2.Operation(
        operationName="DeleteCustomer",
        status=customer_pb2.OperationStatus.DONE,
        response=any_pb2.Any()  # Add any relevant response data
    )
    response = customer_pb2.DeleteCustomerResponse(operation=operation)

    # Convert ProtoBuf response to JSON
    response_json = proto_to_json(response)

    return jsonify(response_json)

@app.route('/get_customer', methods=['GET'])
def get_customer():
    customer_id = request.args.get('customer_id')

    # Simulate retrieving a customer (this would typically query a database)
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

    # Convert ProtoBuf response to JSON
    customer_json = proto_to_json(customer)

    return jsonify(customer_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
