import tempfile
from pathlib import Path

import streamlit as st

from src.enterprise.managers.upload_manager import UploadManager


def show_page():

    st.title("⬆️ Knowledge Admission Firewall")

    st.caption(
        "Analyze enterprise knowledge before admission into the trusted repository."
    )

    st.divider()

    uploaded_file = st.file_uploader(

        "Upload Enterprise Policy",

        type=["txt"],

        help="Supported formats: TXT (PDF/DOCX support can be added later)."

    )

    if uploaded_file is None:
        return

    if st.button("Run Knowledge Admission Firewall", use_container_width=True):

        manager = UploadManager()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".txt"
        ) as tmp:

            tmp.write(uploaded_file.getvalue())

            temp_path = Path(tmp.name)

        with st.spinner("Running Knowledge Admission Firewall..."):

            report = manager.analyze(temp_path)

        st.success("Knowledge Admission Completed")

        st.divider()

        # ==================================================
        # Pipeline Status
        # ==================================================

        st.subheader("🛡 Security Pipeline")

        c1, c2, c3 = st.columns(3)

        c1.success("✅ Policy Parsed")

        c2.success(f"✅ {report.chunks_created} Chunks Created")

        c3.success("✅ Fingerprint Generated")

        c4, c5, c6 = st.columns(3)

        if report.duplicate_found:
            c4.error("❌ Repository Match")
        else:
            c4.success("✅ Repository Check")

        if report.attack_detected:
            c5.error("❌ Attack Detected")
        else:
            c5.success("✅ Attack Analysis")

        if report.sensitive_data_detected:
            c6.warning("⚠ Sensitive Data")
        else:
            c6.success("✅ Sensitive Data Scan")

        st.divider()

        # ==================================================
        # Admission Report
        # ==================================================

        st.subheader("📄 Admission Report")

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Policy", report.policy_id)

        m2.metric("Department", report.department)

        m3.metric("Chunks", report.chunks_created)

        m4.metric(
            "Trust Score",
            f"{report.trust_score:.2f}"
        )

        st.write("### Decision")

        if report.decision == "ACCEPT":

            st.success("✅ ACCEPT")

        elif report.decision == "REVIEW":

            st.warning("🟡 MANUAL REVIEW")

        else:

            st.error("❌ REJECT")

        st.info(
            f"Recommendation: {report.recommendation}"
        )

        if report.warnings:

            st.subheader("Warnings")

            for warning in report.warnings:

                st.warning(warning)

        st.divider()

        st.subheader("Repository Similarity")

        st.progress(report.repository_similarity)

        st.write(
            f"Similarity: {report.repository_similarity:.2%}"
        )