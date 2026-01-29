terraform {
  required_version = ">= 1.0"
}

provider "aws" {
  region = "us-east-1"
}

variable "service_name" {}
variable "environment" {}
variable "instance_count" {}
variable "instance_type" {}
