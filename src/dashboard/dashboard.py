# src/dashboard/dashboard.py
# This file is part of the 2FAS iOS app
# This module defines the main dashboard interface using Streamlit,
# which integrates analytics, LLM agent interactions, RAG-based knowledge retrieval,
# executive summary generation,
# and n8n automation features into a cohesive business intelligence platform.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
from src.data_loader.loader import init_sqlite
from src.analytics.analytics import (
    feature_usage_stats,
    error_frequency_stats,
    inactive_users,
    activity_trend,
    support_ticket_stats,
    user_activity_stats,
)
from src.analytics.insight_engine import generate_insights
from src.analytics.auto_insights import build_auto_insights
from src.analytics.executive_summary import generate_executive_summary
from src.agent.agent import BusinessIntelligenceAgent
from src.llm.provider import LLMProvider
from src.rag.retriever import retrieve_context
from src.integrations.n8n_client import build_n8n_payload, send_to_n8n

st.set_page_config(page_title="AI Business Intelligence Platform", layout="wide")
init_sqlite()

provider_name = os.getenv("LLM_PROVIDER", "demo")
model_name = os.getenv("LLM_MODEL", "gpt-4.1-mini")

st.title("AI Business Intelligence Platform")
st.caption("Analytics | LLM Agent | RAG | Executive Summary | n8n Automation")

with st.sidebar:
    st.header("Configuration")
    st.write(f"**LLM Provider:** {provider_name}")
    st.write(f"**LLM Model:** {model_name}")
    st.write(f"**n8n Enabled:** {os.getenv('N8N_ENABLED', 'false')}")
    st.info("Demo mode works without API keys. Switch provider in environment variables later.")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "LLM Agent",
    "RAG",
    "Automation",
    "Executive Summary"
])

with tab1:
    st.subheader("Business Overview")
    insights = generate_insights()
    auto_insights = build_auto_insights()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Generated Insights")
        for item in insights:
            st.write(f"- {item}")

    with col2:
        st.markdown("### Auto Insights")
        for item in auto_insights:
            badge = "[!]" if item["severity"] == "warning" else "[i]"
            st.write(f"{badge} **{item['title']}** - {item['message']}")

    with col3:
        st.markdown("### Inactive Users")
        st.dataframe(inactive_users(days=7), use_container_width=True)

    st.divider()

    left, right = st.columns(2)

    with left:
        st.markdown("### Feature Usage")
        feature_df = feature_usage_stats()
        st.dataframe(feature_df, use_container_width=True)
        if not feature_df.empty:
            st.bar_chart(feature_df.set_index("feature_used"))

        st.markdown("### Error Distribution")
        error_df = error_frequency_stats()
        st.dataframe(error_df, use_container_width=True)
        if not error_df.empty:
            st.bar_chart(error_df.set_index("event_type"))

    with right:
        st.markdown("### Activity Trend")
        trend_df = activity_trend()
        st.dataframe(trend_df, use_container_width=True)
        if not trend_df.empty:
            temp = trend_df.copy()
            temp["date"] = temp["date"].astype(str)
            st.line_chart(temp.set_index("date"))

        st.markdown("### Support Tickets")
        tickets_df = support_ticket_stats()
        st.dataframe(tickets_df, use_container_width=True)

        st.markdown("### User Activity")
        st.dataframe(user_activity_stats(), use_container_width=True)

with tab2:
    st.subheader("LLM Business Agent")
    q = st.text_input(
        "Ask a business question",
        value="What is the most used feature?"
    )

    if st.button("Run Agent"):
        agent = BusinessIntelligenceAgent()
        sql, df, explanation = agent.ask(q)

        llm = LLMProvider()
        llm_answer = llm.generate(
            system_prompt="You are a business intelligence assistant. Explain data results clearly for a business stakeholder.",
            user_prompt=q,
            context=f"SQL:\n{sql}\n\nResult:\n{df.to_string(index=False) if not df.empty else 'No rows'}\n\nBase Explanation:\n{explanation}"
        )

        st.markdown("### Generated SQL")
        st.code(sql, language="sql")

        st.markdown("### Base Explanation")
        st.write(explanation)

        st.markdown("### Result Data")
        st.dataframe(df, use_container_width=True)

        st.markdown("### LLM Explanation")
        st.write(llm_answer)

with tab3:
    st.subheader("RAG Business Knowledge")
    rag_q = st.text_input(
        "Ask with RAG context",
        value="What business risks should we care about if reports are failing often?"
    )

    if st.button("Run RAG Answer"):
        retrieval = retrieve_context(rag_q, top_k=3)
        context = retrieval["context"]

        llm = LLMProvider()
        rag_answer = llm.generate(
            system_prompt="You are a RAG-based business intelligence assistant. Use retrieved knowledge and current business logic to answer clearly.",
            user_prompt=rag_q,
            context=context
        )

        st.markdown("### Retrieved Sources")
        for doc in retrieval["documents"]:
            st.write(f"- {doc['source']} (score={doc['score']})")

        st.markdown("### Retrieved Context")
        st.text_area("Context", value=context, height=260)

        st.markdown("### RAG Answer")
        st.write(rag_answer)

with tab4:
    st.subheader("n8n Automation")
    auto_insights = build_auto_insights()
    summary_obj = generate_executive_summary()
    payload = build_n8n_payload(auto_insights, summary_obj["summary"])

    st.markdown("### Outgoing Payload Preview")
    st.json(payload)

    if st.button("Send To n8n"):
        result = send_to_n8n(payload)
        st.markdown("### Delivery Result")
        st.json(result)

    st.info("In demo mode, the app builds and displays the payload without requiring a live webhook.")

with tab5:
    st.subheader("Executive Summary Generator")
    if st.button("Generate Executive Summary"):
        obj = generate_executive_summary()
        st.markdown("### Executive Summary")
        st.write(obj["summary"])

        with st.expander("Summary Source Context"):
            st.text(obj["context"])
