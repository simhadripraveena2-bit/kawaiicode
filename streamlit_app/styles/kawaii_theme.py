"""
KawaiiCode Custom CSS Theme
Pink/Purple anime-inspired styling for Streamlit
"""

KAWAII_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Quicksand:wght@300..700&display=swap');
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0');

:root {
    --gojo-dark: #0a0a1a;
    --gojo-deep: #12122a;
    --gojo-purple: #6c5ce7;
    --gojo-violet: #a55eea;
    --gojo-blue: #74b9ff;
    --gojo-cyan: #81ecec;
    --gojo-accent: #fd79a8;
    --gojo-white: #dfe6e9;
    --gojo-gradient: linear-gradient(135deg, #6c5ce7 0%, #a55eea 50%, #74b9ff 100%);
    --gojo-glow: 0 0 20px rgba(108, 92, 231, 0.5);
}

.stApp {
    background: linear-gradient(180deg, #0a0a1a 0%, #12122a 50%, #1a1a3a 100%);
}

.stApp > header {
    background: #0a0a1a !important;
}

/* Hide Streamlit's default header bar */
header[data-testid="stHeader"] {
    background: #0a0a1a !important;
}

/* Fix iframe/embed backgrounds */
iframe, .stApp iframe {
    background: #0a0a1a !important;
}

/* Ensure all text is visible on dark background */
p, span, div, label {
    color: #dfe6e9 !important;
}

h4, h5, h6 {
    color: #81ecec !important;
}

/* Fix markdown text */
.stMarkdown, .stMarkdown p, .stMarkdown span {
    color: #dfe6e9 !important;
}

/* Fix code blocks */
code {
    background: rgba(108, 92, 231, 0.2) !important;
    color: #81ecec !important;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
}

pre {
    background: #0a0a14 !important;
    border: 1px solid rgba(108, 92, 231, 0.3) !important;
    border-radius: 8px !important;
}

h1, h2, h3 {
    font-family: 'Fredoka', sans-serif !important;
    color: var(--gojo-cyan) !important;
    text-shadow: 0 0 10px rgba(129, 236, 236, 0.3);
}

p, span:not([data-testid]), div:not([class*="icon"]):not([class*="Icon"]) {
    font-family: 'Quicksand', sans-serif;
}

/* Hide broken Streamlit icon text */
[data-testid="stExpanderToggleIcon"],
.streamlit-expanderHeader svg,
button[kind="header"] span,
span[class*="eyeqlp"] {
    font-size: 0 !important;
    visibility: hidden !important;
}

/* Also hide via content filter */
span:not([class]) {
    font-family: 'Quicksand', sans-serif;
}

/* Hide keyboard_arrow text artifacts */
[data-testid="stSidebar"] span:empty,
.stExpander span[aria-hidden] {
    display: none !important;
}

.main-title {
    background: var(--gojo-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 3.5rem !important;
    font-weight: 700 !important;
    text-align: center;
    margin-bottom: 0 !important;
    filter: drop-shadow(0 0 20px rgba(108, 92, 231, 0.5));
}

.tagline {
    text-align: center;
    color: var(--gojo-blue);
    font-size: 1.3rem;
    margin-top: 0.5rem;
    font-weight: 500;
}

.arc-card {
    background: rgba(18, 18, 42, 0.9);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 0.8rem 0;
    box-shadow: 0 4px 15px rgba(108, 92, 231, 0.2);
    border: 2px solid rgba(108, 92, 231, 0.3);
    transition: all 0.3s ease;
    cursor: pointer;
}

.arc-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(108, 92, 231, 0.5), 0 0 30px rgba(165, 94, 234, 0.3);
    border-color: var(--gojo-purple);
}

.arc-card.locked {
    opacity: 0.5;
    filter: grayscale(60%);
}

.arc-title {
    font-family: 'Fredoka', sans-serif !important;
    font-size: 1.4rem !important;
    font-weight: 600 !important;
    margin-bottom: 0.3rem !important;
    color: var(--gojo-white) !important;
}

.arc-topic {
    color: var(--gojo-violet);
    font-size: 0.9rem;
    font-weight: 500;
}

.arc-description {
    color: #a0a0b0;
    font-size: 0.95rem;
    margin-top: 0.5rem;
}

.xp-bar {
    background: var(--gojo-gradient);
    height: 8px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(108, 92, 231, 0.5);
}

.xp-container {
    background: rgba(30, 30, 60, 0.8);
    height: 8px;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 0.5rem;
}

.character-bubble {
    background: rgba(18, 18, 42, 0.95);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 4px 15px rgba(108, 92, 231, 0.2);
    border-left: 4px solid var(--gojo-purple);
    position: relative;
}

.character-bubble::before {
    content: '';
    position: absolute;
    left: -10px;
    top: 20px;
    width: 0;
    height: 0;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-right: 10px solid rgba(18, 18, 42, 0.95);
}

.character-name {
    font-family: 'Fredoka', sans-serif !important;
    color: var(--gojo-cyan);
    font-weight: 600;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 10px rgba(129, 236, 236, 0.3);
}

.mission-card {
    background: rgba(18, 18, 42, 0.9);
    border-radius: 15px;
    padding: 1.2rem;
    margin: 0.5rem 0;
    box-shadow: 0 2px 10px rgba(108, 92, 231, 0.2);
    border: 1px solid rgba(108, 92, 231, 0.3);
}

.mission-title {
    font-family: 'Fredoka', sans-serif !important;
    font-size: 1.2rem !important;
    color: var(--gojo-white) !important;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.8rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
}

.difficulty-easy {
    background: rgba(129, 236, 236, 0.2);
    color: var(--gojo-cyan);
    border: 1px solid var(--gojo-cyan);
}

.difficulty-medium {
    background: rgba(108, 92, 231, 0.2);
    color: var(--gojo-purple);
    border: 1px solid var(--gojo-purple);
}

.difficulty-hard {
    background: rgba(253, 121, 168, 0.2);
    color: var(--gojo-accent);
    border: 1px solid var(--gojo-accent);
}

.difficulty-boss {
    background: linear-gradient(135deg, rgba(108, 92, 231, 0.3), rgba(165, 94, 234, 0.3));
    color: var(--gojo-violet);
    border: 1px solid var(--gojo-violet);
    box-shadow: 0 0 15px rgba(165, 94, 234, 0.4);
}

.code-editor-container {
    background: #0d0d1a;
    border-radius: 15px;
    padding: 1rem;
    margin: 1rem 0;
    border: 1px solid rgba(108, 92, 231, 0.3);
}

.output-panel {
    background: #0a0a14;
    border-radius: 10px;
    padding: 1rem;
    color: var(--gojo-cyan);
    font-family: 'Fira Code', monospace;
    min-height: 100px;
    border: 1px solid rgba(129, 236, 236, 0.2);
}

.stButton > button {
    background: var(--gojo-gradient) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.6rem 2rem !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(108, 92, 231, 0.4), 0 0 20px rgba(108, 92, 231, 0.2) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 25px rgba(108, 92, 231, 0.6), 0 0 30px rgba(165, 94, 234, 0.4) !important;
}

.stats-card {
    background: rgba(18, 18, 42, 0.9);
    border-radius: 15px;
    padding: 1rem 1.5rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(108, 92, 231, 0.2);
    border: 1px solid rgba(108, 92, 231, 0.3);
}

.stats-value {
    font-family: 'Fredoka', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    color: var(--gojo-cyan) !important;
    text-shadow: 0 0 15px rgba(129, 236, 236, 0.4);
}

.stats-label {
    color: #8080a0;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.world-map-container {
    background: linear-gradient(180deg, rgba(10, 10, 26, 0.95) 0%, rgba(18, 18, 42, 0.95) 100%);
    border-radius: 25px;
    padding: 2rem;
    margin: 1rem 0;
    border: 1px solid rgba(108, 92, 231, 0.3);
}

.region-node {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    box-shadow: 0 4px 15px rgba(108, 92, 231, 0.3), 0 0 20px rgba(108, 92, 231, 0.2);
    transition: all 0.3s ease;
    cursor: pointer;
}

.region-node:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 25px rgba(108, 92, 231, 0.5), 0 0 30px rgba(165, 94, 234, 0.4);
}

.stTextArea textarea {
    font-family: 'Fira Code', monospace !important;
    background: #0a0a14 !important;
    color: var(--gojo-white) !important;
    border-radius: 10px !important;
    border: 2px solid rgba(108, 92, 231, 0.5) !important;
}

.success-message {
    background: linear-gradient(135deg, rgba(129, 236, 236, 0.2), rgba(116, 185, 255, 0.2));
    color: var(--gojo-cyan);
    padding: 1rem;
    border-radius: 15px;
    text-align: center;
    font-weight: 600;
    animation: glow 2s infinite;
    border: 1px solid var(--gojo-cyan);
}

@keyframes glow {
    0%, 100% { box-shadow: 0 0 10px rgba(129, 236, 236, 0.3); }
    50% { box-shadow: 0 0 25px rgba(129, 236, 236, 0.5); }
}

.error-message {
    background: linear-gradient(135deg, rgba(253, 121, 168, 0.2), rgba(255, 107, 107, 0.2));
    color: var(--gojo-accent);
    padding: 1rem;
    border-radius: 15px;
    text-align: center;
    font-weight: 600;
    border: 1px solid var(--gojo-accent);
}

.sidebar .sidebar-content {
    background: linear-gradient(180deg, #0a0a1a 0%, #12122a 100%) !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0a1a 0%, #12122a 100%) !important;
}

[data-testid="stSidebar"] * {
    color: var(--gojo-white) !important;
}

.stProgress > div > div {
    background: var(--gojo-gradient) !important;
    box-shadow: 0 0 10px rgba(108, 92, 231, 0.5);
}
</style>
"""

def inject_kawaii_css():
    """Inject the Kawaii CSS theme into the Streamlit app."""
    import streamlit as st
    st.markdown(KAWAII_CSS, unsafe_allow_html=True)
