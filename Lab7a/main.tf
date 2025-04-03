terraform {
  backend "s3" {
    bucket         = "unique-bucket-name"
    key            = "terraform/state.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}
resource "aws_instance" "example" {
  ami           = "your-ami-id"
  instance_type = "t2.micro"
  tags = {
    Name = "Terraform-Test-Instance"
  }
}
