provider "aws" {
  region = var.region
}

module "eks" {
  source       = "./modules/eks"
  cluster_name = var.cluster_name
  region       = var.region
  subnet_ids   = var.subnet_ids
}

