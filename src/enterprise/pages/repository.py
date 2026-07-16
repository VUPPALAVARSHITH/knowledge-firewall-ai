"""
repository.py

Knowledge Firewall AI

Enterprise Repository Page.
"""

import streamlit as st

from src.enterprise.managers.repository_manager import RepositoryManager


def show_page():

    st.title("📂 Enterprise Knowledge Repository")

    st.caption(
        "Trusted Knowledge Maintained by Knowledge Firewall AI"
    )

    manager = RepositoryManager()

    policies = manager.get_policy_table()

    chunks = manager.get_chunk_table()

    # -----------------------------------------------------
    # Repository Summary
    # -----------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Policies", manager.total_policies())
    c2.metric("Chunks", manager.total_chunks())
    c3.metric("Trusted", manager.trusted_chunks())
    c4.metric("Blocked", manager.blocked_chunks())

    st.divider()

    # -----------------------------------------------------
    # Policies
    # -----------------------------------------------------

    st.subheader("Enterprise Policies")

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

    st.subheader("Knowledge Chunks")

    if chunks.empty:

        st.info("No chunk database available.")

    else:

        st.dataframe(

            chunks,

            use_container_width=True,

            hide_index=True,

        )