#!/bin/bash

# Define Docker Hub username (replace with your Docker Hub username)
DOCKER_USERNAME="hoaihuy"

# Define Docker Hub repository prefix
DOCKER_REPO_PREFIX="${DOCKER_USERNAME}"
TAG="1.0.4"

# Build and push order-service image
echo "Building order-service image..."
docker build -t "${DOCKER_REPO_PREFIX}/order-service:${TAG}" ./order-service
docker push "${DOCKER_REPO_PREFIX}/order-service:${TAG}"
echo "order-service image pushed to Docker Hub"

# Build and push notification-service image
echo "Building notification-service image..."
docker build -t "${DOCKER_REPO_PREFIX}/notification-service:${TAG}" ./notification-service
docker push "${DOCKER_REPO_PREFIX}/notification-service:${TAG}"
echo "notification-service image pushed to Docker Hub"

# Build and push payment-service image
echo "Building payment-service image..."
docker build -t "${DOCKER_REPO_PREFIX}/payment-service:${TAG}" ./payment-service
docker push "${DOCKER_REPO_PREFIX}/payment-service:${TAG}"
echo "payment-service image pushed to Docker Hub"

echo "All Docker images built and pushed successfully!"

echo "Deploy to kubenetes"
DIRECTORY="kubernetes"
SEARCH_STRING="TAG"

# Use find and sed to replace string in files
find "${DIRECTORY}" -type f -exec sed -i "s/${SEARCH_STRING}/${TAG}/g" {} +
kubectl apply -f kubernetes/