```md
## System Architecture

The platform combines structured analytics, SQL-style business questioning, LLM-powered explanations, retrieval-augmented context, executive summarization, and demo automation through n8n.

The diagram below shows how business data flows through the analytics, agent, RAG, and automation layers.

---

## Architecture Diagram

    U[Business User / Analyst] --> UI[Streamlit UI Dashboard]

    UI --> AGENT[SQL / BI Agent]
    UI --> AUTO[Auto Insight Engine]
    UI --> EXEC[Executive Summary Generator]
    UI --> RAG[RAG Retrieval Layer]
    UI --> N8N[n8n Demo Integration]

    AGENT --> SQLITE[(SQLite Business DB)]
    AUTO --> ANALYTICS[Analytics Engine]
    EXEC --> LLM[LLM Provider Layer]
    RAG --> KB[Knowledge Base]
    N8N --> WEBHOOK[n8n Webhook / Demo Flow]

    ANALYTICS --> USERS[users.csv]
    ANALYTICS --> USAGE[usage_events.csv]
    ANALYTICS --> SYSTEM[system_events.csv]
    ANALYTICS --> TICKETS[tickets.csv]

    USERS --> SQLITE
    USAGE --> SQLITE
    SYSTEM --> SQLITE
    TICKETS --> SQLITE

    AGENT --> LLM
    RAG --> LLM
    EXEC --> LLM

    LLM --> OPENAI[OpenAI API]
    LLM --> OLLAMA[Ollama Local Model]
    LLM --> DEMO[Demo Mode]

    KB --> DOC1[business_glossary.md]
    KB --> DOC2[platform_notes.md]

---