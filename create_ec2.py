import boto3

# Initialize a session using Boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')  # Use your region

# Create an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-085ad6ae776d8f09c',  # Your AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # You can change the instance type if needed
    KeyName='MyWindowsKeyPair',  # Your key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyPythonEC2Instance'}
            ]
        }
    ]
)

print(f'Created instance with ID: {instance[0].id}')
