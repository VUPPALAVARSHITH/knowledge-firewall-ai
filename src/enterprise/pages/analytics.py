"""
analytics.py

Knowledge Firewall AI

Enterprise Trust Analytics Page.
"""

import streamlit as st

from src.enterprise.managers.analytics_manager import AnalyticsManager


def show_page():

    manager = AnalyticsManager()

    summary = manager.get_summary()
    st.info("""
    Knowledge Firewall Analytics

    This dashboard summarizes repository trust, policy distribution,
    risk levels, and verification outcomes across the enterprise
    knowledge base.
    """)

    st.title("📈 Knowledge Firewall Analytics")

    st.caption(
        "Security, Trust, and Repository Analytics for the Knowledge Firewall Framework"
    )

    st.divider()

    # =====================================================
    # Repository Overview
    # =====================================================

    st.subheader("📊 Repository Overview")

    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

    c1.metric(
        "Policies",
        summary["policies"]
    )

    c2.metric(
        "Chunks",
        summary["chunks"]
    )

    c3.metric(
        "Average Trust",
        f"{summary['average_trust']:.2f}%"
    )

    

    c4.metric(
        "Trusted",
        summary["trusted"]
    )

    c5.metric(
        "Suspicious",
        summary["suspicious"]
    )

    c6.metric(
        "Blocked",
        summary["blocked"]
    )

    c7.metric(
        "Repository Health",
        f"{repository_health:.1f}%"
    )

    st.divider()

    # =====================================================
    # Trust Distribution
    # =====================================================

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("🛡 Knowledge Trust Distribution")

            trust = manager.trust_distribution()

            if trust.empty:

                st.info("No trust data available.")

            else:

                st.bar_chart(

                    trust.set_index("Decision")

                )

    with right:

        with st.container(border=True):

            st.subheader("🏢 Department-wise Policies")

            departments = manager.department_distribution()

            if departments.empty:

                st.info("No department data available.")

            else:

                st.bar_chart(

                    departments.set_index("department")

                )

    st.divider()

    # =====================================================
    # Category / Risk
    # =====================================================

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("📂 Policy Category Distribution")

            categories = manager.category_distribution()

            if categories.empty:

                st.info("No category data.")

            else:

                st.bar_chart(

                    categories.set_index("category")

                )

    with right:

        with st.container(border=True):

            st.subheader("⚠ Policy Risk Distribution")

            risk = manager.risk_distribution()

            if risk.empty:

                st.info("No risk data.")

            else:

                st.bar_chart(

                    risk.set_index("risk_level")

                )

    st.divider()

    # =====================================================
    # Classification
    # =====================================================

    st.subheader("🔒 Information Classification Distribution")

    classification = manager.classification_distribution()

    if classification.empty:

        st.info("No classification data.")

    else:

        st.bar_chart(

            classification.set_index("classification")

        )

    
    st.divider()

    st.subheader("🛡 Security Summary")

    st.success("✔ Repository integrity monitored")
    st.success("✔ Knowledge Trust Distribution analyzed")
    st.success("✔ Risk profile generated")
    st.success("✔ Classification statistics generated")
    st.success("✔ Knowledge Firewall analytics completed")