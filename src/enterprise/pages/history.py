"""
history.py

Knowledge Firewall AI

Enterprise Version History Page.
"""

import streamlit as st

from src.enterprise.managers.history_manager import HistoryManager


def show_page():

    manager = HistoryManager()

    st.title("🕒 Version History")

    st.caption(
        "Track fingerprint versions and trust evolution of enterprise knowledge."
    )

    st.divider()

    history = manager.latest_versions()

    if history.empty:

        st.info("No version history available.")

        return

    # =====================================================
    # Repository Overview
    # =====================================================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Policies",
        history["policy_id"].nunique()
    )

    c2.metric(
        "Latest Version",
        history["fingerprint_version"].iloc[0]
    )

    c3.metric(
        "Average Trust",
        f"{history['trust_score'].mean():.2f}%"
    )

    st.divider()

    # =====================================================
    # Policy Selection
    # =====================================================

    selected = st.selectbox(

        "Select Policy",

        sorted(history["policy_id"].unique())

    )

    policy_history = manager.get_policy_history(selected)

    st.subheader(f"History - {selected}")

    st.dataframe(

        policy_history,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Trust Evolution
    # =====================================================

    st.subheader("📈 Trust Evolution")

    if len(policy_history) > 1:

        chart = policy_history.set_index(

            "created_at"

        )["trust_score"]

        st.line_chart(chart)

    else:

        st.info(

            "Only one version available."

        )

    st.divider()

    # =====================================================
    # Latest Repository Versions
    # =====================================================

    st.subheader("Latest Repository Versions")

    st.dataframe(

        history,

        use_container_width=True,

        hide_index=True

    )