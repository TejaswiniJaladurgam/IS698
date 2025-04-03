provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  count         = 3  # Creates 3 EC2 instances
  ami           = "your AMI ID"  # Replace with a valid AMI
  instance_type = "t2.micro"

  tags = {
    Name = "Terraform-Instance-${count.index}"
  }
}

