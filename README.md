# python-app

## Description
This project demonstrates how to deploy a simple REST API application to an Amazon Elastic Kubernetes Service (EKS) cluster on AWS.

## Prerequisites
- An AWS account with appropriate permissions.
- AWS CLI installed and configured.
- Docker installed on your local machine.
- Kubectl installed on your local machine.

## Application
The application in this project is a simple REST API that returns a JSON payload with a message and a timestamp.

## How to Run
Follow these steps to run the application on an AWS EKS cluster:

### 1. Clone the Repository
```bash
git clone https://github.com/your/repo.git
cd your-repo-directory
```

### 2. Build the Docker Image
Build the Docker image for the application:
```bash
docker build -t fashinadolapo/python-app:v1 .
```

### 3. Set Up an Amazon EKS Cluster
Create an Amazon EKS cluster using the AWS CLI. Replace placeholders with your specific configuration:
```bash
eksctl create cluster --name saint-cluster --region eu-west-2 --nodegroup-name standard-workers --node-type t2-micro --nodes 3
```

### 4. Deploy the Application
Apply the Kubernetes deployment and service configuration to your EKS cluster:
```bash
kubectl apply -f deployment.yaml
```

### 5. Access the Application
To find the external IP of the service:
```bash
kubectl get service saint-service
```
You can access the REST API using the provided IP address.

## How to Clean Up
To delete the AWS EKS cluster and associated resources, use the AWS CLI:
```bash
eksctl delete cluster --name saint-cluster- --region eu-west-2
```

