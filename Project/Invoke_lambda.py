import boto3
import json

# Create a Lambda client
lambda_client = boto3.client('lambda')

# Define the payload (simulate an S3 event)
payload = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "is698-bucket-for-project-98"
                },
                "object": {
                    "key": "myfile.txt"
                }
            }
        }
    ]
}

# Invoke Lambda function
response = lambda_client.invoke(
    FunctionName='S3UploadLogger',  # Replace with your Lambda function name
    InvocationType='RequestResponse',  # Synchronous invocation
    Payload=json.dumps(payload)  # Pass the simulated S3 event as JSON
)

# Read and print the response from Lambda
response_payload = response['Payload'].read().decode("utf-8")
print(response_payload)
