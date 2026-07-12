import streamlit as st

from src.enterprise.dashboard.dashboard_manager import DashboardManager


def show_dashboard():

    manager = DashboardManager()

    summary = manager.get_summary()

    st.title("🛡 Knowledge Firewall AI")

    st.caption(
        "Enterprise Knowledge Security Framework"
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Policies", summary["policies"])

    c2.metric("Chunks", summary["chunks"])

    c3.metric("Trusted", summary["trusted"])

    c4.metric(
        "Average Trust",
        f"{summary['average_trust']:.2f}%"
    )

    st.divider()

    st.success(
        f"System Health : {summary['system_health']}"
    )