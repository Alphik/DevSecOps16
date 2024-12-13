provider "aws" {
  region = "us-east-1"
  # access_key="" 
  # secret_key = ""
}

resource "aws_instance" "ec21" {
  ami                    = "ami-0453ec754f44f9a4a"
  instance_type          = "t2.micro"
  availability_zone      = "us-east-1a"
  key_name               = "test11"
  vpc_security_group_ids = ["sg-0838a81dc27dbad85"]
  tags = {
    Name = "fromTerraform"
  }
}
