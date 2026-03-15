# AI Business Intelligence Platform

An AI-powered business intelligence platform that combines structured analytics, SQL-style questioning, LLM-generated explanations, retrieval-augmented context, executive summaries, and demo-ready automation through n8n.

The platform is designed to help analyze product usage, detect inactive users, identify repeated system issues, and generate business-facing insights in a clear and interactive way.

---

## Core Capabilities

- Structured business analytics over product and system activity
- SQL-style business question answering
- LLM-based explanations in demo, OpenAI, or Ollama mode
- Retrieval-Augmented Generation (RAG) using a local knowledge base
- Executive summary generation for business stakeholders
- Demo automation handoff through n8n
- Interactive Streamlit dashboard for exploration and monitoring

---

## Project Components

This project combines:

- structured business analytics
- SQL-style question answering
- LLM explanations
- retrieval-augmented context
- executive summary generation
- demo automation handoff to n8n

---

## Project Structure

```text
ai-business-intelligence-agent/
│
├── data/                # Business datasets + RAG knowledge base
├── src/                 # Application source code
│   ├── agent/           # SQL-style BI agent
│   ├── analytics/       # Metrics, insights, summaries
│   ├── dashboard/       # Streamlit UI
│   ├── llm/             # LLM provider layer
│   ├── rag/             # Retrieval system
│   └── integrations/    # n8n automation integration
│
├── docker/              # Docker build + compose setup
├── n8n/                 # Demo workflow automation
│
├── main.py              # CLI execution entrypoint
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
└── README.md
```

---

## Main Data Sources

The platform works with four main business datasets:

- `users.csv`
- `usage_events.csv`
- `system_events.csv`
- `tickets.csv`

These datasets are loaded into SQLite and used by the analytics engine, SQL agent, dashboard, and summary generation flows.

---

## Main UI Sections
### Overview

Displays business KPIs, analytics tables, feature usage, error distribution, support data, and activity trends.

### LLM Agent

Allows the user to ask business questions and receive:

- SQL-style query logic

- result tables

- natural-language explanation

### RAG

Uses local business documents as retrieval context for richer AI answers.

### Automation

Builds and previews outgoing automation payloads and supports demo handoff to n8n workflows.

### Executive Summary

Generates a concise business-level summary of current activity, risks, and recommended next steps.

---

## Architecture Overview

The platform includes the following layers:

- data ingestion from CSV sources

- SQLite business data layer

- analytics and insight generation

- SQL-style agent logic

- LLM provider layer

- RAG retrieval layer

- executive summary generation

- n8n demo automation integration

- Streamlit user interface

---

## Run Locally
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
streamlit run src/dashboard/dashboard.py
```

---

## Run with Docker:

```bash
docker compose -f docker/docker-compose.yml up --build
```

---

## Environment Configuration:
Copy .env.example to .env and configure the environment as needed.

```bash
copy .env.example .env
-- Then edit .env to set your configuration
```

### Main variables:

LLM_PROVIDER=demo|openai|ollama
LLM_MODEL=...
OPENAI_API_KEY=...
OPENAI_BASE_URL=https://api.openai.com/v1
OLLAMA_BASE_URL=http://localhost:11434
N8N_ENABLED=true|false
N8N_WEBHOOK_URL=http://localhost:5678/webhook/ai-bi-summary

---

## LLM Modes

The platform supports three LLM modes:

### Demo

Runs without any external API or local model dependency.

### OpenAI

Uses the configured OpenAI API key and model.

### Ollama

Uses a local Ollama model endpoint for fully local experimentation.

---

## n8n Integration

The automation layer is designed in demo-first mode.

By default:

- automation payloads are generated inside the UI

- no live webhook is required

- n8n can be connected later when needed

A demo workflow is included in:
  n8n/demo_bi_webhook_workflow.json

---

## Example Business Questions

- What is the most used feature?

- Which users are inactive?

- Which errors appear most often?

- How many open tickets exist?

- What business risks should we care about right now?

---

## Docker Services

The Docker setup includes:

- the AI Business Intelligence application

- the n8n automation service

After startup:

- Streamlit UI: http://localhost:8501

- n8n UI: http://localhost:5678

---

## Notes

- The project is designed as a focused personal AI portfolio project

- Demo mode works without external API keys

- SQLite is rebuilt from CSV data during startup for a simple and stable demo workflow

- The architecture is intentionally lightweight and avoids unnecessary infrastructure overhead

---

## Summary

The AI Business Intelligence Platform demonstrates how analytics, AI reasoning, RAG, executive summaries, and workflow automation can be combined into one business-facing application with a clean local-first architecture.

---