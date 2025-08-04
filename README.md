# 🌦️ DevOps Challenge – Part A: Weather API Deployment

This project is a complete DevOps implementation of a containerized REST API that returns system and weather information for Dhaka. It includes:

- REST API with FastAPI
- Docker & Docker Compose setup
- CI/CD with GitHub Actions
- Terraform code to provision an EKS cluster
- Kubernetes manifests with HPA
- Observability readiness

---

## 🚀 API Features

### `/api/hello`
Returns:
json
{
  "hostname": "your-host",
  "datetime": "YYMMDDHHmm",
  "version": "v1.0.0",
  "weather": {
    "dhaka": {
      "temperature": "30",
      "temp_unit": "c"
    }
  }
}

/api/health
Checks if:

The API is running
The weather API is reachable

## 🐳 Dockerized API
Build and run locally:

docker build -t weather-api .
docker run -p 8000:8000 weather-api

Or use Docker Compose:
docker-compose up --build

## 🔄 CI/CD (GitHub Actions)
CI/CD runs on every push to the dev branch:

Builds Docker image with a timestamp tag (yymmddhhmm)

Pushes image to Docker Hub

Updates the Kubernetes deployment

Applies HPA configuration

Required Secrets
Secret Name	Purpose
DOCKER_USERNAME	Docker Hub username
DOCKER_PASSWORD	Docker Hub password or access token
KUBE_CONFIG	Base64-encoded kubeconfig

## ☁️ Infrastructure-as-Code (Terraform)
Files:
terraform/main.tf: Uses a module to deploy EKS

terraform/modules/eks/: Reusable EKS module

terraform.tfvars: Provides inputs (cluster name, subnet IDs)

Commands:
terraform init
terraform plan
terraform apply

## ☸️ Kubernetes Deployment
Manifests:
deployment.yaml: API deployment with resource limits

service.yaml: ClusterIP service

secret.yaml: Injects weather API key

hpa.yaml: Horizontal Pod Autoscaler (min 2, max 5 pods)

Apply to Cluster:
kubectl apply -f k8s/

## 🔍 Observability
Not deployed, but the code is ready for integration with:

Prometheus (metrics)

Grafana (dashboards)

Loki or EFK (logs)

Jaeger or OpenTelemetry (tracing)

## 🔐 Security
Dockerfile uses python:3.11-slim for minimal footprint

Secrets injected via Kubernetes Secret resources

CI/CD secrets are stored in GitHub Secrets
