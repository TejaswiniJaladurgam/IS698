resource "aws_vpc" "my_vpc" {
   cidr_block = "<your-cidr-block>"  # Example: 10.0.0.0/16
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "<your-public-cidr>"  # Example: 10.0.1.0/24
  map_public_ip_on_launch = true
  availability_zone        = "<your-az>"  # Example: us-east-1a
}

resource "aws_subnet" "private_subnet" {
  vpc_id           = aws_vpc.my_vpc.id
  cidr_block       = "<your-private-cidr>"  # Example: 10.0.2.0/24
  availability_zone = "<your-az>"  # Example: us-east-1b
}
