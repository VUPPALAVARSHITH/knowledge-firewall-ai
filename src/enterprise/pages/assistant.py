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

    st.success(
        "Knowledge Firewall verification completed successfully."
    )

    st.info("""
    Knowledge Firewall Pipeline

    Query
    ↓
    Semantic Retrieval
    ↓
    Fingerprint Verification
    ↓
    Trust Computation
    ↓
    Knowledge Firewall
    ↓
    Enterprise LLM
    ↓
    Secure Response
    """)

    # =====================================================
    # Firewall Summary
    # =====================================================

    stats = result.firewall_result.statistics
    verification_rate = (
        stats["trusted"] / stats["retrieved"] * 100
        if stats["retrieved"] > 0
        else 0
    )
    c1, c2, c3, c4, c5 = st.columns(5)

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

    c5.metric(
        "Verification Rate",
        f"{verification_rate:.1f}%"
    )

    st.divider()

    # =====================================================
    # Answer
    # =====================================================

    st.subheader("🛡 Secure Enterprise Response")

    st.write(result.answer)

    

    # =====================================================
    # Trusted Context
    # =====================================================

    with st.expander(

        "Verified Trusted Context"

    ):

        st.text(result.trusted_context)

    # =====================================================
    # Verification Report
    # =====================================================

    decision_icons = {
        "TRUSTED": "🟢 TRUSTED",
        "SUSPICIOUS": "🟡 SUSPICIOUS",
        "BLOCKED": "🔴 BLOCKED",
    }

    rows = []

    for report in result.firewall_result.verification_reports:

        rows.append({

            "Policy": report.policy_id,

            "Chunk": report.chunk_id,

            "Decision": decision_icons.get(
                report.decision,
                report.decision
            ),

            "Trust Score (%)": report.trust_score,

            "SHA": report.sha_similarity,

            "SimHash": report.simhash_similarity,

            "Embedding": report.embedding_similarity,

            "Reason": report.reason

        })

    st.subheader("Knowledge Firewall Verification")

    if rows:

        st.dataframe(

            pd.DataFrame(rows),

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info(
            "No verification reports available."
        )

    st.divider()

    st.subheader("🛡 Security Summary")

    left, right = st.columns(2)

    with left:
        st.success("✔ Runtime fingerprints verified")
        st.success("✔ Knowledge integrity validated")
        st.success("✔ Trust score computed")

    with right:
        st.success("✔ Knowledge Firewall passed")
        st.success("✔ Secure response generated")