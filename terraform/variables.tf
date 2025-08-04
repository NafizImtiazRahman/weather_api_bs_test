variable "cluster_name" {
  type        = string
  description = "EKS Cluster Weather_API"
}

variable "region" {
  type        = string
  default     = "us-east-1"
}

variable "subnet_ids" {
  type        = list(string)
  description = "List of subnet IDs to use for the EKS cluster"
}

