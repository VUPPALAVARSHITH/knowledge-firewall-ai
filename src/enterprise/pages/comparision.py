"""
comparison.py

Knowledge Firewall AI

Enterprise Policy Comparison Page.
"""

import tempfile
from pathlib import Path

import streamlit as st

from src.enterprise.managers.comparison_manager import ComparisonManager


def show_page():

    st.title("🔍 Compare Enterprise Policies")

    st.caption(
        "Compare two enterprise policies for semantic consistency and trust."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        policy_a = st.file_uploader(

            "Policy A",

            type=["txt"],

            key="policy_a"

        )

    with col2:

        policy_b = st.file_uploader(

            "Policy B",

            type=["txt"],

            key="policy_b"

        )

    if policy_a is None or policy_b is None:

        return

    if not st.button(

        "Compare Policies",

        use_container_width=True

    ):

        return

    with tempfile.NamedTemporaryFile(

        delete=False,

        suffix=".txt"

    ) as tmp1:

        tmp1.write(policy_a.getvalue())

        path_a = Path(tmp1.name)

    with tempfile.NamedTemporaryFile(

        delete=False,

        suffix=".txt"

    ) as tmp2:

        tmp2.write(policy_b.getvalue())

        path_b = Path(tmp2.name)

    manager = ComparisonManager()

    with st.spinner("Comparing policies..."):

        report = manager.compare(

            path_a,

            path_b

        )

    st.success("Comparison Completed")

    st.divider()

    # ===================================================
    # Summary
    # ===================================================

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Semantic Similarity",

        f"{report.semantic_similarity:.2%}"

    )

    c2.metric(

        "Repository Similarity",

        f"{report.repository_similarity:.2%}"

    )

    c3.metric(

        "Trust Score",

        f"{report.trust_score:.2f}%"

    )

    st.divider()

    # ===================================================
    # Security Checks
    # ===================================================

    left, right = st.columns(2)

    with left:

        if report.attack_detected:

            st.error(

                "⚠ Knowledge Manipulation Detected"

            )

        else:

            st.success(

                "✓ No Knowledge Manipulation"

            )

    with right:

        if report.sensitive_data_detected:

            st.warning(

                "⚠ Sensitive Information Detected"

            )

        else:

            st.success(

                "✓ No Sensitive Data"

            )

    st.divider()

    # ===================================================
    # Decision
    # ===================================================

    st.subheader("Decision")

    if report.decision == "ACCEPT":

        st.success("🟢 POLICIES ARE CONSISTENT")

    elif report.decision == "REVIEW":

        st.warning("🟡 MANUAL REVIEW REQUIRED")

    else:

        st.error("🔴 POTENTIAL KNOWLEDGE MANIPULATION")

    st.info(report.recommendation)

    st.divider()

    # ===================================================
    # Details
    # ===================================================

    st.subheader("Comparison Details")

    st.write(f"**Policy A:** {report.policy_a}")

    st.write(f"**Policy B:** {report.policy_b}")