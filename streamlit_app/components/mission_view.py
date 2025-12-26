"""
Mission View Component
Split-screen view with story, task instructions, code editor, and output panel
Supports Python, JavaScript, and HTML/CSS
"""

import streamlit as st
import sys
from io import StringIO
from data.content_data import get_arc_by_id, get_mission_by_id, get_all_arcs
from datetime import date

SAFE_BUILTINS = {
    'print': print,
    'len': len,
    'range': range,
    'int': int,
    'float': float,
    'str': str,
    'bool': bool,
    'list': list,
    'dict': dict,
    'tuple': tuple,
    'set': set,
    'abs': abs,
    'max': max,
    'min': min,
    'sum': sum,
    'round': round,
    'sorted': sorted,
    'enumerate': enumerate,
    'zip': zip,
    'map': map,
    'filter': filter,
    'input': lambda prompt='': 'user_input',
    'type': type,
    'isinstance': isinstance,
    'True': True,
    'False': False,
    'None': None,
}


def run_python_code(code):
    """Execute Python code in a sandboxed environment and capture output."""
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = StringIO()
    redirected_error = StringIO()

    sys.stdout = redirected_output
    sys.stderr = redirected_error

    try:
        safe_globals = {"__builtins__": SAFE_BUILTINS}
        exec(code, safe_globals)
        output = redirected_output.getvalue()
        error = None
    except Exception as e:
        output = redirected_output.getvalue()
        error = str(e)
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

    return output, error


def run_javascript_code(code):
    """Simulate JavaScript execution by parsing console.log statements.
    Note: This is a simplified simulation - not a full JS runtime.
    """
    output_lines = []
    error = None

    try:
        import re

        let_vars = re.findall(r'let\s+(\w+)\s*=\s*([^;]+);', code)
        const_vars = re.findall(r'const\s+(\w+)\s*=\s*([^;]+);', code)
        variables = {}

        for var_name, var_value in let_vars + const_vars:
            var_value = var_value.strip()
            if var_value.startswith('"') or var_value.startswith("'"):
                variables[var_name] = var_value.strip('"\'')
            elif var_value.isdigit():
                variables[var_name] = int(var_value)
            else:
                try:
                    variables[var_name] = eval(var_value, {"__builtins__": {}},
                                               variables)
                except:
                    variables[var_name] = var_value

        console_pattern = r'console\.log\s*\(([^)]+)\)'
        console_calls = re.findall(console_pattern, code)

        for call_arg in console_calls:
            call_arg = call_arg.strip()

            if call_arg.startswith('`') and call_arg.endswith('`'):
                template = call_arg[1:-1]
                result = template
                for var_name, var_value in variables.items():
                    result = result.replace(f'${{{var_name}}}', str(var_value))
                expr_pattern = r'\$\{([^}]+)\}'

                def eval_expr(match):
                    expr = match.group(1)
                    try:
                        return str(eval(expr, {"__builtins__": {}}, variables))
                    except:
                        return f"${{{expr}}}"

                result = re.sub(expr_pattern, eval_expr, result)
                output_lines.append(result)

            elif call_arg.startswith('"') or call_arg.startswith("'"):
                output_lines.append(call_arg.strip('"\''))

            elif call_arg in variables:
                output_lines.append(str(variables[call_arg]))

            elif '+' in call_arg:
                parts = call_arg.split('+')
                result_parts = []
                for part in parts:
                    part = part.strip()
                    if part.startswith('"') or part.startswith("'"):
                        result_parts.append(part.strip('"\''))
                    elif part in variables:
                        result_parts.append(str(variables[part]))
                    else:
                        result_parts.append(part)
                output_lines.append(''.join(result_parts))

            else:
                try:
                    result = eval(call_arg, {"__builtins__": {}}, variables)
                    output_lines.append(str(result))
                except:
                    output_lines.append(f"[Expression: {call_arg}]")

        if not output_lines and code.strip():
            if 'console.log' not in code:
                output_lines.append(
                    "(No console.log found - add console.log() to see output)")

    except Exception as e:
        error = f"Syntax simulation error: {str(e)}"

    return '\n'.join(output_lines), error


def run_html_css_code(code):
    """Validate HTML/CSS code and return it for preview."""
    output = code.strip() if code.strip() else ""
    error = None

    if not output:
        error = "No HTML code provided"

    return output, error


def run_c_code(code):
    """Simulate C code execution by parsing printf statements."""
    output_lines = []
    error = None

    try:
        import re

        int_vars = re.findall(r'int\s+(\w+)\s*=\s*(\d+)\s*;', code)
        variables = {name: int(val) for name, val in int_vars}

        printf_pattern = r'printf\s*\(\s*"([^"]*)"\s*(?:,\s*([^)]+))?\s*\)'
        printf_calls = re.findall(printf_pattern, code)

        for format_str, args in printf_calls:
            result = format_str.replace('\\n', '')
            if '%d' in result and args:
                arg_list = [a.strip() for a in args.split(',')]
                for arg in arg_list:
                    if arg in variables:
                        result = result.replace('%d', str(variables[arg]), 1)
                    elif arg.isdigit():
                        result = result.replace('%d', arg, 1)
            output_lines.append(result)

        if not output_lines and 'printf' not in code and code.strip():
            output_lines.append(
                "(No printf found - add printf() to see output)")

    except Exception as e:
        error = f"Syntax simulation error: {str(e)}"

    return '\n'.join(output_lines), error


def run_cpp_code(code):
    """Simulate C++ code execution by parsing cout statements."""
    output_lines = []
    error = None

    try:
        import re

        int_vars = re.findall(r'int\s+(\w+)\s*=\s*(\d+)\s*;', code)
        string_vars = re.findall(r'string\s+(\w+)\s*=\s*"([^"]*)"\s*;', code)
        variables = {name: int(val) for name, val in int_vars}
        variables.update({name: val for name, val in string_vars})

        cout_pattern = r'cout\s*<<\s*(.+?)(?:<<\s*endl|;)'
        cout_matches = re.findall(cout_pattern, code)

        for match in cout_matches:
            parts = re.split(r'\s*<<\s*', match)
            result_parts = []
            for part in parts:
                part = part.strip()
                if part.startswith('"') and part.endswith('"'):
                    result_parts.append(part[1:-1])
                elif part in variables:
                    result_parts.append(str(variables[part]))
                elif part not in ['endl', '']:
                    result_parts.append(part)
            if result_parts:
                output_lines.append(''.join(result_parts))

        if not output_lines and 'cout' not in code and code.strip():
            output_lines.append("(No cout found - add cout << to see output)")

    except Exception as e:
        error = f"Syntax simulation error: {str(e)}"

    return '\n'.join(output_lines), error


def run_java_code(code):
    """Simulate Java code execution by parsing System.out.println statements."""
    output_lines = []
    error = None

    try:
        import re

        int_vars = re.findall(r'int\s+(\w+)\s*=\s*(\d+)\s*;', code)
        string_vars = re.findall(r'String\s+(\w+)\s*=\s*"([^"]*)"\s*;', code)
        variables = {name: int(val) for name, val in int_vars}
        variables.update({name: val for name, val in string_vars})

        println_pattern = r'System\.out\.println\s*\(\s*(.+?)\s*\)\s*;'
        println_calls = re.findall(println_pattern, code)

        for call_arg in println_calls:
            call_arg = call_arg.strip()

            if call_arg.startswith('"') and call_arg.endswith('"'):
                output_lines.append(call_arg[1:-1])
            elif '+' in call_arg:
                parts = call_arg.split('+')
                result_parts = []
                for part in parts:
                    part = part.strip()
                    if part.startswith('"') and part.endswith('"'):
                        result_parts.append(part[1:-1])
                    elif part in variables:
                        result_parts.append(str(variables[part]))
                    else:
                        result_parts.append(part)
                output_lines.append(''.join(result_parts))
            elif call_arg in variables:
                output_lines.append(str(variables[call_arg]))
            else:
                output_lines.append(call_arg)

        if not output_lines and 'System.out.println' not in code and code.strip(
        ):
            output_lines.append("(No System.out.println found)")

    except Exception as e:
        error = f"Syntax simulation error: {str(e)}"

    return '\n'.join(output_lines), error


def run_code(code, language="python"):
    """Run code based on the language."""
    if language == "python":
        return run_python_code(code)
    elif language == "javascript":
        return run_javascript_code(code)
    elif language == "html_css":
        return run_html_css_code(code)
    elif language == "c":
        return run_c_code(code)
    elif language == "cpp":
        return run_cpp_code(code)
    elif language == "java":
        return run_java_code(code)
    else:
        return "", "Unsupported language"


def get_language_label(language):
    """Get display label for language."""
    labels = {
        "python": "Python",
        "javascript": "JavaScript",
        "html_css": "HTML/CSS",
        "c": "C",
        "cpp": "C++",
        "java": "Java"
    }
    return labels.get(language, "Code")


INFO_ONLY_TRACKS = [
    "ml", "dl", "cv", "nlp", "ai", "excel", "powerbi", "dataeng", "ba"
]

def update_streak_logic():
    """Handles the daily streak and quest status."""
    today = date.today()
    last_date = st.session_state.get("last_mission_date")

    if last_date is None:
        st.session_state.user_streak = 1
    elif last_date != today:
        delta = (today - last_date).days
        if delta == 1:
            st.session_state.user_streak += 1
        else:
            st.session_state.user_streak = 1

    st.session_state.last_mission_date = today
    st.session_state.daily_quest_completed = True

def render_mission(arc_id, mission_id, language="python"):
    """Render the mission page with story, editor, and output."""
    arc = get_arc_by_id(arc_id, language)
    mission = get_mission_by_id(arc_id, mission_id, language)

    if not arc or not mission:
        st.error("Mission not found!")
        return

    if st.button("Back to Arc", key="back_to_arc"):
        st.session_state.current_page = "arc"
        st.rerun()

    is_info_only = language in INFO_ONLY_TRACKS
    lang_label = get_language_label(language)

    st.markdown(f"""
    <div style="margin-bottom: 1.5rem;">
        <span style="
            background: {arc['color']};
            color: white;
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
        ">
            {arc['name']} - {lang_label}
        </span>
        <h1 style="
            font-family: 'Fredoka', sans-serif;
            color: #81ecec;
            margin-top: 0.5rem;
            margin-bottom: 0.3rem;
        ">
            {mission['title']}
        </h1>
        <div style="display: flex; gap: 1rem; align-items: center;">
            <span class="difficulty-badge difficulty-{mission['difficulty']}" style="
                display: inline-block;
                padding: 0.2rem 0.6rem;
                border-radius: 10px;
                font-size: 0.7rem;
                background: {'rgba(129, 236, 236, 0.2)' if mission['difficulty'] == 'easy' else 'rgba(165, 94, 234, 0.2)' if mission['difficulty'] == 'medium' else 'rgba(255, 107, 107, 0.2)'};
                color: {'#81ecec' if mission['difficulty'] == 'easy' else '#a55eea' if mission['difficulty'] == 'medium' else '#ff6b6b'};
            ">
                {mission['difficulty'].upper()}
            </span>
            <span style="color: #FFD700; font-weight: 600;">
                +{mission['xp']} XP
            </span>
        </div>
    </div>
    """,
                unsafe_allow_html=True)

    if mission.get('lesson'):
        lesson = mission['lesson']
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, rgba(108, 92, 231, 0.2) 0%, rgba(165, 94, 234, 0.2) 100%);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 2px solid rgba(108, 92, 231, 0.5);
            box-shadow: 0 0 20px rgba(108, 92, 231, 0.2);
        ">
            <h3 style="font-family: 'Fredoka', sans-serif; color: #81ecec; margin-bottom: 0.8rem; text-shadow: 0 0 10px rgba(129, 236, 236, 0.3);">
                {lesson['title']}
            </h3>
            <p style="color: #a0a0b0; font-size: 1rem; margin: 0; font-weight: 500;">
                {lesson['overview']}
            </p>
        </div>
        """,
                    unsafe_allow_html=True)

        for section in lesson.get('sections', []):
            st.markdown(f"#### {section['heading']}")
            st.markdown(section['content'])

        st.markdown("---")

    col1, col2 = st.columns([1, 1])

    if is_info_only:
        st.info(
            "💡 This is a knowledge-based mission. Read the content above to complete the objective!"
        )

        st.markdown(f"""
        <div style="background: rgba(18, 18, 42, 0.95); border-radius: 20px; padding: 1.5rem; border: 1px solid rgba(108, 92, 231, 0.3);">
            <p style="font-family: 'Fredoka', sans-serif; color: #a55eea; font-weight: 600;">{arc['character']}</p>
            <p style="color: #a0a0b0; font-style: italic;">{mission['story']}</p>
        </div>
        """,
                    unsafe_allow_html=True)

        completed = get_completed_missions_for_lang(language)

        if mission_id in completed:
            st.success("You have already mastered this lesson! 🌟")
            if st.button("Back to Arc Selection", use_container_width=True):
                st.session_state.current_page = "arc"
                st.rerun()
        else:
            if st.button("I've Learned This! (Complete Mission)",
                         type="primary",
                         use_container_width=True):
                add_completed_mission_for_lang(mission_id, language)
                st.session_state.user_xp = st.session_state.get(
                    "user_xp", 0) + mission['xp']

                update_streak_logic()

                arcs = get_all_arcs(language)
                updated_completed = get_completed_missions_for_lang(language)

                for a in arcs:
                    arc_missions = [m['id'] for m in a.get('missions', [])]
                    if arc_missions:
                        completed_in_arc = [
                            m for m in arc_missions if m in updated_completed
                        ]
                        if len(completed_in_arc) == len(arc_missions):
                            add_completed_arc_for_lang(a['id'], language)

                            max_arc_count = len(arcs)
                            next_arc_id = a['id'] + 1
                            current_unlocked = get_current_arc_for_lang(
                                language)

                            if next_arc_id <= max_arc_count and next_arc_id > current_unlocked:
                                set_current_arc_for_lang(next_arc_id, language)
                                st.session_state.selected_arc = next_arc_id
                                st.toast(
                                    f"New Arc Unlocked: Arc {next_arc_id}!",
                                    icon="🔓")

                st.balloons()
                st.session_state.current_page = "arc"
                st.rerun()

    else:
        with col1:
            st.markdown(f"""
            <div style="
                background: rgba(18, 18, 42, 0.95);
                border-radius: 20px;
                padding: 1.5rem;
                margin-bottom: 1rem;
                box-shadow: 0 4px 15px rgba(108, 92, 231, 0.2);
                border: 1px solid rgba(108, 92, 231, 0.3);
            ">
                <p style="font-family: 'Fredoka', sans-serif; color: #a55eea; font-weight: 600; margin-bottom: 0.5rem;">
                    {arc['character']}
                </p>
                <p style="color: #a0a0b0; font-style: italic; line-height: 1.6;">
                    {mission['story']}
                </p>
            </div>
            """,
                        unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
                background: rgba(108, 92, 231, 0.1);
                border-radius: 15px;
                padding: 1.2rem;
                margin-bottom: 1rem;
                border: 1px solid rgba(108, 92, 231, 0.3);
            ">
                <h4 style="font-family: 'Fredoka', sans-serif; color: #81ecec; margin-bottom: 0.5rem;">
                    Your Task
                </h4>
                <p style="color: #a0a0b0; line-height: 1.6;">
                    {mission['task']}
                </p>
            </div>
            """,
                        unsafe_allow_html=True)

            if mission.get('expected_output'):
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, rgba(129, 236, 236, 0.1) 0%, rgba(116, 185, 255, 0.1) 100%);
                    border-radius: 15px;
                    padding: 1.2rem;
                    margin-bottom: 1rem;
                    border: 1px solid rgba(129, 236, 236, 0.3);
                ">
                    <h4 style="font-family: 'Fredoka', sans-serif; color: #81ecec; margin-bottom: 0.5rem;">
                        Expected Output
                    </h4>
                    <pre style="
                        background: rgba(10, 10, 26, 0.8);
                        padding: 0.8rem;
                        border-radius: 8px;
                        color: #81ecec;
                        font-family: 'Fira Code', monospace;
                        font-size: 0.9rem;
                        margin: 0;
                        white-space: pre-wrap;
                        border: 1px solid rgba(108, 92, 231, 0.3);
                    ">{mission['expected_output']}</pre>
                </div>
                """,
                            unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="
                    background: linear-gradient(135deg, rgba(165, 94, 234, 0.1) 0%, rgba(108, 92, 231, 0.1) 100%);
                    border-radius: 15px;
                    padding: 1.2rem;
                    margin-bottom: 1rem;
                    border: 1px solid rgba(165, 94, 234, 0.3);
                ">
                    <h4 style="font-family: 'Fredoka', sans-serif; color: #a55eea; margin-bottom: 0.5rem;">
                        Open-Ended Mission
                    </h4>
                    <p style="color: #a0a0b0; font-size: 0.9rem; margin: 0;">
                        This mission accepts any valid output! Just make sure your code runs without errors.
                    </p>
                </div>
                """,
                            unsafe_allow_html=True)

            with st.expander("Need a hint?"):
                for i, hint in enumerate(mission.get('hints', []), 1):
                    st.markdown(f"**Hint {i}:** {hint}")

        with col2:
            st.markdown(f"""
            <h4 style="font-family: 'Fredoka', sans-serif; color: #81ecec; margin-bottom: 0.5rem;">
                {lang_label} Editor
            </h4>
            """,
                        unsafe_allow_html=True)

            code_key = f"code_{language}_{mission_id}"
            if code_key not in st.session_state:
                st.session_state[code_key] = mission['starter_code']

            code = st.text_area(f"Write your {lang_label} code here:",
                                value=st.session_state[code_key],
                                height=200,
                                key=f"editor_{language}_{mission_id}",
                                label_visibility="collapsed")

            st.session_state[code_key] = code

            col_run, col_reset = st.columns(2)

            with col_run:
                if st.button("Run Code",
                             key=f"run_{language}_{mission_id}",
                             type="primary"):
                    output, error = run_code(code, language)
                    st.session_state[
                        f"output_{language}_{mission_id}"] = output
                    st.session_state[f"error_{language}_{mission_id}"] = error

                    mission_completed = False
                    if mission['expected_output']:
                        if output.strip() == mission['expected_output'].strip(
                        ):
                            st.session_state[
                                f"success_{language}_{mission_id}"] = True
                            completed = get_completed_missions_for_lang(
                                language)
                            if mission_id not in completed:
                                add_completed_mission_for_lang(
                                    mission_id, language)
                                st.session_state.user_xp = st.session_state.get(
                                    "user_xp", 0) + mission['xp']
                                mission_completed = True
                    else:
                        if output.strip() and not error:
                            st.session_state[
                                f"success_{language}_{mission_id}"] = True
                            completed = get_completed_missions_for_lang(
                                language)
                            if mission_id not in completed:
                                add_completed_mission_for_lang(
                                    mission_id, language)
                                st.session_state.user_xp = st.session_state.get(
                                    "user_xp", 0) + mission['xp']
                                mission_completed = True

                    if mission_completed:
                        update_streak_logic()
                        arcs = get_all_arcs(language)
                        completed = get_completed_missions_for_lang(language)
                        for a in arcs:
                            arc_missions = [
                                m['id'] for m in a.get('missions', [])
                            ]
                            if arc_missions:
                                completed_in_arc = [
                                    m for m in arc_missions if m in completed
                                ]
                                if len(completed_in_arc) == len(arc_missions):
                                    add_completed_arc_for_lang(
                                        a['id'], language)
                                    max_arc = len(arcs)
                                    next_arc = a['id'] + 1
                                    current = get_current_arc_for_lang(
                                        language)
                                    if next_arc <= max_arc and next_arc > current:
                                        set_current_arc_for_lang(
                                            next_arc, language)
                                        st.session_state.selected_arc = next_arc
                                        st.session_state.current_page = "arc"
                                        st.toast(f"Arc {next_arc} Unlocked!",
                                                 icon="star")
                        st.rerun()

        with col_reset:
            if st.button("Reset Code", key=f"reset_{language}_{mission_id}"):
                st.session_state[code_key] = mission['starter_code']
                st.session_state[f"output_{language}_{mission_id}"] = ""
                st.session_state[f"error_{language}_{mission_id}"] = None
                st.session_state[f"success_{language}_{mission_id}"] = False
                st.rerun()

        st.markdown("""
        <h4 style="font-family: 'Fredoka', sans-serif; color: #81ecec; margin-top: 1rem; margin-bottom: 0.5rem;">
            Output
        </h4>
        """,
                    unsafe_allow_html=True)

        output = st.session_state.get(f"output_{language}_{mission_id}", "")
        error = st.session_state.get(f"error_{language}_{mission_id}", None)
        success = st.session_state.get(f"success_{language}_{mission_id}",
                                       False)

        if language == "html_css" and output and not error:
            st.markdown(f"""
            <div style="
                background: white;
                border-radius: 10px;
                padding: 1rem;
                min-height: 100px;
                border: 2px solid rgba(108, 92, 231, 0.3);
            ">
                {output}
            </div>
            """,
                        unsafe_allow_html=True)
        elif error:
            st.markdown(f"""
            <div style="
                background: #1a1a2e;
                border-radius: 10px;
                padding: 1rem;
                font-family: 'Fira Code', monospace;
                min-height: 100px;
            ">
                <span style="color: #ff6b6b;">{error}</span>
            </div>
            """,
                        unsafe_allow_html=True)
        elif output:
            st.markdown(f"""
            <div style="
                background: #1a1a2e;
                border-radius: 10px;
                padding: 1rem;
                font-family: 'Fira Code', monospace;
                min-height: 100px;
            ">
                <span style="color: #0f0;">{output}</span>
            </div>
            """,
                        unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="
                background: #1a1a2e;
                border-radius: 10px;
                padding: 1rem;
                font-family: 'Fira Code', monospace;
                min-height: 100px;
                color: #666;
            ">
                Run your code to see output here...
            </div>
            """,
                        unsafe_allow_html=True)

        if success:
            st.balloons()
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #B5EAD7, #98FB98);
                color: #2d5a4a;
                padding: 1rem;
                border-radius: 15px;
                text-align: center;
                font-weight: 600;
                margin-top: 1rem;
            ">
                Mission Complete! You earned {mission['xp']} XP!
            </div>
            """,
                        unsafe_allow_html=True)

            if st.button("Continue to Next Mission",
                         key=f"next_{language}_{mission_id}"):
                st.session_state.current_page = "arc"
                st.rerun()


ALL_LANGUAGES = ["python", "javascript", "html_css", "c", "cpp", "java"]


def ensure_session_state_initialized():
    """Ensure session state has proper multi-language structure."""
    if "completed_missions" not in st.session_state:
        st.session_state.completed_missions = {
            lang: []
            for lang in ALL_LANGUAGES
        }
    elif isinstance(st.session_state.completed_missions, list):
        old_missions = st.session_state.completed_missions
        st.session_state.completed_missions = {
            lang: []
            for lang in ALL_LANGUAGES
        }
        st.session_state.completed_missions["python"] = old_missions
    elif isinstance(st.session_state.completed_missions, dict):
        for lang in ALL_LANGUAGES:
            if lang not in st.session_state.completed_missions:
                st.session_state.completed_missions[lang] = []

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


def get_completed_missions_for_lang(language):
    """Get completed missions for a specific language."""
    ensure_session_state_initialized()
    return st.session_state.completed_missions.get(language, [])


def add_completed_mission_for_lang(mission_id, language):
    """Add completed mission for a specific language."""
    ensure_session_state_initialized()
    if mission_id not in st.session_state.completed_missions[language]:
        st.session_state.completed_missions[language].append(mission_id)


def get_completed_arcs_for_lang(language):
    """Get completed arcs for a specific language."""
    ensure_session_state_initialized()
    return st.session_state.completed_arcs.get(language, [])


def add_completed_arc_for_lang(arc_id, language):
    """Add completed arc for a specific language."""
    ensure_session_state_initialized()
    if arc_id not in st.session_state.completed_arcs[language]:
        st.session_state.completed_arcs[language].append(arc_id)


def get_current_arc_for_lang(language):
    """Get current arc for a specific language."""
    ensure_session_state_initialized()
    return st.session_state.current_arc.get(language, 1)


def set_current_arc_for_lang(arc_id, language):
    """Set current arc for a specific language."""
    ensure_session_state_initialized()
    st.session_state.current_arc[language] = arc_id


def render_mission_list(arc_id, language="python"):
    """Render the list of missions for an arc."""
    arc = get_arc_by_id(arc_id, language)

    if not arc:
        st.error("Arc not found!")
        return

    st.markdown(f"""
    <h3 style="font-family: 'Fredoka', sans-serif; color: #81ecec; margin-top: 1.5rem; text-shadow: 0 0 10px rgba(129, 236, 236, 0.3);">
        Missions
    </h3>
    """,
                unsafe_allow_html=True)

    if not arc['missions']:
        st.info("Missions for this arc are coming soon!")
        return

    completed = get_completed_missions_for_lang(language)

    for mission in arc['missions']:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"""
            <div style="
                background: rgba(18, 18, 42, 0.95);
                border-radius: 15px;
                padding: 1rem 1.5rem;
                margin: 0.5rem 0;
                box-shadow: 0 2px 15px rgba(108, 92, 231, 0.2);
                border: 1px solid rgba(108, 92, 231, 0.3);
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <div>
                    <span style="font-family: 'Fredoka', sans-serif; font-size: 1.1rem; color: #81ecec;">
                        {mission['title']}
                    </span>
                    <div style="margin-top: 0.3rem;">
                        <span class="difficulty-badge difficulty-{mission['difficulty']}" style="
                            display: inline-block;
                            padding: 0.2rem 0.6rem;
                            border-radius: 10px;
                            font-size: 0.7rem;
                            background: {'rgba(129, 236, 236, 0.2)' if mission['difficulty'] == 'easy' else 'rgba(165, 94, 234, 0.2)' if mission['difficulty'] == 'medium' else 'rgba(255, 107, 107, 0.2)'};
                            color: {'#81ecec' if mission['difficulty'] == 'easy' else '#a55eea' if mission['difficulty'] == 'medium' else '#ff6b6b'};
                            border: 1px solid {'rgba(129, 236, 236, 0.3)' if mission['difficulty'] == 'easy' else 'rgba(165, 94, 234, 0.3)' if mission['difficulty'] == 'medium' else 'rgba(255, 107, 107, 0.3)'};
                        ">
                            {mission['difficulty'].upper()}
                        </span>
                        <span style="color: #a55eea; font-weight: 600; margin-left: 0.5rem; font-size: 0.85rem;">
                            +{mission['xp']} XP
                        </span>
                    </div>
                </div>
            </div>
            """,
                        unsafe_allow_html=True)

        with col2:
            is_completed = mission['id'] in completed
            if is_completed:
                st.markdown("""
                <div style="
                    background: linear-gradient(135deg, #B5EAD7 0%, #98d4bb 100%);
                    color: #2d6a4f;
                    padding: 0.4rem 0.8rem;
                    border-radius: 8px;
                    font-size: 0.75rem;
                    font-weight: 600;
                    text-align: center;
                    margin-bottom: 0.3rem;
                ">
                    Completed
                </div>
                """,
                            unsafe_allow_html=True)
                if st.button(
                        "Restart",
                        key=f"restart_mission_{language}_{mission['id']}"):
                    st.session_state.current_page = "mission"
                    st.session_state.selected_mission = mission['id']
                    st.rerun()
            else:
                if st.button("Start",
                             key=f"start_mission_{language}_{mission['id']}"):
                    st.session_state.current_page = "mission"
                    st.session_state.selected_mission = mission['id']
                    st.rerun()
