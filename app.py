import streamlit as st

# --- Configuration ---
st.set_page_config(page_title="Status", layout="wide")

# --- Helper Functions ---
# Initialize session state for status if not present
if "status_top" not in st.session_state:
    st.session_state.status_top = "red"
if "status_bottom" not in st.session_state:
    st.session_state.status_bottom = "red"

def toggle_top():
    current = st.session_state.status_top
    st.session_state.status_top = "green" if current == "red" else "red"

def toggle_bottom():
    current = st.session_state.status_bottom
    st.session_state.status_bottom = "green" if current == "red" else "red"

# --- CSS Definition ---
STATUS_MODE_CSS = """
    <style>
    #MainMenu, footer, header {
        display: none !important;
        visibility: hidden !important;
    }
    
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        width: 100vw !important;
        overflow: hidden !important;
        display: flex !important;       
        flex-direction: column !important;
        align-items: center !important;
        padding-top: 0vh !important; 
    }
    
    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
        padding: 0 !important;
        width: 100vw !important;        
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; 
    }
    
    div[class*="stElementContainer"] {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important; 
        margin: 0 !important;
    }

    .stButton button {
        width: auto !important; 
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    
    .stButton button div p, .stButton button p {
        font-size: 20vh !important; 
        line-height: 1 !important;
        margin: 0 !important;
    }
    
    .section-wrapper {
        height: 28vh; 
        width: 100%; 
        display: flex;
        flex-direction: column;
        align-items: center; 
        text-align: center;  
    }
    
    .align-bottom {
        justify-content: flex-end;
        padding-bottom: 0.5vh; 
    }
    
    .align-top {
        justify-content: flex-start;
        padding-top: 0.5vh; 
    }
    </style>
"""

# --- MAIN LOGIC ---
st.markdown(STATUS_MODE_CSS, unsafe_allow_html=True)

# Top Section
st.markdown('<div class="section-wrapper align-bottom">', unsafe_allow_html=True)
btn_label_top = "🟢" if st.session_state.status_top == "green" else "🔴"
st.button(btn_label_top, key="btn_top", on_click=toggle_top)
st.markdown('</div>', unsafe_allow_html=True)

# Spacer
st.markdown("<div style='height: 1vh;'></div>", unsafe_allow_html=True)

# Bottom Section
st.markdown('<div class="section-wrapper align-top">', unsafe_allow_html=True)
btn_label_bottom = "🟢" if st.session_state.status_bottom == "green" else "🔴"
st.button(btn_label_bottom, key="btn_bottom", on_click=toggle_bottom)
st.markdown('</div>', unsafe_allow_html=True)
