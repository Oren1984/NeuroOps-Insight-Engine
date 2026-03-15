# AI Business Intelligence Platform

This project combines:
- structured business analytics
- SQL-style question answering
- LLM explanations
- retrieval-augmented context
- executive summary generation
- demo automation handoff to n8n

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
streamlit run src/dashboard/dashboard.py
Run with Docker
docker compose -f docker/docker-compose.yml up --build
Environment

Copy .env.example to .env and configure:

LLM_PROVIDER=demo|openai|ollama

LLM_MODEL=...

OPENAI_API_KEY=...

OPENAI_BASE_URL=https://api.openai.com/v1

OLLAMA_BASE_URL=http://localhost:11434

N8N_ENABLED=true|false

N8N_WEBHOOK_URL=http://localhost:5678/webhook/ai-bi-summary

Main UI Sections

Overview

LLM Agent

RAG

Automation

Executive Summary
