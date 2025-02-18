import boto3

s3 = boto3.client('s3')
bucket_name = 'unique-bucket-name'

s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={'Status': 'Enabled'}
)
print(f'Versioning enabled for bucket {bucket_name}!')
