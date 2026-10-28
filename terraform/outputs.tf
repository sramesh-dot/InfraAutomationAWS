
output "security_group_id" {
  description = "ID of the Terraform-managed security group"
  value       = aws_security_group.project.id
}
