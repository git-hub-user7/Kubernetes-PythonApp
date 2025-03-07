# 🚀 Flask Kubernetes Deployment Project  
![Kubernetes](https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white)

**A professional deployment of a Flask application on Kubernetes**    

---

## 🌟 Project Overview
This project demonstrates a production-grade deployment of a Flask web application on Kubernetes, featuring:
- Containerization with Docker
- Kubernetes orchestration
- Load balancing with NodePort service
- Scalable deployment configuration

---

## ✨ Features
- **Simple Flask Web Server**: Minimalist web application with single endpoint
- **Dockerized Environment**: Reproducible container build
- **Kubernetes Deployment**: Cloud-native deployment manifests
- **Service Exposure**: External access via NodePort

---

## 🛠 Prerequisites
![Minikube](https://img.shields.io/badge/minikube-1D94E5?style=flat&logo=kubernetes&logoColor=white)
![kubectl](https://img.shields.io/badge/kubectl-1D94E5?style=flat&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-2496ED?style=flat&logo=docker&logoColor=white)

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- Docker Hub Account

---

## 📂 Project Structure
```
flask-kubernetes-deployment/
├── frontend/
│ ├── app.py            # Flask application
│ ├── Dockerfile        # Container configuration
│ └── requirements.txt  # Python dependencies
└── manifests/
├── deployment.yaml     # Kubernetes deployment
└── service.yaml        # Kubernetes service
```

---

## 🚦 Deployment Guide

### 1. Build Docker Image
```bash
cd frontend
docker build -t dockerprovider/flask-app:v1 .
```
### 2. Push to Container Registry

```bash
docker push <DOCKERHUB_USERNAME>/flask-app:v1
```
### 3. Deploy to Kubernetes

```bash
kubectl apply -f manifests/
```
### 4. Verify Deployment

```bash
kubectl get pods
kubectl get services
```
### 5. Access Application
```bash
minikube service flask-service
```

## Screenshots:

---

## 🧹 Cleanup
```bash

kubectl delete -f manifests/
minikube delete
```
*By [Your Name] • 📧 [Your Email] • 💼 [LinkedIn Profile]*
