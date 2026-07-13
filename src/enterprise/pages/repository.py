import pandas as pd
import streamlit as st

from src.enterprise.managers.repository_manager import RepositoryManager


def show_page():

    st.title("📂 Enterprise Knowledge Repository")

    st.caption(
        "Trusted Knowledge Maintained by Knowledge Firewall AI"
    )

    manager = RepositoryManager()

    policies = manager.get_policies()

    rows = []

    for p in policies:

        rows.append({

            "Policy ID": p.policy_id,

            "Department": p.department,

            "Category": p.category,

            "Trust Score": p.trust_score,

            "Chunks": p.chunks,

            "Status": p.status

        })

    st.dataframe(

        pd.DataFrame(rows),

        use_container_width=True

    )