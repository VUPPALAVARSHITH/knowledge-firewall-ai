"""
assistant.py

Knowledge Firewall AI

Enterprise Assistant Page.
"""

import pandas as pd
import streamlit as st

from src.enterprise.managers.assistant_manager import AssistantManager


@st.cache_resource
def load_manager():

    return AssistantManager()


def show_page():

    manager = load_manager()

    st.title("🤖 Enterprise Assistant")

    st.caption(
        "Query the Trusted Enterprise Knowledge Repository"
    )

    st.divider()

    # =====================================================
    # Sidebar
    # =====================================================

    top_k = st.sidebar.slider(

        "Top K Retrieval",

        1,

        10,

        5

    )

    include_suspicious = st.sidebar.checkbox(

        "Include Suspicious Knowledge",

        False

    )

    # =====================================================
    # Question
    # =====================================================

    question = st.text_input(

        "Ask an Enterprise Question",

        placeholder="Example: Does VPN require MFA?"

    )

    if not st.button(

        "Generate Secure Answer",

        use_container_width=True

    ):

        return

    if not question.strip():

        st.warning("Enter a question.")

        return

    with st.spinner("Running Knowledge Firewall..."):

        result = manager.ask(

            question,

            top_k=top_k,

            include_suspicious=include_suspicious

        )

    st.success("Secure Answer Generated")

    # =====================================================
    # Answer
    # =====================================================

    st.subheader("Enterprise Answer")

    st.write(result.answer)

    # =====================================================
    # Firewall Summary
    # =====================================================

    stats = result.firewall_result.statistics

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "Retrieved",

        stats["retrieved"]

    )

    c2.metric(

        "Trusted",

        stats["trusted"]

    )

    c3.metric(

        "Suspicious",

        stats["suspicious"]

    )

    c4.metric(

        "Blocked",

        stats["blocked"]

    )

    st.divider()

    # =====================================================
    # Trusted Context
    # =====================================================

    with st.expander(

        "Trusted Context"

    ):

        st.text(result.trusted_context)

    # =====================================================
    # Verification Report
    # =====================================================

    rows = []

    for report in result.firewall_result.verification_reports:

        rows.append({

            "Policy": report.policy_id,

            "Chunk": report.chunk_id,

            "Decision": report.decision,

            "Trust": report.trust_score,

            "SHA": report.sha_similarity,

            "SimHash": report.simhash_similarity,

            "Embedding": report.embedding_similarity,

            "Reason": report.reason

        })

    st.subheader(

        "Knowledge Firewall Verification"

    )

    st.dataframe(

        pd.DataFrame(rows),

        use_container_width=True,

        hide_index=True

    )

    st.subheader("Knowledge Firewall Verification")

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        hide_index=True
    )