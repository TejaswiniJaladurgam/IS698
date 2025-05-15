import boto3

# Create S3 client
s3 = boto3.client('s3')

# Create a new S3 bucket (ensure it's globally unique)
bucket_name = 'is698-python-created-bucket-76'  # Example name, change if needed
s3.create_bucket(Bucket=bucket_name)

# Upload a file to the bucket (keep the same name in the bucket)
file_path = r'C:\Users\jteja\Desktop\Cloud\python-files_for_labs\myfile.txt'  # Local file path
s3.upload_file(file_path, bucket_name, 'myfile.txt')  # 'myfile.txt' is the S3 object name

print(f"File uploaded to s3://{bucket_name}/myfile.txt")
