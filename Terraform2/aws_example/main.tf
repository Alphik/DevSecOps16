provider "aws" {
  region = var.region
}

resource "aws_security_group" "sg-for-ec2-terraform" {
  name = "sgec2"
  description = "security groups for ec2 created with tf"
  ingress {
    from_port= 22
    to_port= 22
    protocol= "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }
  ingress {
    from_port= 80
    to_port= 80
    protocol= "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "test_ec2" {
  ami = data.aws_ami.amazon_linux.id
  instance_type = "t2.micro"
  security_groups = [aws_security_group.sg-for-ec2-terraform.name]
  tags = {
    Name= "ec2-ins"
  }

}

