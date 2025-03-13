provider "aws" {
  region = "us-east-1"  # Modify region if needed
}
resource "aws_instance" "my_ec2" {
  ami           = "<your-ami-id>"  # Replace with a valid AMI ID
  instance_type = "t2.micro"
  key_name      = "<your-key-name>"  # Replace with an existing AWS key pair
  tags = {
    Name = "<your-instance-name>"  # Modify instance name
  }
}
