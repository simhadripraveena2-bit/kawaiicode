import streamlit as st
import time
from data.content_data import get_all_arcs, get_languages
from components.mission_view import get_completed_arcs_for_lang, get_current_arc_for_lang

# --- 1. THE GREAT ATLAS ---
CONTINENT_DATA = {
    "python": {"name": "Python Highlands", "icon": "🐍", "color": "#2ecc71", "cat": "Core", "desc": "The lush forest of clean syntax."},
    "c": {"name": "The C Citadel", "icon": "🛡️", "color": "#95a5a6", "cat": "Core", "desc": "The foundational stone of the world."},
    "cpp": {"name": "C++ Power Peaks", "icon": "⚙️", "color": "#3498db", "cat": "Core", "desc": "High-performance mountain ranges."},
    "java": {"name": "Java Enterprise Estate", "icon": "☕", "color": "#e67e22", "cat": "Core", "desc": "The bustling city of objects."},

    "html_css": {"name": "The Styling Shores", "icon": "🎨", "color": "#ff7675", "cat": "Web", "desc": "The colorful coast of design."},
    "javascript": {"name": "JS Neon Isles", "icon": "⚡", "color": "#f1c40f", "cat": "Web", "desc": "Electric islands of interactivity."},
    "react": {"name": "React Reef", "icon": "⚛️", "color": "#61dafb", "cat": "Web", "desc": "The modern flow of components."},
    "php": {"name": "The PHP Port", "icon": "🐘", "color": "#8e44ad", "cat": "Web", "desc": "The classic trade route of the web."},

    "sql": {"name": "The SQL Abyss", "icon": "💎", "color": "#3498db", "cat": "Data", "desc": "Structured depths of data (SQL)."},
    "mongodb": {"name": "NoSQL Oasis", "icon": "🍃", "color": "#00b894", "cat": "Data", "desc": "Flexible sands of documents (MongoDB)."},
    "dsa": {"name": "The Logic Labyrinth", "icon": "🧩", "color": "#a55eea", "cat": "Data", "desc": "Ancient puzzles of efficiency (DSA)."},
    "ml": {"name": "Predictive Plains", "icon": "🤖", "color": "#fdcb6e", "cat": "Data", "desc": "Fields where machines learn (ML)."},
    "dl": {"name": "Neural Node", "icon": "🧠", "color": "#0984e3", "cat": "Data", "desc": "Deep layers of artificial thought (DL)."},
    "cv": {"name": "The All-Seeing Eye", "icon": "👁️", "color": "#e17055", "cat": "Data", "desc": "Where machines learn to see (CV)."},
    "nlp": {"name": "The Linguist Tower", "icon": "🗣️", "color": "#fab1a0", "cat": "Data", "desc": "Understanding the human tongue (NLP)."},
    "ai": {"name": "The Oracle's Sanctum", "icon": "🔮", "color": "#6c5ce7", "cat": "Data", "desc": "The peak of machine intelligence (AI)."},

    "devops": {"name": "The DevOps Dock", "icon": "⚓", "color": "#d63031", "cat": "Tools", "desc": "Shipping and versioning logic (GIT)."},
    "excel": {"name": "Spreadsheet Steppes", "icon": "📊", "color": "#27ae60", "cat": "Tools", "desc": "The classic plains of data (EXCEL)."},
    "powerbi": {"name": "The Insight Forge", "icon": "📈", "color": "#f39c12", "cat": "Tools", "desc": "Visualizing the realm's stats (POWER BI)."},
    "dataeng": {"name": "The Pipeline Path", "icon": "🏗️", "color": "#2d3436", "cat": "Tools", "desc": "Building the world's plumbing (DE)."},
    "ba": {"name": "The Strategist's Tent", "icon": "🗺️", "color": "#ffeaa7", "cat": "Tools", "desc": "Analyzing kingdom needs (DA)."}
}

ARC_ICONS = {"village": "🏡", "valley": "⛰️", "forest": "🌲", "kingdom": "🏰", "library": "📚", "terminal": "💻"}

def render_world_map():
    if "map_view" not in st.session_state:
        st.session_state.map_view = "global"

    if st.session_state.map_view == "global":
        render_global_ocean()
    else:
        render_local_realm(st.session_state.current_language)

def render_global_ocean():
    nav_col, title_col, space_col = st.columns([1, 1, 1])

    with nav_col:
        if st.button("⬅️ Mastery Paths", use_container_width=True):
            st.session_state.current_page = "landing"
            st.session_state.landing_view = "main"
            st.rerun()

    st.markdown("""
    <div style="text-align: center; margin-top: -1rem; margin-bottom: 1rem;">
        <h1 style="font-family: 'Fredoka', sans-serif; color: #81ecec; font-size: 3rem; text-shadow: 0 0 15px rgba(129,236,236,0.4);">
            🗺️ The Great Sea of Code
        </h1>
    </div>
    """, unsafe_allow_html=True)

    # --- THE COMPATIBILITY FIX ---
    categories = ["Core", "Web", "Data", "Tools"]
    cat_icons = ["🛡️ Core Logic", "🌐 Web & Mobile", "🔮 Data & AI", "🛠️ Tools & BA"]

    # Get the index from session state (set by app.py)
    default_idx = st.session_state.get("active_tab_index", 0)

    # We use st.radio with horizontal=True as a reliable segmented control
    selected_label = st.radio(
        "Explore Sectors", 
        options=cat_icons, 
        index=default_idx,
        horizontal=True,
        key="map_sector_selector",
        label_visibility="collapsed" # Hides the 'Explore Sectors' text for a cleaner look
    )

    # Mapping label back to internal category ID
    current_cat = "Core"
    if selected_label:
        current_cat = categories[cat_icons.index(selected_label)]

    st.markdown("<br>", unsafe_allow_html=True)

    # Filter and Display Languages
    langs = {k: v for k, v in CONTINENT_DATA.items() if v['cat'] == current_cat}
    cols = st.columns(2)

    for idx, (key, info) in enumerate(langs.items()):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {info['color']}15 0%, #12122a 100%);
                border: 2px solid {info['color']}44;
                border-radius: 20px;
                padding: 1.5rem;
                text-align: center;
                margin-bottom: 1rem;
                min-height: 200px;
            ">
                <div style="font-size: 3rem; margin-bottom: 10px;">{info['icon']}</div>
                <h3 style="color: {info['color']}; margin: 0; font-family: 'Fredoka';">{info['name']}</h3>
                <p style="color: #8080a0; font-size: 0.85rem; margin-top: 8px;">{info['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Sail to {info['name']}", key=f"sail_{key}", use_container_width=True):
                st.session_state.current_language = key
                st.session_state.map_view = "local"
                st.rerun()

def render_local_realm(language):
    land = CONTINENT_DATA.get(language, CONTINENT_DATA["python"])

    if st.button("⬅️ Return to Global Sea"):
        st.session_state.map_view = "global"
        st.rerun()

    st.markdown(f"""
    <div style="text-align: center; padding: 1.5rem; background: rgba(129, 236, 236, 0.1); border-radius: 20px; border: 1px solid {land['color']}55; margin-bottom: 2rem;">
        <h1 style="color: {land['color']}; margin: 0;">{land['name']}</h1>
        <p style="color: #a0a0b0;">Complete the Arcs to master this language.</p>
    </div>
    """, unsafe_allow_html=True)

    arcs = get_all_arcs(language)
    curr_unlocked = get_current_arc_for_lang(language)
    completed = get_completed_arcs_for_lang(language)

    for idx, arc in enumerate(arcs):
        is_unlocked = arc["id"] <= curr_unlocked
        is_done = arc["id"] in completed
        col_layout = [1, 2, 1]
        align = idx % 3 

        if idx > 0:
            st.markdown(f"<div style='display:flex; justify-content:center; margin:-10px 0;'><div style='width:4px; height:40px; background:{land['color'] if is_unlocked else '#333'};'></div></div>", unsafe_allow_html=True)

        cols = st.columns(col_layout)
        with cols[align]:
            st.markdown(f"""
            <div style="
                background: {'#1a1a2e' if is_unlocked else '#0a0a0a'};
                border: 2px solid {land['color'] if is_unlocked else '#333'};
                padding: 1rem; border-radius: 15px; text-align: center;
                opacity: {1 if is_unlocked else 0.5};
            ">
                <div style="font-size: 1.5rem;">{'✅' if is_done else (ARC_ICONS.get(arc.get('icon_key'), '📍') if is_unlocked else '🔒')}</div>
                <b style="color: {land['color'] if is_unlocked else '#666'};">Arc {arc['id']}</b><br>
                <span style="font-size: 0.8rem; color: #888;">{arc['name']}</span>
            </div>
            """, unsafe_allow_html=True)

            if is_unlocked:
                if st.button("Enter", key=f"enter_{language}_{arc['id']}", use_container_width=True):
                    st.session_state.current_page = "arc"
                    st.session_state.selected_arc = arc["id"]
                    st.rerun()

def render_arc_preview(arc_id, language):
    from data.content_data import get_arc_by_id
    arc = get_arc_by_id(arc_id, language)
    if arc:
        st.markdown(f"""
        <div style="background: rgba(108, 92, 231, 0.1); padding: 2rem; border-radius: 20px; border-left: 5px solid #81ecec; margin-bottom: 2rem;">
            <h2 style="color: #81ecec; margin: 0;">{arc['name']}</h2>
            <p style="color: #a0a0b0; font-style: italic;">{arc.get('topic', 'A new challenge awaits...')}</p>
        </div>
        """, unsafe_allow_html=True)