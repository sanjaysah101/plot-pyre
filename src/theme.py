"""
Python-themed UI configuration for Plot Pyre
Following Python's signature color scheme
"""
import streamlit as st

# Python color scheme
PYTHON_BLUE = "#4B8BBE"
PYTHON_YELLOW = "#FFD43B"
PYTHON_DARK_BLUE = "#306998"
PYTHON_LIGHT_BLUE = "#E6F3FF"
PYTHON_ORANGE = "#FF6B35"
PYTHON_GREEN = "#28A745"
PYTHON_GRAY = "#6C757D"

# Theme configuration
THEME_CONFIG = {
    "primaryColor": PYTHON_BLUE,
    "backgroundColor": "#FFFFFF",
    "secondaryBackgroundColor": PYTHON_LIGHT_BLUE,
    "textColor": "#262730",
    "font": "sans serif"
}

DARK_THEME_CONFIG = {
    "primaryColor": PYTHON_YELLOW,
    "backgroundColor": "#1E1E1E",
    "secondaryBackgroundColor": "#2D2D2D",
    "textColor": "#FFFFFF",
    "font": "sans serif"
}

def apply_python_theme(dark_mode=False):
    """Apply Python-themed styling to Streamlit app"""
    theme = DARK_THEME_CONFIG if dark_mode else THEME_CONFIG
    
    # Apply theme using Streamlit config
    st.set_page_config(
        page_title="Plot Pyre - Python-Powered Data Visualization",
        page_icon="🐍",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Custom CSS for Python theme
    st.markdown(f"""
    <style>
    /* Python theme colors */
    :root {{
        --python-blue: {PYTHON_BLUE};
        --python-yellow: {PYTHON_YELLOW};
        --python-dark-blue: {PYTHON_DARK_BLUE};
    }}
    
    /* Main container styling */
    .main {{
        background-color: {theme['backgroundColor']};
    }}
    
    /* Sidebar styling */
    .css-1d391kg {{
        background-color: {theme['secondaryBackgroundColor']};
    }}
    
    /* Headers */
    h1, h2, h3 {{
        color: {theme['primaryColor']} !important;
    }}
    
    /* Buttons */
    .stButton > button {{
        background-color: {PYTHON_BLUE};
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background-color: {PYTHON_DARK_BLUE};
        transform: translateY(-2px);
    }}
    
    /* Success messages */
    .stSuccess {{
        background-color: {PYTHON_GREEN};
        color: white;
    }}
    
    /* Info messages */
    .stInfo {{
        background-color: {PYTHON_BLUE};
        color: white;
    }}
    
    /* Warning messages */
    .stWarning {{
        background-color: {PYTHON_ORANGE};
        color: white;
    }}
    
    /* Error messages */
    .stError {{
        background-color: #DC3545;
        color: white;
    }}
    
    /* Progress bars */
    .stProgress > div > div {{
        background-color: {PYTHON_BLUE};
    }}
    
    /* Select boxes */
    .stSelectbox > div > div {{
        border-color: {PYTHON_BLUE};
    }}
    
    /* Text inputs */
    .stTextInput > div > div > input {{
        border-color: {PYTHON_BLUE};
    }}
    
    /* Dataframe styling */
    .dataframe {{
        border: 1px solid {PYTHON_BLUE};
    }}
    
    /* Custom Python logo styling */
    .python-logo {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    
    .python-icon {{
        font-size: 2rem;
        color: {PYTHON_YELLOW};
    }}
    </style>
    """, unsafe_allow_html=True)

def get_python_style_css():
    """Return CSS for Python-themed components"""
    return f"""
    <style>
    .python-card {{
        background: linear-gradient(135deg, {PYTHON_BLUE}, {PYTHON_DARK_BLUE});
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }}
    
    .python-button {{
        background-color: {PYTHON_YELLOW};
        color: {PYTHON_DARK_BLUE};
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    
    .python-button:hover {{
        background-color: {PYTHON_ORANGE};
        transform: scale(1.05);
    }}
    
    .python-header {{
        background: linear-gradient(90deg, {PYTHON_BLUE}, {PYTHON_YELLOW});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }}
    </style>
    """
