import streamlit as st

from src.enterprise.pages.dashboard import show_dashboard
from src.enterprise.pages.repository import show_page as show_repository
from src.enterprise.pages.upload import show_page as show_upload
from src.enterprise.pages.integrity import show_page as show_integrity
from src.enterprise.pages.comparison import show_page as show_comparison
from src.enterprise.pages.history import show_page as show_history
from src.enterprise.pages.analytics import show_page as show_analytics
from src.enterprise.pages.assistant import show_page as show_assistant
from src.enterprise.pages.settings import show_page as show_settings

st.set_page_config(
    page_title="Knowledge Firewall AI",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("🛡 Knowledge Firewall AI")
st.sidebar.caption("Enterprise Knowledge Security Framework")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📂 Repository",
        "⬆ Knowledge Admission",
        "🛡 Integrity Scanner",
        "🔍 Compare Policies",
        "🕒 Version History",
        "📈 Trust Analytics",
        "🤖 Enterprise Assistant",
        "⚙ Settings",
    ],
)

if page == "🏠 Dashboard":
    show_dashboard()

elif page == "📂 Repository":
    show_repository()

elif page == "⬆ Knowledge Admission":
    show_upload()

elif page == "🛡 Integrity Scanner":
    show_integrity()

elif page == "🔍 Compare Policies":
    show_comparison()

elif page == "🕒 Version History":
    show_history()

elif page == "📈 Trust Analytics":
    show_analytics()

elif page == "🤖 Enterprise Assistant":
    show_assistant()

elif page == "⚙ Settings":
    show_settings()