# 🌸 KawaiiCode

The Ultimate Gamified Coding Sanctuary. Learn 21 different disciplines—from Core Programming to Data Engineering and Business Analysis—through an anime-inspired, story-driven experience.

Live Demo: [https://kawaiicode-nfujkkr2fm5wrxlowxxj3y.streamlit.app/](https://xyqtjune54wsugtyctuua9.streamlit.app/)

# ✨ Features

- **21 Legendary Realms**: Master a massive curriculum spanning 4 distinct sectors:
    1. **🛡️ Core Logic**: Python, C, C++, Java
    2. **🌐 Web & Mobile**: HTML/CSS, JavaScript, React, PHP
    3. **🔮 Data & AI**: SQL, MongoDB, DSA, ML, Deep Learning, Computer Vision, NLP, AI
    4. **🛠️ Tools & Strategy**: Git/DevOps, Excel, Power BI/Tableau, Data Engineering, Business Analysis
- **650+ Hand-crafted Missions**: Deep content coverage across 252 Learning Arcs.
- **Narrative Learning**: Each mission is guided by unique characters, turning dry syntax into a quest for the realm.
- **Multi-Engine Code Editor**:
    1. Direct Python execution.
    2. Real-time HTML/CSS previewing.
    3. Logic-simulated execution for JS, C, C++, Java, and SQL.
- **RPG Progression**: Earn XP, track your level, and unlock new "Continents" on the World Map as you master prerequisites.
- **The Great Atlas**: An interactive, multi-sector navigation system to visualize your learning journey.

# 🗺️ The World Map: 21 Realms
### 🛡️ Core Logic
- **Python Highlands**: The lush forest of clean syntax and automation.
- **The C Citadel**: The foundational stone of low-level mastery.
- **C++ Power Peaks**: High-performance ranges for systems architects.
- **Java Enterprise Estate**: The bustling city of objects and robust systems.

### 🌐 Web & Mobile
- **The Styling Shores**: Crafting beauty with HTML & CSS.
- **JS Neon Isles**: Electric islands of interactivity and logic.
- **React Reef**: The modern flow of component-based architecture.
- **The PHP Port**: The classic, powerful trade route of the web.

### 🔮 Data & AI
- **The SQL Abyss**: Diving deep into structured data and ancient records.
- **NoSQL Oasis**: Flexible document management with MongoDB.
- **The Logic Labyrinth**: Mastering Data Structures & Algorithms (DSA).
- **Predictive Plains & Neural Nodes**: Exploring ML, Deep Learning, and AI.
- **The Linguist Tower**: Understanding human tongue through NLP.

### 🛠️ Tools & Business Analysis
- **The DevOps Dock**: Shipping code through Git and CI/CD pipelines.
- **Spreadsheet Steppes**: High-level data sorcery with Excel.
- **The Insight Forge**: Visualizing the kingdom’s future with Power BI/Tableau.
- **The Pipeline Path**: Constructing the realm's data plumbing (Data Engineering).
- **The Strategist’s Tent**: Translating realm needs into blueprints (BA).

# Tech Stack

- **Frontend**: Streamlit with custom CSS theming
- **Backend**: Python with sandboxed code execution (Python), simulated execution (JS, C, C++, Java, SQL), HTML preview
- **Styling**: Custom dark purple/violet theme with cyan accents
- **Fonts**: Fredoka (display), Quicksand (body), Fira Code (code)

# 🎭 Hero Classes (Mastery Paths)
Choose a specialized vocation to receive a curated roadmap of languages and skills. Each class defines a unique journey through the Great Sea of Code.

| Hero Class | Specialty | Quest Path |
| :--- | :--- | :--- |
| **🗡️ Grand Architect** | Software Engineering | C ➔ C++ ➔ Java ➔ DSA ➔ Git |
| **🌐 Portal Crafter** | Full-Stack Development | HTML/CSS ➔ JavaScript ➔ React ➔ PHP ➔ SQL |
| **🔮 Royal Analyst** | Data Science & BI | Excel ➔ SQL ➔ Power BI ➔ Python ➔ BA |
| **🤖 Golem Commander** | Artificial Intelligence | Python ➔ Math ➔ ML ➔ Deep Learning ➔ CV |
| **🏗️ Mana Engineer** | Data Engineering | SQL ➔ Python |
| **📜 Script Weaver** | Automation & Web | Python ➔ JavaScript ➔ PHP ➔ SQL ➔ Git |

# 🎮 How to Play
1. **Select a Hero Class**: On the landing page, pick a path that aligns with your dream career.
2. **Unlock the Path**: The system will automatically highlight the first language in your sequence.
3. **Conquer Arcs**: Each language is divided into Arcs. You must master the missions in one Arc to dispel the "fog of war" and unlock the next.
4. **Sail the Global Sea**: Use the World Map to visualize the entire kingdom. The Sector Selector (Core, Web, Data, Tools) allows you to teleport between different continents.
5. **Master the Code**: Use the built-in editor to solve challenges. Watch your XP bar grow as you transform from a Novice to a Master.

# 🚀 Installation & Local Development

1. ### Clone the Repository:

```bash
git clone https://github.com/your-username/kawaiicode.git
cd kawaiicode
```

2. ### Install Dependencies:

```bash
pip install -r requirements.txt
```

3. ### Run the Realm:

```bash
streamlit run app.py
```

# 📂 Project Structure

```
streamlit_app/
├── app.py                  # Entry point & Page Routing
├── components/
│   ├── landing_page.py     # Mastery Path & Hero Class selection
│   ├── world_map.py        # Global Atlas & Local Arc navigation
│   ├── mission_view.py     # Code Editor, Lessons, & XP logic
│   └── dashboard.py        # User stats and progress overview
├── data/
│   ├── content_data.py     # Central database for all 252 Arcs
│   └── hero_classes.py     # Pre-defined learning paths (e.g., "AI Researcher")
├── styles/
│   └── kawaii_theme.py     # Global CSS, animations, and color palettes
└── utils/
    └── code_evaluator.py   # Logic for checking user solutions
```

# 📜 License
This project is created for educational purposes, combining the love for coding and anime aesthetics.

### "The code is your blade. May it stay sharp!" 🗡️✨
