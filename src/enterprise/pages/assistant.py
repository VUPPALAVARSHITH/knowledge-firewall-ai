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

    # =====================================================
    # Run Secure RAG
    # =====================================================

    with st.spinner("Running Knowledge Firewall..."):

        result = manager.ask(
            question,
            top_k=top_k,
            include_suspicious=include_suspicious
        )

    stats = result.firewall_result.statistics

    retrieved = stats.get("retrieved", 0)
    relevant = stats.get("relevant", 0)
    trusted = stats.get("trusted", 0)
    suspicious = stats.get("suspicious", 0)
    blocked = stats.get("blocked", 0)

    # =====================================================
    # Determine Security State
    # =====================================================

    if relevant == 0:

        st.warning(
            "No sufficiently relevant trusted enterprise "
            "knowledge was found for this question."
        )

        firewall_status = "NO RELEVANT KNOWLEDGE"

    elif trusted > 0:

        st.success(
            "Knowledge Firewall verification completed successfully."
        )

        firewall_status = "PASSED"

    else:

        st.warning(
            "Relevant knowledge was found, but no trusted "
            "knowledge was allowed into the response context."
        )

        firewall_status = "BLOCKED / REVIEW"

    # =====================================================
    # Pipeline
    # =====================================================

    st.info("""
Knowledge Firewall Pipeline

Query
↓
Semantic Retrieval
↓
Relevance Gate
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

    # Verification rate now measures:
    #
    # verified trusted chunks / relevant chunks
    #
    # This prevents irrelevant retrieved chunks from
    # being interpreted as successful verification.

    verification_rate = (

        trusted / relevant * 100

        if relevant > 0

        else 0

    )

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.metric(
        "Retrieved",
        retrieved
    )

    c2.metric(
        "Relevant",
        relevant
    )

    c3.metric(
        "Trusted",
        trusted
    )

    c4.metric(
        "Suspicious",
        suspicious
    )

    c5.metric(
        "Blocked",
        blocked
    )

    c6.metric(
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
        "Verified Trusted Context",
        expanded=bool(result.trusted_context.strip())
    ):

        if result.trusted_context.strip():

            st.text(result.trusted_context)

        else:

            st.info(
                "No trusted context was admitted for this query."
            )

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
            "No knowledge chunks passed the relevance gate, "
            "so no fingerprint verification was required."
        )

    st.divider()

    # =====================================================
    # Security Summary
    # =====================================================

    st.subheader("🛡 Security Summary")

    left, right = st.columns(2)

    with left:

        if relevant > 0:

            st.success(
                "✔ Semantic relevance evaluated"
            )

        else:

            st.warning(
                "⚠ No sufficiently relevant knowledge found"
            )

        if trusted > 0:

            st.success(
                "✔ Runtime fingerprints verified"
            )

        else:

            st.info(
                "ℹ No trusted chunks admitted"
            )

        if relevant > 0 and trusted > 0:

            st.success(
                "✔ Knowledge integrity validated"
            )

    with right:

        if firewall_status == "PASSED":

            st.success(
                "✔ Knowledge Firewall passed"
            )

        elif firewall_status == "NO RELEVANT KNOWLEDGE":

            st.warning(
                "⚠ Knowledge Firewall rejected irrelevant context"
            )

        else:

            st.warning(
                "⚠ Knowledge Firewall prevented untrusted context"
            )

        if result.answer.strip():

            st.success(
                "✔ Secure response generated"
            )