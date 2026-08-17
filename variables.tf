variable "region" {
  description = "Region of Deployment"
  type        = string
  default     = "us-east-1"
}

variable "access_key" {
  description = "Access key of user"
  type        = string
}

variable "secret_key" {
  description = "Secret key of user"
  type        = string
}

variable "instance_type" {
  description = "instance type of ec2 instance"
  type        = string
  default     = "t3.micro"
}

variable "key_name" {
  description = "key pair of the user"
  type        = string
  default     = "demokey"
}
