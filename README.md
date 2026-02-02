# DevOps Local CI/CD Project

## Project Overview
This project is made to understand the basics of DevOps. 
In this project, I created a simple Python application and deployed it using Docker.
I also added a basic CI/CD pipeline using GitHub Actions.

## What I Learned
- Basics of Docker and Dockerfile
- How Docker Compose works
- How to manage environment variables using .env file
- Basics of CI/CD using GitHub Actions
- How to check application health after deployment

## Project Architecture
Browser
↓
Reverse Proxy
↓
Docker Network
↓
Python Application

All services are running inside Docker containers.

## Technologies Used
- Python
- Docker
- Docker Compose
- GitHub Actions

Application will be available at : http://app.localhost

## CI/CD Pipeline
This project uses GitHub Actions for CI/CD.

CI:
- Code is fetched from GitHub
- Docker image is built

CD:
- Old containers are stopped
- New containers are started
- Application health is checked

## Health Check
Endpoint:
 This endpoint is used to check whether the application is running or not.

## Author
Keyur Kyada


