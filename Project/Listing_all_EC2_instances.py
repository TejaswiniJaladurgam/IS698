import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Retrieve metadata for all instances
response = ec2.describe_instances()

# Print instance details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"State: {instance['State']['Name']}")
        print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
        print(f"Private IP: {instance.get('PrivateIpAddress', 'N/A')}")
        print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
        print(f"Launch Time: {instance['LaunchTime']}")
        print(f"Tags: {instance.get('Tags', 'No Tags')}")
        

