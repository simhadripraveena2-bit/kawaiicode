"""
KawaiiCode - Learn Coding the Cute Way
Main Streamlit Application - Multi-Language Support
"""

import streamlit as st
import sys
import os
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from styles.kawaii_theme import inject_kawaii_css
from components.world_map import render_world_map, render_arc_preview
from components.mission_view import render_mission, render_mission_list
from data.content_data import get_arc_by_id, get_all_arcs, calculate_level, get_languages

st.set_page_config(
    page_title="KawaiiCode - Learn Coding the Fun Way",
    page_icon="sparkles",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_kawaii_css()

ALL_LANGUAGES = ["python", "javascript", "html_css", "c", "cpp", "java", "sql", "dsa", "react", "mongodb", "php", "devops", "ml", "dl", "cv", "nlp", "ai", "excel", "powerbi", "dataeng", "ba"]

ARTIFACTS = {
    1: {"name": "Syntax Scroll", "icon": "📜", "desc": "The basics are now your weapon."},
    2: {"name": "Logic Blade", "icon": "🗡️", "desc": "You cut through loops with ease."},
    3: {"name": "Data Crystal", "icon": "🔮", "desc": "Complex structures become clear."},
    4: {"name": "Architect's Compass", "icon": "🧭", "desc": "Navigation is second nature."},
    5: {"name": "Master's Key", "icon": "🗝️", "desc": "The realm's secrets are yours."}
}

def init_session_state():
    """Initialize session state with proper structure for multi-language support."""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "landing"
    if "selected_arc" not in st.session_state:
        st.session_state.selected_arc = 1
    if "selected_mission" not in st.session_state:
        st.session_state.selected_mission = 1
    if "user_xp" not in st.session_state:
        st.session_state.user_xp = 0
    if "current_language" not in st.session_state:
        st.session_state.current_language = "python"
    
    if "completed_missions" not in st.session_state:
        st.session_state.completed_missions = {lang: [] for lang in ALL_LANGUAGES}
    elif isinstance(st.session_state.completed_missions, list):
        old_missions = st.session_state.completed_missions
        st.session_state.completed_missions = {lang: [] for lang in ALL_LANGUAGES}
        st.session_state.completed_missions["python"] = old_missions
    elif isinstance(st.session_state.completed_missions, dict):
        for lang in ALL_LANGUAGES:
            if lang not in st.session_state.completed_missions:
                st.session_state.completed_missions[lang] = []
    
    if "current_arc" not in st.session_state:
        st.session_state.current_arc = {lang: 1 for lang in ALL_LANGUAGES}
    elif isinstance(st.session_state.current_arc, int):
        old_arc = st.session_state.current_arc
        st.session_state.current_arc = {lang: 1 for lang in ALL_LANGUAGES}
        st.session_state.current_arc["python"] = old_arc
    elif isinstance(st.session_state.current_arc, dict):
        for lang in ALL_LANGUAGES:
            if lang not in st.session_state.current_arc:
                st.session_state.current_arc[lang] = 1
    
    if "completed_arcs" not in st.session_state:
        st.session_state.completed_arcs = {lang: [] for lang in ALL_LANGUAGES}
    elif isinstance(st.session_state.completed_arcs, list):
        old_arcs = st.session_state.completed_arcs
        st.session_state.completed_arcs = {lang: [] for lang in ALL_LANGUAGES}
        st.session_state.completed_arcs["python"] = old_arcs
    elif isinstance(st.session_state.completed_arcs, dict):
        for lang in ALL_LANGUAGES:
            if lang not in st.session_state.completed_arcs:
                st.session_state.completed_arcs[lang] = []
    if "last_mission_date" not in st.session_state:
        st.session_state.last_mission_date = None
    if "user_streak" not in st.session_state:
        st.session_state.user_streak = 0
    if "daily_quest_completed" not in st.session_state:
        st.session_state.daily_quest_completed = False

init_session_state()

def get_completed_missions():
    """Get completed missions for current language."""
    lang = st.session_state.current_language
    return st.session_state.completed_missions.get(lang, [])

def add_completed_mission(mission_id):
    """Add a completed mission for current language."""
    lang = st.session_state.current_language
    if lang not in st.session_state.completed_missions:
        st.session_state.completed_missions[lang] = []
    if mission_id not in st.session_state.completed_missions[lang]:
        st.session_state.completed_missions[lang].append(mission_id)

def get_completed_arcs():
    """Get completed arcs for current language."""
    lang = st.session_state.current_language
    return st.session_state.completed_arcs.get(lang, [])

def add_completed_arc(arc_id):
    """Add a completed arc for current language."""
    lang = st.session_state.current_language
    if lang not in st.session_state.completed_arcs:
        st.session_state.completed_arcs[lang] = []
    if arc_id not in st.session_state.completed_arcs[lang]:
        st.session_state.completed_arcs[lang].append(arc_id)

def get_current_arc():
    """Get current arc for current language."""
    lang = st.session_state.current_language
    return st.session_state.current_arc.get(lang, 1)

def set_current_arc(arc_id):
    """Set current arc for current language."""
    lang = st.session_state.current_language
    st.session_state.current_arc[lang] = arc_id

def update_arc_progression():
    """Update current_arc based on completed missions."""
    lang = st.session_state.current_language
    arcs = get_all_arcs(lang)
    completed = get_completed_missions()
    
    for arc in arcs:
        arc_missions = [m['id'] for m in arc.get('missions', [])]
        if arc_missions:
            completed_in_arc = [m for m in arc_missions if m in completed]
            if len(completed_in_arc) == len(arc_missions):
                add_completed_arc(arc['id'])
                max_arc = len(arcs)
                next_arc = arc['id'] + 1
                if next_arc <= max_arc and next_arc > get_current_arc():
                    set_current_arc(next_arc)

def render_sidebar():
    """Render the full Fantasy-themed Hero Sidebar."""

    # --- CSS FIX: Prevent white/gray backgrounds on click ---
    st.markdown("""
    <style>
        /* Keep sidebar buttons themed even when focused/active */
        .stSidebar .stButton > button {
            background-color: rgba(108, 92, 231, 0.1) !important;
            color: #dcdde1 !important;
            border: 1px solid rgba(108, 92, 231, 0.3) !important;
        }
        .stSidebar .stButton > button:hover {
            border-color: #81ecec !important;
            color: white !important;
            background: rgba(108, 92, 231, 0.2) !important;
        }
        .stSidebar .stButton > button:active, .stSidebar .stButton > button:focus {
            background-color: #6c5ce7 !important;
            color: white !important;
            box-shadow: 0 0 15px rgba(108, 92, 231, 0.5) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    lang = st.session_state.current_language

    with st.sidebar:
        # --- 2. HERO IDENTITY & RANK ---
        st.markdown(f"""
        <div style="text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1rem; margin-bottom: 1rem;">
            <div style="font-size: 3rem; filter: drop-shadow(0 0 10px #81ecec);">🧙‍♂️</div>
            <h2 style="font-family: 'Fredoka', sans-serif; color: #81ecec; margin:0;">Hero Profile</h2>
            <p style="color: #a55eea; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px;">
                {lang.replace('_', ' ').upper()} MASTER
            </p>
        </div>
        """, unsafe_allow_html=True)

        # --- 3. DYNAMIC PROGRESS & STATS ---
        level, xp_in_level, xp_needed = calculate_level(st.session_state.user_xp)
        completed_arcs = get_completed_arcs() # List of IDs like [1, 2]

        # Realm Conquest Bar
        total_arcs = 12 
        progress_pct = (len(completed_arcs) / total_arcs) * 100

        st.markdown(f"""
        <div style="background: rgba(18, 18, 42, 0.6); padding: 12px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
            <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #8080a0; margin-bottom: 4px;">
                <span>REALM CONQUEST</span>
                <span>{int(progress_pct)}%</span>
            </div>
            <div style="background: #1e1e3c; height: 8px; border-radius: 10px; margin-bottom: 12px;">
                <div style="background: linear-gradient(90deg, #55efc4, #81ecec); width: {progress_pct}%; height: 100%; border-radius: 10px;"></div>
            </div>
            <div style="display: flex; justify-content: space-around; text-align: center;">
                <div><div style="color: #a55eea; font-weight: bold; font-size: 1.1rem;">{level}</div><div style="font-size: 0.6rem; color: #8080a0;">LVL</div></div>
                <div style="border-left: 1px solid rgba(255,255,255,0.1);"></div>
                <div><div style="color: #74b9ff; font-weight: bold; font-size: 1.1rem;">{st.session_state.user_xp}</div><div style="font-size: 0.6rem; color: #8080a0;">MANA (XP)</div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # --- 4. ARTIFACT INVENTORY (The Loot Slots) ---
        st.markdown("<p style='font-size: 0.7rem; color: #8080a0; font-weight: bold; margin: 15px 0 5px 0;'>INVENTORY</p>", unsafe_allow_html=True)

        artifact_cols = st.columns(4)
        for i in range(1, 5): 
            with artifact_cols[i-1]:
                if i in completed_arcs:
                    item = ARTIFACTS.get(i, {"icon": "🎁", "name": "Mystery"})
                    st.markdown(f"""
                    <div title="{item['name']}: {item['desc']}" style="background: rgba(165, 94, 234, 0.15); border: 1px solid #a55eea; border-radius: 8px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">
                        {item['icon']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="background: rgba(255,255,255,0.02); border: 1px dashed rgba(255,255,255,0.1); border-radius: 8px; height: 40px; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.1);">
                        🔒
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # --- 5. NAVIGATION REALMS ---
        if st.button("🗺️ World Map", use_container_width=True):
            st.session_state.current_page = "world_map"
            st.rerun()

        if st.button("🏆 Mastery Paths", use_container_width=True):
            st.session_state.current_page = "landing"
            st.session_state.landing_view = "main"
            st.rerun()

        st.markdown("---")

        # --- 6. REALM CATEGORIES (Expanders) ---
        with st.expander("🛡️ Foundation Pillars"):
            for name, key in [("Python", "python"), ("C", "c"), ("C++", "cpp"), ("Java", "java")]:
                if st.button(name, key=f"side_{key}", use_container_width=True):
                    st.session_state.current_language = key
                    st.session_state.current_page = "world_map"
                    st.rerun()

        with st.expander("🌐 Portal Crafters"):
            for name, key in [("HTML/CSS", "html_css"), ("JS", "javascript"), ("React", "react")]:
                if st.button(name, key=f"side_{key}", use_container_width=True):
                    st.session_state.current_language = key
                    st.session_state.current_page = "world_map"
                    st.rerun()

        with st.expander("🔮 Oracle's Sanctum"):
            for name, key in [("SQL", "sql"), ("ML", "ml"), ("AI", "ai"), ("DSA", "dsa")]:
                if st.button(name, key=f"side_{key}", use_container_width=True):
                    st.session_state.current_language = key
                    st.session_state.current_page = "world_map"
                    st.rerun()

        # --- 7. DYNAMIC STREAK & DAILY QUEST ---
        streak = st.session_state.get("user_streak", 0)
        quest_done = st.session_state.get("daily_quest_completed", False)
        quest_color = "#55efc4" if quest_done else "#ff7675"
        quest_status = "✅ QUEST COMPLETE" if quest_done else "⚔️ ACTIVE DAILY QUEST"

        st.markdown(f"""
        <div style="margin-top: 2rem; text-align: center; padding: 12px; background: rgba({int(not quest_done)*255}, {int(quest_done)*239}, 117, 0.1); border-radius: 12px; border: 1px solid {quest_color}44;">
            <div style="font-size: 1.2rem; margin-bottom: 2px;">{'🔥' if streak > 0 else '🛡️'}</div>
            <span style="color: {quest_color}; font-size: 0.75rem; font-weight: bold; letter-spacing: 1px;">{streak} DAY SPIRIT STREAK</span>
            <p style="margin: 5px 0 0 0; font-size: 0.65rem; color: #a0a0b0;">{quest_status}</p>
        </div>
        """, unsafe_allow_html=True)

def render_landing_page():
    """Render the themed curriculum overview landing page."""

    st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem;">
        <h1 class="main-title">KawaiiCode</h1>
        <p style="color: #81ecec; font-size: 1.3rem; margin-top: 0.5rem; font-weight: 500;">Learn Coding the Fun Way</p>
    </div>
    """, unsafe_allow_html=True)

    if "landing_view" not in st.session_state:
        st.session_state.landing_view = "main"

    # --- ACTION: BACK BUTTON ---
    if st.session_state.landing_view != "main":
        if st.button("⬅ Back to Mastery Paths"):
            st.session_state.landing_view = "main"
            st.rerun()

    # --- CATEGORY DATA DEFINITION ---
    categories = {
        "core": {
            "title": "1. Core Logic: The Foundation Pillars",
            "focus": "Mastering the fundamental rules of the digital world.",
            "vibe": "Building the 'Iron Roots' of the realm.",
            "color": "#ff7675",
            "icon": "🛡️",
            "langs": [
                ("Python", "python"), ("C", "c"), ("C++", "cpp"), 
                ("Java", "java")
            ]
        },
        "web": {
            "title": "2. Web & Mobile: The Portal Crafters",
            "focus": "Creating beautiful interfaces and windows into the realm.",
            "vibe": "Designing the magical 'Mirrors and Gates' users interact with.",
            "color": "#74b9ff",
            "icon": "🌐",
            "langs": [
                ("HTML/CSS", "html_css"), ("JavaScript", "javascript"), 
                ("React", "react"), ("PHP", "php")
            ]
        },
        "data": {
            "title": "3. Data & Logic: The Oracle’s Sanctum",
            "focus": "Managing vast records and teaching golems to think.",
            "vibe": "Consulting the 'Infinite Scrolls' and awakening the 'Great Golem.'",
            "color": "#a55eea",
            "icon": "🔮",
            "langs": [
                ("SQL", "sql"), ("MongoDB", "mongodb"), ("DSA", "dsa"), 
                ("ML", "ml"), ("DL", "dl"), ("CV", "cv"), ("NLP", "nlp"), ("AI", "ai")
            ]
        },
        "tools": {
            "title": "4. Tools: The Architect’s Workshop",
            "focus": "Controlling time, moving data, and strategic planning.",
            "vibe": "Managing the 'Temporal Gates' and 'Mana Pipelines' of the kingdom.",
            "color": "#55efc4",
            "icon": "⚒️",
            "langs": [
                ("Git/DevOps", "devops"), ("Excel", "excel"), 
                ("Power BI", "powerbi"), ("Data Eng", "dataeng"), ("BA", "ba")
            ]
        }
    }

    # --- VIEW: MAIN CATEGORY SELECTION ---
    if st.session_state.landing_view == "main":
        st.markdown("<h1 style='text-align: center; color: #81ecec;'>Choose Your Mastery Path</h1>", unsafe_allow_html=True)

        # Display 2x2 Grid of Category Cards
        col1, col2 = st.columns(2)
        cat_keys = list(categories.keys())

        for i, key in enumerate(cat_keys):
            target_col = col1 if i % 2 == 0 else col2
            cat = categories[key]

            with target_col:
                st.markdown(f"""
                <div style="
                    background: rgba(18, 18, 42, 0.9);
                    border-radius: 20px;
                    padding: 1.5rem;
                    border: 1px solid rgba(108, 92, 231, 0.3);
                    border-top: 5px solid {cat['color']};
                    margin-bottom: 20px;
                    min-height: 220px;
                ">
                    <h3 style="color: {cat['color']}; margin-bottom: 0px;">{cat['icon']} {cat['title']}</h3>
                    <p style="color: #a0a0b0; font-size: 0.9rem; margin-top: 10px;"><b>Focus:</b> {cat['focus']}</p>
                    <p style="color: #81ecec; font-style: italic; font-size: 0.85rem;">Vibe: {cat['vibe']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Enter {cat['icon']} {key.title()}", key=f"cat_{key}", use_container_width=True):
                    tab_mapping = {
                        "core": 0,
                        "web": 1,
                        "data": 2,
                        "tools": 3
                    }
                    st.session_state.current_language = cat['langs'][0][1] 

                    st.session_state.active_tab_index = tab_mapping.get(key, 0)

                    st.session_state.current_page = "world_map"
                    st.session_state.map_view = "global"
                    st.rerun()

    else:
        view = st.session_state.landing_view
        cat = categories[view]

        st.markdown(f"""
            <div style="text-align: center; padding: 2rem;">
                <h1 style="color: {cat['color']};">{cat['icon']} {cat['title']}</h1>
                <p style="color: #a0a0b0;">{cat['focus']}</p>
            </div>
        """, unsafe_allow_html=True)

        st.info(f"✨ Select a language scroll to begin your journey in the {cat['icon']} {view.title()} sector.")

        # Display Languages as themed cards
        lang_cols = st.columns(3)
        for idx, (name, lang_id) in enumerate(cat['langs']):
            with lang_cols[idx % 3]:
                st.markdown(f"""
                <div style="
                    background: rgba(30, 30, 60, 0.5);
                    padding: 1rem;
                    border-radius: 15px;
                    text-align: center;
                    border: 1px solid {cat['color']}44;
                    margin-bottom: 10px;
                ">
                    <h4 style="color: white; margin: 0;">{name}</h4>
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"Begin {name}", key=f"start_{lang_id}", use_container_width=True):
                    st.session_state.current_language = lang_id
                    st.session_state.current_page = "world_map"
                    st.session_state.selected_arc = 1
                    st.rerun()

    # --- INTERACTIVE HERO CLASSES ---
    st.markdown("<br><br><h2 style='text-align: center; color: #81ecec; font-family: \"Fredoka\", sans-serif;'>🏆 Choose Your Hero Class</h2>", unsafe_allow_html=True)

    # Define the Quest Data
    quest_lines = {
        "analyst": {
            "name": "The Royal Analyst", "icon": "📊", "outcome": "Data Analyst", "color": "#74b9ff",
            "path": [("Python", "python"), ("SQL", "sql"), ("Excel", "excel"), ("Power BI", "powerbi"), ("BA", "ba")]
        },
        "architect": {
            "name": "The Realm Architect", "icon": "🏰", "outcome": "Full-Stack Developer", "color": "#ff7675",
            "path": [("HTML/CSS", "html_css"), ("JS", "javascript"), ("React", "react"), ("SQL", "sql"), ("DevOps", "devops")]
        },
        "whisperer": {
            "name": "The Golem Whisperer", "icon": "🤖", "outcome": "AI/ML Engineer", "color": "#a55eea",
            "path": [("Python", "python"), ("SQL", "sql"), ("ML", "ml"), ("DL", "dl"), ("AI", "ai")]
        },
        "mana_eng": {
            "name": "The Mana Engineer", "icon": "⚙️", "outcome": "Data Engineer", "color": "#55efc4",
            "path": [("Python", "python"), ("SQL", "sql"), ("DSA", "dsa"), ("DevOps", "devops"), ("Data Eng", "dataeng")]
        },
        "guardian": {
            "name": "The Systems Guardian", "icon": "🛡️", "outcome": "Systems Programmer", "color": "#ffeaa7",
            "path": [("C", "c"), ("C++", "cpp"), ("Java", "java"), ("DSA", "dsa"), ("DevOps", "devops")]
        }
    }

    # Track selection in session state
    if "selected_hero_quest" not in st.session_state:
        st.session_state.selected_hero_quest = None

    # Create the clickable list
    for key, quest in quest_lines.items():
        # Highlighting the selected card
        is_selected = st.session_state.selected_hero_quest == key
        bg_style = "background: rgba(108, 92, 231, 0.25);" if is_selected else "background: rgba(18, 18, 42, 0.9);"

        # We use a container and a button to make the whole row "clickable"
        with st.container():
            st.markdown(f"""
            <div style="{bg_style} border-left: 5px solid {quest['color']}; border-radius: 15px; padding: 1rem; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div style="display: flex; align-items: center;">
                        <span style="font-size: 2rem; margin-right: 15px;">{quest['icon']}</span>
                        <div>
                            <h4 style="margin: 0; color: {quest['color']};">{quest['name']}</h4>
                            <small style="color: #81ecec;">Class Outcome: {quest['outcome']}</small>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Click to Expand/Select
            if st.button(f"Unlock {quest['name']} Quest Path", key=f"select_{key}", use_container_width=True):
                # This grabs the internal ID (e.g., 'python') of the first step
                first_step_lang = quest['path'][0][1] 

                st.session_state.current_language = first_step_lang
                st.session_state.current_page = "world_map"
                st.session_state.selected_arc = 1
                st.rerun()

        # If this quest is selected, show the clickable language path
        if is_selected:
            st.markdown(f"<div style='padding-left: 50px; margin-bottom: 20px; border-left: 2px dashed {quest['color']};'>", unsafe_allow_html=True)
            st.info(f"✨ Journey to becoming a {quest['outcome']}: Click a skill to start!")

            # Show path as buttons
            cols = st.columns(len(quest['path']))
            for idx, (lang_label, lang_id) in enumerate(quest['path']):
                with cols[idx]:
                    if st.button(f"Step {idx+1}\n{lang_label}", key=f"path_{key}_{lang_id}", use_container_width=True):
                        st.session_state.current_language = lang_id
                        st.session_state.current_page = "world_map"
                        st.session_state.selected_arc = 1
                        st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)


def render_dashboard():
    """Render the user dashboard."""
    lang = st.session_state.current_language
    languages = get_languages()
    lang_info = languages.get(lang, languages["python"])
    
    st.markdown(f"""
    <h1 style="font-family: 'Fredoka', sans-serif; color: #81ecec; text-align: center; text-shadow: 0 0 15px rgba(129, 236, 236, 0.3);">
        Your {lang_info['name']} Dashboard
    </h1>
    """, unsafe_allow_html=True)
    
    level, xp_in_level, xp_needed = calculate_level(st.session_state.user_xp)
    completed = get_completed_missions()
    current_arc_id = get_current_arc()
    
    col1, col2, col3, col4 = st.columns(4)
    
    stats = [
        ("Level", level, "#6c5ce7"),
        ("Total XP", st.session_state.user_xp, "#a55eea"),
        ("Missions Done", len(completed), "#81ecec"),
        ("Current Arc", current_arc_id, "#74b9ff")
    ]
    
    for col, (label, value, color) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(f"""
            <div style="
                background: rgba(18, 18, 42, 0.9);
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                box-shadow: 0 4px 15px rgba(108, 92, 231, 0.2);
                border-top: 4px solid {color};
                border: 1px solid rgba(108, 92, 231, 0.3);
            ">
                <div style="font-size: 2.5rem; font-weight: 700; color: #a55eea; text-shadow: 0 0 10px rgba(165, 94, 234, 0.3);">
                    {value}
                </div>
                <div style="color: #a0a0b0; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">
                    {label}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Continue Learning", use_container_width=True, type="primary"):
            st.session_state.current_page = "arc"
            st.session_state.selected_arc = current_arc_id
            st.rerun()
    with col2:
        if st.button("View World Map", use_container_width=True):
            st.session_state.current_page = "world_map"
            st.rerun()


def render_arc_page():
    """Render the arc/saga page."""
    lang = st.session_state.current_language

    # Logic to go back
    if st.button("⬅️ Back to Map"):
        st.session_state.current_page = "world_map"
        # Optional: ensure we return to the 'local' view of the map
        st.session_state.map_view = "local"
        st.rerun()

    # Display the header and mission list
    render_arc_preview(st.session_state.selected_arc, lang)
    render_mission_list(st.session_state.selected_arc, lang)


def main():
    """Main application entry point."""
    update_arc_progression()
    render_sidebar()
    
    if st.session_state.current_page == "landing":
        render_landing_page()
    elif st.session_state.current_page == "world_map":
        render_world_map()
    elif st.session_state.current_page == "dashboard":
        render_dashboard()
    elif st.session_state.current_page == "arc":
        render_arc_page()
    elif st.session_state.current_page == "mission":
        lang = st.session_state.current_language
        render_mission(st.session_state.selected_arc, st.session_state.selected_mission, lang)


if __name__ == "__main__":
    main()
