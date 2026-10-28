
data "aws_vpc" "default" {
  default = true
}

resource "aws_security_group" "project" {
  name        = "${var.project_name}-sg"
  description = "Security group managed by Terraform"
  vpc_id      = data.aws_vpc.default.id

  # No inbound rules are defined.

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "${var.project_name}-sg"
    Project     = var.project_name
    Environment = var.environment
  }
}
