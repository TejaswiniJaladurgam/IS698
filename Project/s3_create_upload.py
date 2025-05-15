import boto3
# Create S3 client
s3 = boto3.client('s3')
# Create a new S3 bucket 
bucket_name = 'is698-python-created-bucket-76' 
s3.create_bucket(Bucket=bucket_name)
# Upload a file to the bucket 
file_path = r'C:\Users\jteja\Desktop\Cloud\python-files_for_labs\myfile.txt' 
s3.upload_file(file_path, bucket_name, 'myfile.txt')
print(f"File uploaded to s3://{bucket_name}/myfile.txt")
