variable "instances" {
  type = map
  default = {
    "web1" = "t2.micro"
    "web2" = "t3.micro"
    "web3" = "t2.small"
  }
}

resource "aws_instance" "web" {
  for_each = var.instances

  ami           = "your AMI ID"
  instance_type = each.value

  tags = {
    Name = "${each.key}"
  }
}
