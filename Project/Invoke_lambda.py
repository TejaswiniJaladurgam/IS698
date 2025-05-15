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
    FunctionName='S3UploadLogger',  
    InvocationType='RequestResponse',  
    Payload=json.dumps(payload)  
)
# Read and print the response from Lambda
response_payload = response['Payload'].read().decode("utf-8")
print(response_payload)
