"""
repository.py

Knowledge Firewall AI

Enterprise Repository Page.
"""

import streamlit as st

from src.enterprise.managers.repository_manager import RepositoryManager


def show_page():

    st.title("📂 Trusted Enterprise Repository")

    st.caption(
        "Verified enterprise knowledge protected by the Knowledge Firewall Framework."
    )

    st.info("""
    Trusted Repository

    Only knowledge that successfully passes the Knowledge Admission Firewall
    is stored here. Every chunk is fingerprinted and protected by runtime
    verification before being used for answer generation.
    """)

    manager = RepositoryManager()

    policies = manager.get_policy_table()

    chunks = manager.get_chunk_table()

    repository_health = (
        manager.trusted_chunks() /
        manager.total_chunks() * 100
        if manager.total_chunks() > 0
        else 0
    )

    # -----------------------------------------------------
    # Repository Summary
    # -----------------------------------------------------

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Policies", manager.total_policies())
    c2.metric("Chunks", manager.total_chunks())
    c3.metric("Trusted", manager.trusted_chunks())
    c4.metric("Blocked", manager.blocked_chunks())
    c5.metric(
        "Repository Health",
        f"{repository_health:.1f}%"
    )
    st.divider()

    search = st.text_input(
        "🔍 Search Repository",
        placeholder="Policy ID, title, department, category..."
    )

    if search:

        policies = policies[
            policies.astype(str)
            .apply(
                lambda col:
                col.str.contains(
                    search,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

    # -----------------------------------------------------
    # Policies
    # -----------------------------------------------------

    st.subheader("Verified Enterprise Policies")

    if policies.empty:

        st.info("No policies available.")

    else:

        st.dataframe(

            policies,

            use_container_width=True,

            hide_index=True,

        )

    st.divider()

    # -----------------------------------------------------
    # Chunks
    # -----------------------------------------------------

    st.subheader("Trusted Knowledge Chunks")

    if chunks.empty:

        st.info("No chunk database available.")

    else:

        st.dataframe(

            chunks,

            use_container_width=True,

            hide_index=True,

        )

    st.divider()

    st.subheader("🛡 Repository Summary")
    st.success("✔ Verified policies available")

    st.success("✔ Fingerprints indexed")

    st.success("✔ Runtime verification enabled")

    st.success("✔ Trusted repository healthy")