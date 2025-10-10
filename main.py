"""
BQuant-Ray Report Viewer
Simple Streamlit app to display BQuant-Ray HTML reports
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="BQuant-Ray Portfolio Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit default styling
st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Load and display the HTML report
report_path = Path('bquant_ray_report.html')

if report_path.exists():
    # Read the HTML file
    with open(report_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Display it
    components.html(html_content, height=1200, scrolling=True)
    
else:
    st.error(f"❌ Report file not found: {report_path}")
    st.info("Expected file: bquant_ray_report.html")
