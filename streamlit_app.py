"""
streamlit_app.py

Knowledge Firewall AI

Secure RAG Web Interface
"""

import pandas as pd
import streamlit as st

from src.core.rag.secure_rag import SecureRAG


# ---------------------------------------------------------
# Page
# ---------------------------------------------------------

st.set_page_config(

    page_title="Knowledge Firewall AI",

    page_icon="🛡️",

    layout="wide"

)

st.title("🛡️ Knowledge Firewall AI")

st.caption(
    "Secure Retrieval-Augmented Generation for Enterprise Knowledge"
)

# ---------------------------------------------------------
# Load RAG once
# ---------------------------------------------------------

@st.cache_resource
def load_rag():

    return SecureRAG()


rag = load_rag()

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.header("Settings")

top_k = st.sidebar.slider(

    "Top K Retrieval",

    1,

    10,

    5

)

include_suspicious = st.sidebar.checkbox(

    "Include Suspicious Chunks",

    False

)

# ---------------------------------------------------------
# Input
# ---------------------------------------------------------

question = st.text_input(

    "Ask an Enterprise Question",

    placeholder="Example: Does VPN require authentication?"

)

# ---------------------------------------------------------
# Search
# ---------------------------------------------------------

if st.button("Generate Secure Answer"):

    if not question.strip():

        st.warning("Enter a question.")

        st.stop()

    with st.spinner("Running Knowledge Firewall..."):

        result = rag.ask(

            question,

            top_k=top_k,

            include_suspicious=include_suspicious

        )

    # -----------------------------------------------------
    # Answer
    # -----------------------------------------------------

    st.success("Answer Generated")

    st.subheader("Enterprise Answer")

    st.write(result.answer)

    # -----------------------------------------------------
    # Statistics
    # -----------------------------------------------------

    stats = result.firewall_result.statistics

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Retrieved", stats["retrieved"])

    c2.metric("Trusted", stats["trusted"])

    c3.metric("Suspicious", stats["suspicious"])

    c4.metric("Blocked", stats["blocked"])

    # -----------------------------------------------------
    # Trusted Context
    # -----------------------------------------------------

    with st.expander("Trusted Context", expanded=False):

        st.text(result.trusted_context)

    # -----------------------------------------------------
    # Verification
    # -----------------------------------------------------

    reports = []

    for report in result.firewall_result.verification_reports:

        reports.append({

            "Policy": report.policy_id,

            "Chunk": report.chunk_id,

            "Decision": report.decision,

            "Trust Score": report.trust_score,

            "SHA": report.sha_similarity,

            "SimHash": report.simhash_similarity,

            "Embedding": report.embedding_similarity,

            "Reason": report.reason

        })

    st.subheader("Knowledge Firewall Report")

    st.dataframe(

        pd.DataFrame(reports),

        use_container_width=True

    )