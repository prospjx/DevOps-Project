output "aws_vpc" {
  description = "AWS VPC"
  value       = aws_vpc.main.id
}

output "aws_subnet" {
  description = "AWS VPC"
  value       = aws_subnet.main.id
}

output "aws_internet_gateway" {
  description = "AWS Internet Gateway"
  value       = aws_internet_gateway.main.id
}

output "aws_route_table" {
  description = "AWS Route Table"
  value       = aws_route_table.main.id
}

output "aws_route_table_association" {
  description = "AWS VPC"
  value       = aws_route_table_association.main.id
}

output "aws_security_group" {
  description = "AWS Security Group"
  value       = aws_security_group.main.id
}

output "aws_ami" {
  description = "AWS AMI"
  value       = data.aws_ami.amazon_linux.id
}

output "aws_eip" {
  description = "AWS EIP"
  value       = aws_eip.main.id
}

