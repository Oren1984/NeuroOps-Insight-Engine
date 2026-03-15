# Docker Runtime Environment

This directory contains the container runtime configuration for the **AI Business Intelligence Platform**.

Docker is used to package the application and ensure it runs consistently across different environments without requiring manual dependency installation.

---

## Components

The Docker environment includes two services:

1. **AI Business Intelligence Application**
2. **n8n Automation Engine**

These services are orchestrated using Docker Compose.

---

## Dockerfile

The `Dockerfile` defines the runtime image used to execute the application.

Main responsibilities:

• install Python runtime  
• install project dependencies  
• copy the project source code  
• start the Streamlit dashboard  

Key steps:

1. Use a lightweight Python base image.

python:3.11-slim

2. Install project dependencies from:

requirements.txt

3. Copy the full project into the container.

4. Start the Streamlit UI server.

streamlit run src/dashboard/dashboard.py

- The Streamlit server runs on port:

8501

---

## docker-compose.yml

Docker Compose orchestrates the entire runtime stack.

### Service 1 — AI BI Platform

Runs the Streamlit application.

- Configuration:

• container name  
• exposed port  
• mounted data volume  
• environment variables  

- Port mapping:
8501 → Streamlit UI

- Data folder mapping:

host data → /app/data

This allows the dataset to persist outside the container.

---

### Service 2 — n8n

Runs the automation engine used by the platform.

Port mapping:

5678 → n8n web interface

The n8n container stores its internal state in a Docker volume.

---

## Environment Variables

- Environment variables are loaded using:

.env

- Key variables include:

LLM_PROVIDER
OPENAI_API_KEY
OLLAMA_BASE_URL
N8N_ENABLED
N8N_WEBHOOK_URL

These control how the system connects to external services.

---

## Running the System

- From the project root run:

docker compose -f docker/docker-compose.yml up --build

- Docker will:

1. Build the AI application image
2. Install dependencies
3. Start the Streamlit server
4. Start the n8n service

---

## Accessing the Services

After startup the following endpoints are available:

### AI Business Intelligence Dashboard

http://localhost:8501

### n8n Workflow Editor

http://localhost:5678

---

## Container Lifecycle

- Stop containers:

docker compose -f docker/docker-compose.yml down

- Rebuild containers:

docker compose -f docker/docker-compose.yml up --build

---

## Architectural Role

Docker provides a **portable runtime environment** for the entire platform.

This ensures that:

• the application runs identically on any machine  
• dependencies remain isolated  
• the system can be deployed easily in the future  

Docker also prepares the project for future upgrades such as:

• cloud deployment  
• Kubernetes orchestration  
• CI/CD pipelines

---