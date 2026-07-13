import streamlit as st

from src.enterprise.managers.dashboard_manager import DashboardManager


def show_dashboard():

    manager = DashboardManager()

    summary = manager.get_summary()
    activities = manager.get_recent_activity()
    alerts = manager.get_alerts()

    st.title("🛡 Knowledge Firewall AI")

    st.caption(
        "Enterprise Knowledge Security Framework"
    )

    st.divider()

    # =====================================================
    # Repository Overview
    # =====================================================

    st.subheader("📊 Repository Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Policies", summary.total_policies)
    c2.metric("Chunks", summary.total_chunks)
    c3.metric("Trusted", summary.trusted_chunks)
    c4.metric("Average Trust", f"{summary.average_trust:.2f}%")

    c5, c6, c7, c8 = st.columns(4)

    c5.metric("Suspicious", summary.suspicious_chunks)
    c6.metric("Blocked", summary.blocked_chunks)
    c7.metric("Last Scan", summary.last_scan)
    c8.metric("Health", summary.repository_health)

    st.divider()

    # =====================================================
    # Repository Health
    # =====================================================

    with st.container(border=True):

        st.subheader("🛡 Repository Health")

        st.write(
            f"**Status:** {summary.repository_health}"
        )

        st.write(
            f"**Average Trust:** {summary.average_trust:.2f}%"
        )

        st.write(
            f"**Last Scan:** {summary.last_scan}"
        )

        st.write(
            "**Knowledge Firewall:** Active ✅"
        )

    st.divider()

    # =====================================================
    # Charts
    # =====================================================

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("📊 Trust Distribution")

            trust = manager.get_trust_distribution()

            if trust.empty:

                st.info("No trust data available.")

            else:

                st.bar_chart(
                    trust.set_index("Decision")
                )

    with right:

        with st.container(border=True):

            st.subheader("🏢 Department Distribution")

            departments = manager.get_department_statistics()

            if departments.empty:

                st.info(
                    "No department statistics available."
                )

            else:

                st.bar_chart(
                    departments.set_index("department")
                )

    st.divider()

    # =====================================================
    # Activity & Alerts
    # =====================================================

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("📋 Recent Activity")

            if not activities:

                st.info("No recent activity.")

            else:

                for activity in activities:

                    if activity.status == "Warning":

                        st.warning(
                            f"{activity.timestamp} • {activity.title}"
                        )

                    else:

                        st.success(
                            f"{activity.timestamp} • {activity.title}"
                        )

    with right:

        with st.container(border=True):

            st.subheader("🚨 Security Alerts")

            if not alerts:

                st.success(
                    "No active security alerts."
                )

            else:

                for alert in alerts:

                    if alert.severity == "High":

                        st.error(
                            f"**{alert.title}**\n\n{alert.description}"
                        )

                    elif alert.severity == "Medium":

                        st.warning(
                            f"**{alert.title}**\n\n{alert.description}"
                        )

                    else:

                        st.info(
                            f"**{alert.title}**\n\n{alert.description}"
                        )

    st.divider()

    # =====================================================
    # Enterprise Repository
    # =====================================================

    st.subheader("📂 Enterprise Knowledge Repository")

    policies = manager.get_recent_policies()

    if policies.empty:

        st.info(
            "No enterprise policies available."
        )

    else:

        st.dataframe(

            policies,

            use_container_width=True,

            hide_index=True,

        )

    st.divider()

    # =====================================================
    # Quick Actions
    # =====================================================

    st.subheader("⚡ Quick Actions")

    q1, q2, q3, q4 = st.columns(4)

    q1.button(
        "⬆ Upload Knowledge",
        use_container_width=True,
        disabled=True,
    )

    q2.button(
        "🛡 Integrity Scanner",
        use_container_width=True,
        disabled=True,
    )

    q3.button(
        "📈 Analytics",
        use_container_width=True,
        disabled=True,
    )

    q4.button(
        "🤖 Enterprise Assistant",
        use_container_width=True,
        disabled=True,
    )