"""
integrity.py

Knowledge Firewall AI

Repository Integrity Scanner Page.
"""

import pandas as pd
import streamlit as st

from src.enterprise.managers.integrity_manager import IntegrityManager


def show_page():

    st.title("🛡 Repository Integrity Scanner")

    st.caption(
        "Verify the integrity and trustworthiness of the enterprise knowledge repository."
    )

    st.divider()

    if not st.button(
        "Run Repository Integrity Scan",
        use_container_width=True
    ):
        return

    manager = IntegrityManager()

    with st.spinner("Scanning repository..."):

        reports = manager.scan_repository()

    st.success("Repository Scan Completed")

    if not reports:

        st.warning("No policies found.")

        return

    # =====================================================
    # Summary
    # =====================================================

    trusted = sum(r.decision == "ACCEPT" for r in reports)

    review = sum(r.decision == "REVIEW" for r in reports)

    blocked = sum(r.decision == "REJECT" for r in reports)

    average = round(

        sum(r.trust_score for r in reports) /

        len(reports),

        2

    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Policies",
        len(reports)
    )

    c2.metric(
        "Trusted",
        trusted
    )

    c3.metric(
        "Review",
        review
    )

    c4.metric(
        "Blocked",
        blocked
    )

    st.metric(
        "Repository Trust",
        f"{average:.2f}%"
    )

    st.divider()

    # =====================================================
    # Report
    # =====================================================

    rows = []

    for report in reports:

        rows.append({

            "Policy ID": report.policy_id,

            "Department": report.department,

            "Category": report.category,

            "Trust Score": report.trust_score,

            "Similarity": round(
                report.repository_similarity,
                4
            ),

            "Attack": report.attack_detected,

            "Decision": report.decision

        })

    st.subheader("Repository Integrity Report")

    st.dataframe(

        pd.DataFrame(rows),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    st.subheader("Trust Distribution")

    chart = (

        pd.DataFrame(rows)

        .groupby("Decision")

        .size()

        .reset_index(name="Policies")

    )

    st.bar_chart(

        chart.set_index("Decision")

    )