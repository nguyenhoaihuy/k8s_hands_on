#!/bin/bash

# Define Docker Hub username (replace with your Docker Hub username)
DOCKER_USERNAME="hoaihuy"

# Define Docker Hub repository prefix
DOCKER_REPO_PREFIX="${DOCKER_USERNAME}"

# Build and push order-service image
echo "Building order-service image..."
docker build -t "${DOCKER_REPO_PREFIX}/order-service:latest" ./order-service
docker push "${DOCKER_REPO_PREFIX}/order-service:latest"
echo "order-service image pushed to Docker Hub"

# Build and push notification-service image
echo "Building notification-service image..."
docker build -t "${DOCKER_REPO_PREFIX}/notification-service:latest" ./notification-service
docker push "${DOCKER_REPO_PREFIX}/notification-service:latest"
echo "notification-service image pushed to Docker Hub"

# Build and push payment-service image
echo "Building payment-service image..."
docker build -t "${DOCKER_REPO_PREFIX}/payment-service:latest" ./payment-service
docker push "${DOCKER_REPO_PREFIX}/payment-service:latest"
echo "payment-service image pushed to Docker Hub"

echo "All Docker images built and pushed successfully!"
