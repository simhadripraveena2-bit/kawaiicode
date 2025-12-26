"""
KawaiiCode Content Data
Contains all arcs, missions, characters, and story content for multiple programming languages.
"""

LANGUAGES = {
    "python": {
        "name": "Python",
        "icon": "snake",
        "color": "#3776ab",
        "description": "Begin your coding journey with Python - the perfect language for beginners!"
    },
    "javascript": {
        "name": "JavaScript",
        "icon": "code",
        "color": "#f7df1e",
        "description": "Master the language of the web and bring pages to life!"
    },
    "html_css": {
        "name": "HTML & CSS",
        "icon": "palette",
        "color": "#e44d26",
        "description": "Create beautiful web pages with the building blocks of the internet!"
    },
    "c": {
        "name": "C",
        "icon": "cpu",
        "color": "#555555",
        "description": "Learn the foundational language that powers operating systems and embedded devices!"
    },
    "cpp": {
        "name": "C++",
        "icon": "zap",
        "color": "#00599C",
        "description": "Master high-performance programming with objects and advanced features!"
    },
    "java": {
        "name": "Java",
        "icon": "coffee",
        "color": "#f89820",
        "description": "Build cross-platform applications with one of the world's most popular languages!"
    },
    "sql": {
        "name": "SQL",
        "icon": "database",
        "color": "#336791",
        "description": "Master the language of databases and manage the vast data scrolls of the realm!"
    },
    "dsa": {
        "name": "DSA",
        "icon": "brain",
        "color": "#e74c3c",
        "description": "Master Data Structures & Algorithms - the foundation of efficient problem solving!"
    },
    "react": {
        "name": "React",
        "icon": "layout",
        "color": "#61dafb",
        "description": "Master the Portal of Interfaces - craft magical UI windows for users to interact with!"
    },
    "mongodb": {
        "name": "MongoDB",
        "icon": "scroll",
        "color": "#47a248",
        "description": "Master the Scroll of Infinite Documents - store data in flexible, magical scrolls!"
    },
    "php": {
        "name": "PHP",
        "icon": "code",
        "color": "#777bb4",
        "description": "Master the Web Weaver's Loom - spin server-side threads that hold the web together!"
    },
    "devops": {
        "name": "Git & DevOps",
        "icon": "git-branch",
        "color": "#f05033",
        "description": "Master the Temporal Gates - control versions and build deployment portals!"
    },
    "ml": {
        "name": "Machine Learning",
        "icon": "brain",
        "color": "#ff6f00",
        "description": "Awaken the Mind of the Machine - teach golems to think and predict!"
    },
    "dl": {
        "name": "Deep Learning",
        "icon": "cpu",
        "color": "#9c27b0",
        "description": "Enter the Neural Nexus - build the brain of the realm with neural pathways!"
    },
    "cv": {
        "name": "Computer Vision",
        "icon": "eye",
        "color": "#00bcd4",
        "description": "Become the Prism Gazer - grant golems the ability to see and interpret visual light!"
    },
    "nlp": {
        "name": "NLP",
        "icon": "message-square",
        "color": "#e91e63",
        "description": "Become the Script-Weaver - understand the ancient scripts and spoken languages of the realm!"
    },
    "ai": {
        "name": "AI",
        "icon": "brain",
        "color": "#673ab7",
        "description": "Become the Grand Architect - understand the philosophical and logical foundations of The Great Golem!"
    },
    "excel": {
        "name": "Excel",
        "icon": "table",
        "color": "#217346",
        "description": "Master the Excel Grimoire - learn spreadsheet sorcery to organize the realm's chaotic records!"
    },
    "powerbi": {
        "name": "Power BI/Tableau",
        "icon": "bar-chart-2",
        "color": "#f2c811",
        "description": "Gaze through the Visionary Lens - create magical dashboards to predict the future of the kingdom!"
    },
    "dataeng": {
        "name": "Data Engineering",
        "icon": "database",
        "color": "#00acc1",
        "description": "Build the Great Pipeline - construct massive aqueducts and forges that transport Mana (Data) across the realm!"
    },
    "ba": {
        "name": "Business Analysis",
        "icon": "briefcase",
        "color": "#7b1fa2",
        "description": "Walk the Royal Counselor's Path - master the art of translating the realm's wishes into precise blueprints!"
    }
}

PYTHON_ARCS = [
    {
        "id": 1,
        "name": "Awakening Village",
        "topic": "Variables and Print",
        "description": "Begin your journey in the peaceful Awakening Village, where young coders first learn to speak the language of Python.",
        "story_intro": "The Logic Corruption has begun to spread across the Kawaii Code Realm. In Awakening Village, Sensei Luna awaits a new hero who can learn the ancient art of Python to restore balance.",
        "character": "Sensei Luna",
        "character_quote": "Every great coder starts with a single print statement. Let's begin your journey!",
        "icon": "village",
        "color": "#FFB7B2",
        "missions": [
            {
                "id": 1,
                "title": "Hello, Kawaii World!",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "The print() Function",
                    "overview": "The print() function is your first Python spell! It displays text on the screen.",
                    "sections": [
                        {
                            "heading": "What is print()?",
                            "content": "In Python, `print()` is a built-in function that outputs text to the console. Think of it as your way of making the computer talk!"
                        },
                        {
                            "heading": "How to Use It",
                            "content": "Put your message inside the parentheses, wrapped in quotes:\n\n```python\nprint(\"Hello!\")\nprint('You can use single quotes too!')\n```"
                        },
                        {
                            "heading": "Quick Example",
                            "content": "```python\nprint(\"Welcome to Python!\")\n# Output: Welcome to Python!\n```"
                        }
                    ]
                },
                "story": "Sensei Luna smiles warmly. 'To begin cleansing the corruption, you must first learn to speak. Use the print() spell to announce your presence to the realm!'",
                "task": "Write a Python program that prints 'Hello, Kawaii World!' to the console.",
                "starter_code": "# Your first spell! Use print() to say hello\n",
                "expected_output": "Hello, Kawaii World!",
                "hints": ["Use print() with text inside quotes", "The text should match exactly: Hello, Kawaii World!"]
            },
            {
                "id": 2,
                "title": "The Name Scroll",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Variables - Storing Information",
                    "overview": "Variables are like labeled boxes that store information for you to use later.",
                    "sections": [
                        {
                            "heading": "What is a Variable?",
                            "content": "A variable is a name that refers to a value. You create one using the `=` sign:\n\n```python\nname = \"Luna\"\nage = 25\n```"
                        },
                        {
                            "heading": "Naming Rules",
                            "content": "- Start with a letter or underscore\n- Use letters, numbers, and underscores\n- No spaces! Use `hero_name` not `hero name`\n- Python is case-sensitive: `Name` and `name` are different"
                        },
                        {
                            "heading": "Using Variables with print()",
                            "content": "You can print variables directly or combine them with text:\n\n```python\nhero = \"Sakura\"\nprint(hero)           # Output: Sakura\nprint(f\"Hello, {hero}!\")  # Output: Hello, Sakura!\n```"
                        }
                    ]
                },
                "story": "Luna nods approvingly. 'Now you must learn to store power in variables. A variable is like a magical scroll that remembers things for you.'",
                "task": "Create a variable called 'hero_name' and set it to your name. Then print a greeting using that variable.",
                "starter_code": "# Create your hero identity\nhero_name = \n\n# Print your greeting\nprint()",
                "expected_output": None,
                "hints": ["Variables store values: hero_name = 'YourName'", "You can use + to combine strings or use f-strings"]
            },
            {
                "id": 3,
                "title": "Power Levels",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Numbers and Math",
                    "overview": "Python can work with numbers and do math just like a calculator!",
                    "sections": [
                        {
                            "heading": "Number Types",
                            "content": "Python has two main number types:\n- **Integers (int)**: Whole numbers like `10`, `42`, `-5`\n- **Floats**: Decimal numbers like `3.14`, `99.9`"
                        },
                        {
                            "heading": "Math Operations",
                            "content": "```python\na = 10\nb = 3\n\nprint(a + b)   # Addition: 13\nprint(a - b)   # Subtraction: 7\nprint(a * b)   # Multiplication: 30\nprint(a / b)   # Division: 3.333...\n```"
                        },
                        {
                            "heading": "Combining with Strings",
                            "content": "Use f-strings to mix numbers with text:\n\n```python\nscore = 100\nprint(f\"Your score is: {score}\")\n# Output: Your score is: 100\n```"
                        }
                    ]
                },
                "story": "'Every hero has power levels,' Luna explains. 'Numbers are the foundation of all magic in our realm.'",
                "task": "Create two variables: 'attack_power' set to 50 and 'defense_power' set to 30. Print their sum as 'Total Power: X'",
                "starter_code": "# Define your power levels\nattack_power = \ndefense_power = \n\n# Calculate and print total\n",
                "expected_output": "Total Power: 80",
                "hints": ["Use = to assign number values", "You can add variables together with +"]
            },
            {
                "id": 4,
                "title": "Village Elder's Test",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Putting It All Together",
                    "overview": "Let's combine everything you've learned: print, variables, and formatting!",
                    "sections": [
                        {
                            "heading": "F-Strings (Formatted Strings)",
                            "content": "F-strings let you embed variables directly in text. Just add `f` before the quotes and use `{variable_name}` to insert values:\n\n```python\nname = \"Hero\"\nlevel = 5\nprint(f\"Name: {name}\")\nprint(f\"Level: {level}\")\n```"
                        },
                        {
                            "heading": "Multiple Print Statements",
                            "content": "Each `print()` creates a new line:\n\n```python\nprint(\"Line 1\")\nprint(\"Line 2\")\nprint(\"Line 3\")\n```"
                        },
                        {
                            "heading": "Creating a Status Card",
                            "content": "Combine multiple variables to display information:\n\n```python\nweapon = \"Sword\"\ndamage = 25\nprint(f\"Weapon: {weapon}\")\nprint(f\"Damage: {damage}\")\n```"
                        }
                    ]
                },
                "story": "The Village Elder appears! 'To prove you've mastered the basics, complete this challenge combining all you've learned.'",
                "task": "Create variables for your hero's name, level (5), and health (100). Print a status card showing all three values.",
                "starter_code": "# Hero Status Card\nname = \nlevel = \nhealth = \n\n# Print the status card\n",
                "expected_output": None,
                "hints": ["Use f-strings for clean formatting: f'Name: {name}'", "Print each stat on its own line"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Decision Valley",
        "topic": "If/Else Logic",
        "description": "Navigate the branching paths of Decision Valley, where every choice leads to a different outcome.",
        "story_intro": "The paths in Decision Valley have become tangled by corruption. Only logical thinking can guide you through the maze of choices.",
        "character": "Kira the Navigator",
        "character_quote": "In coding, as in life, we must make decisions. Let me teach you the way of if and else!",
        "icon": "valley",
        "color": "#E0BBE4",
        "missions": [
            {
                "id": 5,
                "title": "The First Fork",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "If Statements - Making Decisions",
                    "overview": "The `if` statement lets your code make decisions based on conditions!",
                    "sections": [
                        {
                            "heading": "What is an If Statement?",
                            "content": "An `if` statement checks if something is true, then runs code only if it is:\n\n```python\nif condition:\n    # This code runs only if condition is True\n```"
                        },
                        {
                            "heading": "Comparison Operators",
                            "content": "Use these to compare values:\n- `>` greater than\n- `<` less than\n- `>=` greater or equal\n- `<=` less or equal\n- `==` equal to\n- `!=` not equal to"
                        },
                        {
                            "heading": "Example",
                            "content": "```python\nage = 18\nif age >= 18:\n    print(\"You are an adult!\")\n```\n\n**Important:** Don't forget the colon `:` and indent the code inside!"
                        }
                    ]
                },
                "story": "Kira points to a fork in the road. 'See how one path glows and one is dark? We must check conditions to choose wisely.'",
                "task": "Create a variable 'power' set to 75. Write an if statement that prints 'Strong!' if power is greater than 50.",
                "starter_code": "power = 75\n\n# Check the power level\n",
                "expected_output": "Strong!",
                "hints": ["Use if power > 50:", "Don't forget the colon and indentation"]
            },
            {
                "id": 6,
                "title": "Two Paths",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "If-Else - Two Choices",
                    "overview": "Sometimes you need to do one thing OR another. That's where `else` comes in!",
                    "sections": [
                        {
                            "heading": "The Else Clause",
                            "content": "When the `if` condition is False, the `else` block runs instead:\n\n```python\nif condition:\n    # Runs if True\nelse:\n    # Runs if False\n```"
                        },
                        {
                            "heading": "Example",
                            "content": "```python\ntemperature = 15\n\nif temperature > 25:\n    print(\"It's hot!\")\nelse:\n    print(\"It's cool.\")\n\n# Output: It's cool.\n```"
                        },
                        {
                            "heading": "Remember",
                            "content": "- `else` doesn't need a condition\n- `else` must come right after the `if` block\n- Only ONE of the blocks will run, never both!"
                        }
                    ]
                },
                "story": "'Sometimes there are exactly two choices,' Kira explains. 'This is where else comes in.'",
                "task": "Check if a variable 'health' (set to 30) is above 50. Print 'Healthy' if true, otherwise print 'Need healing'.",
                "starter_code": "health = 30\n\n# Make the decision\n",
                "expected_output": "Need healing",
                "hints": ["Use if-else structure", "else doesn't need a condition"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Time Loop Forest",
        "topic": "For/While Loops",
        "description": "In this mystical forest, time flows in circles. Master the art of loops to escape!",
        "story_intro": "The corruption has trapped travelers in endless loops. Only by understanding iteration can you break free and help others.",
        "character": "Echo the Timekeeper",
        "character_quote": "Time repeats itself here. Learn to control the loops, and you control time itself!",
        "icon": "forest",
        "color": "#957DAD",
        "missions": [
            {
                "id": 7,
                "title": "The For Loop",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "For Loops",
                    "overview": "For loops repeat code a specific number of times.",
                    "sections": [
                        {"heading": "Basic For Loop", "content": "```python\nfor i in range(5):\n    print(i)  # Prints 0, 1, 2, 3, 4\n```"},
                        {"heading": "range() Function", "content": "- `range(5)`: 0 to 4\n- `range(1, 6)`: 1 to 5\n- `range(0, 10, 2)`: 0, 2, 4, 6, 8"}
                    ]
                },
                "story": "Echo waves her staff. 'Watch as time repeats itself!'",
                "task": "Use a for loop to print numbers 1 to 5.",
                "starter_code": "# Print 1 to 5\n",
                "expected_output": "1\n2\n3\n4\n5",
                "hints": ["Use range(1, 6)", "for i in range(1, 6):"]
            },
            {
                "id": 8,
                "title": "While We Wait",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "While Loops",
                    "overview": "While loops repeat while a condition is true.",
                    "sections": [
                        {"heading": "While Syntax", "content": "```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n```"},
                        {"heading": "Be Careful!", "content": "Always make sure the condition becomes False eventually, or you'll have an infinite loop!"}
                    ]
                },
                "story": "'Sometimes we loop until something changes,' Echo explains.",
                "task": "Use a while loop to print numbers from 5 down to 1.",
                "starter_code": "num = 5\n# While loop here\n",
                "expected_output": "5\n4\n3\n2\n1",
                "hints": ["while num > 0:", "Don't forget to decrease num!"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Inventory Kingdom",
        "topic": "Lists and Dictionaries",
        "description": "The grand kingdom where all treasures are cataloged and organized in magical containers.",
        "story_intro": "The royal inventory has been scrambled by corruption. Restore order by mastering lists and dictionaries.",
        "character": "Keeper Max",
        "character_quote": "Every item has its place. Lists for order, dictionaries for meaning!",
        "icon": "kingdom",
        "color": "#B5EAD7",
        "missions": [
            {
                "id": 9,
                "title": "List Basics",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Python Lists",
                    "overview": "Lists store multiple items in order.",
                    "sections": [
                        {"heading": "Creating Lists", "content": "```python\nitems = [\"sword\", \"shield\", \"potion\"]\nnumbers = [1, 2, 3, 4, 5]\n```"},
                        {"heading": "Accessing Items", "content": "```python\nprint(items[0])  # sword\nprint(items[-1]) # potion (last item)\n```"}
                    ]
                },
                "story": "Keeper Max opens a treasure chest. 'Lists keep things in order!'",
                "task": "Create a list of 3 fruits and print the second one.",
                "starter_code": "# Create your list\n",
                "expected_output": None,
                "hints": ["fruits = [\"apple\", \"banana\", \"cherry\"]", "Index 1 for second item"]
            },
            {
                "id": 10,
                "title": "Dictionary Magic",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Python Dictionaries",
                    "overview": "Dictionaries store key-value pairs.",
                    "sections": [
                        {"heading": "Creating Dictionaries", "content": "```python\nhero = {\"name\": \"Sakura\", \"level\": 5, \"health\": 100}\n```"},
                        {"heading": "Accessing Values", "content": "```python\nprint(hero[\"name\"])  # Sakura\nhero[\"level\"] = 6    # Update value\n```"}
                    ]
                },
                "story": "'Dictionaries give meaning to data,' Max explains.",
                "task": "Create a dictionary for a pet with name, species, and age. Print the name.",
                "starter_code": "# Create pet dictionary\n",
                "expected_output": None,
                "hints": ["pet = {\"name\": \"Fluffy\", ...}", "pet[\"name\"]"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Spell Scroll Library",
        "topic": "Functions (def/return)",
        "description": "The ancient library where coders learn to write their own spells - reusable magic called functions.",
        "story_intro": "The librarians have lost the ability to create new spells. Teach them the art of functions to restore the library's power.",
        "character": "Sage Pythia",
        "character_quote": "A function is a spell you write once and cast forever. Let me show you the way.",
        "icon": "library",
        "color": "#FFDAC1",
        "missions": [
            {
                "id": 11,
                "title": "Your First Function",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Defining Functions",
                    "overview": "Functions are reusable blocks of code.",
                    "sections": [
                        {"heading": "def Keyword", "content": "```python\ndef greet():\n    print(\"Hello!\")\n\ngreet()  # Call the function\n```"},
                        {"heading": "With Parameters", "content": "```python\ndef greet(name):\n    print(f\"Hello, {name}!\")\n\ngreet(\"Sakura\")\n```"}
                    ]
                },
                "story": "Sage Pythia opens an ancient scroll. 'Write your first spell!'",
                "task": "Create a function called 'welcome' that prints 'Welcome, hero!'",
                "starter_code": "# Define your function\n\n# Call it\n",
                "expected_output": "Welcome, hero!",
                "hints": ["def welcome():", "Don't forget to call it!"]
            },
            {
                "id": 12,
                "title": "Return Values",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Returning Values",
                    "overview": "Functions can return values to be used elsewhere.",
                    "sections": [
                        {"heading": "return Statement", "content": "```python\ndef add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)  # 8\n```"},
                        {"heading": "Multiple Returns", "content": "```python\ndef get_stats():\n    return 100, 50  # Returns tuple\n\nhealth, mana = get_stats()\n```"}
                    ]
                },
                "story": "'Functions can give back values,' Pythia reveals.",
                "task": "Create a function 'double' that takes a number and returns it doubled.",
                "starter_code": "# Create double function\n\nprint(double(5))  # Should print 10\n",
                "expected_output": "10",
                "hints": ["return num * 2", "def double(num):"]
            }
        ]
    },
    {
        "id": 6,
        "name": "String Sanctuary",
        "topic": "Slicing and Formatting",
        "description": "A peaceful sanctuary where words and text are shaped and molded like clay.",
        "story_intro": "The sacred texts have been corrupted. Only by mastering string manipulation can you restore the ancient writings.",
        "character": "Scribe Aria",
        "character_quote": "Words have power. Learn to slice, format, and transform them!",
        "icon": "sanctuary",
        "color": "#FF9AA2",
        "missions": [
            {
                "id": 13,
                "title": "String Slicing",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Slicing Strings",
                    "overview": "Extract parts of strings with slicing.",
                    "sections": [
                        {"heading": "Basic Slicing", "content": "```python\ntext = \"Hello World\"\nprint(text[0:5])   # Hello\nprint(text[6:])    # World\nprint(text[:5])    # Hello\n```"},
                        {"heading": "Negative Indices", "content": "```python\nprint(text[-5:])   # World\nprint(text[:-6])   # Hello\n```"}
                    ]
                },
                "story": "Scribe Aria shows ancient texts. 'Extract the parts you need!'",
                "task": "Extract and print the first 3 characters of 'Python'.",
                "starter_code": "text = \"Python\"\n# Slice it\n",
                "expected_output": "Pyt",
                "hints": ["text[0:3]", "or text[:3]"]
            },
            {
                "id": 14,
                "title": "F-String Magic",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "F-Strings",
                    "overview": "Format strings with embedded expressions.",
                    "sections": [
                        {"heading": "F-String Syntax", "content": "```python\nname = \"Hero\"\nlevel = 10\nprint(f\"{name} is level {level}\")\n```"},
                        {"heading": "Expressions in F-Strings", "content": "```python\nprint(f\"2 + 2 = {2 + 2}\")\nprint(f\"Name: {name.upper()}\")\n```"}
                    ]
                },
                "story": "'F-strings make formatting elegant,' Aria explains.",
                "task": "Use an f-string to print 'Player: [name], Score: [score]' with variables.",
                "starter_code": "name = \"Sakura\"\nscore = 1500\n# Use f-string\n",
                "expected_output": "Player: Sakura, Score: 1500",
                "hints": ["f\"Player: {name}...\"", "Embed variables in curly braces"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Object Guild",
        "topic": "OOP (Classes/Objects)",
        "description": "The prestigious guild where coders learn to create their own types of magical entities.",
        "story_intro": "The guild's blueprints for creating new beings have been stolen. Master object-oriented programming to restore them.",
        "character": "Architect Nova",
        "character_quote": "Everything is an object. Learn to create your own, and you become a true creator.",
        "icon": "guild",
        "color": "#C7CEEA",
        "missions": [
            {
                "id": 15,
                "title": "Creating Classes",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Python Classes",
                    "overview": "Classes are blueprints for creating objects.",
                    "sections": [
                        {"heading": "Class Definition", "content": "```python\nclass Hero:\n    def __init__(self, name):\n        self.name = name\n    \n    def greet(self):\n        print(f\"I am {self.name}!\")\n```"},
                        {"heading": "Creating Objects", "content": "```python\nhero = Hero(\"Sakura\")\nhero.greet()  # I am Sakura!\n```"}
                    ]
                },
                "story": "Architect Nova unveils the blueprints. 'Create your own beings!'",
                "task": "Create a Pet class with a name attribute and a speak method.",
                "starter_code": "# Create Pet class\n\npet = Pet(\"Whiskers\")\npet.speak()\n",
                "expected_output": None,
                "hints": ["Use __init__ for initialization", "self.name = name"]
            },
            {
                "id": 16,
                "title": "Methods and Attributes",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Object Methods",
                    "overview": "Objects can have attributes (data) and methods (actions).",
                    "sections": [
                        {"heading": "Instance Methods", "content": "```python\nclass Player:\n    def __init__(self, name):\n        self.name = name\n        self.score = 0\n    \n    def add_points(self, points):\n        self.score += points\n```"}
                    ]
                },
                "story": "'Objects have state and behavior,' Nova explains.",
                "task": "Create a Counter class with an increment method.",
                "starter_code": "# Counter class\n\nc = Counter()\nc.increment()\nc.increment()\nprint(c.count)  # Should print 2\n",
                "expected_output": "2",
                "hints": ["self.count = 0 in __init__", "self.count += 1 in increment"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Mirror Realm",
        "topic": "Recursion",
        "description": "A reality-bending dimension where things reflect themselves infinitely.",
        "story_intro": "The mirrors show infinite reflections of corruption. Break the cycle by understanding recursion.",
        "character": "Phantom Rex",
        "character_quote": "To understand recursion, you must first understand recursion...",
        "icon": "mirror",
        "color": "#E2F0CB",
        "missions": [
            {
                "id": 17,
                "title": "Recursive Basics",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "What is Recursion?",
                    "overview": "A function that calls itself to solve smaller subproblems.",
                    "sections": [
                        {"heading": "Base Case", "content": "Every recursive function needs a stopping condition:\n```python\ndef countdown(n):\n    if n <= 0:  # Base case\n        print(\"Done!\")\n    else:\n        print(n)\n        countdown(n - 1)  # Recursive call\n```"},
                        {"heading": "Factorial Example", "content": "```python\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n```"}
                    ]
                },
                "story": "Phantom Rex stands before a mirror. 'The reflection reflects itself...'",
                "task": "Write a recursive function to calculate factorial of 5.",
                "starter_code": "def factorial(n):\n    # Base case and recursive case\n    pass\n\nprint(factorial(5))  # Should print 120\n",
                "expected_output": "120",
                "hints": ["if n <= 1: return 1", "return n * factorial(n-1)"]
            },
            {
                "id": 18,
                "title": "Recursive Sum",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Recursive Sum",
                    "overview": "Sum a list using recursion.",
                    "sections": [
                        {"heading": "Breaking Down", "content": "```python\ndef sum_list(lst):\n    if len(lst) == 0:\n        return 0\n    return lst[0] + sum_list(lst[1:])\n```"}
                    ]
                },
                "story": "'Break the problem into smaller pieces,' Rex advises.",
                "task": "Write a recursive function to sum all numbers in a list.",
                "starter_code": "def sum_list(lst):\n    # Recursive sum\n    pass\n\nprint(sum_list([1, 2, 3, 4, 5]))  # Should print 15\n",
                "expected_output": "15",
                "hints": ["Base case: empty list returns 0", "lst[0] + sum_list(lst[1:])"]
            }
        ]
    },
    {
        "id": 9,
        "name": "World Tree",
        "topic": "Tree Traversal",
        "description": "The colossal tree that connects all realms, with branches reaching into every corner of the code.",
        "story_intro": "The World Tree's branches are tangled. Navigate its structure to restore the connections between realms.",
        "character": "Guardian Yew",
        "character_quote": "Every branch leads somewhere. Learn to traverse the tree, and all paths open to you.",
        "icon": "tree",
        "color": "#B5EAD7",
        "missions": [
            {
                "id": 19,
                "title": "Tree Node",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Tree Data Structure",
                    "overview": "Trees have nodes with children.",
                    "sections": [
                        {"heading": "Node Class", "content": "```python\nclass TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n```"},
                        {"heading": "Building a Tree", "content": "```python\nroot = TreeNode(1)\nroot.left = TreeNode(2)\nroot.right = TreeNode(3)\n```"}
                    ]
                },
                "story": "Guardian Yew shows the World Tree. 'Each node has children...'",
                "task": "Create a TreeNode class and build a simple 3-node tree.",
                "starter_code": "# TreeNode class\n\n# Build tree\n",
                "expected_output": None,
                "hints": ["class TreeNode:", "self.left = None, self.right = None"]
            },
            {
                "id": 20,
                "title": "Inorder Traversal",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Tree Traversal",
                    "overview": "Visit all nodes in a specific order.",
                    "sections": [
                        {"heading": "Inorder", "content": "Left -> Root -> Right\n```python\ndef inorder(node):\n    if node:\n        inorder(node.left)\n        print(node.value)\n        inorder(node.right)\n```"}
                    ]
                },
                "story": "'Walk the tree in order,' Yew instructs.",
                "task": "Implement inorder traversal for a binary tree.",
                "starter_code": "# Inorder traversal function\n",
                "expected_output": None,
                "hints": ["Recursive function", "Left, then print, then right"]
            }
        ]
    },
    {
        "id": 10,
        "name": "City of Paths",
        "topic": "Graphs (BFS/DFS)",
        "description": "A sprawling metropolis where every street connects to countless others.",
        "story_intro": "The city's pathways have become a maze. Master graph algorithms to find the way through.",
        "character": "Navigator Sol",
        "character_quote": "In a world of connections, knowing how to search is the ultimate power.",
        "icon": "city",
        "color": "#FFEFD5",
        "missions": [
            {
                "id": 21,
                "title": "Graph Representation",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Graphs in Python",
                    "overview": "Graphs are networks of connected nodes.",
                    "sections": [
                        {"heading": "Adjacency List", "content": "```python\ngraph = {\n    'A': ['B', 'C'],\n    'B': ['A', 'D'],\n    'C': ['A', 'D'],\n    'D': ['B', 'C']\n}\n```"}
                    ]
                },
                "story": "Navigator Sol maps the city. 'Every location connects to others.'",
                "task": "Create a graph representing 4 connected locations.",
                "starter_code": "# Graph as adjacency list\n",
                "expected_output": None,
                "hints": ["Use a dictionary", "Keys are nodes, values are lists of neighbors"]
            },
            {
                "id": 22,
                "title": "BFS Search",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Breadth-First Search",
                    "overview": "Explore all neighbors before going deeper.",
                    "sections": [
                        {"heading": "BFS Algorithm", "content": "```python\nfrom collections import deque\n\ndef bfs(graph, start):\n    visited = set()\n    queue = deque([start])\n    while queue:\n        node = queue.popleft()\n        if node not in visited:\n            print(node)\n            visited.add(node)\n            queue.extend(graph[node])\n```"}
                    ]
                },
                "story": "'Search level by level,' Sol guides.",
                "task": "Implement BFS to visit all nodes starting from 'A'.",
                "starter_code": "from collections import deque\n\n# BFS function\n",
                "expected_output": None,
                "hints": ["Use a queue (deque)", "Track visited nodes"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Memory Palace",
        "topic": "Dynamic Programming",
        "description": "A palace where past solutions are remembered to solve future challenges.",
        "story_intro": "The palace's memory has faded. Restore it by learning to remember and reuse solutions.",
        "character": "Oracle Mem",
        "character_quote": "Those who forget the past are doomed to recompute it. Remember wisely!",
        "icon": "palace",
        "color": "#DCD0FF",
        "missions": [
            {
                "id": 23,
                "title": "Memoization",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Remember Past Results",
                    "overview": "Store computed values to avoid recomputation.",
                    "sections": [
                        {"heading": "Memoized Fibonacci", "content": "```python\nmemo = {}\ndef fib(n):\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fib(n-1) + fib(n-2)\n    return memo[n]\n```"}
                    ]
                },
                "story": "Oracle Mem opens a glowing book. 'Remember to not repeat yourself!'",
                "task": "Implement memoized Fibonacci to calculate fib(30) efficiently.",
                "starter_code": "# Memoized Fibonacci\n\nprint(fib(30))\n",
                "expected_output": "832040",
                "hints": ["Use a dictionary to store results", "Check memo before computing"]
            },
            {
                "id": 24,
                "title": "Climbing Stairs",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Classic DP Problem",
                    "overview": "Count ways to climb n stairs (1 or 2 steps at a time).",
                    "sections": [
                        {"heading": "Bottom-Up DP", "content": "```python\ndef climb_stairs(n):\n    if n <= 2:\n        return n\n    dp = [0] * (n + 1)\n    dp[1], dp[2] = 1, 2\n    for i in range(3, n + 1):\n        dp[i] = dp[i-1] + dp[i-2]\n    return dp[n]\n```"}
                    ]
                },
                "story": "'Build solutions from smaller pieces,' Oracle explains.",
                "task": "Calculate the number of ways to climb 10 stairs.",
                "starter_code": "# Climbing stairs DP\n\nprint(climb_stairs(10))  # Should print 89\n",
                "expected_output": "89",
                "hints": ["Similar to Fibonacci", "dp[i] = dp[i-1] + dp[i-2]"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Elite Trials",
        "topic": "Advanced Mixed Challenges",
        "description": "The ultimate proving ground where only the strongest coders can survive.",
        "story_intro": "The final corruption awaits. Combine everything you've learned to face the Elite Trials and save the realm!",
        "character": "Grand Master Py",
        "character_quote": "You've come far, young coder. Now face the ultimate test!",
        "icon": "trials",
        "color": "#FFD700",
        "missions": [
            {
                "id": 25,
                "title": "Data Class Challenge",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Combining Concepts",
                    "overview": "Use classes with collections and algorithms.",
                    "sections": [
                        {"heading": "Real-World Design", "content": "Combine:\n- Classes for entities\n- Lists/dicts for storage\n- Methods for operations"}
                    ]
                },
                "story": "Grand Master Py observes. 'Show me your mastery!'",
                "task": "Create a TodoList class with add, remove, and list methods.",
                "starter_code": "# TodoList class\n\ntodos = TodoList()\ntodos.add(\"Learn Python\")\ntodos.add(\"Build projects\")\ntodos.list_all()\n",
                "expected_output": None,
                "hints": ["Use a list to store items", "Methods: add, remove, list_all"]
            },
            {
                "id": 26,
                "title": "The Final Challenge",
                "difficulty": "boss",
                "xp": 100,
                "lesson": {
                    "title": "Ultimate Test",
                    "overview": "Combine all your knowledge in one challenge.",
                    "sections": [
                        {"heading": "Requirements", "content": "Build a complete mini-application using:\n- Functions\n- Classes\n- Data structures\n- Control flow\n- Error handling"}
                    ]
                },
                "story": "Grand Master Py nods. 'Build something worthy of a true Pythonista!'",
                "task": "Create a simple inventory system with items, quantities, and operations.",
                "starter_code": "# Your complete solution\n",
                "expected_output": None,
                "hints": ["Class for Item", "Class for Inventory", "Methods for add/remove/list"]
            }
        ]
    }
]

JAVASCRIPT_ARCS = [
    {
        "id": 1,
        "name": "Mana Currents",
        "topic": "let, const, data types",
        "description": "Where the magical currents of data flow through variables!",
        "story_intro": "The Spark of Life realm needs its energy restored. At Mana Currents, you'll learn to channel data through variables.",
        "character": "Mage Variable",
        "character_quote": "Every spark of magic starts with storing energy. Let's channel the mana!",
        "icon": "terminal",
        "color": "#f7df1e",
        "missions": [
            {
                "id": 101,
                "title": "Channeling Mana",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Variables with let and const",
                    "overview": "JavaScript uses let and const to create variables that store data.",
                    "sections": [
                        {"heading": "let vs const", "content": "Use `let` for values that can change, `const` for constants:\n\n```javascript\nlet score = 0;\nconst name = \"Hero\";\n```"},
                        {"heading": "Data Types", "content": "- String: `\"Hello\"`\n- Number: `42`, `3.14`\n- Boolean: `true`, `false`\n- Undefined, Null"}
                    ]
                },
                "story": "Mage Variable opens a glowing tome. 'Variables are vessels for your data. Let's fill them with power!'",
                "task": "Create a const 'heroName' with your name and a let 'level' set to 1. Log both.",
                "starter_code": "// Create your variables\n\n// Log them\n",
                "expected_output": None,
                "hints": ["Use const for name, let for level", "Use console.log()"]
            },
            {
                "id": 102,
                "title": "Data Streams",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Working with Data Types",
                    "overview": "Understanding strings, numbers, and booleans.",
                    "sections": [
                        {"heading": "Strings", "content": "```javascript\nlet greeting = \"Hello\";\nlet name = 'World';\nconsole.log(greeting + \" \" + name);\n```"},
                        {"heading": "Numbers", "content": "```javascript\nlet a = 10;\nlet b = 3;\nconsole.log(a + b);  // 13\n```"},
                        {"heading": "Template Literals", "content": "```javascript\nlet name = \"Hero\";\nconsole.log(`Welcome, ${name}!`);\n```"}
                    ]
                },
                "story": "'Data flows like water,' the Mage explains. 'Learn to work with different types!'",
                "task": "Create variables for name (string), age (number), and isHero (boolean true). Log them all.",
                "starter_code": "// Define your data\n",
                "expected_output": None,
                "hints": ["Use appropriate types for each", "Booleans are true or false without quotes"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Spark Gateways",
        "topic": "if/else, comparison operators",
        "description": "The gateways that open based on logical conditions!",
        "story_intro": "The gateways are sealed. Only those who master logic can pass through.",
        "character": "Guardian Logic",
        "character_quote": "Every gate responds to a condition. Think logically!",
        "icon": "signpost",
        "color": "#61dafb",
        "missions": [
            {
                "id": 103,
                "title": "Gateway Conditions",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "If Statements",
                    "overview": "Make decisions in your code with if statements.",
                    "sections": [
                        {"heading": "Basic If", "content": "```javascript\nif (power > 50) {\n    console.log(\"Strong!\");\n}\n```"},
                        {"heading": "Comparison Operators", "content": "- `>` `<` `>=` `<=`\n- `===` strict equal\n- `!==` not equal"}
                    ]
                },
                "story": "Guardian Logic stands before the first gate. 'Prove you understand conditions!'",
                "task": "Create 'power' set to 75. Log 'Strong!' if power > 50.",
                "starter_code": "let power = 75;\n\n// Check power\n",
                "expected_output": "Strong!",
                "hints": ["Use if (power > 50) { }"]
            },
            {
                "id": 104,
                "title": "The Dual Path",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "If-Else Statements",
                    "overview": "Handle two outcomes with if-else.",
                    "sections": [
                        {"heading": "If-Else", "content": "```javascript\nif (health > 50) {\n    console.log(\"Healthy\");\n} else {\n    console.log(\"Injured\");\n}\n```"},
                        {"heading": "Else If", "content": "```javascript\nif (score >= 90) {\n    console.log(\"A\");\n} else if (score >= 80) {\n    console.log(\"B\");\n} else {\n    console.log(\"C\");\n}\n```"}
                    ]
                },
                "story": "'Two paths diverge,' Logic explains. 'Your condition chooses the way.'",
                "task": "Check if 'health' (30) is above 50. Log 'Healthy' or 'Need healing'.",
                "starter_code": "let health = 30;\n\n// Decide\n",
                "expected_output": "Need healing",
                "hints": ["Use if-else structure"]
            },
            {
                "id": 127,
                "title": "Comparison Operators",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Comparing Values",
                    "overview": "Comparison operators compare values and return true or false.",
                    "sections": [
                        {"heading": "Comparison Operators", "content": "```javascript\n===  // strict equal\n!==  // strict not equal\n>    // greater than\n<    // less than\n>=   // greater or equal\n<=   // less or equal\n```"},
                        {"heading": "Strict vs Loose", "content": "```javascript\n5 == '5'   // true (loose)\n5 === '5'  // false (strict)\n```\nAlways use === for strict comparison!"}
                    ]
                },
                "story": "'Comparison is the basis of all decisions,' Logic teaches. 'Master these operators!'",
                "task": "Compare two values using multiple comparison operators and log the results.",
                "starter_code": "let a = 10;\nlet b = 5;\n\n// Compare and log\n",
                "expected_output": "a > b: true\na === b: false",
                "hints": ["Use console.log for each comparison"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Cycle of Echoes",
        "topic": "for, while, forEach",
        "description": "A mystical cave where sounds repeat in patterns!",
        "story_intro": "The echoes have gone silent. Restore them by mastering loops.",
        "character": "Echo Weaver",
        "character_quote": "Repetition is the heartbeat of code. Let's make it echo!",
        "icon": "waves",
        "color": "#68d391",
        "missions": [
            {
                "id": 105,
                "title": "The For Loop",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "For Loops",
                    "overview": "Repeat code a specific number of times.",
                    "sections": [
                        {"heading": "For Loop Syntax", "content": "```javascript\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}\n// Outputs: 0, 1, 2, 3, 4\n```"},
                        {"heading": "Parts of a For Loop", "content": "- Initialization: `let i = 0`\n- Condition: `i < 5`\n- Increment: `i++`"}
                    ]
                },
                "story": "Echo Weaver gestures at the cave walls. 'Watch how the echoes repeat!'",
                "task": "Write a for loop that logs numbers 1 through 5.",
                "starter_code": "// Create the echo\n",
                "expected_output": "1\n2\n3\n4\n5",
                "hints": ["Start i at 1, go while i <= 5"]
            },
            {
                "id": 106,
                "title": "While Echoes",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "While Loops",
                    "overview": "Repeat while a condition is true.",
                    "sections": [
                        {"heading": "While Syntax", "content": "```javascript\nlet count = 0;\nwhile (count < 3) {\n    console.log(count);\n    count++;\n}\n```"}
                    ]
                },
                "story": "'Sometimes we repeat until something changes,' the Weaver explains.",
                "task": "Use a while loop to log 'Echo!' 3 times.",
                "starter_code": "let count = 0;\n\n// While loop\n",
                "expected_output": "Echo!\nEcho!\nEcho!",
                "hints": ["While count < 3, log and increment"]
            },
            {
                "id": 126,
                "title": "ForEach Power",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "forEach Method",
                    "overview": "forEach is an array method that runs a function on each element.",
                    "sections": [
                        {"heading": "forEach Syntax", "content": "```javascript\nconst items = ['apple', 'banana', 'cherry'];\nitems.forEach(item => {\n    console.log(item);\n});\n```"},
                        {"heading": "With Index", "content": "```javascript\nitems.forEach((item, index) => {\n    console.log(index + ': ' + item);\n});\n```"}
                    ]
                },
                "story": "'forEach is elegant,' the Weaver smiles. 'Each element gets its turn!'",
                "task": "Use forEach to log each hero name from the array.",
                "starter_code": "const heroes = ['Luna', 'Kai', 'Nova'];\n\n// Use forEach\n",
                "expected_output": "Luna\nKai\nNova",
                "hints": ["heroes.forEach(hero => console.log(hero));"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Scroll Synthesis",
        "topic": "arrow functions, parameters",
        "description": "The library where reusable spells are crafted!",
        "story_intro": "The scrolls have lost their magic. Restore them by creating functions.",
        "character": "Scribe Arrow",
        "character_quote": "A function is a spell you write once and cast forever!",
        "icon": "scroll",
        "color": "#b794f4",
        "missions": [
            {
                "id": 107,
                "title": "Function Scrolls",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Creating Functions",
                    "overview": "Functions are reusable blocks of code.",
                    "sections": [
                        {"heading": "Function Declaration", "content": "```javascript\nfunction greet(name) {\n    return \"Hello, \" + name;\n}\n```"},
                        {"heading": "Arrow Functions", "content": "```javascript\nconst greet = (name) => {\n    return \"Hello, \" + name;\n};\n// Or shorter:\nconst greet = name => \"Hello, \" + name;\n```"}
                    ]
                },
                "story": "Scribe Arrow reveals an ancient scroll. 'Learn to write reusable magic!'",
                "task": "Create an arrow function 'double' that takes a number and returns it doubled.",
                "starter_code": "// Create the function\n\n// Test it\nconsole.log(double(5));",
                "expected_output": "10",
                "hints": ["const double = (num) => num * 2;"]
            },
            {
                "id": 108,
                "title": "Parameters and Returns",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Function Parameters",
                    "overview": "Pass data into functions and get results back.",
                    "sections": [
                        {"heading": "Multiple Parameters", "content": "```javascript\nconst add = (a, b) => a + b;\nconsole.log(add(3, 5)); // 8\n```"},
                        {"heading": "Default Parameters", "content": "```javascript\nconst greet = (name = \"Friend\") => `Hello, ${name}!`;\n```"}
                    ]
                },
                "story": "'Functions can accept any data you give them,' the Scribe notes.",
                "task": "Create a function 'introduce' that takes name and age, returns 'I am [name], age [age]'.",
                "starter_code": "// Create introduce function\n\nconsole.log(introduce(\"Sakura\", 20));",
                "expected_output": "I am Sakura, age 20",
                "hints": ["Use template literals in the return"]
            },
            {
                "id": 128,
                "title": "Arrow Functions",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Arrow Function Syntax",
                    "overview": "Arrow functions provide a concise syntax for writing functions.",
                    "sections": [
                        {"heading": "Arrow Syntax", "content": "```javascript\n// Traditional\nfunction add(a, b) { return a + b; }\n\n// Arrow\nconst add = (a, b) => a + b;\n```"},
                        {"heading": "Single Parameter", "content": "```javascript\nconst double = n => n * 2;  // No parentheses needed\n```"},
                        {"heading": "No Parameters", "content": "```javascript\nconst greet = () => 'Hello!';\n```"}
                    ]
                },
                "story": "'Arrow functions are elegant,' the Scribe reveals. 'Short and powerful!'",
                "task": "Convert a regular function to arrow syntax: multiply two numbers.",
                "starter_code": "// Convert to arrow function\nfunction multiply(a, b) {\n    return a * b;\n}\n\n// Your arrow version:\n",
                "expected_output": "Result: 15",
                "hints": ["const multiply = (a, b) => a * b;"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Puppet Theater",
        "topic": "getElementById, innerHTML",
        "description": "Where JavaScript brings HTML elements to life!",
        "story_intro": "The puppets are frozen. Learn DOM manipulation to animate them!",
        "character": "Puppeteer DOM",
        "character_quote": "The DOM is your stage. JavaScript is the strings!",
        "icon": "layout",
        "color": "#e74c3c",
        "missions": [
            {
                "id": 109,
                "title": "Selecting Elements",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "DOM Selection",
                    "overview": "Select HTML elements with JavaScript.",
                    "sections": [
                        {"heading": "getElementById", "content": "```javascript\nconst title = document.getElementById('title');\n```"},
                        {"heading": "querySelector", "content": "```javascript\nconst button = document.querySelector('.btn');\nconst items = document.querySelectorAll('li');\n```"}
                    ]
                },
                "story": "Puppeteer DOM shows you the strings. 'First, grab hold of your elements!'",
                "task": "Select an element with id 'message' and log it.",
                "starter_code": "// Select and log the element\n",
                "expected_output": None,
                "hints": ["Use document.getElementById('message')"]
            },
            {
                "id": 110,
                "title": "Changing Content",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Modifying the DOM",
                    "overview": "Change what's displayed on the page.",
                    "sections": [
                        {"heading": "innerHTML", "content": "```javascript\nelement.innerHTML = '<b>New content!</b>';\n```"},
                        {"heading": "textContent", "content": "```javascript\nelement.textContent = 'Plain text';\n```"},
                        {"heading": "Style", "content": "```javascript\nelement.style.color = 'red';\n```"}
                    ]
                },
                "story": "'Now make the puppets dance!' the Puppeteer exclaims.",
                "task": "Change the innerHTML of an element to 'Hello, World!'",
                "starter_code": "const el = document.getElementById('output');\n// Change its content\n",
                "expected_output": None,
                "hints": ["el.innerHTML = 'Hello, World!';"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Reaction Ruins",
        "topic": "Event listeners (click, input)",
        "description": "Ancient ruins that respond to user actions!",
        "story_intro": "The ruins are dormant. Awaken them with event listeners!",
        "character": "Guardian Event",
        "character_quote": "Every click, every keystroke - the ruins respond to all!",
        "icon": "signpost",
        "color": "#9b59b6",
        "missions": [
            {
                "id": 111,
                "title": "Click Events",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "addEventListener",
                    "overview": "Respond to user interactions.",
                    "sections": [
                        {"heading": "Click Event", "content": "```javascript\nbutton.addEventListener('click', () => {\n    console.log('Clicked!');\n});\n```"},
                        {"heading": "Event Types", "content": "- 'click': Mouse click\n- 'input': Text input change\n- 'submit': Form submission\n- 'mouseover': Hover"}
                    ]
                },
                "story": "Guardian Event touches an ancient button. 'Watch it spring to life!'",
                "task": "Add a click event to a button that logs 'Button clicked!'",
                "starter_code": "const btn = document.querySelector('button');\n// Add event listener\n",
                "expected_output": "Button clicked!",
                "hints": ["btn.addEventListener('click', () => { })"]
            },
            {
                "id": 112,
                "title": "Input Reactions",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Input Events",
                    "overview": "React to user typing in real-time.",
                    "sections": [
                        {"heading": "Input Event", "content": "```javascript\ninput.addEventListener('input', (e) => {\n    console.log(e.target.value);\n});\n```"},
                        {"heading": "Event Object", "content": "The event `e` contains details about what happened."}
                    ]
                },
                "story": "'The ruins can hear every word you type,' Guardian reveals.",
                "task": "Log the value of an input field as the user types.",
                "starter_code": "const input = document.querySelector('input');\n// Listen for input\n",
                "expected_output": None,
                "hints": ["Use the 'input' event and e.target.value"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Array Archipelago",
        "topic": "push, pop, filter, map",
        "description": "An island chain of organized data collections!",
        "story_intro": "The islands have scattered. Organize them with array methods!",
        "character": "Keeper Node",
        "character_quote": "Arrays hold many values. Learn to manipulate them!",
        "icon": "islands",
        "color": "#fbb6ce",
        "missions": [
            {
                "id": 113,
                "title": "Array Basics",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Working with Arrays",
                    "overview": "Create and modify arrays.",
                    "sections": [
                        {"heading": "Creating Arrays", "content": "```javascript\nconst fruits = ['apple', 'banana', 'orange'];\n```"},
                        {"heading": "Push and Pop", "content": "```javascript\nfruits.push('grape');  // Add to end\nfruits.pop();          // Remove from end\n```"}
                    ]
                },
                "story": "Keeper Node presents a collection of islands. 'Arrays are like these islands - organized!'",
                "task": "Create an array of 3 colors and add a 4th with push.",
                "starter_code": "// Create array and add element\n",
                "expected_output": None,
                "hints": ["Use push() to add to the array"]
            },
            {
                "id": 114,
                "title": "Map and Filter",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Array Methods",
                    "overview": "Transform and filter arrays.",
                    "sections": [
                        {"heading": "Map", "content": "```javascript\nconst doubled = numbers.map(n => n * 2);\n```"},
                        {"heading": "Filter", "content": "```javascript\nconst evens = numbers.filter(n => n % 2 === 0);\n```"}
                    ]
                },
                "story": "'Transform the islands!' Keeper commands. 'Map changes each one!'",
                "task": "Use map to double all numbers in [1, 2, 3, 4, 5].",
                "starter_code": "const nums = [1, 2, 3, 4, 5];\n// Double them\n",
                "expected_output": "[2, 4, 6, 8, 10]",
                "hints": ["const doubled = nums.map(n => n * 2);"]
            },
            {
                "id": 129,
                "title": "Push and Pop",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Adding and Removing Elements",
                    "overview": "push and pop modify arrays by adding or removing from the end.",
                    "sections": [
                        {"heading": "Push", "content": "```javascript\nconst items = ['apple', 'banana'];\nitems.push('cherry');  // ['apple', 'banana', 'cherry']\n```\nAdds to the end of the array."},
                        {"heading": "Pop", "content": "```javascript\nconst last = items.pop();  // 'cherry'\n// items is now ['apple', 'banana']\n```\nRemoves and returns the last element."}
                    ]
                },
                "story": "'Push adds, pop removes,' Keeper explains. 'Simple but powerful!'",
                "task": "Create an inventory array, push 'sword' and 'shield', then pop one item.",
                "starter_code": "const inventory = ['potion'];\n\n// Push and pop\n",
                "expected_output": "Inventory: potion,sword,shield\nRemoved: shield\nFinal: potion,sword",
                "hints": ["Use push() to add", "Use pop() to remove the last item"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Object Oasis",
        "topic": "Key-value pairs, JSON",
        "description": "An oasis where data is structured in objects!",
        "story_intro": "The oasis needs organization. Structure it with objects!",
        "character": "Builder JSON",
        "character_quote": "Objects group related data beautifully!",
        "icon": "oasis",
        "color": "#ffd93d",
        "missions": [
            {
                "id": 115,
                "title": "Creating Objects",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "JavaScript Objects",
                    "overview": "Store related data in key-value pairs.",
                    "sections": [
                        {"heading": "Object Syntax", "content": "```javascript\nconst hero = {\n    name: 'Sakura',\n    level: 5,\n    health: 100\n};\n```"},
                        {"heading": "Accessing Properties", "content": "```javascript\nconsole.log(hero.name);    // Dot notation\nconsole.log(hero['level']); // Bracket notation\n```"}
                    ]
                },
                "story": "Builder JSON shapes the sand. 'Objects organize data like this oasis!'",
                "task": "Create a 'pet' object with name, type, and age properties.",
                "starter_code": "// Create pet object\n",
                "expected_output": None,
                "hints": ["Use { key: value } syntax"]
            },
            {
                "id": 116,
                "title": "JSON Format",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "JSON",
                    "overview": "Convert between objects and JSON strings.",
                    "sections": [
                        {"heading": "JSON.stringify", "content": "```javascript\nconst json = JSON.stringify(obj);\n```"},
                        {"heading": "JSON.parse", "content": "```javascript\nconst obj = JSON.parse(jsonString);\n```"}
                    ]
                },
                "story": "'JSON is how data travels,' Builder explains. 'Learn to convert!'",
                "task": "Convert an object to a JSON string and log it.",
                "starter_code": "const data = { message: 'Hello' };\n// Convert to JSON\n",
                "expected_output": None,
                "hints": ["Use JSON.stringify(data)"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Oracle's Portal",
        "topic": "setTimeout, Promises",
        "description": "A portal where time flows differently with async magic!",
        "story_intro": "The portal's timing is off. Restore it with async understanding!",
        "character": "Oracle Async",
        "character_quote": "Some things take time. Learn to wait gracefully!",
        "icon": "sparkles",
        "color": "#00cec9",
        "missions": [
            {
                "id": 117,
                "title": "Delayed Magic",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "setTimeout",
                    "overview": "Delay code execution.",
                    "sections": [
                        {"heading": "setTimeout", "content": "```javascript\nsetTimeout(() => {\n    console.log('After 2 seconds');\n}, 2000);\n```"},
                        {"heading": "Milliseconds", "content": "1000ms = 1 second"}
                    ]
                },
                "story": "Oracle Async waves her hand. 'Time bends to our will here!'",
                "task": "Log 'Delayed!' after 1 second using setTimeout.",
                "starter_code": "// Delayed log\n",
                "expected_output": "Delayed!",
                "hints": ["Use 1000 for 1 second"]
            },
            {
                "id": 118,
                "title": "Promises",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "JavaScript Promises",
                    "overview": "Handle async operations with promises.",
                    "sections": [
                        {"heading": "Creating Promises", "content": "```javascript\nconst promise = new Promise((resolve, reject) => {\n    resolve('Success!');\n});\n```"},
                        {"heading": "Using Promises", "content": "```javascript\npromise.then(result => console.log(result));\n```"}
                    ]
                },
                "story": "'Promises are contracts with the future,' Oracle explains.",
                "task": "Create a promise that resolves with 'Done!' and log the result.",
                "starter_code": "// Create and use promise\n",
                "expected_output": "Done!",
                "hints": ["Use .then() to get the result"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Spirit Fetcher",
        "topic": "fetch(), async/await",
        "description": "Summon data spirits from distant API realms!",
        "story_intro": "The data spirits are lost. Learn to fetch them back!",
        "character": "Summoner Fetch",
        "character_quote": "APIs hold vast knowledge. Let's summon it!",
        "icon": "terminal",
        "color": "#6c5ce7",
        "missions": [
            {
                "id": 119,
                "title": "The Fetch Spell",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Fetch API",
                    "overview": "Get data from external sources.",
                    "sections": [
                        {"heading": "Basic Fetch", "content": "```javascript\nfetch('https://api.example.com/data')\n    .then(response => response.json())\n    .then(data => console.log(data));\n```"}
                    ]
                },
                "story": "Summoner Fetch draws a portal. 'Data awaits beyond!'",
                "task": "Write a fetch call to any API URL and log the response.",
                "starter_code": "// Fetch data\n",
                "expected_output": None,
                "hints": ["Chain .then() for response and data"]
            },
            {
                "id": 120,
                "title": "Async/Await",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Async/Await Syntax",
                    "overview": "Cleaner way to work with promises.",
                    "sections": [
                        {"heading": "Async Function", "content": "```javascript\nasync function getData() {\n    const response = await fetch(url);\n    const data = await response.json();\n    return data;\n}\n```"}
                    ]
                },
                "story": "'Await makes async feel synchronous,' Summoner reveals.",
                "task": "Rewrite a fetch call using async/await.",
                "starter_code": "async function fetchData() {\n    // Use await\n}\n",
                "expected_output": None,
                "hints": ["Add await before fetch and .json()"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Class Academy",
        "topic": "Classes, this, constructors",
        "description": "The academy where object blueprints are taught!",
        "story_intro": "The academy needs new students. Learn to create class blueprints!",
        "character": "Professor Class",
        "character_quote": "Classes are blueprints for creating objects!",
        "icon": "building",
        "color": "#fd79a8",
        "missions": [
            {
                "id": 121,
                "title": "Creating Classes",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "JavaScript Classes",
                    "overview": "Create object blueprints with classes.",
                    "sections": [
                        {"heading": "Class Syntax", "content": "```javascript\nclass Hero {\n    constructor(name) {\n        this.name = name;\n    }\n    greet() {\n        return `I am ${this.name}!`;\n    }\n}\n```"},
                        {"heading": "Creating Instances", "content": "```javascript\nconst hero = new Hero('Sakura');\nconsole.log(hero.greet());\n```"}
                    ]
                },
                "story": "Professor Class draws on the board. 'A class is a template!'",
                "task": "Create a Pet class with name property and a speak method.",
                "starter_code": "// Create Pet class\n\nconst pet = new Pet('Fluffy');\nconsole.log(pet.speak());",
                "expected_output": None,
                "hints": ["Use constructor to set this.name"]
            },
            {
                "id": 122,
                "title": "Methods and This",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Class Methods",
                    "overview": "Add behavior to your classes.",
                    "sections": [
                        {"heading": "The 'this' Keyword", "content": "`this` refers to the current instance."},
                        {"heading": "Multiple Methods", "content": "```javascript\nclass Counter {\n    constructor() {\n        this.count = 0;\n    }\n    increment() {\n        this.count++;\n    }\n    getCount() {\n        return this.count;\n    }\n}\n```"}
                    ]
                },
                "story": "'Methods define what your objects can do,' the Professor explains.",
                "task": "Create a Counter class with increment and getCount methods.",
                "starter_code": "// Create Counter class\n",
                "expected_output": None,
                "hints": ["Use this.count to track the count"]
            },
            {
                "id": 130,
                "title": "Constructors",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Class Constructors",
                    "overview": "Constructors initialize new objects with starting values.",
                    "sections": [
                        {"heading": "Constructor Syntax", "content": "```javascript\nclass Hero {\n    constructor(name, level) {\n        this.name = name;\n        this.level = level;\n        this.health = 100;\n    }\n}\nconst hero = new Hero('Luna', 5);\n```"},
                        {"heading": "Default Values", "content": "```javascript\nconstructor(name, level = 1) {\n    this.name = name;\n    this.level = level;\n}\n```"}
                    ]
                },
                "story": "'The constructor births each instance,' the Professor explains. 'Set the initial values!'",
                "task": "Create a Pet class with a constructor that takes name and species.",
                "starter_code": "// Create Pet class with constructor\n\nconst myPet = new Pet('Fluffy', 'cat');\nconsole.log(myPet.name, myPet.species);",
                "expected_output": "Fluffy cat",
                "hints": ["Use constructor(name, species)", "Assign to this.name and this.species"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Spark Master Boss",
        "topic": "Building an interactive Pet Game",
        "description": "The ultimate trial - build a complete interactive project!",
        "story_intro": "You've learned all the arts. Now prove your mastery by building a Pet Game!",
        "character": "Grand Spark Master",
        "character_quote": "Show me everything you've learned. Create life!",
        "icon": "trophy",
        "color": "#f1c40f",
        "missions": [
            {
                "id": 123,
                "title": "Pet Class Design",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Designing the Pet",
                    "overview": "Create the Pet class with properties and methods.",
                    "sections": [
                        {"heading": "Pet Properties", "content": "- name, hunger, happiness, energy"},
                        {"heading": "Pet Methods", "content": "- feed(), play(), sleep()"}
                    ]
                },
                "story": "Grand Spark Master watches. 'Design your pet's soul!'",
                "task": "Create a Pet class with hunger, happiness, and methods to change them.",
                "starter_code": "class Pet {\n    // Your design\n}\n",
                "expected_output": None,
                "hints": ["Each method should modify the pet's stats"]
            },
            {
                "id": 124,
                "title": "Interactive UI",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Connecting to the DOM",
                    "overview": "Create buttons that control your pet.",
                    "sections": [
                        {"heading": "Button Events", "content": "Connect feed, play, and sleep buttons to pet methods."},
                        {"heading": "Display Updates", "content": "Update the page to show current pet stats."}
                    ]
                },
                "story": "'Now give your creation a body!' the Master commands.",
                "task": "Create buttons that call pet methods and update a display.",
                "starter_code": "// Connect DOM to Pet\n",
                "expected_output": None,
                "hints": ["Use addEventListener for each button"]
            },
            {
                "id": 125,
                "title": "Final Polish",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "Complete the Game",
                    "overview": "Add finishing touches to your pet game.",
                    "sections": [
                        {"heading": "Animations", "content": "Add visual feedback when actions occur."},
                        {"heading": "Game Logic", "content": "What happens when hunger reaches 0? Add conditions!"}
                    ]
                },
                "story": "The Grand Spark Master nods. 'Complete your masterpiece!'",
                "task": "Add game over logic when hunger reaches 0, and victory when happiness reaches 100.",
                "starter_code": "// Add game logic\n",
                "expected_output": None,
                "hints": ["Check stats after each action"]
            }
        ]
    }
]

HTML_CSS_ARCS = [
    {
        "id": 1,
        "name": "Blueprint Village",
        "topic": "Tags, Head vs Body, Text Elements",
        "description": "Where every structure begins with the foundational blueprints of HTML!",
        "story_intro": "The Architect's Realm lies in ruins. At Blueprint Village, Master Blueprint teaches the fundamentals of HTML structure.",
        "character": "Master Blueprint",
        "character_quote": "Every webpage is a building. Let's lay the foundation together!",
        "icon": "building",
        "color": "#e44d26",
        "missions": [
            {
                "id": 201,
                "title": "The HTML Document",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "HTML Document Structure",
                    "overview": "Every HTML page follows a specific structure with html, head, and body sections.",
                    "sections": [
                        {"heading": "Basic Structure", "content": "```html\n<!DOCTYPE html>\n<html>\n<head>\n    <title>Page Title</title>\n</head>\n<body>\n    Content here\n</body>\n</html>\n```"},
                        {"heading": "Head vs Body", "content": "- `<head>`: Contains metadata, title, links to CSS\n- `<body>`: Contains visible content"}
                    ]
                },
                "story": "Master Blueprint unfurls an ancient scroll. 'Every webpage needs a proper structure. Let's create one!'",
                "task": "Create a basic HTML document with a title 'My First Page' and a heading in the body.",
                "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <!-- Add title here -->\n</head>\n<body>\n    <!-- Add heading here -->\n</body>\n</html>",
                "expected_output": None,
                "hints": ["Use <title> in the head", "Use <h1> in the body"]
            },
            {
                "id": 202,
                "title": "Text Elements",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Headings and Paragraphs",
                    "overview": "HTML provides tags for organizing text content.",
                    "sections": [
                        {"heading": "Headings", "content": "`<h1>` through `<h6>` create headings of decreasing size."},
                        {"heading": "Paragraphs", "content": "`<p>` creates paragraph blocks of text."},
                        {"heading": "Example", "content": "```html\n<h1>Main Title</h1>\n<p>This is a paragraph.</p>\n```"}
                    ]
                },
                "story": "'Words are the bricks of our buildings,' Blueprint explains. 'Learn to structure them!'",
                "task": "Create an h1 heading and two paragraphs below it.",
                "starter_code": "<!-- Create heading and paragraphs -->\n",
                "expected_output": None,
                "hints": ["Use <h1> and <p> tags"]
            },
            {
                "id": 228,
                "title": "Head vs Body",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Head and Body Sections",
                    "overview": "HTML documents have two main sections: head and body.",
                    "sections": [
                        {"heading": "The Head", "content": "```html\n<head>\n  <title>Page Title</title>\n  <meta charset=\"UTF-8\">\n  <link rel=\"stylesheet\" href=\"style.css\">\n</head>\n```\nContains metadata, title, and links to resources."},
                        {"heading": "The Body", "content": "```html\n<body>\n  <h1>Welcome!</h1>\n  <p>Visible content goes here.</p>\n</body>\n```\nContains all visible content."}
                    ]
                },
                "story": "'Head is for thinking, body is for showing,' Blueprint explains. 'Know the difference!'",
                "task": "Create a complete HTML document with a title in the head and a heading in the body.",
                "starter_code": "<!DOCTYPE html>\n<html>\n<!-- Add head and body -->\n</html>",
                "expected_output": None,
                "hints": ["Use <h1> for the heading", "Use <p> for each paragraph"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Hyperlink Harbor",
        "topic": "Anchors, Paths, Attributes",
        "description": "The harbor where all pathways connect through the power of links!",
        "story_intro": "The connections between structures have broken. Learn to create links and navigate the realm!",
        "character": "Navigator Anchor",
        "character_quote": "Links are the bridges between worlds. Let's build them!",
        "icon": "signpost",
        "color": "#3498db",
        "missions": [
            {
                "id": 203,
                "title": "Creating Links",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "The Anchor Tag",
                    "overview": "The `<a>` tag creates clickable links to other pages.",
                    "sections": [
                        {"heading": "Basic Link", "content": "```html\n<a href=\"https://example.com\">Click me!</a>\n```"},
                        {"heading": "Attributes", "content": "- `href`: The destination URL\n- `target=\"_blank\"`: Opens in new tab"}
                    ]
                },
                "story": "Navigator Anchor shows you the harbor map. 'Every link is a voyage. Let's set sail!'",
                "task": "Create a link that says 'Visit KawaiiCode' linking to https://example.com",
                "starter_code": "<!-- Create your link -->\n",
                "expected_output": None,
                "hints": ["Use <a href=\"url\">text</a>"]
            },
            {
                "id": 204,
                "title": "Path Types",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Absolute vs Relative Paths",
                    "overview": "URLs can be absolute (full address) or relative (from current location).",
                    "sections": [
                        {"heading": "Absolute", "content": "`https://example.com/page.html` - Full URL"},
                        {"heading": "Relative", "content": "`./page.html` or `../folder/page.html` - From current location"},
                        {"heading": "ID Links", "content": "`#section` - Links to an ID on the same page"}
                    ]
                },
                "story": "'Some paths are long, some are short,' Anchor explains. 'Know the difference!'",
                "task": "Create a link to '#about' that says 'Go to About Section'",
                "starter_code": "<!-- Create an internal link -->\n",
                "expected_output": None,
                "hints": ["Use href=\"#about\""]
            },
            {
                "id": 229,
                "title": "HTML Attributes",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Element Attributes",
                    "overview": "Attributes provide extra information about HTML elements.",
                    "sections": [
                        {"heading": "Common Attributes", "content": "- `id` - Unique identifier\n- `class` - For CSS styling\n- `href` - Link destination\n- `src` - Source for images/scripts\n- `alt` - Alternative text"},
                        {"heading": "Syntax", "content": "```html\n<element attribute=\"value\">\n<a href=\"page.html\" class=\"nav-link\" id=\"home-link\">Home</a>\n```"}
                    ]
                },
                "story": "'Attributes are like name tags,' Anchor says. 'They describe and identify!'",
                "task": "Create a link with id, class, and href attributes.",
                "starter_code": "<!-- Create link with multiple attributes -->\n",
                "expected_output": None,
                "hints": ["Use href=\"#about\""]
            }
        ]
    },
    {
        "id": 3,
        "name": "Pixel Portrait Gallery",
        "topic": "Images, Favicons, Alt-text",
        "description": "A gallery where images bring the realm to life!",
        "story_intro": "The gallery walls are empty. Learn to display images and make the realm beautiful!",
        "character": "Curator Pixel",
        "character_quote": "A picture is worth a thousand tags!",
        "icon": "paintbrush",
        "color": "#9b59b6",
        "missions": [
            {
                "id": 205,
                "title": "Adding Images",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "The Image Tag",
                    "overview": "The `<img>` tag displays images on your page.",
                    "sections": [
                        {"heading": "Basic Image", "content": "```html\n<img src=\"image.jpg\" alt=\"Description\">\n```"},
                        {"heading": "Required Attributes", "content": "- `src`: Image source/path\n- `alt`: Alternative text for accessibility"}
                    ]
                },
                "story": "Curator Pixel gestures at the empty frames. 'Let's fill this gallery with images!'",
                "task": "Add an image with src='cat.jpg' and alt='A cute cat'",
                "starter_code": "<!-- Add your image -->\n",
                "expected_output": None,
                "hints": ["img is a self-closing tag", "Include both src and alt attributes"]
            },
            {
                "id": 206,
                "title": "Image Sizing",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Controlling Image Size",
                    "overview": "You can control image dimensions with width and height attributes.",
                    "sections": [
                        {"heading": "Size Attributes", "content": "```html\n<img src=\"pic.jpg\" alt=\"Photo\" width=\"300\" height=\"200\">\n```"},
                        {"heading": "CSS Sizing", "content": "```html\n<img src=\"pic.jpg\" alt=\"Photo\" style=\"width: 100%;\">\n```"}
                    ]
                },
                "story": "'Size matters in a gallery,' Pixel winks. 'Control your image dimensions!'",
                "task": "Create an image with width of 200 pixels.",
                "starter_code": "<!-- Add sized image -->\n",
                "expected_output": None,
                "hints": ["Add width=\"200\" to the img tag"]
            },
            {
                "id": 226,
                "title": "Favicons and Alt-text",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Favicons and Accessibility",
                    "overview": "Favicons identify your site; alt-text makes images accessible.",
                    "sections": [
                        {"heading": "Favicon", "content": "```html\n<head>\n  <link rel=\"icon\" href=\"favicon.ico\" type=\"image/x-icon\">\n</head>\n```\nThe small icon in the browser tab!"},
                        {"heading": "Alt-text", "content": "```html\n<img src=\"hero.jpg\" alt=\"A brave warrior holding a sword\">\n```\n- Describes the image for screen readers\n- Shows when image fails to load\n- Important for accessibility!"}
                    ]
                },
                "story": "'Every image needs a voice,' Pixel explains. 'Alt-text speaks for images!'",
                "task": "Add an image with descriptive alt-text and add a favicon link to the head.",
                "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n  <!-- Add favicon -->\n</head>\n<body>\n  <!-- Add image with alt-text -->\n</body>\n</html>",
                "expected_output": None,
                "hints": ["link rel=\"icon\" for favicon", "alt=\"description\" for accessibility"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Prism Tower",
        "topic": "CSS Selectors, Hex Codes, Typography",
        "description": "The tower of colors where CSS magic transforms plain elements!",
        "story_intro": "Prism Tower has lost its colors. Restore them with the power of CSS!",
        "character": "Chromancer Prism",
        "character_quote": "Colors speak louder than words. Let's paint the web!",
        "icon": "paintbrush",
        "color": "#e74c3c",
        "missions": [
            {
                "id": 207,
                "title": "CSS Selectors",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Selecting Elements",
                    "overview": "CSS selectors target HTML elements to apply styles.",
                    "sections": [
                        {"heading": "Type Selector", "content": "`p { color: blue; }` - Selects all <p> elements"},
                        {"heading": "Class Selector", "content": "`.highlight { color: yellow; }` - Selects elements with class=\"highlight\""},
                        {"heading": "ID Selector", "content": "`#header { color: red; }` - Selects element with id=\"header\""}
                    ]
                },
                "story": "Chromancer Prism waves their wand. 'First, you must learn to select your targets!'",
                "task": "Create a style tag with CSS that makes all paragraphs purple.",
                "starter_code": "<style>\n/* Add your CSS here */\n</style>\n<p>Test paragraph</p>",
                "expected_output": None,
                "hints": ["Use p { color: purple; }"]
            },
            {
                "id": 208,
                "title": "Hex Colors",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Color Values",
                    "overview": "CSS supports multiple ways to define colors.",
                    "sections": [
                        {"heading": "Hex Codes", "content": "`#FF5733` - 6-digit hexadecimal (RRGGBB)"},
                        {"heading": "RGB", "content": "`rgb(255, 87, 51)` - Red, Green, Blue values 0-255"},
                        {"heading": "Named Colors", "content": "`coral`, `steelblue`, `tomato` - CSS color names"}
                    ]
                },
                "story": "'Hex codes unlock infinite colors,' Prism explains. 'Master them!'",
                "task": "Style a div with background color #6c5ce7 (purple).",
                "starter_code": "<!-- Add styled div -->\n",
                "expected_output": None,
                "hints": ["Use style=\"background-color: #6c5ce7;\""]
            },
            {
                "id": 227,
                "title": "Typography Magic",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "CSS Typography",
                    "overview": "Control how text looks with CSS font properties.",
                    "sections": [
                        {"heading": "Font Family", "content": "```css\np {\n  font-family: 'Arial', sans-serif;\n}\n```\nUse web-safe fonts or Google Fonts."},
                        {"heading": "Font Size & Weight", "content": "```css\nh1 {\n  font-size: 32px;\n  font-weight: bold;\n}\n```"},
                        {"heading": "Text Properties", "content": "```css\np {\n  line-height: 1.5;\n  letter-spacing: 1px;\n  text-align: center;\n}\n```"}
                    ]
                },
                "story": "'Typography is the voice of design,' Prism explains. 'Make your text sing!'",
                "task": "Style a heading with a custom font-family, size, and weight.",
                "starter_code": "<style>\n  /* Style the heading */\n</style>\n<h1>Welcome to Kawaii World</h1>",
                "expected_output": None,
                "hints": ["font-family: 'Georgia', serif;", "font-size: 24px; font-weight: bold;"]
            }
        ]
    },
    {
        "id": 5,
        "name": "The Great Box Wall",
        "topic": "Margin, Padding, Border, Width",
        "description": "Understanding the CSS Box Model that surrounds every element!",
        "story_intro": "The wall's boxes are misaligned. Learn the box model to restore order!",
        "character": "Guardian Box",
        "character_quote": "Every element lives in a box. Master the box, master the layout!",
        "icon": "layout",
        "color": "#2ecc71",
        "missions": [
            {
                "id": 209,
                "title": "The Box Model",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "CSS Box Model",
                    "overview": "Every HTML element is a box with content, padding, border, and margin.",
                    "sections": [
                        {"heading": "The Layers", "content": "Content -> Padding -> Border -> Margin (inside to outside)"},
                        {"heading": "Properties", "content": "- `padding`: Space inside the border\n- `border`: The visible edge\n- `margin`: Space outside the border"}
                    ]
                },
                "story": "Guardian Box reveals the secret layers. 'Understand these, and you control space itself!'",
                "task": "Create a div with 20px padding, 2px solid border, and 10px margin.",
                "starter_code": "<!-- Create your box -->\n",
                "expected_output": None,
                "hints": ["Use style with padding, border, and margin properties"]
            },
            {
                "id": 210,
                "title": "Width and Height",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Sizing Elements",
                    "overview": "Control element dimensions with width and height.",
                    "sections": [
                        {"heading": "Fixed Sizes", "content": "`width: 300px; height: 200px;`"},
                        {"heading": "Percentages", "content": "`width: 50%;` - Relative to parent"},
                        {"heading": "Max/Min", "content": "`max-width: 100%; min-height: 50px;`"}
                    ]
                },
                "story": "'Size your boxes precisely,' Box instructs. 'Too big or small causes chaos!'",
                "task": "Create a div that is 200px wide and 100px tall with a background color.",
                "starter_code": "<!-- Create sized box -->\n",
                "expected_output": None,
                "hints": ["Use style with width, height, and background-color"]
            },
            {
                "id": 230,
                "title": "Border Styling",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "CSS Borders",
                    "overview": "Borders add visual boundaries around elements.",
                    "sections": [
                        {"heading": "Border Shorthand", "content": "`border: 2px solid #333;` - width, style, color"},
                        {"heading": "Border Styles", "content": "`solid`, `dashed`, `dotted`, `double`, `none`"},
                        {"heading": "Individual Sides", "content": "```css\nborder-top: 1px solid red;\nborder-left: 3px dashed blue;\nborder-radius: 10px; /* Rounded corners */\n```"}
                    ]
                },
                "story": "'Borders frame your content,' Box explains. 'Like a picture frame for your elements!'",
                "task": "Create a div with a 3px solid purple border and 10px border-radius.",
                "starter_code": "<!-- Create bordered box -->\n",
                "expected_output": None,
                "hints": ["Use width and height in the style attribute"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Flex-Flow Falls",
        "topic": "Flexbox: Justify, Align, Direction",
        "description": "Where elements flow like water with the power of Flexbox!",
        "story_intro": "The waterfalls have frozen. Restore the flow with Flexbox magic!",
        "character": "Flow Master",
        "character_quote": "Flexbox makes layouts flow naturally. Embrace the flex!",
        "icon": "waterfall",
        "color": "#1abc9c",
        "missions": [
            {
                "id": 211,
                "title": "Flexbox Basics",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Introduction to Flexbox",
                    "overview": "Flexbox is a powerful layout system for arranging items.",
                    "sections": [
                        {"heading": "Enable Flexbox", "content": "`display: flex;` on the container"},
                        {"heading": "Direction", "content": "`flex-direction: row | column;`"},
                        {"heading": "Justify Content", "content": "`justify-content: center | space-between | flex-start;`"}
                    ]
                },
                "story": "Flow Master stands at the waterfall's edge. 'Let the elements flow with flex!'",
                "task": "Create a flex container with three child divs centered horizontally.",
                "starter_code": "<div style=\"display: flex;\">\n    <!-- Add children -->\n</div>",
                "expected_output": None,
                "hints": ["Add justify-content: center;", "Add three div children"]
            },
            {
                "id": 212,
                "title": "Align Items",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Cross-Axis Alignment",
                    "overview": "Control vertical alignment with align-items.",
                    "sections": [
                        {"heading": "Align Items", "content": "`align-items: center | flex-start | flex-end | stretch;`"},
                        {"heading": "Center Both Ways", "content": "```css\ndisplay: flex;\njustify-content: center;\nalign-items: center;\n```"}
                    ]
                },
                "story": "'Perfect centering is the ultimate power,' Flow Master whispers. 'Achieve it!'",
                "task": "Create a flex container that centers its content both horizontally and vertically.",
                "starter_code": "<!-- Create centered flex container -->\n",
                "expected_output": None,
                "hints": ["Use both justify-content and align-items set to center"]
            },
            {
                "id": 231,
                "title": "Flex Direction",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Controlling Flex Direction",
                    "overview": "flex-direction controls whether items flow horizontally or vertically.",
                    "sections": [
                        {"heading": "Direction Values", "content": "- `row` (default) - Left to right\n- `row-reverse` - Right to left\n- `column` - Top to bottom\n- `column-reverse` - Bottom to top"},
                        {"heading": "Example", "content": "```css\n.container {\n  display: flex;\n  flex-direction: column;\n}\n```"}
                    ]
                },
                "story": "'Flow can go any direction,' Flow Master teaches. 'Vertical or horizontal, you decide!'",
                "task": "Create a flex container with 3 items stacked vertically using flex-direction: column.",
                "starter_code": "<!-- Create vertical flex container -->\n",
                "expected_output": None,
                "hints": ["Add flex-direction: column to the container style"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Crystal Grid City",
        "topic": "CSS Grid: Areas, Rows, Columns",
        "description": "A city built on the precise grid system of CSS!",
        "story_intro": "The city grid has shattered. Rebuild it with CSS Grid!",
        "character": "Architect Grid",
        "character_quote": "Grid gives you the power of two dimensions!",
        "icon": "city",
        "color": "#3498db",
        "missions": [
            {
                "id": 213,
                "title": "Grid Basics",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Introduction to CSS Grid",
                    "overview": "CSS Grid creates two-dimensional layouts with rows and columns.",
                    "sections": [
                        {"heading": "Enable Grid", "content": "`display: grid;`"},
                        {"heading": "Define Columns", "content": "`grid-template-columns: 1fr 1fr 1fr;` - Three equal columns"},
                        {"heading": "Gap", "content": "`gap: 10px;` - Space between grid items"}
                    ]
                },
                "story": "Architect Grid surveys the ruins. 'With Grid, we rebuild perfectly aligned!'",
                "task": "Create a 3-column grid with 4 items.",
                "starter_code": "<div style=\"display: grid;\">\n    <!-- Add grid items -->\n</div>",
                "expected_output": None,
                "hints": ["Add grid-template-columns: 1fr 1fr 1fr;"]
            },
            {
                "id": 214,
                "title": "Grid Areas",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Named Grid Areas",
                    "overview": "Name areas of your grid for easier layout management.",
                    "sections": [
                        {"heading": "Template Areas", "content": "```css\ngrid-template-areas:\n    \"header header\"\n    \"sidebar main\"\n    \"footer footer\";\n```"},
                        {"heading": "Assign Areas", "content": "`.header { grid-area: header; }`"}
                    ]
                },
                "story": "'Name your zones,' Grid advises. 'Organization brings clarity!'",
                "task": "Create a grid with header, sidebar, main, and footer areas.",
                "starter_code": "<!-- Create grid layout -->\n",
                "expected_output": None,
                "hints": ["Use grid-template-areas to define the layout"]
            },
            {
                "id": 234,
                "title": "Rows and Columns",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Grid Tracks",
                    "overview": "Define grid rows and columns with precise sizing.",
                    "sections": [
                        {"heading": "Defining Columns", "content": "```css\ngrid-template-columns: 200px 1fr 1fr;\n/* 200px fixed, then two equal flexible columns */\n```"},
                        {"heading": "Defining Rows", "content": "```css\ngrid-template-rows: 80px auto 60px;\n/* Fixed header, flexible main, fixed footer */\n```"},
                        {"heading": "Repeat Function", "content": "```css\ngrid-template-columns: repeat(3, 1fr);\n/* Three equal columns */\n```"}
                    ]
                },
                "story": "'Rows and columns are the skeleton,' Grid explains. 'Build them strong!'",
                "task": "Create a 3-column, 2-row grid using grid-template-columns and grid-template-rows.",
                "starter_code": "<!-- Create grid with rows and columns -->\n",
                "expected_output": None,
                "hints": ["Use grid-template-columns: repeat(3, 1fr)", "Use grid-template-rows for row sizing"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Scroll of Forms",
        "topic": "Text inputs, Buttons, Labels",
        "description": "The ancient scrolls that teach the art of collecting user input!",
        "story_intro": "The realm needs to hear from its citizens. Create forms to gather their voices!",
        "character": "Scribe Input",
        "character_quote": "Forms are how the web listens. Let's create the conversation!",
        "icon": "form",
        "color": "#f39c12",
        "missions": [
            {
                "id": 215,
                "title": "Input Fields",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "HTML Form Inputs",
                    "overview": "Create interactive input fields for user data.",
                    "sections": [
                        {"heading": "Text Input", "content": "`<input type=\"text\" placeholder=\"Enter name\">`"},
                        {"heading": "Input Types", "content": "- `text`: Regular text\n- `email`: Email validation\n- `password`: Hidden characters\n- `number`: Numeric input"}
                    ]
                },
                "story": "Scribe Input presents a blank form. 'Teach the page to listen!'",
                "task": "Create a text input with placeholder 'Enter your name'.",
                "starter_code": "<!-- Create input field -->\n",
                "expected_output": None,
                "hints": ["Use <input type=\"text\">", "Add placeholder attribute"]
            },
            {
                "id": 216,
                "title": "Labels and Buttons",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Form Labels and Submission",
                    "overview": "Labels describe inputs, buttons trigger actions.",
                    "sections": [
                        {"heading": "Labels", "content": "```html\n<label for=\"email\">Email:</label>\n<input id=\"email\" type=\"email\">\n```"},
                        {"heading": "Buttons", "content": "`<button type=\"submit\">Send</button>`"}
                    ]
                },
                "story": "'A form without a button is incomplete,' Scribe notes. 'Add the call to action!'",
                "task": "Create a labeled input and a submit button.",
                "starter_code": "<!-- Create form elements -->\n",
                "expected_output": None,
                "hints": ["Connect label to input with for and id", "Use <button> for submission"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Shape-Shifter Forest",
        "topic": "Media Queries, Viewport, Percentages",
        "description": "A magical forest where layouts transform to fit any screen!",
        "story_intro": "The forest must adapt to all visitors. Learn responsive design!",
        "character": "Shifter Responsive",
        "character_quote": "True design adapts to any device. Be like water!",
        "icon": "tree",
        "color": "#27ae60",
        "missions": [
            {
                "id": 217,
                "title": "Viewport Meta",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Mobile-First Setup",
                    "overview": "The viewport meta tag is essential for responsive design.",
                    "sections": [
                        {"heading": "Viewport Tag", "content": "`<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">`"},
                        {"heading": "Why It Matters", "content": "Without this, mobile browsers zoom out to fit desktop layouts."}
                    ]
                },
                "story": "Shifter Responsive shows you a shrinking landscape. 'First, set the viewport!'",
                "task": "Add the viewport meta tag to an HTML head section.",
                "starter_code": "<head>\n    <!-- Add viewport meta -->\n</head>",
                "expected_output": None,
                "hints": ["Use the meta tag with name=\"viewport\""]
            },
            {
                "id": 218,
                "title": "Media Queries",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Responsive Breakpoints",
                    "overview": "Media queries apply styles based on screen size.",
                    "sections": [
                        {"heading": "Basic Query", "content": "```css\n@media (max-width: 768px) {\n    .sidebar { display: none; }\n}\n```"},
                        {"heading": "Common Breakpoints", "content": "- Mobile: 480px\n- Tablet: 768px\n- Desktop: 1024px+"}
                    ]
                },
                "story": "'The forest changes with the season,' Shifter explains. 'Your layout should too!'",
                "task": "Write a media query that hides an element on screens under 600px.",
                "starter_code": "<style>\n/* Add media query */\n</style>",
                "expected_output": None,
                "hints": ["Use @media (max-width: 600px)", "Set display: none;"]
            },
            {
                "id": 232,
                "title": "Percentage Units",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Responsive Percentages",
                    "overview": "Percentages make elements scale relative to their parent.",
                    "sections": [
                        {"heading": "Width Percentages", "content": "```css\n.half { width: 50%; }\n.full { width: 100%; }\n```\nRelative to parent width."},
                        {"heading": "Height Percentages", "content": "Parent must have defined height for % to work on children."},
                        {"heading": "Common Patterns", "content": "```css\n.sidebar { width: 25%; }\n.main-content { width: 75%; }\n```"}
                    ]
                },
                "story": "'Percentages adapt,' Shifter explains. 'They grow and shrink with their container!'",
                "task": "Create two divs side by side, one 30% width and one 70% width.",
                "starter_code": "<!-- Create percentage-based layout -->\n",
                "expected_output": None,
                "hints": ["Use display: flex on parent", "Set width: 30% and width: 70%"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Motion Meadow",
        "topic": "Keyframes, Transitions, Hover effects",
        "description": "The meadow where everything dances with CSS animations!",
        "story_intro": "The meadow has frozen still. Bring it to life with motion!",
        "character": "Dancer Motion",
        "character_quote": "Animation breathes life into the static. Let's dance!",
        "icon": "sparkles",
        "color": "#e91e63",
        "missions": [
            {
                "id": 219,
                "title": "CSS Transitions",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Smooth State Changes",
                    "overview": "Transitions animate changes between CSS states.",
                    "sections": [
                        {"heading": "Transition Property", "content": "`transition: all 0.3s ease;`"},
                        {"heading": "Hover Effects", "content": "```css\n.button {\n    background: blue;\n    transition: background 0.3s;\n}\n.button:hover {\n    background: darkblue;\n}\n```"}
                    ]
                },
                "story": "Dancer Motion twirls gracefully. 'Smooth movements are key to elegance!'",
                "task": "Create a button that changes color smoothly on hover.",
                "starter_code": "<style>\n/* Add button styles */\n</style>\n<button>Hover Me</button>",
                "expected_output": None,
                "hints": ["Add transition property to the base state", "Define :hover styles"]
            },
            {
                "id": 220,
                "title": "Keyframe Animations",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Custom Animations",
                    "overview": "Keyframes define complex multi-step animations.",
                    "sections": [
                        {"heading": "Define Keyframes", "content": "```css\n@keyframes bounce {\n    0% { transform: translateY(0); }\n    50% { transform: translateY(-20px); }\n    100% { transform: translateY(0); }\n}\n```"},
                        {"heading": "Apply Animation", "content": "`.element { animation: bounce 1s infinite; }`"}
                    ]
                },
                "story": "'True animation tells a story frame by frame,' Motion explains. 'Create your dance!'",
                "task": "Create a keyframe animation that fades an element in.",
                "starter_code": "<style>\n/* Define keyframes */\n</style>",
                "expected_output": None,
                "hints": ["Use @keyframes with opacity from 0 to 1", "Apply with animation property"]
            },
            {
                "id": 233,
                "title": "Hover Effects",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Interactive Hover States",
                    "overview": "The :hover pseudo-class adds interactivity when users hover over elements.",
                    "sections": [
                        {"heading": "Hover Syntax", "content": "```css\n.button:hover {\n  background-color: #6c5ce7;\n  transform: scale(1.05);\n}\n```"},
                        {"heading": "Common Effects", "content": "- Color changes\n- Scale transforms\n- Shadow additions\n- Opacity changes"}
                    ]
                },
                "story": "'Hover brings elements to life,' Motion explains. 'React to the user's touch!'",
                "task": "Create a button that changes background color and grows slightly on hover.",
                "starter_code": "<style>\n/* Add hover styles */\n</style>\n<button class=\"magic-btn\">Hover Me!</button>",
                "expected_output": None,
                "hints": ["Use .magic-btn:hover", "Add transform: scale(1.1) for growth effect"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Component Cathedral",
        "topic": "Semantic HTML, Headings, Lists",
        "description": "A sacred cathedral of properly structured, meaningful HTML!",
        "story_intro": "The cathedral's meaning has been lost. Restore it with semantic HTML!",
        "character": "Bishop Semantic",
        "character_quote": "Meaningful markup is accessible markup. Structure with purpose!",
        "icon": "landmark",
        "color": "#8e44ad",
        "missions": [
            {
                "id": 221,
                "title": "Semantic Elements",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Meaningful HTML Tags",
                    "overview": "Semantic tags describe their content's purpose.",
                    "sections": [
                        {"heading": "Structural Tags", "content": "- `<header>`: Page/section header\n- `<nav>`: Navigation links\n- `<main>`: Main content\n- `<footer>`: Page/section footer"},
                        {"heading": "Content Tags", "content": "- `<article>`: Independent content\n- `<section>`: Thematic grouping\n- `<aside>`: Sidebar content"}
                    ]
                },
                "story": "Bishop Semantic reveals the cathedral's blueprint. 'Each section has a sacred name!'",
                "task": "Create a page with header, main, and footer semantic tags.",
                "starter_code": "<!-- Use semantic structure -->\n",
                "expected_output": None,
                "hints": ["Use <header>, <main>, and <footer> tags"]
            },
            {
                "id": 222,
                "title": "Lists",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "HTML Lists",
                    "overview": "Organize content with ordered and unordered lists.",
                    "sections": [
                        {"heading": "Unordered List", "content": "```html\n<ul>\n    <li>Item 1</li>\n    <li>Item 2</li>\n</ul>\n```"},
                        {"heading": "Ordered List", "content": "```html\n<ol>\n    <li>First</li>\n    <li>Second</li>\n</ol>\n```"}
                    ]
                },
                "story": "'Organization brings clarity,' Bishop notes. 'List your elements properly!'",
                "task": "Create an unordered list with three items.",
                "starter_code": "<!-- Create a list -->\n",
                "expected_output": None,
                "hints": ["Use <ul> with <li> children"]
            },
            {
                "id": 235,
                "title": "Heading Hierarchy",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "HTML Headings",
                    "overview": "Headings create structure and hierarchy in your content.",
                    "sections": [
                        {"heading": "Heading Levels", "content": "```html\n<h1>Main Title</h1>\n<h2>Section</h2>\n<h3>Subsection</h3>\n<h4>Sub-subsection</h4>\n<h5>Minor heading</h5>\n<h6>Smallest heading</h6>\n```"},
                        {"heading": "Best Practices", "content": "- Only one `<h1>` per page\n- Don't skip levels (h1 -> h3)\n- Use for structure, not styling"}
                    ]
                },
                "story": "'Headings guide the reader,' Bishop teaches. 'Use them wisely!'",
                "task": "Create a page structure with h1, h2, and h3 headings in proper hierarchy.",
                "starter_code": "<!-- Create heading hierarchy -->\n",
                "expected_output": None,
                "hints": ["Start with h1 for main title", "Use h2 for sections, h3 for subsections"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Architect's Trial",
        "topic": "Building a full Kawaii Portfolio",
        "description": "The ultimate trial where you build a complete portfolio page!",
        "story_intro": "You have learned all the arts of the Architect's Realm. Now prove your mastery!",
        "character": "Grand Architect",
        "character_quote": "Show me everything you've learned. Build your masterpiece!",
        "icon": "trophy",
        "color": "#f1c40f",
        "missions": [
            {
                "id": 223,
                "title": "Portfolio Header",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Building the Header",
                    "overview": "Start your portfolio with a stunning header section.",
                    "sections": [
                        {"heading": "Header Elements", "content": "Include your name, navigation, and a brief tagline."},
                        {"heading": "Styling", "content": "Use flexbox for navigation layout, add colors and fonts."}
                    ]
                },
                "story": "The Grand Architect watches. 'Your portfolio begins with a memorable header!'",
                "task": "Create a styled header with your name and a navigation menu.",
                "starter_code": "<!-- Build portfolio header -->\n",
                "expected_output": None,
                "hints": ["Use <header> with <nav>", "Style with flexbox and colors"]
            },
            {
                "id": 224,
                "title": "Portfolio Main Section",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Building the Main Content",
                    "overview": "Create sections for about, projects, and contact.",
                    "sections": [
                        {"heading": "About Section", "content": "Introduce yourself with image and text."},
                        {"heading": "Projects Grid", "content": "Display projects using CSS Grid."},
                        {"heading": "Contact Form", "content": "Add a form for visitors to reach you."}
                    ]
                },
                "story": "'The body of your portfolio tells your story,' Grand Architect advises. 'Make it count!'",
                "task": "Create a main section with about, projects, and contact areas.",
                "starter_code": "<!-- Build main content sections -->\n",
                "expected_output": None,
                "hints": ["Use semantic <section> tags", "Apply grid for projects"]
            },
            {
                "id": 225,
                "title": "Final Polish",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Finishing Touches",
                    "overview": "Add responsive design, animations, and final styling.",
                    "sections": [
                        {"heading": "Responsive", "content": "Add media queries for mobile devices."},
                        {"heading": "Animations", "content": "Subtle hover effects and transitions."},
                        {"heading": "Polish", "content": "Consistent spacing, fonts, and colors throughout."}
                    ]
                },
                "story": "The Grand Architect nods approvingly. 'Complete your masterpiece!'",
                "task": "Add responsive styles and hover effects to complete your portfolio.",
                "starter_code": "<!-- Add final polish -->\n",
                "expected_output": None,
                "hints": ["Add media queries for mobile", "Include transition effects"]
            }
        ]
    }
]

C_ARCS = [
    {
        "id": 1,
        "name": "Iron Root Village",
        "topic": "main(), data types, printf",
        "description": "Where every C programmer begins their journey into the machine's heart!",
        "story_intro": "The Foundation Stone realm holds the deepest secrets of computing. At Iron Root Village, you'll learn to speak the machine's language.",
        "character": "Elder Root",
        "character_quote": "C is the language of the machine. Let's plant your first roots!",
        "icon": "terminal",
        "color": "#555555",
        "missions": [
            {
                "id": 301,
                "title": "The Main Function",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "C Program Structure",
                    "overview": "Every C program starts with main().",
                    "sections": [
                        {"heading": "Basic Structure", "content": "```c\n#include <stdio.h>\n\nint main() {\n    printf(\"Hello!\\n\");\n    return 0;\n}\n```"},
                        {"heading": "Components", "content": "- `#include`: Brings in libraries\n- `main()`: Entry point\n- `return 0`: Success code"}
                    ]
                },
                "story": "Elder Root unfurls an ancient scroll. 'Every program begins with main. Let's write your first!'",
                "task": "Write a C program that prints 'Hello, C World!'",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}",
                "expected_output": "Hello, C World!",
                "hints": ["Use printf(\"text\\n\");"]
            },
            {
                "id": 302,
                "title": "Data Types",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "C Data Types",
                    "overview": "C requires explicit type declarations.",
                    "sections": [
                        {"heading": "Basic Types", "content": "- `int`: Integers\n- `float`: Decimals\n- `char`: Single character\n- `double`: Double precision"},
                        {"heading": "Example", "content": "```c\nint age = 25;\nfloat price = 9.99;\nchar grade = 'A';\n```"}
                    ]
                },
                "story": "'Types define the nature of your data,' Elder explains. 'Choose wisely!'",
                "task": "Create an int 'level' = 10 and print 'Level: 10'",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // Declare and print\n    return 0;\n}",
                "expected_output": "Level: 10",
                "hints": ["Use %d for integers in printf"]
            },
            {
                "id": 330,
                "title": "Printf Mastery",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Formatted Output with printf",
                    "overview": "printf is C's powerful output function with format specifiers.",
                    "sections": [
                        {"heading": "Format Specifiers", "content": "- `%d` or `%i`: Integer\n- `%f`: Float/double\n- `%c`: Character\n- `%s`: String\n- `%%`: Percent sign"},
                        {"heading": "Formatting Options", "content": "```c\nprintf(\"Name: %s, Age: %d\\n\", name, age);\nprintf(\"Price: %.2f\\n\", 9.99);  // 2 decimals\nprintf(\"Padded: %5d\\n\", 42);    // width 5\n```"},
                        {"heading": "Escape Sequences", "content": "- `\\n`: New line\n- `\\t`: Tab\n- `\\\\`: Backslash"}
                    ]
                },
                "story": "'printf is your voice in C,' Elder Root reveals. 'Master its formats!'",
                "task": "Print a formatted message: 'Hero: Luna, HP: 100, Gold: 250.50' using printf with variables.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    char name[] = \"Luna\";\n    int hp = 100;\n    float gold = 250.50;\n    // Use printf with format specifiers\n    return 0;\n}",
                "expected_output": "Hero: Luna, HP: 100, Gold: 250.50",
                "hints": ["printf(\"Hero: %s, HP: %d, Gold: %.2f\", name, hp, gold);", "Use %s for strings, %d for int, %.2f for float with 2 decimals"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Forge of Logic",
        "topic": "operators, switch, if/else",
        "description": "The forge where decisions are hammered out!",
        "story_intro": "Logic is the hammer that shapes code. Learn to make decisions!",
        "character": "Smith Binary",
        "character_quote": "True or false - the forge knows only two states!",
        "icon": "signpost",
        "color": "#666666",
        "missions": [
            {
                "id": 303,
                "title": "If/Else Forging",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Conditional Statements",
                    "overview": "Make decisions with if/else.",
                    "sections": [
                        {"heading": "If Statement", "content": "```c\nif (x > 10) {\n    printf(\"Big!\\n\");\n} else {\n    printf(\"Small!\\n\");\n}\n```"}
                    ]
                },
                "story": "Smith Binary heats the forge. 'Decide the path!'",
                "task": "Check if 'power' (75) is > 50. Print 'Strong!' or 'Weak!'",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    int power = 75;\n    // Your logic\n    return 0;\n}",
                "expected_output": "Strong!",
                "hints": ["Use if (power > 50)"]
            },
            {
                "id": 304,
                "title": "Switch Blade",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Switch Statements",
                    "overview": "Handle multiple cases efficiently.",
                    "sections": [
                        {"heading": "Switch Syntax", "content": "```c\nswitch(choice) {\n    case 1: printf(\"One\"); break;\n    case 2: printf(\"Two\"); break;\n    default: printf(\"Other\");\n}\n```"}
                    ]
                },
                "story": "'Many paths, one switch,' the Smith explains.",
                "task": "Use switch to print the day name for day=3 (Wednesday).",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    int day = 3;\n    // Switch statement\n    return 0;\n}",
                "expected_output": "Wednesday",
                "hints": ["Don't forget break;"]
            },
            {
                "id": 331,
                "title": "Operators Mastery",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "C Operators",
                    "overview": "Operators perform calculations and comparisons.",
                    "sections": [
                        {"heading": "Arithmetic", "content": "```c\nint sum = 10 + 5;    // 15\nint diff = 10 - 5;   // 5\nint prod = 10 * 5;   // 50\nint quot = 10 / 5;   // 2\nint mod = 10 % 3;    // 1 (remainder)\n```"},
                        {"heading": "Comparison", "content": "```c\n==  // equal\n!=  // not equal\n>   // greater than\n<   // less than\n>=  // greater or equal\n<=  // less or equal\n```"},
                        {"heading": "Logical", "content": "```c\n&&  // AND\n||  // OR\n!   // NOT\n```"}
                    ]
                },
                "story": "'Operators are your tools,' Smith Binary explains. 'Use them wisely!'",
                "task": "Calculate the area of a rectangle (width=5, height=3) and check if it's greater than 10.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    int width = 5, height = 3;\n    // Calculate and compare\n    return 0;\n}",
                "expected_output": "Area: 15, Greater than 10: Yes",
                "hints": ["Use * for multiplication", "Use > for comparison"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Clockwork Gears",
        "topic": "while, for, nested loops",
        "description": "The mechanical heart where repetition powers everything!",
        "story_intro": "The gears have stopped. Restart them with loops!",
        "character": "Gear Master",
        "character_quote": "Round and round, the gears turn with each iteration!",
        "icon": "waves",
        "color": "#777777",
        "missions": [
            {
                "id": 305,
                "title": "For Loop Gears",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "For Loops in C",
                    "overview": "Repeat with for loops.",
                    "sections": [
                        {"heading": "For Syntax", "content": "```c\nfor (int i = 0; i < 5; i++) {\n    printf(\"%d\\n\", i);\n}\n```"}
                    ]
                },
                "story": "Gear Master spins a wheel. 'Watch the gears turn!'",
                "task": "Print numbers 1 to 5 using a for loop.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // For loop\n    return 0;\n}",
                "expected_output": "1\n2\n3\n4\n5",
                "hints": ["Start at 1, go while <= 5"]
            },
            {
                "id": 306,
                "title": "While Loop Power",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "While Loops in C",
                    "overview": "Repeat while a condition is true.",
                    "sections": [
                        {"heading": "While Syntax", "content": "```c\nint i = 0;\nwhile (i < 5) {\n    printf(\"%d\\n\", i);\n    i++;\n}\n```"},
                        {"heading": "Key Points", "content": "- Check condition BEFORE running\n- Must update the variable inside\n- Useful when count is unknown"}
                    ]
                },
                "story": "Gear Master points to a spinning wheel. 'While the condition holds, the gears turn!'",
                "task": "Use a while loop to print numbers 5 down to 1.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    int n = 5;\n    // While loop\n    return 0;\n}",
                "expected_output": "5\n4\n3\n2\n1",
                "hints": ["while (n > 0)", "Don't forget n--"]
            },
            {
                "id": 327,
                "title": "Nested Gears",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Nested Loops",
                    "overview": "Loops inside loops for complex patterns.",
                    "sections": [
                        {"heading": "Nested For", "content": "```c\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 3; j++) {\n        printf(\"*\");\n    }\n    printf(\"\\n\");\n}\n```"}
                    ]
                },
                "story": "'Gears within gears,' the Master reveals. 'Nested power!'",
                "task": "Print a 3x3 grid of asterisks.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // Nested loops\n    return 0;\n}",
                "expected_output": "***\n***\n***",
                "hints": ["Outer loop for rows, inner for columns"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Module Mines",
        "topic": "prototypes, return types",
        "description": "Deep mines where reusable code modules are forged!",
        "story_intro": "The mines need organization. Create functions!",
        "character": "Miner Modular",
        "character_quote": "A function is a tool you craft once and use forever!",
        "icon": "scroll",
        "color": "#888888",
        "missions": [
            {
                "id": 307,
                "title": "Function Basics",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "C Functions",
                    "overview": "Create reusable code blocks.",
                    "sections": [
                        {"heading": "Function Syntax", "content": "```c\nint add(int a, int b) {\n    return a + b;\n}\n```"},
                        {"heading": "Prototypes", "content": "Declare before main:\n```c\nint add(int a, int b);\n```"}
                    ]
                },
                "story": "Miner Modular hands you a pickaxe. 'Carve your first function!'",
                "task": "Create a function 'square' that returns x*x.",
                "starter_code": "#include <stdio.h>\n\n// Function here\n\nint main() {\n    printf(\"%d\\n\", square(5));\n    return 0;\n}",
                "expected_output": "25",
                "hints": ["int square(int x) { return x*x; }"]
            },
            {
                "id": 308,
                "title": "Void Functions",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Void Return Type",
                    "overview": "Functions that don't return values.",
                    "sections": [
                        {"heading": "Void Functions", "content": "```c\nvoid greet(char *name) {\n    printf(\"Hello, %s!\\n\", name);\n}\n```"}
                    ]
                },
                "story": "'Some functions just act,' Miner explains. 'They need no return!'",
                "task": "Create a void function 'shout' that prints 'HELLO!'",
                "starter_code": "#include <stdio.h>\n\n// Void function\n\nint main() {\n    shout();\n    return 0;\n}",
                "expected_output": "HELLO!",
                "hints": ["void shout() { printf... }"]
            },
            {
                "id": 332,
                "title": "Function Prototypes",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Forward Declarations",
                    "overview": "Prototypes declare functions before their full definition.",
                    "sections": [
                        {"heading": "Why Prototypes", "content": "C reads top-to-bottom. To call a function before defining it, declare a prototype first."},
                        {"heading": "Prototype Syntax", "content": "```c\n// Prototype (declaration)\nint add(int a, int b);\n\nint main() {\n    int result = add(3, 5);  // Works!\n    return 0;\n}\n\n// Definition (later)\nint add(int a, int b) {\n    return a + b;\n}\n```"}
                    ]
                },
                "story": "'Declare your intentions first,' Miner advises. 'Then define the details!'",
                "task": "Write a function prototype for 'multiply', then define it below main.",
                "starter_code": "#include <stdio.h>\n\n// Prototype here\n\nint main() {\n    printf(\"%d\\n\", multiply(4, 3));\n    return 0;\n}\n\n// Definition here",
                "expected_output": "12",
                "hints": ["int multiply(int a, int b);", "Define the function after main()"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Vector Valley",
        "topic": "single & multidimensional arrays",
        "description": "A valley of organized data stretching to the horizon!",
        "story_intro": "Data lies scattered. Organize it with arrays!",
        "character": "Index Guardian",
        "character_quote": "Arrays start at zero. Never forget!",
        "icon": "islands",
        "color": "#999999",
        "missions": [
            {
                "id": 309,
                "title": "Array Basics",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "C Arrays",
                    "overview": "Store multiple values of the same type.",
                    "sections": [
                        {"heading": "Declaring Arrays", "content": "```c\nint nums[5] = {1, 2, 3, 4, 5};\nprintf(\"%d\", nums[0]); // First element\n```"}
                    ]
                },
                "story": "Index Guardian points to the valley. 'Each slot holds a value!'",
                "task": "Create an array of 3 numbers and print the first.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // Create and access array\n    return 0;\n}",
                "expected_output": None,
                "hints": ["int arr[3] = {10, 20, 30};"]
            },
            {
                "id": 310,
                "title": "2D Arrays",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Multidimensional Arrays",
                    "overview": "Arrays of arrays for grids and matrices.",
                    "sections": [
                        {"heading": "2D Array", "content": "```c\nint grid[2][3] = {{1,2,3}, {4,5,6}};\nprintf(\"%d\", grid[1][2]); // 6\n```"}
                    ]
                },
                "story": "'The valley has depth,' Guardian reveals. 'Rows and columns!'",
                "task": "Create a 2x2 matrix and print element [1][1].",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // 2D array\n    return 0;\n}",
                "expected_output": None,
                "hints": ["int mat[2][2] = {{1,2},{3,4}};"]
            }
        ]
    },
    {
        "id": 6,
        "name": "String Sanctuary",
        "topic": "char arrays, string.h functions",
        "description": "A sacred place where characters unite as strings!",
        "story_intro": "Words have power. Learn to wield string magic!",
        "character": "Scribe Char",
        "character_quote": "In C, strings are just arrays of characters!",
        "icon": "scroll",
        "color": "#aaaaaa",
        "missions": [
            {
                "id": 311,
                "title": "Character Arrays",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Strings in C",
                    "overview": "Strings are null-terminated char arrays.",
                    "sections": [
                        {"heading": "String Declaration", "content": "```c\nchar name[] = \"Hero\";\nchar name2[10] = \"Hero\";\n```"},
                        {"heading": "Null Terminator", "content": "Strings end with '\\0' automatically."}
                    ]
                },
                "story": "Scribe Char writes in the air. 'Characters become words!'",
                "task": "Create a string 'greeting' with value 'Hello' and print it.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // String variable\n    return 0;\n}",
                "expected_output": "Hello",
                "hints": ["char greeting[] = \"Hello\";"]
            },
            {
                "id": 312,
                "title": "String Functions",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "string.h Library",
                    "overview": "Useful functions for string manipulation.",
                    "sections": [
                        {"heading": "Common Functions", "content": "- `strlen(s)`: Length\n- `strcpy(dest, src)`: Copy\n- `strcat(dest, src)`: Concatenate\n- `strcmp(a, b)`: Compare"}
                    ]
                },
                "story": "'The library holds ancient string spells,' Scribe reveals.",
                "task": "Find and print the length of 'Hello World'.",
                "starter_code": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    char str[] = \"Hello World\";\n    // Use strlen\n    return 0;\n}",
                "expected_output": "11",
                "hints": ["printf(\"%lu\", strlen(str));"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Void Compass",
        "topic": "Addresses (&), dereferencing (*)",
        "description": "Navigate the realm of memory addresses!",
        "story_intro": "Pointers reveal the true locations of data. Master them!",
        "character": "Navigator Pointer",
        "character_quote": "Every variable has an address. Pointers find them!",
        "icon": "signpost",
        "color": "#bbbbbb",
        "missions": [
            {
                "id": 313,
                "title": "Pointer Basics",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Introduction to Pointers",
                    "overview": "Pointers store memory addresses.",
                    "sections": [
                        {"heading": "Address Operator", "content": "```c\nint x = 10;\nprintf(\"%p\", &x); // Address of x\n```"},
                        {"heading": "Pointer Variable", "content": "```c\nint *ptr = &x;\nprintf(\"%d\", *ptr); // Value at address\n```"}
                    ]
                },
                "story": "Navigator Pointer holds up a compass. 'It points to memory!'",
                "task": "Create int x=42, a pointer to it, and print the value via pointer.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // Pointer magic\n    return 0;\n}",
                "expected_output": "42",
                "hints": ["int *ptr = &x; printf(\"%d\", *ptr);"]
            },
            {
                "id": 314,
                "title": "Pointer Modification",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Modifying via Pointers",
                    "overview": "Change values through their addresses.",
                    "sections": [
                        {"heading": "Dereferencing", "content": "```c\nint x = 10;\nint *ptr = &x;\n*ptr = 20; // x is now 20\n```"}
                    ]
                },
                "story": "'Change the destination through the compass,' Navigator instructs.",
                "task": "Use a pointer to change x from 10 to 100, then print x.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    int x = 10;\n    // Modify via pointer\n    return 0;\n}",
                "expected_output": "100",
                "hints": ["*ptr = 100;"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Memory Chamber",
        "topic": "Pointer arithmetic, arrays as pointers",
        "description": "The deep chamber where pointers and arrays merge!",
        "story_intro": "Arrays and pointers are deeply connected. Discover the truth!",
        "character": "Sage Memory",
        "character_quote": "An array name is just a pointer to its first element!",
        "icon": "layout",
        "color": "#cccccc",
        "missions": [
            {
                "id": 315,
                "title": "Pointer Arithmetic",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Pointer Math",
                    "overview": "Move through memory with pointer arithmetic.",
                    "sections": [
                        {"heading": "Incrementing Pointers", "content": "```c\nint arr[] = {10, 20, 30};\nint *p = arr;\np++; // Now points to arr[1]\nprintf(\"%d\", *p); // 20\n```"}
                    ]
                },
                "story": "Sage Memory reveals a secret. 'Pointers can walk through arrays!'",
                "task": "Use pointer arithmetic to print the second element of an array.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    int arr[] = {5, 10, 15};\n    int *p = arr;\n    // Print second element\n    return 0;\n}",
                "expected_output": "10",
                "hints": ["p++ then *p, or *(p+1)"]
            },
            {
                "id": 316,
                "title": "Arrays as Pointers",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Array-Pointer Equivalence",
                    "overview": "Array names decay to pointers.",
                    "sections": [
                        {"heading": "Equivalence", "content": "```c\nint arr[] = {1, 2, 3};\nprintf(\"%d\", *(arr + 2)); // Same as arr[2]\n```"}
                    ]
                },
                "story": "'Arrays and pointers are two sides of one coin,' Sage explains.",
                "task": "Access arr[2] using pointer notation *(arr + 2).",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    int arr[] = {100, 200, 300};\n    // Pointer notation\n    return 0;\n}",
                "expected_output": "300",
                "hints": ["printf(\"%d\", *(arr + 2));"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Struct Stone-Circle",
        "topic": "struct, typedef, unions",
        "description": "Ancient stones that group data into meaningful structures!",
        "story_intro": "Related data belongs together. Create structures!",
        "character": "Architect Struct",
        "character_quote": "Structures give meaning to raw data!",
        "icon": "building",
        "color": "#dddddd",
        "missions": [
            {
                "id": 317,
                "title": "Creating Structs",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Structures in C",
                    "overview": "Group related variables together.",
                    "sections": [
                        {"heading": "Struct Syntax", "content": "```c\nstruct Hero {\n    char name[50];\n    int level;\n    int health;\n};\n```"},
                        {"heading": "Using Structs", "content": "```c\nstruct Hero h1;\nh1.level = 5;\n```"}
                    ]
                },
                "story": "Architect Struct arranges the stones. 'Data united has power!'",
                "task": "Create a struct 'Point' with x and y, then print a point.",
                "starter_code": "#include <stdio.h>\n\n// Define struct\n\nint main() {\n    // Create and print\n    return 0;\n}",
                "expected_output": None,
                "hints": ["struct Point { int x; int y; };"]
            },
            {
                "id": 318,
                "title": "Typedef Magic",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Typedef",
                    "overview": "Create type aliases for convenience.",
                    "sections": [
                        {"heading": "Typedef Syntax", "content": "```c\ntypedef struct {\n    int x;\n    int y;\n} Point;\n\nPoint p1; // No need for 'struct'\n```"}
                    ]
                },
                "story": "'Name your structures for easy use,' Architect advises.",
                "task": "Use typedef to create a Player type with name and score.",
                "starter_code": "#include <stdio.h>\n\n// Typedef struct\n\nint main() {\n    // Create Player\n    return 0;\n}",
                "expected_output": None,
                "hints": ["typedef struct { ... } Player;"]
            },
            {
                "id": 328,
                "title": "Union Power",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Unions in C",
                    "overview": "Unions share memory between members.",
                    "sections": [
                        {"heading": "Union Syntax", "content": "```c\nunion Data {\n    int i;\n    float f;\n    char c;\n};\n// Only ONE member active at a time\n```"},
                        {"heading": "Key Difference", "content": "- Struct: all members have separate memory\n- Union: all members SHARE the same memory\n- Size = largest member"}
                    ]
                },
                "story": "'Unions are magical,' Architect explains. 'One space, many forms!'",
                "task": "Create a union that can hold either an int or a float, demonstrate both uses.",
                "starter_code": "#include <stdio.h>\n\n// Define union\n\nint main() {\n    // Use union\n    return 0;\n}",
                "expected_output": None,
                "hints": ["union Number { int i; float f; };", "Only use one member at a time"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Alchemy Lab",
        "topic": "malloc(), free(), calloc()",
        "description": "The laboratory where memory is conjured and released!",
        "story_intro": "Static allocation has limits. Learn dynamic memory!",
        "character": "Alchemist Malloc",
        "character_quote": "Conjure memory at will - but always release it!",
        "icon": "sparkles",
        "color": "#ee9944",
        "missions": [
            {
                "id": 319,
                "title": "Dynamic Allocation",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "malloc and free",
                    "overview": "Allocate memory at runtime.",
                    "sections": [
                        {"heading": "malloc", "content": "```c\nint *arr = (int*)malloc(5 * sizeof(int));\n```"},
                        {"heading": "free", "content": "```c\nfree(arr); // Release memory\n```"}
                    ]
                },
                "story": "Alchemist Malloc stirs a cauldron. 'Memory from nothing!'",
                "task": "Allocate an array of 3 ints, set values, print, then free.",
                "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Dynamic allocation\n    return 0;\n}",
                "expected_output": None,
                "hints": ["malloc(3 * sizeof(int))"]
            },
            {
                "id": 320,
                "title": "Memory Safety",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Safe Memory Practices",
                    "overview": "Avoid memory leaks and errors.",
                    "sections": [
                        {"heading": "Check NULL", "content": "```c\nint *p = malloc(100);\nif (p == NULL) {\n    printf(\"Allocation failed!\");\n    return 1;\n}\n```"},
                        {"heading": "Always Free", "content": "Every malloc needs a free!"}
                    ]
                },
                "story": "'Leaked memory haunts the realm,' Alchemist warns. 'Always clean up!'",
                "task": "Allocate memory, check for NULL, use it, then free it.",
                "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Safe allocation\n    return 0;\n}",
                "expected_output": None,
                "hints": ["if (ptr == NULL) return 1;"]
            },
            {
                "id": 329,
                "title": "Calloc Magic",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "calloc - Zero-Initialized Memory",
                    "overview": "calloc allocates AND initializes memory to zero.",
                    "sections": [
                        {"heading": "calloc Syntax", "content": "```c\n// calloc(count, size)\nint *arr = (int*)calloc(5, sizeof(int));\n// All elements are 0!\n```"},
                        {"heading": "malloc vs calloc", "content": "- malloc: faster, garbage values\n- calloc: slower, all zeros\n- Use calloc when you need zeroed memory"}
                    ]
                },
                "story": "'calloc gives you clean memory,' Alchemist reveals. 'No garbage, only zeros!'",
                "task": "Use calloc to allocate 5 ints, verify they're all zero, then free.",
                "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Use calloc\n    return 0;\n}",
                "expected_output": None,
                "hints": ["calloc(5, sizeof(int))", "Print each element to verify zeros"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Archive Library",
        "topic": "fopen, fprintf, fscanf",
        "description": "The great library where data is written to eternal files!",
        "story_intro": "Memory is temporary. Files are forever. Learn file I/O!",
        "character": "Archivist File",
        "character_quote": "Save your data before the program ends!",
        "icon": "scroll",
        "color": "#8899aa",
        "missions": [
            {
                "id": 321,
                "title": "Writing Files",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "File Output",
                    "overview": "Write data to files.",
                    "sections": [
                        {"heading": "fopen and fprintf", "content": "```c\nFILE *f = fopen(\"data.txt\", \"w\");\nfprintf(f, \"Hello File!\\n\");\nfclose(f);\n```"}
                    ]
                },
                "story": "Archivist File opens a dusty tome. 'Let's write to the archives!'",
                "task": "Write 'Hello, File!' to a file called output.txt.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // File writing\n    return 0;\n}",
                "expected_output": None,
                "hints": ["fopen with \"w\" mode, fprintf, fclose"]
            },
            {
                "id": 322,
                "title": "Reading Files",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "File Input",
                    "overview": "Read data from files.",
                    "sections": [
                        {"heading": "fscanf", "content": "```c\nFILE *f = fopen(\"data.txt\", \"r\");\nchar buffer[100];\nfscanf(f, \"%s\", buffer);\nfclose(f);\n```"}
                    ]
                },
                "story": "'The archives hold ancient knowledge,' Archivist reveals. 'Read it!'",
                "task": "Read a word from a file and print it.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // File reading\n    return 0;\n}",
                "expected_output": None,
                "hints": ["fopen with \"r\" mode, fscanf"]
            },
            {
                "id": 333,
                "title": "Opening Files",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "fopen Function",
                    "overview": "fopen opens files for reading, writing, or appending.",
                    "sections": [
                        {"heading": "File Modes", "content": "```c\nFILE *f;\nf = fopen(\"data.txt\", \"r\");  // Read\nf = fopen(\"data.txt\", \"w\");  // Write (creates/overwrites)\nf = fopen(\"data.txt\", \"a\");  // Append\n```"},
                        {"heading": "Error Checking", "content": "```c\nFILE *f = fopen(\"data.txt\", \"r\");\nif (f == NULL) {\n    printf(\"Error opening file!\\n\");\n    return 1;\n}\nfclose(f);  // Always close!\n```"}
                    ]
                },
                "story": "'The gate to the archives is fopen,' Archivist explains. 'Choose your mode wisely!'",
                "task": "Open a file for writing, check if it opened successfully, then close it.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    // Open, check, and close a file\n    return 0;\n}",
                "expected_output": "File opened successfully!",
                "hints": ["Use fopen with \"w\" mode", "Check if result is NULL"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Hardware Hero Trial",
        "topic": "Direct memory manipulation challenge",
        "description": "The ultimate trial where you master the machine itself!",
        "story_intro": "You've learned the ways of C. Now prove your mastery!",
        "character": "Grand Master C",
        "character_quote": "Show me you understand the machine. Build something powerful!",
        "icon": "trophy",
        "color": "#ffd700",
        "missions": [
            {
                "id": 323,
                "title": "Memory Manager",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Building a Memory Pool",
                    "overview": "Create a simple memory management system.",
                    "sections": [
                        {"heading": "The Challenge", "content": "Combine structs, pointers, and dynamic allocation."},
                        {"heading": "Design", "content": "Track allocated blocks and their sizes."}
                    ]
                },
                "story": "Grand Master C watches silently. 'Manage memory yourself!'",
                "task": "Create a struct to track memory blocks with pointer and size.",
                "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\n// Your memory manager\n\nint main() {\n    return 0;\n}",
                "expected_output": None,
                "hints": ["struct Block { void *ptr; size_t size; };"]
            },
            {
                "id": 324,
                "title": "Binary Operations",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Bit Manipulation",
                    "overview": "Work directly with bits.",
                    "sections": [
                        {"heading": "Bit Operators", "content": "- `&` AND\n- `|` OR\n- `^` XOR\n- `<<` Left shift\n- `>>` Right shift"}
                    ]
                },
                "story": "'The deepest level,' Master reveals. 'Individual bits!'",
                "task": "Use bitwise operations to set and check specific bits.",
                "starter_code": "#include <stdio.h>\n\nint main() {\n    unsigned char flags = 0;\n    // Bit operations\n    return 0;\n}",
                "expected_output": None,
                "hints": ["flags |= (1 << 3); to set bit 3"]
            },
            {
                "id": 325,
                "title": "The Final Program",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "Complete C Application",
                    "overview": "Build a complete program using all C concepts.",
                    "sections": [
                        {"heading": "Requirements", "content": "- Structs for data\n- Dynamic memory\n- File I/O\n- Functions for organization"}
                    ]
                },
                "story": "Grand Master C nods. 'Create your masterpiece!'",
                "task": "Build a contact book that saves/loads from a file.",
                "starter_code": "// Complete C application\n#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// Your code here",
                "expected_output": None,
                "hints": ["Struct for Contact, array/list of contacts, file save/load"]
            }
        ]
    }
]

CPP_ARCS = [
    {
        "id": 1,
        "name": "Blade-Smith Shop",
        "topic": "cin/cout, namespaces, strings",
        "description": "Where every C++ warrior forges their first blade of code!",
        "story_intro": "The Guardian's Blade realm awaits. At the Blade-Smith Shop, you'll learn the foundations of C++.",
        "character": "Smith Stroustrup",
        "character_quote": "C++ sharpens C into a powerful blade. Let's forge yours!",
        "icon": "terminal",
        "color": "#0066aa",
        "missions": [
            {
                "id": 401,
                "title": "Streams of Power",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "cin and cout",
                    "overview": "C++ uses streams for input and output.",
                    "sections": [
                        {"heading": "cout Output", "content": "```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello!\" << endl;\n    return 0;\n}\n```"},
                        {"heading": "cin Input", "content": "```cpp\nint age;\ncin >> age;\n```"}
                    ]
                },
                "story": "Smith Stroustrup hands you a blade. 'Streams carry your data. Master them!'",
                "task": "Write a C++ program that prints 'Hello, C++ World!'",
                "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code\n    return 0;\n}",
                "expected_output": "Hello, C++ World!",
                "hints": ["cout << \"text\" << endl;"]
            },
            {
                "id": 402,
                "title": "String Blades",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "C++ Strings",
                    "overview": "C++ has a proper string class.",
                    "sections": [
                        {"heading": "string Class", "content": "```cpp\n#include <string>\nstring name = \"Hero\";\ncout << name.length();\n```"}
                    ]
                },
                "story": "'Strings in C++ are objects,' Smith explains. 'Much more powerful than C!'",
                "task": "Create a string variable and print its length.",
                "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    // String work\n    return 0;\n}",
                "expected_output": None,
                "hints": ["string s = \"Hello\"; cout << s.length();"]
            },
            {
                "id": 426,
                "title": "Namespace Magic",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "C++ Namespaces",
                    "overview": "Namespaces prevent naming conflicts.",
                    "sections": [
                        {"heading": "Using Namespaces", "content": "```cpp\n// Option 1: using directive\nusing namespace std;\ncout << \"Hello\";\n\n// Option 2: explicit prefix\nstd::cout << \"Hello\";\n```"},
                        {"heading": "Why Namespaces?", "content": "- Prevent name collisions\n- Organize code\n- std:: is the standard library namespace"}
                    ]
                },
                "story": "'Namespaces keep your code organized,' Smith explains. 'No more name conflicts!'",
                "task": "Write a program using std:: prefix instead of 'using namespace std'.",
                "starter_code": "#include <iostream>\n#include <string>\n\nint main() {\n    // Use std:: prefix\n    return 0;\n}",
                "expected_output": "Hello, Namespace!",
                "hints": ["std::cout << \"text\" << std::endl;", "std::string name = \"test\";"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Reference Ridge",
        "topic": "references vs pointers",
        "description": "The ridge where references and pointers are compared!",
        "story_intro": "C++ offers references - a safer alternative to pointers. Learn both!",
        "character": "Guide Ampersand",
        "character_quote": "References are aliases. Pointers are addresses. Know the difference!",
        "icon": "signpost",
        "color": "#0088cc",
        "missions": [
            {
                "id": 403,
                "title": "Reference Basics",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "References in C++",
                    "overview": "References are aliases to existing variables.",
                    "sections": [
                        {"heading": "Creating References", "content": "```cpp\nint x = 10;\nint& ref = x;  // ref is an alias for x\nref = 20;      // x is now 20\n```"}
                    ]
                },
                "story": "Guide Ampersand points to twin paths. 'References are simpler than pointers!'",
                "task": "Create a reference to an int and use it to change the original value.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 10;\n    // Create reference and modify\n    return 0;\n}",
                "expected_output": "20",
                "hints": ["int& ref = x; ref = 20;"]
            },
            {
                "id": 404,
                "title": "Pass by Reference",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Reference Parameters",
                    "overview": "Pass arguments by reference to modify them.",
                    "sections": [
                        {"heading": "Reference Parameters", "content": "```cpp\nvoid increment(int& n) {\n    n++;\n}\n```"}
                    ]
                },
                "story": "'Functions can modify their arguments,' Guide reveals. 'Use references!'",
                "task": "Create a function that doubles a number using reference parameter.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\n// doubleIt function\n\nint main() {\n    int x = 5;\n    doubleIt(x);\n    cout << x << endl;\n    return 0;\n}",
                "expected_output": "10",
                "hints": ["void doubleIt(int& n) { n *= 2; }"]
            },
            {
                "id": 427,
                "title": "References vs Pointers",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Comparing References and Pointers",
                    "overview": "Both allow indirect access, but differ in syntax and behavior.",
                    "sections": [
                        {"heading": "Key Differences", "content": "```cpp\n// Pointer - can be null, can be reassigned\nint* ptr = nullptr;\nptr = &x;\n*ptr = 10;  // Dereference needed\n\n// Reference - must be initialized, cannot be reassigned\nint& ref = x;  // Binds to x forever\nref = 10;      // Direct syntax\n```"},
                        {"heading": "When to Use", "content": "- References: cleaner syntax, safer (can't be null)\n- Pointers: when you need null or reassignment"}
                    ]
                },
                "story": "'References are safer aliases,' Guide explains. 'Pointers are more flexible. Know both!'",
                "task": "Create both a reference and a pointer to the same variable, modify via each.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 5;\n    // Create reference and pointer\n    return 0;\n}",
                "expected_output": None,
                "hints": ["int& ref = x;", "int* ptr = &x;"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Object Armory",
        "topic": "Classes, objects, access modifiers",
        "description": "The armory where objects are crafted from class blueprints!",
        "story_intro": "Object-oriented programming is the heart of C++. Learn to create classes!",
        "character": "Armorer Class",
        "character_quote": "Classes are blueprints. Objects are the weapons forged from them!",
        "icon": "building",
        "color": "#00aacc",
        "missions": [
            {
                "id": 405,
                "title": "First Class",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Creating Classes",
                    "overview": "Define your own types with classes.",
                    "sections": [
                        {"heading": "Class Syntax", "content": "```cpp\nclass Hero {\npublic:\n    string name;\n    int health;\n    void greet() {\n        cout << \"I am \" << name << endl;\n    }\n};\n```"}
                    ]
                },
                "story": "Armorer Class presents a template. 'Your first class awaits!'",
                "task": "Create a Weapon class with name and damage, and a display method.",
                "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\n// Weapon class\n\nint main() {\n    Weapon w;\n    w.name = \"Sword\";\n    w.damage = 50;\n    w.display();\n    return 0;\n}",
                "expected_output": None,
                "hints": ["class Weapon { public: string name; int damage; void display()... };"]
            },
            {
                "id": 406,
                "title": "Access Control",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Access Modifiers",
                    "overview": "Control access with public, private, protected.",
                    "sections": [
                        {"heading": "Private Members", "content": "```cpp\nclass Account {\nprivate:\n    int balance;\npublic:\n    void setBalance(int b) { balance = b; }\n    int getBalance() { return balance; }\n};\n```"}
                    ]
                },
                "story": "'Not everything should be public,' Armorer warns. 'Protect your data!'",
                "task": "Create a class with private data and public getter/setter.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\n// Class with encapsulation\n\nint main() {\n    return 0;\n}",
                "expected_output": None,
                "hints": ["private: for data, public: for methods"]
            },
            {
                "id": 428,
                "title": "Creating Objects",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Instantiating Objects",
                    "overview": "Objects are instances of classes created in your program.",
                    "sections": [
                        {"heading": "Stack Objects", "content": "```cpp\nHero hero1;           // Default constructor\nHero hero2(\"Luna\");   // Parameterized constructor\n```"},
                        {"heading": "Heap Objects", "content": "```cpp\nHero* hero = new Hero(\"Kai\");\n// ... use hero\ndelete hero;  // Don't forget!\n```"},
                        {"heading": "Calling Methods", "content": "```cpp\nhero1.attack();\nhero->defend();  // Pointer syntax\n```"}
                    ]
                },
                "story": "'Classes are blueprints,' Armorer explains. 'Objects are the actual weapons forged from them!'",
                "task": "Create a Weapon class and instantiate two different weapon objects.",
                "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\n// Weapon class\n\nint main() {\n    // Create weapon objects\n    return 0;\n}",
                "expected_output": None,
                "hints": ["Weapon sword(\"Excalibur\", 50);", "sword.display();"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Legacy Temple",
        "topic": "Inheritance, constructors",
        "description": "The temple where classes inherit power from their ancestors!",
        "story_intro": "Inheritance lets classes share code. Learn the legacy!",
        "character": "Elder Inherit",
        "character_quote": "Children inherit from parents. So do classes!",
        "icon": "landmark",
        "color": "#00ccee",
        "missions": [
            {
                "id": 407,
                "title": "Inheritance Basics",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Class Inheritance",
                    "overview": "Derive new classes from existing ones.",
                    "sections": [
                        {"heading": "Inheritance Syntax", "content": "```cpp\nclass Animal {\npublic:\n    void speak() { cout << \"Sound\" << endl; }\n};\n\nclass Dog : public Animal {\npublic:\n    void bark() { cout << \"Woof!\" << endl; }\n};\n```"}
                    ]
                },
                "story": "Elder Inherit shows the family tree. 'Dogs are Animals. Code reflects life!'",
                "task": "Create a Vehicle base class and a Car derived class.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\n// Vehicle and Car classes\n\nint main() {\n    Car c;\n    c.move();\n    c.honk();\n    return 0;\n}",
                "expected_output": None,
                "hints": ["class Car : public Vehicle { ... };"]
            },
            {
                "id": 408,
                "title": "Constructors",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Constructors in C++",
                    "overview": "Initialize objects with constructors.",
                    "sections": [
                        {"heading": "Constructor Syntax", "content": "```cpp\nclass Hero {\npublic:\n    string name;\n    Hero(string n) : name(n) {}\n};\n\nHero h(\"Sakura\");\n```"}
                    ]
                },
                "story": "'Objects must be born properly,' Elder explains. 'Use constructors!'",
                "task": "Create a class with a constructor that initializes its data.",
                "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\n// Class with constructor\n\nint main() {\n    Player p(\"Hero\", 100);\n    return 0;\n}",
                "expected_output": None,
                "hints": ["Player(string n, int h) : name(n), health(h) {}"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Prism Polymorph",
        "topic": "Virtual functions, overriding",
        "description": "Where objects transform and take many forms!",
        "story_intro": "Polymorphism means many forms. Objects can behave differently!",
        "character": "Shifter Virtual",
        "character_quote": "One interface, many implementations. That's polymorphism!",
        "icon": "sparkles",
        "color": "#6699ff",
        "missions": [
            {
                "id": 409,
                "title": "Virtual Functions",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Virtual and Override",
                    "overview": "Enable runtime polymorphism with virtual functions.",
                    "sections": [
                        {"heading": "Virtual Functions", "content": "```cpp\nclass Animal {\npublic:\n    virtual void speak() { cout << \"...\" << endl; }\n};\n\nclass Dog : public Animal {\npublic:\n    void speak() override { cout << \"Woof!\" << endl; }\n};\n```"}
                    ]
                },
                "story": "Shifter Virtual transforms. 'The same call, different behavior!'",
                "task": "Create a Shape base with virtual area(), and Circle/Rectangle that override it.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\n// Shape hierarchy\n\nint main() {\n    return 0;\n}",
                "expected_output": None,
                "hints": ["virtual double area() { return 0; }"]
            },
            {
                "id": 410,
                "title": "Polymorphic Pointers",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Base Class Pointers",
                    "overview": "Use base pointers to call derived methods.",
                    "sections": [
                        {"heading": "Polymorphism in Action", "content": "```cpp\nAnimal* pet = new Dog();\npet->speak(); // Calls Dog::speak()\ndelete pet;\n```"}
                    ]
                },
                "story": "'The pointer sees Animal, but the object is Dog,' Shifter explains.",
                "task": "Create different shapes and call area() through base pointer.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\n// Use polymorphism\n\nint main() {\n    return 0;\n}",
                "expected_output": None,
                "hints": ["Shape* s = new Circle(5);"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Template Workshop",
        "topic": "Function & Class templates",
        "description": "The workshop where generic code is crafted!",
        "story_intro": "Templates let you write code that works with any type!",
        "character": "Crafter Template",
        "character_quote": "Write once, use with any type. That's the power of templates!",
        "icon": "scroll",
        "color": "#9966ff",
        "missions": [
            {
                "id": 411,
                "title": "Function Templates",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Generic Functions",
                    "overview": "Create functions that work with any type.",
                    "sections": [
                        {"heading": "Template Syntax", "content": "```cpp\ntemplate<typename T>\nT maximum(T a, T b) {\n    return (a > b) ? a : b;\n}\n\nint m1 = maximum(3, 5);\ndouble m2 = maximum(3.5, 2.1);\n```"}
                    ]
                },
                "story": "Crafter Template shows a flexible mold. 'One function, many types!'",
                "task": "Create a template function that swaps two values of any type.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\n// Template swap function\n\nint main() {\n    int a = 5, b = 10;\n    mySwap(a, b);\n    cout << a << \" \" << b << endl;\n    return 0;\n}",
                "expected_output": "10 5",
                "hints": ["template<typename T> void mySwap(T& a, T& b)"]
            },
            {
                "id": 412,
                "title": "Class Templates",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Generic Classes",
                    "overview": "Create classes that work with any type.",
                    "sections": [
                        {"heading": "Template Class", "content": "```cpp\ntemplate<typename T>\nclass Box {\nprivate:\n    T value;\npublic:\n    void set(T v) { value = v; }\n    T get() { return value; }\n};\n```"}
                    ]
                },
                "story": "'Classes can be generic too,' Crafter reveals. 'A box for anything!'",
                "task": "Create a Pair template class that holds two values of any type.",
                "starter_code": "#include <iostream>\nusing namespace std;\n\n// Pair template\n\nint main() {\n    Pair<int, string> p(1, \"one\");\n    return 0;\n}",
                "expected_output": None,
                "hints": ["template<typename T1, typename T2> class Pair"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Container Vault",
        "topic": "Vectors, Lists, Pairs",
        "description": "A vault filled with powerful STL containers!",
        "story_intro": "The Standard Template Library provides ready-made containers!",
        "character": "Keeper STL",
        "character_quote": "Why reinvent the wheel? The STL has it all!",
        "icon": "layout",
        "color": "#cc66ff",
        "missions": [
            {
                "id": 413,
                "title": "Vectors",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "std::vector",
                    "overview": "Dynamic arrays that grow automatically.",
                    "sections": [
                        {"heading": "Vector Basics", "content": "```cpp\n#include <vector>\nvector<int> nums = {1, 2, 3};\nnums.push_back(4);\ncout << nums.size();\n```"}
                    ]
                },
                "story": "Keeper STL opens the vault. 'Vectors - arrays that grow!'",
                "task": "Create a vector of integers, add elements, and print size.",
                "starter_code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    // Use vector\n    return 0;\n}",
                "expected_output": None,
                "hints": ["vector<int> v; v.push_back(10);"]
            },
            {
                "id": 414,
                "title": "Pairs and Tuples",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "std::pair",
                    "overview": "Store two related values together.",
                    "sections": [
                        {"heading": "Pair Usage", "content": "```cpp\n#include <utility>\npair<string, int> player(\"Hero\", 100);\ncout << player.first << \": \" << player.second;\n```"}
                    ]
                },
                "story": "'Pairs hold two values together,' Keeper explains.",
                "task": "Create a pair of name and score, then print both.",
                "starter_code": "#include <iostream>\n#include <utility>\nusing namespace std;\n\nint main() {\n    // Use pair\n    return 0;\n}",
                "expected_output": None,
                "hints": ["pair<string, int> p(\"Name\", 100);"]
            },
            {
                "id": 429,
                "title": "Linked Lists",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "std::list",
                    "overview": "Lists are doubly-linked containers with fast insertion/removal.",
                    "sections": [
                        {"heading": "List Basics", "content": "```cpp\n#include <list>\nlist<int> nums;\nnums.push_back(10);\nnums.push_front(5);\n```"},
                        {"heading": "List vs Vector", "content": "- List: Fast insert/remove anywhere, no random access\n- Vector: Fast random access, slow insert in middle"}
                    ]
                },
                "story": "'Lists link elements like a chain,' Keeper explains. 'Fast to break and reconnect!'",
                "task": "Create a list, add elements to front and back, then iterate and print.",
                "starter_code": "#include <iostream>\n#include <list>\nusing namespace std;\n\nint main() {\n    // Use std::list\n    return 0;\n}",
                "expected_output": "5 10 15",
                "hints": ["list<int> nums;", "push_front and push_back"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Dictionary Dunes",
        "topic": "Maps, Sets, Iterators",
        "description": "Sandy dunes hiding powerful associative containers!",
        "story_intro": "Maps and sets provide fast lookups. Master them!",
        "character": "Cartographer Map",
        "character_quote": "Keys lead to values. That's the map's magic!",
        "icon": "signpost",
        "color": "#ff66cc",
        "missions": [
            {
                "id": 415,
                "title": "Maps",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "std::map",
                    "overview": "Key-value pairs with fast lookup.",
                    "sections": [
                        {"heading": "Map Basics", "content": "```cpp\n#include <map>\nmap<string, int> scores;\nscores[\"Alice\"] = 100;\nscores[\"Bob\"] = 85;\ncout << scores[\"Alice\"];\n```"}
                    ]
                },
                "story": "Cartographer Map draws in the sand. 'Keys unlock values!'",
                "task": "Create a map of names to ages and print one value.",
                "starter_code": "#include <iostream>\n#include <map>\nusing namespace std;\n\nint main() {\n    // Use map\n    return 0;\n}",
                "expected_output": None,
                "hints": ["map<string, int> ages;"]
            },
            {
                "id": 416,
                "title": "Iterators",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Iterating Containers",
                    "overview": "Use iterators to traverse containers.",
                    "sections": [
                        {"heading": "Iterator Loop", "content": "```cpp\nfor (auto it = vec.begin(); it != vec.end(); ++it) {\n    cout << *it << endl;\n}\n// Or range-based:\nfor (auto& x : vec) {\n    cout << x << endl;\n}\n```"}
                    ]
                },
                "story": "'Iterators walk through containers,' Cartographer explains.",
                "task": "Use a range-based for loop to print all elements of a vector.",
                "starter_code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> nums = {1, 2, 3, 4, 5};\n    // Iterate and print\n    return 0;\n}",
                "expected_output": "1\n2\n3\n4\n5",
                "hints": ["for (int n : nums) { cout << n << endl; }"]
            },
            {
                "id": 430,
                "title": "Sets",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "std::set",
                    "overview": "Sets store unique elements in sorted order.",
                    "sections": [
                        {"heading": "Set Basics", "content": "```cpp\n#include <set>\nset<int> nums;\nnums.insert(5);\nnums.insert(3);\nnums.insert(5);  // Ignored (duplicate)\n// nums contains: 3, 5 (sorted)\n```"},
                        {"heading": "Set Operations", "content": "```cpp\nnums.count(5);   // 1 if exists, 0 otherwise\nnums.erase(3);   // Remove element\nnums.find(5);    // Iterator to element\n```"}
                    ]
                },
                "story": "'Sets keep only unique treasures,' Cartographer explains. 'No duplicates allowed!'",
                "task": "Create a set, insert some values including duplicates, then print all unique values.",
                "starter_code": "#include <iostream>\n#include <set>\nusing namespace std;\n\nint main() {\n    // Use std::set\n    return 0;\n}",
                "expected_output": "1 2 3 5",
                "hints": ["set<int> s;", "Duplicates are automatically ignored"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Shield of Safety",
        "topic": "try/catch, throw",
        "description": "The shield that protects against runtime errors!",
        "story_intro": "Exceptions handle errors gracefully. Learn to catch them!",
        "character": "Guardian Catch",
        "character_quote": "Errors happen. Catch them before they crash!",
        "icon": "layout",
        "color": "#ff9966",
        "missions": [
            {
                "id": 417,
                "title": "Try-Catch Basics",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Exception Handling",
                    "overview": "Catch and handle runtime errors.",
                    "sections": [
                        {"heading": "Try-Catch", "content": "```cpp\ntry {\n    throw runtime_error(\"Oops!\");\n} catch (exception& e) {\n    cout << \"Error: \" << e.what() << endl;\n}\n```"}
                    ]
                },
                "story": "Guardian Catch raises a shield. 'Catch errors before they strike!'",
                "task": "Write code that throws an exception and catches it.",
                "starter_code": "#include <iostream>\n#include <stdexcept>\nusing namespace std;\n\nint main() {\n    // Try-catch\n    return 0;\n}",
                "expected_output": None,
                "hints": ["throw runtime_error(\"message\");"]
            },
            {
                "id": 418,
                "title": "Custom Exceptions",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Creating Exception Classes",
                    "overview": "Define your own exception types.",
                    "sections": [
                        {"heading": "Custom Exception", "content": "```cpp\nclass GameError : public exception {\n    const char* what() const noexcept override {\n        return \"Game error occurred!\";\n    }\n};\n```"}
                    ]
                },
                "story": "'Create shields for specific dangers,' Guardian advises.",
                "task": "Create a custom exception class and throw/catch it.",
                "starter_code": "#include <iostream>\n#include <exception>\nusing namespace std;\n\n// Custom exception\n\nint main() {\n    return 0;\n}",
                "expected_output": None,
                "hints": ["class MyError : public exception"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Smart Spirit Links",
        "topic": "unique_ptr, shared_ptr",
        "description": "Spirit links that manage memory automatically!",
        "story_intro": "Smart pointers prevent memory leaks. Use them!",
        "character": "Spirit Keeper",
        "character_quote": "Let the spirits handle memory. No more leaks!",
        "icon": "sparkles",
        "color": "#66ccff",
        "missions": [
            {
                "id": 419,
                "title": "unique_ptr",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Unique Ownership",
                    "overview": "One owner for dynamically allocated memory.",
                    "sections": [
                        {"heading": "unique_ptr", "content": "```cpp\n#include <memory>\nunique_ptr<int> p = make_unique<int>(42);\ncout << *p;\n// Automatically deleted when p goes out of scope\n```"}
                    ]
                },
                "story": "Spirit Keeper summons a link. 'One spirit, one master!'",
                "task": "Create a unique_ptr to a Hero object and use it.",
                "starter_code": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nclass Hero {\npublic:\n    string name = \"Warrior\";\n};\n\nint main() {\n    // Use unique_ptr\n    return 0;\n}",
                "expected_output": None,
                "hints": ["unique_ptr<Hero> h = make_unique<Hero>();"]
            },
            {
                "id": 420,
                "title": "shared_ptr",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Shared Ownership",
                    "overview": "Multiple owners share the same memory.",
                    "sections": [
                        {"heading": "shared_ptr", "content": "```cpp\nshared_ptr<int> p1 = make_shared<int>(100);\nshared_ptr<int> p2 = p1; // Both own the memory\ncout << p1.use_count(); // 2\n```"}
                    ]
                },
                "story": "'Some spirits can be shared,' Keeper reveals.",
                "task": "Create shared_ptrs and show the use count.",
                "starter_code": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nint main() {\n    // Use shared_ptr\n    return 0;\n}",
                "expected_output": None,
                "hints": ["shared_ptr<int> p = make_shared<int>(42);"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Stream Streams",
        "topic": "fstream, stringstream",
        "description": "Advanced streams for files and strings!",
        "story_intro": "Streams work with files and strings too!",
        "character": "Flow Master",
        "character_quote": "Everything is a stream. Files, strings, everything!",
        "icon": "scroll",
        "color": "#66ff99",
        "missions": [
            {
                "id": 421,
                "title": "File Streams",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "fstream",
                    "overview": "Read and write files with streams.",
                    "sections": [
                        {"heading": "File I/O", "content": "```cpp\n#include <fstream>\nofstream out(\"data.txt\");\nout << \"Hello File!\";\nout.close();\n\nifstream in(\"data.txt\");\nstring line;\ngetline(in, line);\n```"}
                    ]
                },
                "story": "Flow Master opens a file. 'Streams flow to files too!'",
                "task": "Write 'Hello, File!' to a text file.",
                "starter_code": "#include <iostream>\n#include <fstream>\nusing namespace std;\n\nint main() {\n    // File output\n    return 0;\n}",
                "expected_output": None,
                "hints": ["ofstream out(\"file.txt\");"]
            },
            {
                "id": 422,
                "title": "String Streams",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "stringstream",
                    "overview": "Parse and build strings with streams.",
                    "sections": [
                        {"heading": "stringstream", "content": "```cpp\n#include <sstream>\nstringstream ss(\"42 3.14 Hello\");\nint i; double d; string s;\nss >> i >> d >> s;\n```"}
                    ]
                },
                "story": "'Strings can be streams,' Flow Master reveals.",
                "task": "Parse integers from a string using stringstream.",
                "starter_code": "#include <iostream>\n#include <sstream>\nusing namespace std;\n\nint main() {\n    string data = \"10 20 30\";\n    // Parse with stringstream\n    return 0;\n}",
                "expected_output": "60",
                "hints": ["stringstream ss(data); int a, b, c; ss >> a >> b >> c;"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Guardian's Final Stand",
        "topic": "Building a Battle Engine",
        "description": "The ultimate trial - build a complete battle system!",
        "story_intro": "You've mastered C++. Now create a Battle Engine!",
        "character": "Grand Guardian",
        "character_quote": "Show me everything you've learned. Build the ultimate engine!",
        "icon": "trophy",
        "color": "#ffd700",
        "missions": [
            {
                "id": 423,
                "title": "Character System",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Character Classes",
                    "overview": "Design a class hierarchy for game characters.",
                    "sections": [
                        {"heading": "Design", "content": "- Base Character class\n- Derived: Warrior, Mage, Archer\n- Stats: health, attack, defense"}
                    ]
                },
                "story": "Grand Guardian watches. 'Build your warriors!'",
                "task": "Create a Character base class and Warrior/Mage derived classes.",
                "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\n// Character hierarchy\n\nint main() {\n    return 0;\n}",
                "expected_output": None,
                "hints": ["Use inheritance and virtual methods"]
            },
            {
                "id": 424,
                "title": "Combat System",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Battle Mechanics",
                    "overview": "Implement attack, defend, and special abilities.",
                    "sections": [
                        {"heading": "Combat", "content": "- attack(Character& target)\n- takeDamage(int amount)\n- Special abilities per class"}
                    ]
                },
                "story": "'Warriors must fight!' the Guardian declares.",
                "task": "Implement combat methods and a simple battle loop.",
                "starter_code": "// Battle system\n",
                "expected_output": None,
                "hints": ["while both alive, take turns attacking"]
            },
            {
                "id": 425,
                "title": "Complete Engine",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "Putting It Together",
                    "overview": "Combine all systems into a working game.",
                    "sections": [
                        {"heading": "Requirements", "content": "- Multiple character types\n- Combat system\n- Smart pointers for memory\n- File save/load\n- Exception handling"}
                    ]
                },
                "story": "Grand Guardian nods. 'Complete your masterpiece!'",
                "task": "Build the complete Battle Engine with all features.",
                "starter_code": "// Complete Battle Engine\n#include <iostream>\n#include <memory>\n#include <vector>\n#include <fstream>\nusing namespace std;\n\n// Your code here",
                "expected_output": None,
                "hints": ["Combine classes, smart pointers, STL, and file I/O"]
            }
        ]
    }
]

JAVA_ARCS = [
    {
        "id": 1,
        "name": "Royal Welcome",
        "topic": "JVM, main method, variables",
        "description": "Enter the Grand Enterprise Kingdom and receive the royal welcome!",
        "story_intro": "The Grand Enterprise Kingdom awaits. Java powers the largest systems in the realm!",
        "character": "Duke Java",
        "character_quote": "Write once, run anywhere! Welcome to the enterprise!",
        "icon": "building",
        "color": "#f89820",
        "missions": [
            {
                "id": 501,
                "title": "The Main Gate",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Java Program Structure",
                    "overview": "Every Java program needs a main method.",
                    "sections": [
                        {"heading": "The JVM", "content": "Java runs on the JVM (Java Virtual Machine) - that's why it works everywhere!"},
                        {"heading": "Main Method", "content": "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello!\");\n    }\n}\n```"}
                    ]
                },
                "story": "Duke Java opens the gates. 'Every journey begins with main!'",
                "task": "Write a Java program that prints 'Hello, Java World!'",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        // Your code\n    }\n}",
                "expected_output": "Hello, Java World!",
                "hints": ["System.out.println(\"text\");"]
            },
            {
                "id": 502,
                "title": "Royal Variables",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Java Variables",
                    "overview": "Java is strongly typed.",
                    "sections": [
                        {"heading": "Types", "content": "```java\nint age = 25;\nString name = \"Hero\";\ndouble price = 9.99;\nboolean active = true;\n```"}
                    ]
                },
                "story": "'Variables are the kingdom's treasures,' Duke explains. 'Type them well!'",
                "task": "Create int 'gold' = 100 and print 'Gold: 100'",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        // Variables\n    }\n}",
                "expected_output": "Gold: 100",
                "hints": ["int gold = 100; System.out.println(\"Gold: \" + gold);"]
            },
            {
                "id": 529,
                "title": "The JVM",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Java Virtual Machine",
                    "overview": "Java runs on the JVM, enabling 'write once, run anywhere'.",
                    "sections": [
                        {"heading": "How Java Works", "content": "1. Write `.java` source code\n2. Compile to `.class` bytecode (javac)\n3. JVM executes bytecode on any platform"},
                        {"heading": "JVM Benefits", "content": "- Platform independence\n- Memory management (garbage collection)\n- Security sandbox\n- Just-In-Time (JIT) compilation"}
                    ]
                },
                "story": "'The JVM is the kingdom's foundation,' Duke explains. 'It runs your code everywhere!'",
                "task": "Write a program that prints 'Running on JVM!' to understand the execution flow.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        // Print message\n    }\n}",
                "expected_output": "Running on JVM!",
                "hints": ["System.out.println(\"Running on JVM!\");"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Decree of Choice",
        "topic": "boolean, switch, operators",
        "description": "The royal court where decisions are decreed!",
        "story_intro": "Every ruler must make decisions. Learn the logic of choice!",
        "character": "Judge Boolean",
        "character_quote": "True or false - the decree is final!",
        "icon": "signpost",
        "color": "#e88c1f",
        "missions": [
            {
                "id": 503,
                "title": "If-Else Decrees",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Conditional Statements",
                    "overview": "Make decisions with if-else.",
                    "sections": [
                        {"heading": "If-Else", "content": "```java\nif (score > 50) {\n    System.out.println(\"Pass!\");\n} else {\n    System.out.println(\"Fail!\");\n}\n```"}
                    ]
                },
                "story": "Judge Boolean raises the gavel. 'Decide the path!'",
                "task": "Check if 'rank' (75) is > 50. Print 'Knight!' or 'Squire!'",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        int rank = 75;\n        // Decision\n    }\n}",
                "expected_output": "Knight!",
                "hints": ["if (rank > 50) { ... }"]
            },
            {
                "id": 504,
                "title": "Switch Proclamation",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Switch Statements",
                    "overview": "Handle multiple cases cleanly.",
                    "sections": [
                        {"heading": "Switch", "content": "```java\nswitch(day) {\n    case 1: System.out.println(\"Mon\"); break;\n    case 2: System.out.println(\"Tue\"); break;\n    default: System.out.println(\"Other\");\n}\n```"}
                    ]
                },
                "story": "'Many choices, one switch,' the Judge decrees.",
                "task": "Use switch for season=2 to print 'Spring'.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        int season = 2;\n        // Switch\n    }\n}",
                "expected_output": "Spring",
                "hints": ["case 1: Winter, case 2: Spring, etc."]
            },
            {
                "id": 526,
                "title": "Boolean and Operators",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Boolean Type and Operators",
                    "overview": "Java has a dedicated boolean type and various operators.",
                    "sections": [
                        {"heading": "Boolean", "content": "```java\nboolean isHero = true;\nboolean isVillain = false;\n```"},
                        {"heading": "Comparison Operators", "content": "```java\n==  // equal\n!=  // not equal\n>   <   >=   <=\n```"},
                        {"heading": "Logical Operators", "content": "```java\n&&  // AND\n||  // OR\n!   // NOT\n```"}
                    ]
                },
                "story": "'Booleans are the foundation of logic,' the Judge explains. 'True or false, always!'",
                "task": "Create boolean variables and use operators to check if a hero (level 15) is strong (>10) AND experienced (>5).",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        int level = 15;\n        // Boolean operations\n    }\n}",
                "expected_output": "Is ready: true",
                "hints": ["boolean isStrong = level > 10;", "Use && for AND"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Infinite Gardens",
        "topic": "for-each, while, break/continue",
        "description": "Gardens where patterns repeat in beautiful loops!",
        "story_intro": "The gardens grow in patterns. Master the loops!",
        "character": "Gardener Loop",
        "character_quote": "Plant once, harvest many times!",
        "icon": "waves",
        "color": "#d87d15",
        "missions": [
            {
                "id": 505,
                "title": "For Loop Rows",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "For Loops",
                    "overview": "Repeat with for loops.",
                    "sections": [
                        {"heading": "For Syntax", "content": "```java\nfor (int i = 0; i < 5; i++) {\n    System.out.println(i);\n}\n```"}
                    ]
                },
                "story": "Gardener Loop plants seeds. 'Watch them grow in order!'",
                "task": "Print numbers 1 to 5 using a for loop.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        // For loop\n    }\n}",
                "expected_output": "1\n2\n3\n4\n5",
                "hints": ["for (int i = 1; i <= 5; i++)"]
            },
            {
                "id": 506,
                "title": "For-Each Harvest",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Enhanced For Loop",
                    "overview": "Iterate collections easily.",
                    "sections": [
                        {"heading": "For-Each", "content": "```java\nint[] nums = {1, 2, 3};\nfor (int n : nums) {\n    System.out.println(n);\n}\n```"}
                    ]
                },
                "story": "'Harvest each element,' Gardener shows.",
                "task": "Use for-each to print all elements of an array.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        String[] fruits = {\"Apple\", \"Banana\", \"Cherry\"};\n        // For-each\n    }\n}",
                "expected_output": "Apple\nBanana\nCherry",
                "hints": ["for (String fruit : fruits)"]
            },
            {
                "id": 527,
                "title": "While and Control Flow",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "While Loops with Break/Continue",
                    "overview": "Control loop execution with while, break, and continue.",
                    "sections": [
                        {"heading": "While Loop", "content": "```java\nint i = 0;\nwhile (i < 5) {\n    System.out.println(i);\n    i++;\n}\n```"},
                        {"heading": "Break", "content": "```java\nwhile (true) {\n    if (condition) break;  // Exit loop\n}\n```"},
                        {"heading": "Continue", "content": "```java\nfor (int i = 0; i < 10; i++) {\n    if (i % 2 == 0) continue;  // Skip even numbers\n    System.out.println(i);\n}\n```"}
                    ]
                },
                "story": "'Break escapes, continue skips,' Gardener teaches. 'Control your loops!'",
                "task": "Use a while loop to print numbers 1-10, but skip number 5 using continue.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        int i = 0;\n        // While loop with continue\n    }\n}",
                "expected_output": "1\n2\n3\n4\n6\n7\n8\n9\n10",
                "hints": ["if (i == 5) continue;", "Don't forget to increment i before continue!"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Guild of Objects",
        "topic": "Attributes, methods, this",
        "description": "The guild where objects are crafted by masters!",
        "story_intro": "Objects are Java's building blocks. Join the guild!",
        "character": "Craftsman Object",
        "character_quote": "Everything in Java is an object. Learn to craft them!",
        "icon": "building",
        "color": "#c86e0a",
        "missions": [
            {
                "id": 507,
                "title": "First Object",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Creating Classes",
                    "overview": "Define your own types with classes.",
                    "sections": [
                        {"heading": "Class Syntax", "content": "```java\nclass Hero {\n    String name;\n    int health;\n    \n    void greet() {\n        System.out.println(\"I am \" + name);\n    }\n}\n```"}
                    ]
                },
                "story": "Craftsman Object shows blueprints. 'Create your first object!'",
                "task": "Create a Knight class with name and level, and a display method.",
                "starter_code": "// Knight class\n\npublic class Main {\n    public static void main(String[] args) {\n        Knight k = new Knight();\n        k.name = \"Arthur\";\n        k.level = 5;\n        k.display();\n    }\n}",
                "expected_output": None,
                "hints": ["class Knight { String name; int level; void display()... }"]
            },
            {
                "id": 508,
                "title": "The 'this' Keyword",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Using 'this'",
                    "overview": "Reference the current object with 'this'.",
                    "sections": [
                        {"heading": "This Keyword", "content": "```java\nclass Hero {\n    String name;\n    Hero(String name) {\n        this.name = name;\n    }\n}\n```"}
                    ]
                },
                "story": "'this' refers to yourself,' Craftsman explains.",
                "task": "Create a constructor using 'this' to set attributes.",
                "starter_code": "class Player {\n    String name;\n    int score;\n    // Constructor with this\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Player p = new Player(\"Hero\", 100);\n    }\n}",
                "expected_output": None,
                "hints": ["Player(String name, int score) { this.name = name; ... }"]
            },
            {
                "id": 530,
                "title": "Attributes and Methods",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Class Members",
                    "overview": "Classes contain attributes (data) and methods (behavior).",
                    "sections": [
                        {"heading": "Attributes", "content": "```java\nclass Hero {\n    String name;      // Attribute\n    int health = 100; // With default\n    private int level; // Private attribute\n}\n```"},
                        {"heading": "Methods", "content": "```java\nclass Hero {\n    void attack() {\n        System.out.println(\"Attacking!\");\n    }\n    int getHealth() {\n        return health;\n    }\n}\n```"}
                    ]
                },
                "story": "'Attributes are what you have, methods are what you do,' Craftsman teaches.",
                "task": "Create a Pet class with name/age attributes and a speak() method.",
                "starter_code": "// Pet class\n\npublic class Main {\n    public static void main(String[] args) {\n        // Create pet and call speak()\n    }\n}",
                "expected_output": "Meow!",
                "hints": ["void speak() { System.out.println(\"Meow!\"); }"]
            }
        ]
    },
    {
        "id": 5,
        "name": "The Royal Lineage",
        "topic": "Inheritance (extends, super)",
        "description": "The royal family tree where classes inherit power!",
        "story_intro": "Children inherit from parents. So do classes!",
        "character": "Herald Inherit",
        "character_quote": "The lineage passes down traits through generations!",
        "icon": "landmark",
        "color": "#b86000",
        "missions": [
            {
                "id": 509,
                "title": "Extends the Line",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Inheritance in Java",
                    "overview": "Use extends to inherit from a parent class.",
                    "sections": [
                        {"heading": "Extends", "content": "```java\nclass Animal {\n    void speak() { System.out.println(\"...\"); }\n}\n\nclass Dog extends Animal {\n    void bark() { System.out.println(\"Woof!\"); }\n}\n```"}
                    ]
                },
                "story": "Herald Inherit shows the family tree. 'Dogs are Animals!'",
                "task": "Create a Character class and a Warrior that extends it.",
                "starter_code": "// Character and Warrior\n\npublic class Main {\n    public static void main(String[] args) {\n        Warrior w = new Warrior();\n        w.speak();\n        w.attack();\n    }\n}",
                "expected_output": None,
                "hints": ["class Warrior extends Character { ... }"]
            },
            {
                "id": 510,
                "title": "Super Power",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "The super Keyword",
                    "overview": "Call parent class methods and constructors.",
                    "sections": [
                        {"heading": "Super", "content": "```java\nclass Dog extends Animal {\n    Dog() {\n        super(); // Call parent constructor\n    }\n    void speak() {\n        super.speak(); // Call parent method\n        System.out.println(\"Woof!\");\n    }\n}\n```"}
                    ]
                },
                "story": "'Super calls upon your ancestors,' Herald reveals.",
                "task": "Use super() in a constructor and super.method() to call parent.",
                "starter_code": "class Vehicle {\n    String type = \"Vehicle\";\n    void info() { System.out.println(type); }\n}\n\nclass Car extends Vehicle {\n    // Use super\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Car c = new Car();\n        c.info();\n    }\n}",
                "expected_output": None,
                "hints": ["super.info(); then add your own output"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Contract Cove",
        "topic": "Interfaces, Abstract classes",
        "description": "The cove where contracts are signed and sealed!",
        "story_intro": "Interfaces are contracts. Abstract classes are templates!",
        "character": "Notary Abstract",
        "character_quote": "Sign the contract, and you must fulfill it!",
        "icon": "scroll",
        "color": "#a85500",
        "missions": [
            {
                "id": 511,
                "title": "Interface Contracts",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Interfaces",
                    "overview": "Define behavior contracts with interfaces.",
                    "sections": [
                        {"heading": "Interface", "content": "```java\ninterface Flyable {\n    void fly();\n}\n\nclass Bird implements Flyable {\n    public void fly() {\n        System.out.println(\"Flapping wings!\");\n    }\n}\n```"}
                    ]
                },
                "story": "Notary Abstract presents a scroll. 'Sign and implement!'",
                "task": "Create a Fightable interface with attack() and a Knight that implements it.",
                "starter_code": "// Interface and implementation\n\npublic class Main {\n    public static void main(String[] args) {\n        Knight k = new Knight();\n        k.attack();\n    }\n}",
                "expected_output": None,
                "hints": ["interface Fightable { void attack(); }"]
            },
            {
                "id": 512,
                "title": "Abstract Templates",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Abstract Classes",
                    "overview": "Partial implementations with abstract classes.",
                    "sections": [
                        {"heading": "Abstract", "content": "```java\nabstract class Shape {\n    abstract double area();\n    void describe() {\n        System.out.println(\"I am a shape\");\n    }\n}\n\nclass Circle extends Shape {\n    double radius;\n    double area() { return 3.14 * radius * radius; }\n}\n```"}
                    ]
                },
                "story": "'Abstract classes are incomplete blueprints,' Notary explains.",
                "task": "Create an abstract Enemy class with abstract attack() method.",
                "starter_code": "// Abstract class\n\npublic class Main {\n    public static void main(String[] args) {\n        Goblin g = new Goblin();\n        g.attack();\n    }\n}",
                "expected_output": None,
                "hints": ["abstract class Enemy { abstract void attack(); }"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Collection Castle",
        "topic": "ArrayList, HashMap, Iterator",
        "description": "The castle treasury of data structures!",
        "story_intro": "Collections store and organize your data!",
        "character": "Treasurer List",
        "character_quote": "Arrays are limited. Collections are boundless!",
        "icon": "layout",
        "color": "#984a00",
        "missions": [
            {
                "id": 513,
                "title": "ArrayList Treasury",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "ArrayList",
                    "overview": "Dynamic arrays that grow.",
                    "sections": [
                        {"heading": "ArrayList", "content": "```java\nimport java.util.ArrayList;\n\nArrayList<String> names = new ArrayList<>();\nnames.add(\"Alice\");\nnames.add(\"Bob\");\nSystem.out.println(names.size());\n```"}
                    ]
                },
                "story": "Treasurer List opens a chest. 'ArrayLists grow as needed!'",
                "task": "Create an ArrayList of Strings, add items, and print size.",
                "starter_code": "import java.util.ArrayList;\n\npublic class Main {\n    public static void main(String[] args) {\n        // ArrayList\n    }\n}",
                "expected_output": None,
                "hints": ["ArrayList<String> list = new ArrayList<>();"]
            },
            {
                "id": 514,
                "title": "HashMap Vault",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "HashMap",
                    "overview": "Key-value pairs for fast lookup.",
                    "sections": [
                        {"heading": "HashMap", "content": "```java\nimport java.util.HashMap;\n\nHashMap<String, Integer> scores = new HashMap<>();\nscores.put(\"Alice\", 100);\nSystem.out.println(scores.get(\"Alice\"));\n```"}
                    ]
                },
                "story": "'Keys open vaults to values,' Treasurer reveals.",
                "task": "Create a HashMap of names to ages and retrieve one.",
                "starter_code": "import java.util.HashMap;\n\npublic class Main {\n    public static void main(String[] args) {\n        // HashMap\n    }\n}",
                "expected_output": None,
                "hints": ["HashMap<String, Integer> map = new HashMap<>();"]
            },
            {
                "id": 528,
                "title": "Iterator Magic",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Using Iterators",
                    "overview": "Iterators provide a way to traverse collections safely.",
                    "sections": [
                        {"heading": "Iterator Basics", "content": "```java\nimport java.util.Iterator;\nimport java.util.ArrayList;\n\nArrayList<String> list = new ArrayList<>();\nIterator<String> it = list.iterator();\nwhile (it.hasNext()) {\n    System.out.println(it.next());\n}\n```"},
                        {"heading": "Safe Removal", "content": "```java\nwhile (it.hasNext()) {\n    String item = it.next();\n    if (condition) {\n        it.remove();  // Safe way to remove during iteration\n    }\n}\n```"}
                    ]
                },
                "story": "'Iterators walk through collections safely,' Treasurer explains. 'No concurrent modification errors!'",
                "task": "Use an Iterator to print all elements of an ArrayList.",
                "starter_code": "import java.util.ArrayList;\nimport java.util.Iterator;\n\npublic class Main {\n    public static void main(String[] args) {\n        ArrayList<String> heroes = new ArrayList<>();\n        heroes.add(\"Luna\");\n        heroes.add(\"Kai\");\n        // Use Iterator\n    }\n}",
                "expected_output": "Luna\nKai",
                "hints": ["Iterator<String> it = heroes.iterator();", "while (it.hasNext())"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Error Fortress",
        "topic": "Checked vs Unchecked exceptions",
        "description": "The fortress that guards against errors!",
        "story_intro": "Errors happen. Catch them before they crash!",
        "character": "Guardian Catch",
        "character_quote": "Try to catch every exception before it escapes!",
        "icon": "layout",
        "color": "#883f00",
        "missions": [
            {
                "id": 515,
                "title": "Try-Catch Shield",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Exception Handling",
                    "overview": "Catch and handle runtime errors.",
                    "sections": [
                        {"heading": "Try-Catch", "content": "```java\ntry {\n    int result = 10 / 0;\n} catch (ArithmeticException e) {\n    System.out.println(\"Cannot divide by zero!\");\n}\n```"}
                    ]
                },
                "story": "Guardian Catch raises a shield. 'Catch errors before they strike!'",
                "task": "Write code that handles a division by zero exception.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        // Try-catch\n    }\n}",
                "expected_output": None,
                "hints": ["catch (ArithmeticException e)"]
            },
            {
                "id": 516,
                "title": "Throw Your Own",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Throwing Exceptions",
                    "overview": "Create and throw your own exceptions.",
                    "sections": [
                        {"heading": "Throw", "content": "```java\nvoid validate(int age) throws Exception {\n    if (age < 0) {\n        throw new Exception(\"Invalid age!\");\n    }\n}\n```"}
                    ]
                },
                "story": "'Sometimes you must throw to signal danger,' Guardian explains.",
                "task": "Create a method that throws an exception for invalid input.",
                "starter_code": "public class Main {\n    // Method that throws\n    \n    public static void main(String[] args) {\n        // Call and catch\n    }\n}",
                "expected_output": None,
                "hints": ["throw new IllegalArgumentException(\"message\");"]
            },
            {
                "id": 531,
                "title": "Checked vs Unchecked",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Exception Types",
                    "overview": "Java has checked (compile-time) and unchecked (runtime) exceptions.",
                    "sections": [
                        {"heading": "Checked Exceptions", "content": "```java\n// Must be caught or declared\nvoid readFile() throws IOException {\n    FileReader fr = new FileReader(\"file.txt\");\n}\n```\nExamples: IOException, SQLException"},
                        {"heading": "Unchecked Exceptions", "content": "```java\n// Don't require explicit handling\nint x = 10 / 0; // ArithmeticException\nString s = null;\ns.length(); // NullPointerException\n```\nExamples: RuntimeException, NullPointerException"}
                    ]
                },
                "story": "'Checked exceptions must be declared,' Guardian explains. 'Unchecked ones surprise you at runtime!'",
                "task": "Write code that demonstrates both a checked and unchecked exception scenario.",
                "starter_code": "import java.io.*;\n\npublic class Main {\n    // Demonstrate both exception types\n    public static void main(String[] args) {\n        \n    }\n}",
                "expected_output": None,
                "hints": ["IOException is checked", "NullPointerException is unchecked"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Thread Theater",
        "topic": "Runnable, Thread.sleep()",
        "description": "The theater where multiple performances run simultaneously!",
        "story_intro": "Threads let multiple things happen at once!",
        "character": "Director Thread",
        "character_quote": "Multiple actors, one stage. That's threading!",
        "icon": "sparkles",
        "color": "#783400",
        "missions": [
            {
                "id": 517,
                "title": "Thread Basics",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Creating Threads",
                    "overview": "Run code concurrently with threads.",
                    "sections": [
                        {"heading": "Runnable", "content": "```java\nclass MyTask implements Runnable {\n    public void run() {\n        System.out.println(\"Running in thread!\");\n    }\n}\n\nThread t = new Thread(new MyTask());\nt.start();\n```"}
                    ]
                },
                "story": "Director Thread raises the curtain. 'Multiple performers at once!'",
                "task": "Create a Runnable that prints a message and run it in a thread.",
                "starter_code": "// Thread example\n\npublic class Main {\n    public static void main(String[] args) {\n        // Create and start thread\n    }\n}",
                "expected_output": None,
                "hints": ["implements Runnable { public void run()... }"]
            },
            {
                "id": 518,
                "title": "Sleep and Wait",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Thread Control",
                    "overview": "Pause and control thread execution.",
                    "sections": [
                        {"heading": "Thread.sleep", "content": "```java\ntry {\n    Thread.sleep(1000); // Pause 1 second\n} catch (InterruptedException e) {\n    e.printStackTrace();\n}\n```"}
                    ]
                },
                "story": "'Sometimes actors must pause,' Director explains.",
                "task": "Create a thread that prints messages with delays between them.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        // Thread with sleep\n    }\n}",
                "expected_output": None,
                "hints": ["Thread.sleep(500); // 500 milliseconds"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Stream Spring",
        "topic": "Streams API, Lambda expressions",
        "description": "The spring where data flows in modern streams!",
        "story_intro": "Streams and lambdas bring modern power to Java!",
        "character": "Flow Oracle",
        "character_quote": "Data flows through streams. Lambdas shape it!",
        "icon": "waves",
        "color": "#682900",
        "missions": [
            {
                "id": 519,
                "title": "Lambda Light",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Lambda Expressions",
                    "overview": "Concise function syntax.",
                    "sections": [
                        {"heading": "Lambda Syntax", "content": "```java\n// Traditional\nRunnable r = new Runnable() {\n    public void run() { System.out.println(\"Hi\"); }\n};\n\n// Lambda\nRunnable r = () -> System.out.println(\"Hi\");\n```"}
                    ]
                },
                "story": "Flow Oracle shows the light. 'Lambdas are functions distilled!'",
                "task": "Use a lambda to create a Runnable and run it.",
                "starter_code": "public class Main {\n    public static void main(String[] args) {\n        // Lambda Runnable\n    }\n}",
                "expected_output": None,
                "hints": ["Runnable r = () -> System.out.println(\"Hello\");"]
            },
            {
                "id": 520,
                "title": "Stream Flow",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Streams API",
                    "overview": "Process collections functionally.",
                    "sections": [
                        {"heading": "Streams", "content": "```java\nimport java.util.Arrays;\nimport java.util.List;\n\nList<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);\nnums.stream()\n    .filter(n -> n > 2)\n    .forEach(System.out::println);\n```"}
                    ]
                },
                "story": "'Streams flow through data,' Oracle reveals.",
                "task": "Use streams to filter and print numbers greater than 3.",
                "starter_code": "import java.util.Arrays;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6);\n        // Stream operations\n    }\n}",
                "expected_output": "4\n5\n6",
                "hints": [".filter(n -> n > 3).forEach(System.out::println)"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Package Province",
        "topic": "Packages, imports, Jar files",
        "description": "The organized provinces where code is packaged!",
        "story_intro": "Large projects need organization. Packages provide it!",
        "character": "Organizer Package",
        "character_quote": "Order brings clarity. Packages bring order!",
        "icon": "scroll",
        "color": "#581e00",
        "missions": [
            {
                "id": 521,
                "title": "Package Organization",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Java Packages",
                    "overview": "Organize code into packages.",
                    "sections": [
                        {"heading": "Package Declaration", "content": "```java\npackage com.game.characters;\n\npublic class Hero {\n    // class code\n}\n```"},
                        {"heading": "Imports", "content": "```java\nimport com.game.characters.Hero;\nimport java.util.*;\n```"}
                    ]
                },
                "story": "Organizer Package sorts the scrolls. 'Group related classes!'",
                "task": "Understand package structure (conceptual - no execution needed).",
                "starter_code": "// Package example\npackage com.kingdom.units;\n\npublic class Knight {\n    public void fight() {\n        System.out.println(\"For the kingdom!\");\n    }\n}",
                "expected_output": None,
                "hints": ["package declaration goes at the top"]
            },
            {
                "id": 522,
                "title": "Import Mastery",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Import Statements",
                    "overview": "Bring classes from other packages.",
                    "sections": [
                        {"heading": "Import Types", "content": "```java\nimport java.util.ArrayList; // Specific\nimport java.util.*;          // Wildcard\nimport static java.lang.Math.PI; // Static\n```"}
                    ]
                },
                "story": "'Import what you need,' Organizer advises.",
                "task": "Import ArrayList and Scanner, create both.",
                "starter_code": "// Imports\n\npublic class Main {\n    public static void main(String[] args) {\n        // Use ArrayList and Scanner\n    }\n}",
                "expected_output": None,
                "hints": ["import java.util.ArrayList; import java.util.Scanner;"]
            },
            {
                "id": 532,
                "title": "JAR Files",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Java Archive Files",
                    "overview": "JAR files bundle Java classes for distribution.",
                    "sections": [
                        {"heading": "What is a JAR", "content": "- Java ARchive - a ZIP file containing .class files\n- Can include resources (images, configs)\n- Executable JARs have a manifest specifying main class"},
                        {"heading": "Creating JARs", "content": "```bash\n# Create JAR\njar cf myapp.jar *.class\n\n# Create executable JAR\njar cfe myapp.jar MainClass *.class\n\n# Run JAR\njava -jar myapp.jar\n```"}
                    ]
                },
                "story": "'JARs package your kingdom for travel,' Organizer explains. 'Bundle and deploy!'",
                "task": "Write a simple class that could be bundled into a JAR, with a main method.",
                "starter_code": "// A class ready for JAR packaging\npublic class Main {\n    public static void main(String[] args) {\n        // Your application entry point\n    }\n}",
                "expected_output": "Kingdom app started!",
                "hints": ["System.out.println(\"Kingdom app started!\");"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Grand Architect Trial",
        "topic": "Designing a Kingdom Management System",
        "description": "The ultimate trial - design an enterprise system!",
        "story_intro": "You've mastered Java. Now architect a kingdom!",
        "character": "Grand Architect",
        "character_quote": "Show me your mastery. Build a system worthy of the enterprise!",
        "icon": "trophy",
        "color": "#ffd700",
        "missions": [
            {
                "id": 523,
                "title": "Kingdom Entities",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Entity Classes",
                    "overview": "Design the data model for your kingdom.",
                    "sections": [
                        {"heading": "Entities", "content": "- Kingdom, Province, Castle\n- Citizen, Knight, King\n- Resource, Treasury"}
                    ]
                },
                "story": "Grand Architect watches. 'Design your entities!'",
                "task": "Create entity classes for Kingdom, Province, and Citizen.",
                "starter_code": "// Kingdom Management Entities\n\npublic class Main {\n    public static void main(String[] args) {\n        // Test your entities\n    }\n}",
                "expected_output": None,
                "hints": ["Use inheritance: Citizen -> Knight -> King"]
            },
            {
                "id": 524,
                "title": "Kingdom Services",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Service Layer",
                    "overview": "Business logic in service classes.",
                    "sections": [
                        {"heading": "Services", "content": "- KingdomService: manage provinces\n- TreasuryService: manage gold\n- ArmyService: manage knights"}
                    ]
                },
                "story": "'Services power the kingdom,' Architect explains.",
                "task": "Create service classes with business logic.",
                "starter_code": "// Kingdom Services\n\npublic class Main {\n    public static void main(String[] args) {\n        // Test services\n    }\n}",
                "expected_output": None,
                "hints": ["Use collections to store entities"]
            },
            {
                "id": 525,
                "title": "Complete Kingdom",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "Full System",
                    "overview": "Combine everything into a working system.",
                    "sections": [
                        {"heading": "Requirements", "content": "- Entity classes with inheritance\n- Interfaces for contracts\n- Services for business logic\n- Collections for data\n- Exception handling\n- Console UI for interaction"}
                    ]
                },
                "story": "Grand Architect nods. 'Complete your masterpiece!'",
                "task": "Build the complete Kingdom Management System.",
                "starter_code": "// Complete Kingdom Management System\nimport java.util.*;\n\n// Your comprehensive solution here",
                "expected_output": None,
                "hints": ["Combine entities, services, collections, and exception handling"]
            }
        ]
    }
]

SQL_ARCS = [
    {
        "id": 1,
        "name": "Scroll of Schema",
        "topic": "CREATE, DROP, ALTER, Data Types",
        "description": "Learn to define the structure of your data scrolls.",
        "story_intro": "The Archives of the Ancients hold vast knowledge. First, you must learn to create and shape the scrolls that store it.",
        "character": "Archivist Scroll",
        "character_quote": "Every record begins with a well-defined structure. Learn the DDL arts!",
        "icon": "scroll",
        "color": "#336791",
        "missions": [
            {
                "id": 601,
                "title": "Creating Tables",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "CREATE TABLE",
                    "overview": "Tables are the foundation of databases - they store your data in rows and columns.",
                    "sections": [
                        {"heading": "CREATE Syntax", "content": "```sql\nCREATE TABLE heroes (\n    id INTEGER PRIMARY KEY,\n    name VARCHAR(100),\n    level INTEGER\n);\n```"},
                        {"heading": "Common Data Types", "content": "- INTEGER: Whole numbers\n- VARCHAR(n): Text up to n characters\n- TEXT: Long text\n- BOOLEAN: True/False\n- DATE: Calendar dates"}
                    ]
                },
                "story": "'To store knowledge, you must first create the scrolls,' Archivist explains.",
                "task": "Create a table called 'students' with columns: id (INTEGER PRIMARY KEY), name (VARCHAR), and age (INTEGER).",
                "starter_code": "-- Create the students table\n",
                "expected_output": None,
                "hints": ["CREATE TABLE students (...);"]
            },
            {
                "id": 602,
                "title": "Data Types Mastery",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "SQL Data Types",
                    "overview": "Choose the right data type for each column.",
                    "sections": [
                        {"heading": "Numeric Types", "content": "- INTEGER / INT: Whole numbers\n- DECIMAL(p,s): Precise decimals\n- FLOAT: Approximate decimals"},
                        {"heading": "Text Types", "content": "- CHAR(n): Fixed-length text\n- VARCHAR(n): Variable-length text\n- TEXT: Unlimited text"},
                        {"heading": "Other Types", "content": "- DATE: YYYY-MM-DD\n- TIMESTAMP: Date and time\n- BOOLEAN: TRUE/FALSE"}
                    ]
                },
                "story": "'Each type of data needs the right container,' Archivist teaches.",
                "task": "Create a 'products' table with id (INTEGER), name (VARCHAR), price (DECIMAL), and created_at (TIMESTAMP).",
                "starter_code": "-- Create products with proper data types\n",
                "expected_output": None,
                "hints": ["DECIMAL(10,2) for currency"]
            },
            {
                "id": 603,
                "title": "Altering Scrolls",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "ALTER TABLE",
                    "overview": "Modify existing table structures.",
                    "sections": [
                        {"heading": "Add Column", "content": "```sql\nALTER TABLE heroes ADD COLUMN power INTEGER;\n```"},
                        {"heading": "Drop Column", "content": "```sql\nALTER TABLE heroes DROP COLUMN power;\n```"},
                        {"heading": "Modify Column", "content": "```sql\nALTER TABLE heroes ALTER COLUMN name TYPE VARCHAR(200);\n```"}
                    ]
                },
                "story": "'Scrolls can be modified,' Archivist reveals. 'But be careful!'",
                "task": "Add an 'email' column (VARCHAR) to an existing 'users' table.",
                "starter_code": "-- Modify the users table\n",
                "expected_output": None,
                "hints": ["ALTER TABLE users ADD COLUMN ..."]
            },
            {
                "id": 604,
                "title": "Dropping Tables",
                "difficulty": "medium",
                "xp": 25,
                "lesson": {
                    "title": "DROP TABLE",
                    "overview": "Remove tables from the database.",
                    "sections": [
                        {"heading": "DROP Syntax", "content": "```sql\nDROP TABLE heroes;\n```"},
                        {"heading": "Safe Drop", "content": "```sql\nDROP TABLE IF EXISTS heroes;\n```\nThis avoids errors if the table doesn't exist."}
                    ]
                },
                "story": "'Sometimes scrolls must be destroyed,' Archivist warns. 'This cannot be undone!'",
                "task": "Safely drop a table called 'old_records' if it exists.",
                "starter_code": "-- Drop the old_records table safely\n",
                "expected_output": None,
                "hints": ["DROP TABLE IF EXISTS ..."]
            }
        ]
    },
    {
        "id": 2,
        "name": "The Record Forge",
        "topic": "INSERT, UPDATE, DELETE",
        "description": "Learn to create, modify, and remove data records.",
        "story_intro": "The Record Forge is where data is shaped and molded. Master the DML arts!",
        "character": "Forgemaster Data",
        "character_quote": "Data is the lifeblood of the archives. Learn to forge it well!",
        "icon": "hammer",
        "color": "#e74c3c",
        "missions": [
            {
                "id": 605,
                "title": "Inserting Records",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "INSERT INTO",
                    "overview": "Add new rows to your tables.",
                    "sections": [
                        {"heading": "Basic Insert", "content": "```sql\nINSERT INTO heroes (name, level)\nVALUES ('Luna', 10);\n```"},
                        {"heading": "Multiple Rows", "content": "```sql\nINSERT INTO heroes (name, level)\nVALUES ('Luna', 10), ('Kai', 15);\n```"}
                    ]
                },
                "story": "'Every record starts here,' Forgemaster explains. 'Insert with care!'",
                "task": "Insert a new hero named 'Sakura' with level 5 into the heroes table.",
                "starter_code": "-- Insert a new hero\n",
                "expected_output": None,
                "hints": ["INSERT INTO heroes (name, level) VALUES ..."]
            },
            {
                "id": 606,
                "title": "Updating Records",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "UPDATE",
                    "overview": "Modify existing data in your tables.",
                    "sections": [
                        {"heading": "Update Syntax", "content": "```sql\nUPDATE heroes\nSET level = 20\nWHERE name = 'Luna';\n```"},
                        {"heading": "Update Multiple Columns", "content": "```sql\nUPDATE heroes\nSET level = 25, power = 100\nWHERE id = 1;\n```"}
                    ]
                },
                "story": "'Records change over time,' Forgemaster teaches. 'Always use WHERE!'",
                "task": "Update the level to 50 for the hero named 'Sakura'.",
                "starter_code": "-- Update Sakura's level\n",
                "expected_output": None,
                "hints": ["UPDATE heroes SET level = 50 WHERE ..."]
            },
            {
                "id": 607,
                "title": "Deleting Records",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "DELETE",
                    "overview": "Remove rows from your tables.",
                    "sections": [
                        {"heading": "Delete Syntax", "content": "```sql\nDELETE FROM heroes\nWHERE level < 5;\n```"},
                        {"heading": "Warning", "content": "DELETE without WHERE removes ALL rows!\n```sql\nDELETE FROM heroes; -- Deletes everything!\n```"}
                    ]
                },
                "story": "'Sometimes records must be purged,' Forgemaster warns. 'Be precise!'",
                "task": "Delete all heroes where level is less than 10.",
                "starter_code": "-- Delete low-level heroes\n",
                "expected_output": None,
                "hints": ["DELETE FROM heroes WHERE level < 10"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Visionary Lens",
        "topic": "SELECT, WHERE, DISTINCT",
        "description": "Learn to query and filter data from your tables.",
        "story_intro": "The Visionary Lens lets you see into the archives. Learn to query wisely!",
        "character": "Oracle Sight",
        "character_quote": "To find what you seek, you must learn to ask the right questions!",
        "icon": "eye",
        "color": "#9b59b6",
        "missions": [
            {
                "id": 608,
                "title": "Basic SELECT",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "SELECT Statement",
                    "overview": "Retrieve data from your tables.",
                    "sections": [
                        {"heading": "Select All", "content": "```sql\nSELECT * FROM heroes;\n```"},
                        {"heading": "Select Columns", "content": "```sql\nSELECT name, level FROM heroes;\n```"}
                    ]
                },
                "story": "'The lens reveals all,' Oracle explains. 'Learn to focus it!'",
                "task": "Select all columns from the heroes table.",
                "starter_code": "-- Query all heroes\n",
                "expected_output": None,
                "hints": ["SELECT * FROM heroes;"]
            },
            {
                "id": 609,
                "title": "Filtering with WHERE",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "WHERE Clause",
                    "overview": "Filter your results with conditions.",
                    "sections": [
                        {"heading": "Basic Filter", "content": "```sql\nSELECT * FROM heroes\nWHERE level > 10;\n```"},
                        {"heading": "Operators", "content": "- = Equal\n- <> Not equal\n- > Greater than\n- < Less than\n- LIKE Pattern matching\n- IN List matching"}
                    ]
                },
                "story": "'Filter the noise,' Oracle teaches. 'Find only what matters!'",
                "task": "Select heroes where level is greater than or equal to 20.",
                "starter_code": "-- Find high-level heroes\n",
                "expected_output": None,
                "hints": ["WHERE level >= 20"]
            },
            {
                "id": 610,
                "title": "Unique Values",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "DISTINCT",
                    "overview": "Get unique values from your queries.",
                    "sections": [
                        {"heading": "DISTINCT Usage", "content": "```sql\nSELECT DISTINCT class FROM heroes;\n```\nReturns each unique class only once."},
                        {"heading": "Multiple Columns", "content": "```sql\nSELECT DISTINCT class, level FROM heroes;\n```\nUnique combinations of class and level."}
                    ]
                },
                "story": "'See only the unique,' Oracle reveals. 'No duplicates!'",
                "task": "Select distinct classes from the heroes table.",
                "starter_code": "-- Get unique hero classes\n",
                "expected_output": None,
                "hints": ["SELECT DISTINCT class FROM heroes;"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Sorting Blade",
        "topic": "ORDER BY, LIMIT, OFFSET",
        "description": "Learn to sort and paginate your query results.",
        "story_intro": "The Sorting Blade arranges data in perfect order. Master its techniques!",
        "character": "Knight Order",
        "character_quote": "Order brings clarity. Learn to sort your results!",
        "icon": "sort",
        "color": "#3498db",
        "missions": [
            {
                "id": 611,
                "title": "Sorting Results",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "ORDER BY",
                    "overview": "Sort your query results.",
                    "sections": [
                        {"heading": "Ascending", "content": "```sql\nSELECT * FROM heroes\nORDER BY level ASC;\n```"},
                        {"heading": "Descending", "content": "```sql\nSELECT * FROM heroes\nORDER BY level DESC;\n```"},
                        {"heading": "Multiple Columns", "content": "```sql\nSELECT * FROM heroes\nORDER BY class, level DESC;\n```"}
                    ]
                },
                "story": "'Arrange your data,' Knight Order commands. 'From lowest to highest!'",
                "task": "Select all heroes ordered by level in descending order.",
                "starter_code": "-- Sort heroes by level\n",
                "expected_output": None,
                "hints": ["ORDER BY level DESC"]
            },
            {
                "id": 612,
                "title": "Limiting Results",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "LIMIT",
                    "overview": "Restrict the number of rows returned.",
                    "sections": [
                        {"heading": "LIMIT Usage", "content": "```sql\nSELECT * FROM heroes\nORDER BY level DESC\nLIMIT 5;\n```\nReturns only the top 5 heroes."}
                    ]
                },
                "story": "'You don't always need everything,' Knight explains. 'Take only what you need!'",
                "task": "Select the top 3 highest-level heroes.",
                "starter_code": "-- Get top 3 heroes\n",
                "expected_output": None,
                "hints": ["ORDER BY level DESC LIMIT 3"]
            },
            {
                "id": 613,
                "title": "Pagination with OFFSET",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "OFFSET",
                    "overview": "Skip rows for pagination.",
                    "sections": [
                        {"heading": "OFFSET Usage", "content": "```sql\nSELECT * FROM heroes\nORDER BY id\nLIMIT 10 OFFSET 20;\n```\nSkips first 20 rows, returns next 10 (page 3)."},
                        {"heading": "Pagination Formula", "content": "OFFSET = (page_number - 1) * page_size"}
                    ]
                },
                "story": "'For large archives, you must paginate,' Knight teaches. 'Skip and take!'",
                "task": "Get the second page of heroes (5 per page).",
                "starter_code": "-- Get page 2 of heroes\n",
                "expected_output": None,
                "hints": ["LIMIT 5 OFFSET 5"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Alchemist's Cauldron",
        "topic": "COUNT, SUM, AVG, GROUP BY, HAVING",
        "description": "Learn to aggregate and summarize your data.",
        "story_intro": "The Alchemist's Cauldron transforms raw data into powerful insights!",
        "character": "Alchemist Sum",
        "character_quote": "Combine data to reveal hidden truths. Master aggregation!",
        "icon": "flask",
        "color": "#27ae60",
        "missions": [
            {
                "id": 614,
                "title": "Counting Records",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "COUNT Function",
                    "overview": "Count rows in your results.",
                    "sections": [
                        {"heading": "Count All", "content": "```sql\nSELECT COUNT(*) FROM heroes;\n```"},
                        {"heading": "Count Column", "content": "```sql\nSELECT COUNT(email) FROM users;\n```\nCounts non-NULL values only."}
                    ]
                },
                "story": "'How many heroes exist?' Alchemist asks. 'Count them!'",
                "task": "Count the total number of heroes in the heroes table.",
                "starter_code": "-- Count all heroes\n",
                "expected_output": None,
                "hints": ["SELECT COUNT(*) FROM heroes;"]
            },
            {
                "id": 615,
                "title": "SUM Function",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "SUM",
                    "overview": "Calculate totals of numeric columns.",
                    "sections": [
                        {"heading": "SUM Usage", "content": "```sql\nSELECT SUM(gold) FROM heroes;\n```\nReturns the total of all gold values."},
                        {"heading": "SUM with WHERE", "content": "```sql\nSELECT SUM(gold) FROM heroes WHERE level > 10;\n```"}
                    ]
                },
                "story": "'Add them all up,' Alchemist instructs. 'Find the total!'",
                "task": "Find the total gold of all heroes.",
                "starter_code": "-- Calculate the total gold\n",
                "expected_output": None,
                "hints": ["SELECT SUM(gold) FROM heroes;"]
            },
            {
                "id": 638,
                "title": "AVG Function",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "AVG",
                    "overview": "Calculate averages of numeric columns.",
                    "sections": [
                        {"heading": "AVG Usage", "content": "```sql\nSELECT AVG(level) FROM heroes;\n```\nReturns the average of all level values."},
                        {"heading": "AVG with Rounding", "content": "```sql\nSELECT ROUND(AVG(level), 2) FROM heroes;\n```"}
                    ]
                },
                "story": "'What is the typical value?' Alchemist asks. 'Find the average!'",
                "task": "Find the average level of all heroes.",
                "starter_code": "-- Calculate the average level\n",
                "expected_output": None,
                "hints": ["SELECT AVG(level) FROM heroes;"]
            },
            {
                "id": 616,
                "title": "Grouping Data",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "GROUP BY",
                    "overview": "Group rows and aggregate per group.",
                    "sections": [
                        {"heading": "GROUP BY", "content": "```sql\nSELECT class, COUNT(*) as count\nFROM heroes\nGROUP BY class;\n```\nCounts heroes per class."}
                    ]
                },
                "story": "'Separate by category,' Alchemist teaches. 'Then count each!'",
                "task": "Count heroes per class using GROUP BY.",
                "starter_code": "-- Count heroes by class\n",
                "expected_output": None,
                "hints": ["GROUP BY class"]
            },
            {
                "id": 617,
                "title": "Filtering Groups",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "HAVING",
                    "overview": "Filter groups after aggregation.",
                    "sections": [
                        {"heading": "HAVING vs WHERE", "content": "```sql\nSELECT class, COUNT(*) as count\nFROM heroes\nGROUP BY class\nHAVING COUNT(*) > 5;\n```\nHAVING filters after grouping, WHERE filters before."}
                    ]
                },
                "story": "'Not all groups matter,' Alchemist reveals. 'Filter them!'",
                "task": "Find classes with more than 3 heroes.",
                "starter_code": "-- Find popular classes\n",
                "expected_output": None,
                "hints": ["HAVING COUNT(*) > 3"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Guild Hall Gathering",
        "topic": "INNER JOIN, LEFT JOIN, ON clause",
        "description": "Learn to combine data from multiple tables.",
        "story_intro": "The Guild Hall brings different scrolls together. Learn to join them!",
        "character": "Guildmaster Link",
        "character_quote": "Data spread across scrolls must be united. Master the joins!",
        "icon": "link",
        "color": "#e67e22",
        "missions": [
            {
                "id": 618,
                "title": "INNER JOIN",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "INNER JOIN",
                    "overview": "Combine matching rows from two tables.",
                    "sections": [
                        {"heading": "INNER JOIN", "content": "```sql\nSELECT heroes.name, guilds.name\nFROM heroes\nINNER JOIN guilds ON heroes.guild_id = guilds.id;\n```\nOnly returns rows that match in both tables."}
                    ]
                },
                "story": "'Find where scrolls intersect,' Guildmaster explains. 'INNER JOIN!'",
                "task": "Join heroes and guilds tables to show hero names with their guild names.",
                "starter_code": "-- Join heroes with their guilds\n",
                "expected_output": None,
                "hints": ["INNER JOIN guilds ON heroes.guild_id = guilds.id"]
            },
            {
                "id": 619,
                "title": "LEFT JOIN",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "LEFT JOIN",
                    "overview": "Include all rows from the left table.",
                    "sections": [
                        {"heading": "LEFT JOIN", "content": "```sql\nSELECT heroes.name, guilds.name\nFROM heroes\nLEFT JOIN guilds ON heroes.guild_id = guilds.id;\n```\nReturns all heroes, even those without a guild (NULL)."}
                    ]
                },
                "story": "'Include everyone from the left scroll,' Guildmaster teaches. 'Even loners!'",
                "task": "List all heroes with their guilds (include heroes without guilds).",
                "starter_code": "-- Left join heroes and guilds\n",
                "expected_output": None,
                "hints": ["LEFT JOIN guilds ON ..."]
            },
            {
                "id": 620,
                "title": "The ON Clause",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "ON Clause",
                    "overview": "Define how tables are connected.",
                    "sections": [
                        {"heading": "ON Clause", "content": "```sql\nSELECT *\nFROM orders o\nINNER JOIN customers c ON o.customer_id = c.id;\n```\nThe ON clause specifies the relationship between tables."},
                        {"heading": "Multiple Conditions", "content": "```sql\nON a.id = b.a_id AND a.type = b.type\n```"}
                    ]
                },
                "story": "'The ON clause is the bridge,' Guildmaster explains. 'Define the connection!'",
                "task": "Join orders and products using the product_id column.",
                "starter_code": "-- Join orders with products\n",
                "expected_output": None,
                "hints": ["ON orders.product_id = products.id"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Cross-Realm Links",
        "topic": "RIGHT JOIN, FULL OUTER JOIN, Self Joins",
        "description": "Master advanced join techniques.",
        "story_intro": "Cross-realm connections require advanced techniques. Learn them all!",
        "character": "Linkmaster Cross",
        "character_quote": "Sometimes you need to see everything. Master all join types!",
        "icon": "network",
        "color": "#8e44ad",
        "missions": [
            {
                "id": 621,
                "title": "RIGHT JOIN",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "RIGHT JOIN",
                    "overview": "Include all rows from the right table.",
                    "sections": [
                        {"heading": "RIGHT JOIN", "content": "```sql\nSELECT heroes.name, guilds.name\nFROM heroes\nRIGHT JOIN guilds ON heroes.guild_id = guilds.id;\n```\nReturns all guilds, even those with no heroes."}
                    ]
                },
                "story": "'Now include everyone from the right scroll,' Linkmaster teaches.",
                "task": "List all guilds with their heroes (include guilds with no heroes).",
                "starter_code": "-- Right join\n",
                "expected_output": None,
                "hints": ["RIGHT JOIN guilds ON ..."]
            },
            {
                "id": 622,
                "title": "FULL OUTER JOIN",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "FULL OUTER JOIN",
                    "overview": "Include all rows from both tables.",
                    "sections": [
                        {"heading": "FULL OUTER JOIN", "content": "```sql\nSELECT heroes.name, guilds.name\nFROM heroes\nFULL OUTER JOIN guilds ON heroes.guild_id = guilds.id;\n```\nReturns all rows from both tables, with NULLs where there's no match."}
                    ]
                },
                "story": "'See the complete picture,' Linkmaster reveals. 'All from both sides!'",
                "task": "Show all heroes and all guilds, matched or not.",
                "starter_code": "-- Full outer join\n",
                "expected_output": None,
                "hints": ["FULL OUTER JOIN ... ON ..."]
            },
            {
                "id": 623,
                "title": "Self Joins",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "Self Joins",
                    "overview": "Join a table to itself.",
                    "sections": [
                        {"heading": "Self Join", "content": "```sql\nSELECT e.name as employee, m.name as manager\nFROM employees e\nLEFT JOIN employees m ON e.manager_id = m.id;\n```\nUseful for hierarchical data."}
                    ]
                },
                "story": "'A scroll can reference itself,' Linkmaster explains. 'Master self joins!'",
                "task": "Find each employee with their manager's name using a self join.",
                "starter_code": "-- Self join for hierarchy\n",
                "expected_output": None,
                "hints": ["Use table aliases: employees e, employees m"]
            }
        ]
    },
    {
        "id": 8,
        "name": "The Hidden Archives",
        "topic": "Nested SELECTs, IN, EXISTS",
        "description": "Learn the power of subqueries.",
        "story_intro": "Within queries lie other queries. Master the hidden archives!",
        "character": "Nested One",
        "character_quote": "Queries within queries unlock deeper truths. Learn subqueries!",
        "icon": "layers",
        "color": "#1abc9c",
        "missions": [
            {
                "id": 624,
                "title": "Nested SELECTs",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Subqueries",
                    "overview": "Use a query inside another query.",
                    "sections": [
                        {"heading": "Subquery in WHERE", "content": "```sql\nSELECT * FROM heroes\nWHERE level > (SELECT AVG(level) FROM heroes);\n```\nFinds heroes above average level."},
                        {"heading": "Subquery in FROM", "content": "```sql\nSELECT * FROM (\n    SELECT name, level FROM heroes\n) AS h;\n```"}
                    ]
                },
                "story": "'Queries can contain queries,' Nested One reveals. 'Go deeper!'",
                "task": "Find heroes whose level is above the average level.",
                "starter_code": "-- Subquery to find above-average heroes\n",
                "expected_output": None,
                "hints": ["WHERE level > (SELECT AVG(level) FROM heroes)"]
            },
            {
                "id": 625,
                "title": "The IN Operator",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "IN with Subqueries",
                    "overview": "Check if a value exists in a list.",
                    "sections": [
                        {"heading": "IN Usage", "content": "```sql\nSELECT * FROM heroes\nWHERE guild_id IN (SELECT id FROM guilds WHERE size > 100);\n```\nFinds heroes in large guilds."}
                    ]
                },
                "story": "'Check if values belong to a set,' Nested One teaches. 'Use IN!'",
                "task": "Find heroes who belong to elite guilds (guild rank = 'elite').",
                "starter_code": "-- Find heroes in elite guilds\n",
                "expected_output": None,
                "hints": ["WHERE guild_id IN (SELECT id FROM guilds WHERE ...)"]
            },
            {
                "id": 626,
                "title": "EXISTS Operator",
                "difficulty": "hard",
                "xp": 40,
                "lesson": {
                    "title": "EXISTS",
                    "overview": "Check if a subquery returns any rows.",
                    "sections": [
                        {"heading": "EXISTS Usage", "content": "```sql\nSELECT * FROM guilds g\nWHERE EXISTS (\n    SELECT 1 FROM heroes h\n    WHERE h.guild_id = g.id AND h.level > 50\n);\n```\nFinds guilds that have at least one high-level hero."}
                    ]
                },
                "story": "'Does something exist?' Nested One asks. 'EXISTS tells you!'",
                "task": "Find guilds that have at least one member.",
                "starter_code": "-- Find guilds with members\n",
                "expected_output": None,
                "hints": ["WHERE EXISTS (SELECT 1 FROM heroes WHERE ...)"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Virtual Reflections",
        "topic": "CREATE VIEW, Dropping Views",
        "description": "Create virtual tables for complex queries.",
        "story_intro": "Views are reflections of data - virtual tables that simplify complex queries.",
        "character": "Mirror Sage",
        "character_quote": "Create reflections of your data. Views simplify complexity!",
        "icon": "mirror",
        "color": "#f39c12",
        "missions": [
            {
                "id": 627,
                "title": "Creating Views",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "CREATE VIEW",
                    "overview": "Save a query as a virtual table.",
                    "sections": [
                        {"heading": "CREATE VIEW", "content": "```sql\nCREATE VIEW high_level_heroes AS\nSELECT name, level, class\nFROM heroes\nWHERE level > 50;\n```"},
                        {"heading": "Using Views", "content": "```sql\nSELECT * FROM high_level_heroes;\n```\nQuery it like a regular table!"}
                    ]
                },
                "story": "'Create a reflection,' Mirror Sage teaches. 'A view simplifies!'",
                "task": "Create a view called 'elite_heroes' showing heroes with level > 40.",
                "starter_code": "-- Create the elite_heroes view\n",
                "expected_output": None,
                "hints": ["CREATE VIEW elite_heroes AS SELECT ..."]
            },
            {
                "id": 628,
                "title": "Dropping Views",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "DROP VIEW",
                    "overview": "Remove views from the database.",
                    "sections": [
                        {"heading": "DROP VIEW", "content": "```sql\nDROP VIEW high_level_heroes;\n```"},
                        {"heading": "Safe Drop", "content": "```sql\nDROP VIEW IF EXISTS high_level_heroes;\n```"}
                    ]
                },
                "story": "'Reflections can be shattered,' Mirror Sage warns. 'Drop wisely!'",
                "task": "Safely drop a view called 'old_view' if it exists.",
                "starter_code": "-- Drop the view\n",
                "expected_output": None,
                "hints": ["DROP VIEW IF EXISTS old_view;"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Flow of Sequence",
        "topic": "ROW_NUMBER, RANK, PARTITION BY",
        "description": "Master window functions for advanced analytics.",
        "story_intro": "Window functions let you see across rows while keeping each row. Advanced magic!",
        "character": "Window Walker",
        "character_quote": "See beyond single rows. Window functions reveal patterns!",
        "icon": "grid",
        "color": "#16a085",
        "missions": [
            {
                "id": 629,
                "title": "ROW_NUMBER",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "ROW_NUMBER()",
                    "overview": "Assign sequential numbers to rows.",
                    "sections": [
                        {"heading": "ROW_NUMBER", "content": "```sql\nSELECT name, level,\n    ROW_NUMBER() OVER (ORDER BY level DESC) as rank\nFROM heroes;\n```\nAssigns 1, 2, 3... based on level order."}
                    ]
                },
                "story": "'Number each row,' Window Walker instructs. 'ROW_NUMBER!'",
                "task": "Assign row numbers to heroes ordered by level descending.",
                "starter_code": "-- Add row numbers\n",
                "expected_output": None,
                "hints": ["ROW_NUMBER() OVER (ORDER BY level DESC)"]
            },
            {
                "id": 630,
                "title": "RANK Function",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "RANK()",
                    "overview": "Assign ranks with gaps for ties.",
                    "sections": [
                        {"heading": "RANK vs ROW_NUMBER", "content": "```sql\nSELECT name, level,\n    RANK() OVER (ORDER BY level DESC) as rank\nFROM heroes;\n```\nRank handles ties: 1, 1, 3 (skips 2 for ties)."},
                        {"heading": "DENSE_RANK", "content": "DENSE_RANK() doesn't skip: 1, 1, 2"}
                    ]
                },
                "story": "'Handle ties properly,' Window Walker teaches. 'RANK!'",
                "task": "Rank heroes by level, handling ties appropriately.",
                "starter_code": "-- Rank heroes\n",
                "expected_output": None,
                "hints": ["RANK() OVER (ORDER BY level DESC)"]
            },
            {
                "id": 631,
                "title": "PARTITION BY",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "PARTITION BY",
                    "overview": "Apply window functions within groups.",
                    "sections": [
                        {"heading": "PARTITION BY", "content": "```sql\nSELECT name, class, level,\n    RANK() OVER (PARTITION BY class ORDER BY level DESC) as class_rank\nFROM heroes;\n```\nRanks heroes within their own class."}
                    ]
                },
                "story": "'Partition your data,' Window Walker reveals. 'Rank within groups!'",
                "task": "Rank heroes within each class by their level.",
                "starter_code": "-- Rank within classes\n",
                "expected_output": None,
                "hints": ["PARTITION BY class ORDER BY level DESC"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Eternal Transaction",
        "topic": "ACID, COMMIT, ROLLBACK, Constraints",
        "description": "Learn data integrity and transaction control.",
        "story_intro": "Data integrity is sacred. Master transactions and constraints!",
        "character": "Guardian Integrity",
        "character_quote": "Protect your data at all costs. Master ACID principles!",
        "icon": "shield",
        "color": "#c0392b",
        "missions": [
            {
                "id": 632,
                "title": "ACID Principles",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "ACID Properties",
                    "overview": "The four pillars of database reliability.",
                    "sections": [
                        {"heading": "ACID", "content": "- **A**tomicity: All or nothing\n- **C**onsistency: Valid state to valid state\n- **I**solation: Transactions don't interfere\n- **D**urability: Committed data survives crashes"}
                    ]
                },
                "story": "'ACID keeps data safe,' Guardian explains. 'Understand these principles!'",
                "task": "Write a comment explaining each ACID property in your own words.",
                "starter_code": "-- Explain ACID:\n-- A - \n-- C - \n-- I - \n-- D - ",
                "expected_output": None,
                "hints": ["Atomicity means all-or-nothing"]
            },
            {
                "id": 633,
                "title": "COMMIT",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "COMMIT",
                    "overview": "Save your changes permanently.",
                    "sections": [
                        {"heading": "COMMIT Usage", "content": "```sql\nBEGIN;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT;\n```\nCOMMIT makes all changes permanent."}
                    ]
                },
                "story": "'Commit seals the deal,' Guardian teaches. 'Changes become permanent!'",
                "task": "Write a transaction that transfers gold and commits it.",
                "starter_code": "-- Transfer 50 gold from hero 1 to hero 2\nBEGIN;\n-- Your updates here\n",
                "expected_output": None,
                "hints": ["End with COMMIT;"]
            },
            {
                "id": 639,
                "title": "ROLLBACK",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "ROLLBACK",
                    "overview": "Undo changes before committing.",
                    "sections": [
                        {"heading": "ROLLBACK Usage", "content": "```sql\nBEGIN;\nDELETE FROM heroes WHERE level < 5;\nROLLBACK; -- Undo the delete!\n```\nROLLBACK discards all changes since BEGIN."},
                        {"heading": "When to Rollback", "content": "Use ROLLBACK when:\n- An error occurs mid-transaction\n- You realize a mistake before committing\n- Testing destructive operations safely"}
                    ]
                },
                "story": "'Made a mistake?' Guardian asks. 'Rollback undoes everything!'",
                "task": "Write a transaction that deletes data but then rolls back.",
                "starter_code": "-- Delete low-level heroes but undo it\nBEGIN;\n-- Your delete here\n",
                "expected_output": None,
                "hints": ["End with ROLLBACK;"]
            },
            {
                "id": 634,
                "title": "Constraints",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Data Constraints",
                    "overview": "Enforce rules on your data.",
                    "sections": [
                        {"heading": "Common Constraints", "content": "```sql\nCREATE TABLE heroes (\n    id INTEGER PRIMARY KEY,\n    name VARCHAR(100) NOT NULL,\n    email VARCHAR(100) UNIQUE,\n    level INTEGER CHECK (level >= 1),\n    guild_id INTEGER REFERENCES guilds(id)\n);\n```"},
                        {"heading": "Constraint Types", "content": "- PRIMARY KEY: Unique identifier\n- NOT NULL: Required field\n- UNIQUE: No duplicates\n- CHECK: Custom validation\n- FOREIGN KEY: References another table"}
                    ]
                },
                "story": "'Constraints enforce rules,' Guardian explains. 'Data stays valid!'",
                "task": "Create a table with PRIMARY KEY, NOT NULL, and CHECK constraints.",
                "starter_code": "-- Create a constrained table\n",
                "expected_output": None,
                "hints": ["level INTEGER CHECK (level > 0)"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Grand Oracle",
        "topic": "Indexes, Triggers, Execution Plans",
        "description": "Master database optimization and automation.",
        "story_intro": "The Grand Oracle reveals the deepest secrets of database mastery!",
        "character": "Grand Oracle",
        "character_quote": "Speed and automation - the final arts. Master optimization!",
        "icon": "zap",
        "color": "#ffd700",
        "missions": [
            {
                "id": 635,
                "title": "Creating Indexes",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Indexes",
                    "overview": "Speed up queries with indexes.",
                    "sections": [
                        {"heading": "CREATE INDEX", "content": "```sql\nCREATE INDEX idx_heroes_level ON heroes(level);\n```"},
                        {"heading": "When to Index", "content": "- Columns used in WHERE clauses\n- Columns used in JOINs\n- Columns used in ORDER BY\n- Don't over-index (slows INSERT/UPDATE)"}
                    ]
                },
                "story": "'Indexes speed up searches,' Oracle reveals. 'Use them wisely!'",
                "task": "Create an index on the 'email' column of the users table.",
                "starter_code": "-- Create an index for faster email lookups\n",
                "expected_output": None,
                "hints": ["CREATE INDEX idx_users_email ON users(email);"]
            },
            {
                "id": 636,
                "title": "Triggers",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Triggers",
                    "overview": "Automate actions on data changes.",
                    "sections": [
                        {"heading": "CREATE TRIGGER", "content": "```sql\nCREATE TRIGGER log_hero_update\nAFTER UPDATE ON heroes\nFOR EACH ROW\nEXECUTE FUNCTION log_changes();\n```"},
                        {"heading": "Trigger Events", "content": "- BEFORE/AFTER INSERT\n- BEFORE/AFTER UPDATE\n- BEFORE/AFTER DELETE"}
                    ]
                },
                "story": "'Triggers react automatically,' Oracle explains. 'Set and forget!'",
                "task": "Describe a trigger that logs hero level changes.",
                "starter_code": "-- Describe a trigger for logging level changes\n-- TRIGGER: \n-- EVENT: \n-- ACTION: ",
                "expected_output": None,
                "hints": ["AFTER UPDATE ON heroes"]
            },
            {
                "id": 637,
                "title": "Execution Plans",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "EXPLAIN",
                    "overview": "Understand how queries are executed.",
                    "sections": [
                        {"heading": "EXPLAIN", "content": "```sql\nEXPLAIN SELECT * FROM heroes WHERE level > 50;\n```\nShows the query execution plan."},
                        {"heading": "EXPLAIN ANALYZE", "content": "```sql\nEXPLAIN ANALYZE SELECT * FROM heroes WHERE level > 50;\n```\nActually runs the query and shows real timing."}
                    ]
                },
                "story": "'See how queries execute,' Oracle reveals. 'Optimize with knowledge!'",
                "task": "Use EXPLAIN to analyze a query joining heroes and guilds.",
                "starter_code": "-- Analyze the join query\n",
                "expected_output": None,
                "hints": ["EXPLAIN SELECT * FROM heroes JOIN guilds ON ..."]
            }
        ]
    }
]

DSA_ARCS = [
    {
        "id": 1,
        "name": "Efficiency Compass",
        "topic": "Big-O Notation, Time, Space",
        "description": "Learn to measure algorithm efficiency.",
        "story_intro": "The Logic Corruption spreads chaos. To fight it, you must first understand efficiency!",
        "character": "Master Complexity",
        "character_quote": "Speed and memory - the two measures of every algorithm!",
        "icon": "gauge",
        "color": "#e74c3c",
        "missions": [
            {
                "id": 701,
                "title": "Big-O Notation",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Big-O Notation",
                    "overview": "Big-O describes how algorithm performance scales with input size.",
                    "sections": [
                        {"heading": "Common Complexities", "content": "- O(1): Constant - same time regardless of input\n- O(log n): Logarithmic - halving each step\n- O(n): Linear - grows with input\n- O(n log n): Linearithmic - efficient sorting\n- O(n²): Quadratic - nested loops"},
                        {"heading": "Example", "content": "```python\n# O(1) - Constant\ndef get_first(arr):\n    return arr[0]\n\n# O(n) - Linear\ndef find_max(arr):\n    max_val = arr[0]\n    for x in arr:\n        if x > max_val:\n            max_val = x\n    return max_val\n```"}
                    ]
                },
                "story": "'Every algorithm has a cost,' Master explains. 'Big-O reveals it!'",
                "task": "Identify the Big-O complexity of a function that iterates through an array once.",
                "starter_code": "# What is the Big-O of this function?\ndef sum_array(arr):\n    total = 0\n    for x in arr:\n        total += x\n    return total\n\n# Answer: O(?)",
                "expected_output": "O(n)",
                "hints": ["Single loop through n elements = O(n)"]
            },
            {
                "id": 702,
                "title": "Time Complexity",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Time Complexity",
                    "overview": "How long does your algorithm take as input grows?",
                    "sections": [
                        {"heading": "Analyzing Loops", "content": "- Single loop: O(n)\n- Nested loops: O(n²)\n- Loop halving input: O(log n)"},
                        {"heading": "Example", "content": "```python\n# O(n²) - Nested loops\nfor i in range(n):\n    for j in range(n):\n        print(i, j)\n```"}
                    ]
                },
                "story": "'Time is precious,' Master warns. 'Measure how your code uses it!'",
                "task": "Determine the time complexity of nested loops.",
                "starter_code": "# What is the time complexity?\ndef print_pairs(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(n):\n            print(arr[i], arr[j])\n\n# Answer: O(?)",
                "expected_output": "O(n^2)",
                "hints": ["Two nested loops each running n times"]
            },
            {
                "id": 703,
                "title": "Space Complexity",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Space Complexity",
                    "overview": "How much memory does your algorithm need?",
                    "sections": [
                        {"heading": "Space Analysis", "content": "- O(1): Fixed number of variables\n- O(n): Creating array of size n\n- O(n²): 2D array of n×n"},
                        {"heading": "Example", "content": "```python\n# O(n) space - creates new array\ndef double_all(arr):\n    result = []\n    for x in arr:\n        result.append(x * 2)\n    return result\n```"}
                    ]
                },
                "story": "'Memory is finite,' Master explains. 'Use it wisely!'",
                "task": "Analyze the space complexity of a function that creates a copy of an array.",
                "starter_code": "# What is the space complexity?\ndef copy_array(arr):\n    new_arr = []\n    for x in arr:\n        new_arr.append(x)\n    return new_arr\n\n# Answer: O(?)",
                "expected_output": "O(n)",
                "hints": ["New array stores n elements"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Array Citadel",
        "topic": "Static Arrays, Dynamic Arrays, Strings",
        "description": "Master the fundamental linear data structure.",
        "story_intro": "The Array Citadel holds indexed treasures. Learn to access and manipulate them!",
        "character": "Keeper Index",
        "character_quote": "Arrays are the foundation of all data structures!",
        "icon": "grid",
        "color": "#3498db",
        "missions": [
            {
                "id": 704,
                "title": "Static Arrays",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Static Arrays",
                    "overview": "Fixed-size collections of elements accessed by index.",
                    "sections": [
                        {"heading": "Array Basics", "content": "- Fixed size at creation\n- O(1) access by index\n- Contiguous memory"},
                        {"heading": "Operations", "content": "```python\narr = [1, 2, 3, 4, 5]\nprint(arr[0])  # O(1) access\narr[2] = 10   # O(1) update\n```"}
                    ]
                },
                "story": "'Each element has its place,' Keeper explains. 'Access by index!'",
                "task": "Access the third element of an array (index 2).",
                "starter_code": "arr = [10, 20, 30, 40, 50]\n# Get the third element\nresult = ",
                "expected_output": "30",
                "hints": ["arr[2] gets index 2"]
            },
            {
                "id": 705,
                "title": "Dynamic Arrays",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Dynamic Arrays",
                    "overview": "Arrays that can grow and shrink.",
                    "sections": [
                        {"heading": "Dynamic Operations", "content": "- append(): O(1) amortized\n- pop(): O(1)\n- insert(i, x): O(n)\n- remove(x): O(n)"},
                        {"heading": "Example", "content": "```python\narr = []\narr.append(1)  # [1]\narr.append(2)  # [1, 2]\narr.pop()      # [1]\n```"}
                    ]
                },
                "story": "'Dynamic arrays grow as needed,' Keeper teaches. 'Flexible and powerful!'",
                "task": "Append elements 1, 2, 3 to an empty array.",
                "starter_code": "arr = []\n# Append 1, 2, 3\n",
                "expected_output": "[1, 2, 3]",
                "hints": ["Use arr.append() three times"]
            },
            {
                "id": 706,
                "title": "String Operations",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Strings as Arrays",
                    "overview": "Strings are arrays of characters.",
                    "sections": [
                        {"heading": "String as Array", "content": "- Access by index: s[0]\n- Immutable in most languages\n- Slicing: s[1:4]"},
                        {"heading": "Common Operations", "content": "```python\ns = \"hello\"\nprint(s[0])      # 'h'\nprint(s[1:4])    # 'ell'\nprint(len(s))    # 5\n```"}
                    ]
                },
                "story": "'Strings are character arrays,' Keeper reveals. 'Treat them similarly!'",
                "task": "Extract the first 3 characters of a string.",
                "starter_code": "s = \"algorithm\"\n# Get first 3 characters\nresult = ",
                "expected_output": "alg",
                "hints": ["s[0:3] or s[:3]"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Chain of Spirits",
        "topic": "Singly Linked Lists, Doubly Linked Lists",
        "description": "Learn node-based linear structures.",
        "story_intro": "Spirits link together in chains. Each knows only its neighbor!",
        "character": "Spirit Link",
        "character_quote": "Nodes point to nodes - that's the power of linked lists!",
        "icon": "link",
        "color": "#9b59b6",
        "missions": [
            {
                "id": 707,
                "title": "Singly Linked Lists",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Singly Linked List",
                    "overview": "Each node points to the next node.",
                    "sections": [
                        {"heading": "Structure", "content": "```python\nclass Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n```"},
                        {"heading": "Operations", "content": "- Access: O(n) - must traverse\n- Insert at head: O(1)\n- Insert at tail: O(n)\n- Delete: O(n)"}
                    ]
                },
                "story": "'Each spirit knows only the next,' Spirit Link explains.",
                "task": "Create a simple linked list with 3 nodes: 1 -> 2 -> 3.",
                "starter_code": "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\n# Create: 1 -> 2 -> 3\nhead = Node(1)\n",
                "expected_output": "1 -> 2 -> 3",
                "hints": ["head.next = Node(2), then head.next.next = Node(3)"]
            },
            {
                "id": 708,
                "title": "Doubly Linked Lists",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Doubly Linked List",
                    "overview": "Each node points to both next and previous.",
                    "sections": [
                        {"heading": "Structure", "content": "```python\nclass DNode:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n        self.prev = None\n```"},
                        {"heading": "Advantages", "content": "- Traverse both directions\n- O(1) delete if you have the node\n- More memory per node"}
                    ]
                },
                "story": "'Doubly linked spirits see both past and future,' Spirit Link reveals.",
                "task": "Create a doubly linked list node with prev and next pointers.",
                "starter_code": "class DNode:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n        self.prev = None\n\n# Create nodes and link them\n",
                "expected_output": None,
                "hints": ["Set both next and prev pointers"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Echo Chamber",
        "topic": "Stacks (LIFO), Queues (FIFO)",
        "description": "Learn ordered insertion and removal patterns.",
        "story_intro": "The Echo Chamber follows strict rules - first in or last in, you decide!",
        "character": "Echo Keeper",
        "character_quote": "LIFO or FIFO - order matters in the chamber!",
        "icon": "layers",
        "color": "#1abc9c",
        "missions": [
            {
                "id": 709,
                "title": "Stacks (LIFO)",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Stacks",
                    "overview": "Last In, First Out - like a stack of plates.",
                    "sections": [
                        {"heading": "Operations", "content": "- push(x): Add to top - O(1)\n- pop(): Remove from top - O(1)\n- peek(): View top - O(1)"},
                        {"heading": "Example", "content": "```python\nstack = []\nstack.append(1)  # push\nstack.append(2)\nstack.pop()      # returns 2\n```"}
                    ]
                },
                "story": "'Last in, first out,' Echo Keeper explains. 'Like stacking plates!'",
                "task": "Push 1, 2, 3 onto a stack, then pop once.",
                "starter_code": "stack = []\n# Push 1, 2, 3\n# Pop once\n",
                "expected_output": "[1, 2]",
                "hints": ["append() to push, pop() to remove"]
            },
            {
                "id": 710,
                "title": "Queues (FIFO)",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Queues",
                    "overview": "First In, First Out - like a line at a store.",
                    "sections": [
                        {"heading": "Operations", "content": "- enqueue(x): Add to back - O(1)\n- dequeue(): Remove from front - O(1)\n- Use collections.deque for efficiency"},
                        {"heading": "Example", "content": "```python\nfrom collections import deque\nq = deque()\nq.append(1)    # enqueue\nq.append(2)\nq.popleft()    # dequeue, returns 1\n```"}
                    ]
                },
                "story": "'First in, first out,' Echo Keeper teaches. 'Fair and orderly!'",
                "task": "Enqueue 1, 2, 3 then dequeue once.",
                "starter_code": "from collections import deque\nq = deque()\n# Enqueue 1, 2, 3\n# Dequeue once\n",
                "expected_output": "deque([2, 3])",
                "hints": ["append() to enqueue, popleft() to dequeue"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Recursive Mirror",
        "topic": "Recursion, Call Stacks, Backtracking",
        "description": "Master functions that call themselves.",
        "story_intro": "The Recursive Mirror reflects infinitely. Learn to control it!",
        "character": "Mirror Sage",
        "character_quote": "To understand recursion, first understand recursion!",
        "icon": "repeat",
        "color": "#e67e22",
        "missions": [
            {
                "id": 711,
                "title": "Recursion Basics",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Recursion",
                    "overview": "A function that calls itself with a smaller problem.",
                    "sections": [
                        {"heading": "Key Components", "content": "1. Base case: When to stop\n2. Recursive case: Call with smaller input"},
                        {"heading": "Example", "content": "```python\ndef factorial(n):\n    if n <= 1:      # base case\n        return 1\n    return n * factorial(n - 1)  # recursive\n```"}
                    ]
                },
                "story": "'The mirror reflects itself,' Sage explains. 'But must have an end!'",
                "task": "Write a recursive function to calculate factorial.",
                "starter_code": "def factorial(n):\n    # Base case\n    \n    # Recursive case\n    ",
                "expected_output": "120",
                "hints": ["if n <= 1: return 1"]
            },
            {
                "id": 712,
                "title": "Call Stacks",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Call Stack",
                    "overview": "How the computer tracks function calls.",
                    "sections": [
                        {"heading": "Stack Frames", "content": "Each function call adds a frame to the stack.\nWhen function returns, frame is removed."},
                        {"heading": "Stack Overflow", "content": "Too many recursive calls without base case leads to stack overflow!"}
                    ]
                },
                "story": "'Each call stacks upon the last,' Sage teaches. 'Don't overflow!'",
                "task": "Trace the call stack for factorial(3).",
                "starter_code": "# Trace factorial(3)\n# Call 1: factorial(3)\n# Call 2: ?\n# Call 3: ?\n# Returns: ?",
                "expected_output": "6",
                "hints": ["factorial(3) -> factorial(2) -> factorial(1)"]
            },
            {
                "id": 713,
                "title": "Backtracking",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Backtracking",
                    "overview": "Try a path, undo if it fails, try another.",
                    "sections": [
                        {"heading": "Pattern", "content": "1. Make a choice\n2. Recurse\n3. If fails, undo choice\n4. Try next option"},
                        {"heading": "Example", "content": "```python\ndef find_path(maze, x, y, path):\n    if is_goal(x, y):\n        return path\n    for dx, dy in directions:\n        path.append((x+dx, y+dy))\n        if find_path(maze, x+dx, y+dy, path):\n            return path\n        path.pop()  # backtrack\n    return None\n```"}
                    ]
                },
                "story": "'When one path fails,' Sage reveals, 'step back and try another!'",
                "task": "Understand backtracking by generating all subsets of [1, 2].",
                "starter_code": "def subsets(nums):\n    result = []\n    def backtrack(start, current):\n        result.append(current[:])\n        for i in range(start, len(nums)):\n            current.append(nums[i])\n            backtrack(i + 1, current)\n            current.pop()  # backtrack\n    backtrack(0, [])\n    return result\n\nprint(subsets([1, 2]))",
                "expected_output": "[[], [1], [1, 2], [2]]",
                "hints": ["Add element, recurse, remove element"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Sorted Valley",
        "topic": "Binary Search, Linear Search, Two-Pointers",
        "description": "Learn efficient searching techniques.",
        "story_intro": "In Sorted Valley, finding items is an art. Learn the fastest ways!",
        "character": "Seeker Swift",
        "character_quote": "Why check every item when you can halve the search?",
        "icon": "search",
        "color": "#2ecc71",
        "missions": [
            {
                "id": 714,
                "title": "Linear Search",
                "difficulty": "easy",
                "xp": 20,
                "lesson": {
                    "title": "Linear Search",
                    "overview": "Check each element one by one.",
                    "sections": [
                        {"heading": "Complexity", "content": "- Time: O(n)\n- Works on unsorted data"},
                        {"heading": "Example", "content": "```python\ndef linear_search(arr, target):\n    for i, x in enumerate(arr):\n        if x == target:\n            return i\n    return -1\n```"}
                    ]
                },
                "story": "'The simplest search,' Seeker explains. 'Check one by one!'",
                "task": "Implement linear search to find target 30 in [10, 20, 30, 40].",
                "starter_code": "def linear_search(arr, target):\n    # Your code\n    pass\n\nprint(linear_search([10, 20, 30, 40], 30))",
                "expected_output": "2",
                "hints": ["Loop and compare each element"]
            },
            {
                "id": 715,
                "title": "Binary Search",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Binary Search",
                    "overview": "Halve the search space each step.",
                    "sections": [
                        {"heading": "Requirements", "content": "- Array must be SORTED\n- Time: O(log n)"},
                        {"heading": "Algorithm", "content": "```python\ndef binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n```"}
                    ]
                },
                "story": "'Halve the search each time,' Seeker teaches. 'Logarithmic speed!'",
                "task": "Implement binary search on sorted array [1, 3, 5, 7, 9].",
                "starter_code": "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    # Your code\n    pass\n\nprint(binary_search([1, 3, 5, 7, 9], 7))",
                "expected_output": "3",
                "hints": ["Compare mid, adjust left or right"]
            },
            {
                "id": 716,
                "title": "Two-Pointers",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Two-Pointer Technique",
                    "overview": "Use two pointers to solve problems efficiently.",
                    "sections": [
                        {"heading": "Common Patterns", "content": "- Start/End pointers moving inward\n- Fast/Slow pointers\n- Sliding window"},
                        {"heading": "Example", "content": "```python\n# Two Sum in sorted array\ndef two_sum(arr, target):\n    left, right = 0, len(arr) - 1\n    while left < right:\n        s = arr[left] + arr[right]\n        if s == target:\n            return [left, right]\n        elif s < target:\n            left += 1\n        else:\n            right -= 1\n```"}
                    ]
                },
                "story": "'Two pointers work together,' Seeker reveals. 'Efficient and elegant!'",
                "task": "Use two pointers to check if a string is a palindrome.",
                "starter_code": "def is_palindrome(s):\n    left, right = 0, len(s) - 1\n    # Your code\n    pass\n\nprint(is_palindrome(\"racecar\"))",
                "expected_output": "True",
                "hints": ["Compare s[left] and s[right], move inward"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Sacred World Tree",
        "topic": "Binary Trees, BST, Traversals (Pre/In/Post)",
        "description": "Learn hierarchical tree structures.",
        "story_intro": "The Sacred World Tree branches infinitely. Learn to navigate it!",
        "character": "Tree Elder",
        "character_quote": "From root to leaves, every path tells a story!",
        "icon": "git-branch",
        "color": "#27ae60",
        "missions": [
            {
                "id": 717,
                "title": "Binary Trees",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Binary Trees",
                    "overview": "Each node has at most two children.",
                    "sections": [
                        {"heading": "Structure", "content": "```python\nclass TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n```"},
                        {"heading": "Terms", "content": "- Root: Top node\n- Leaf: Node with no children\n- Height: Longest path to leaf"}
                    ]
                },
                "story": "'Each branch splits in two,' Elder explains. 'Left and right!'",
                "task": "Create a binary tree with root 1, left child 2, right child 3.",
                "starter_code": "class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\n# Create tree: 1 -> (2, 3)\nroot = TreeNode(1)\n",
                "expected_output": "1 -> 2, 3",
                "hints": ["root.left = TreeNode(2)"]
            },
            {
                "id": 718,
                "title": "Binary Search Tree",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "BST",
                    "overview": "Left < Root < Right - always ordered.",
                    "sections": [
                        {"heading": "BST Property", "content": "- All left descendants < node\n- All right descendants > node"},
                        {"heading": "Operations", "content": "- Search: O(log n) average\n- Insert: O(log n) average\n- O(n) worst case if unbalanced"}
                    ]
                },
                "story": "'In a BST, order is maintained,' Elder teaches. 'Left is less, right is more!'",
                "task": "Insert value 25 into a BST with root 20, left 10, right 30.",
                "starter_code": "# BST: 20 -> (10, 30)\n# Where does 25 go?\n# Answer: ",
                "expected_output": "Left child of 30",
                "hints": ["25 > 20 (go right), 25 < 30 (go left)"]
            },
            {
                "id": 719,
                "title": "Tree Traversals - Pre/In",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Pre-order & In-order",
                    "overview": "Different ways to visit all nodes.",
                    "sections": [
                        {"heading": "Pre-order", "content": "Root -> Left -> Right\n```python\ndef preorder(node):\n    if node:\n        print(node.val)\n        preorder(node.left)\n        preorder(node.right)\n```"},
                        {"heading": "In-order", "content": "Left -> Root -> Right\nFor BST: gives sorted order!"}
                    ]
                },
                "story": "'Pre-order visits root first,' Elder explains. 'In-order visits root in middle!'",
                "task": "What is the in-order traversal of BST: 2 -> (1, 3)?",
                "starter_code": "# Tree: 2 -> (1, 3)\n# In-order: Left, Root, Right\n# Answer: ",
                "expected_output": "1, 2, 3",
                "hints": ["In-order gives sorted order for BST"]
            },
            {
                "id": 720,
                "title": "Tree Traversals - Post",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Post-order Traversal",
                    "overview": "Visit children before parent.",
                    "sections": [
                        {"heading": "Post-order", "content": "Left -> Right -> Root\n```python\ndef postorder(node):\n    if node:\n        postorder(node.left)\n        postorder(node.right)\n        print(node.val)\n```"},
                        {"heading": "Use Case", "content": "Useful for deleting trees (delete children first)"}
                    ]
                },
                "story": "'Post-order saves root for last,' Elder reveals.",
                "task": "What is the post-order traversal of tree: 1 -> (2, 3)?",
                "starter_code": "# Tree: 1 -> (2, 3)\n# Post-order: Left, Right, Root\n# Answer: ",
                "expected_output": "2, 3, 1",
                "hints": ["Visit left, then right, then root"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Priority Peak",
        "topic": "Min Heaps, Max Heaps, Priority Queues",
        "description": "Learn heap-based priority structures.",
        "story_intro": "At Priority Peak, the most important rises to the top!",
        "character": "Peak Master",
        "character_quote": "Heaps keep priorities in perfect order!",
        "icon": "arrow-up",
        "color": "#f39c12",
        "missions": [
            {
                "id": 721,
                "title": "Min Heaps",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Min Heap",
                    "overview": "Parent is always smaller than children.",
                    "sections": [
                        {"heading": "Properties", "content": "- Complete binary tree\n- Min element at root\n- O(log n) insert/delete\n- O(1) get min"},
                        {"heading": "Python heapq", "content": "```python\nimport heapq\nh = []\nheapq.heappush(h, 3)\nheapq.heappush(h, 1)\nprint(heapq.heappop(h))  # 1\n```"}
                    ]
                },
                "story": "'The smallest rises to top,' Peak Master explains.",
                "task": "Use heapq to get the minimum of [5, 2, 8, 1].",
                "starter_code": "import heapq\nnums = [5, 2, 8, 1]\nheapq.heapify(nums)\nprint(heapq.heappop(nums))",
                "expected_output": "1",
                "hints": ["heapify turns list into min heap"]
            },
            {
                "id": 722,
                "title": "Max Heaps",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Max Heap",
                    "overview": "Parent is always larger than children.",
                    "sections": [
                        {"heading": "Python Trick", "content": "Python only has min heap. For max heap, negate values!"},
                        {"heading": "Example", "content": "```python\nimport heapq\nh = []\nheapq.heappush(h, -5)  # negate\nheapq.heappush(h, -3)\nmax_val = -heapq.heappop(h)  # 5\n```"}
                    ]
                },
                "story": "'For max heap, flip the values,' Peak Master teaches.",
                "task": "Get the maximum of [3, 7, 2, 9] using a max heap.",
                "starter_code": "import heapq\nnums = [3, 7, 2, 9]\n# Negate for max heap\nh = [-x for x in nums]\nheapq.heapify(h)\nprint(-heapq.heappop(h))",
                "expected_output": "9",
                "hints": ["Negate values, use min heap, negate result"]
            },
            {
                "id": 723,
                "title": "Priority Queues",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Priority Queue",
                    "overview": "Queue where highest priority is served first.",
                    "sections": [
                        {"heading": "Implementation", "content": "Typically implemented using heaps."},
                        {"heading": "Example", "content": "```python\nimport heapq\npq = []\nheapq.heappush(pq, (2, 'low'))\nheapq.heappush(pq, (1, 'high'))\nprint(heapq.heappop(pq))  # (1, 'high')\n```"}
                    ]
                },
                "story": "'Priority queues serve the most urgent first,' Peak Master reveals.",
                "task": "Create a priority queue and process highest priority task.",
                "starter_code": "import heapq\ntasks = []\nheapq.heappush(tasks, (3, 'email'))\nheapq.heappush(tasks, (1, 'urgent'))\nheapq.heappush(tasks, (2, 'meeting'))\nprint(heapq.heappop(tasks))",
                "expected_output": "(1, 'urgent')",
                "hints": ["Lower number = higher priority"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Nexus of Paths",
        "topic": "Adjacency Lists, Graph Basics",
        "description": "Learn to represent connected networks.",
        "story_intro": "The Nexus connects all realms. Learn to map these connections!",
        "character": "Nexus Weaver",
        "character_quote": "Nodes and edges form the fabric of networks!",
        "icon": "share-2",
        "color": "#8e44ad",
        "missions": [
            {
                "id": 724,
                "title": "Graph Basics",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Graph Fundamentals",
                    "overview": "Graphs model relationships between objects.",
                    "sections": [
                        {"heading": "Components", "content": "- Vertices (nodes): Objects\n- Edges: Connections between vertices"},
                        {"heading": "Types", "content": "- Directed: A -> B (one-way)\n- Undirected: A -- B (two-way)\n- Weighted: Edges have costs"}
                    ]
                },
                "story": "'Graphs are everywhere,' Weaver explains. 'Social networks, maps, the web!'",
                "task": "Identify vertices and edges in a friend network: A-B, B-C, A-C.",
                "starter_code": "# Friend network: A-B, B-C, A-C\n# Vertices: \n# Edges: \n# Type: ",
                "expected_output": "Vertices: A, B, C. Edges: 3. Type: Undirected",
                "hints": ["Count unique nodes and connections"]
            },
            {
                "id": 725,
                "title": "Adjacency Lists",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Adjacency List",
                    "overview": "Store graph as dictionary of neighbors.",
                    "sections": [
                        {"heading": "Structure", "content": "```python\ngraph = {\n    'A': ['B', 'C'],\n    'B': ['A', 'C'],\n    'C': ['A', 'B']\n}\n```"},
                        {"heading": "Advantages", "content": "- Space efficient for sparse graphs\n- Easy to iterate neighbors"}
                    ]
                },
                "story": "'Store each node's neighbors,' Weaver teaches.",
                "task": "Create an adjacency list for: A-B, B-C, C-D.",
                "starter_code": "# Graph: A-B, B-C, C-D (undirected)\ngraph = {\n    'A': [],\n    'B': [],\n    'C': [],\n    'D': []\n}\n# Fill in the neighbors",
                "expected_output": "{'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C']}",
                "hints": ["Add both directions for undirected"]
            }
        ]
    },
    {
        "id": 10,
        "name": "The Flow of Many",
        "topic": "Breadth-First (BFS), Depth-First (DFS)",
        "description": "Master graph traversal algorithms.",
        "story_intro": "Two paths through the nexus: wide or deep. Choose wisely!",
        "character": "Path Walker",
        "character_quote": "BFS explores layer by layer, DFS dives deep!",
        "icon": "navigation",
        "color": "#16a085",
        "missions": [
            {
                "id": 726,
                "title": "Breadth-First Search",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "BFS",
                    "overview": "Explore all neighbors before going deeper.",
                    "sections": [
                        {"heading": "Algorithm", "content": "1. Start at root, add to queue\n2. While queue not empty:\n   - Dequeue node\n   - Visit neighbors\n   - Add unvisited to queue"},
                        {"heading": "Code", "content": "```python\nfrom collections import deque\ndef bfs(graph, start):\n    visited = set([start])\n    queue = deque([start])\n    while queue:\n        node = queue.popleft()\n        print(node)\n        for neighbor in graph[node]:\n            if neighbor not in visited:\n                visited.add(neighbor)\n                queue.append(neighbor)\n```"}
                    ]
                },
                "story": "'BFS explores level by level,' Walker explains.",
                "task": "Trace BFS from A in graph: A-B, A-C, B-D.",
                "starter_code": "# Graph: A-B, A-C, B-D\n# BFS from A visits: ",
                "expected_output": "A, B, C, D",
                "hints": ["Visit A, then its neighbors B,C, then D"]
            },
            {
                "id": 727,
                "title": "Depth-First Search",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "DFS",
                    "overview": "Go as deep as possible before backtracking.",
                    "sections": [
                        {"heading": "Algorithm", "content": "1. Start at root\n2. Visit node, mark visited\n3. Recurse on unvisited neighbors\n4. Backtrack when stuck"},
                        {"heading": "Code", "content": "```python\ndef dfs(graph, node, visited=None):\n    if visited is None:\n        visited = set()\n    visited.add(node)\n    print(node)\n    for neighbor in graph[node]:\n        if neighbor not in visited:\n            dfs(graph, neighbor, visited)\n```"}
                    ]
                },
                "story": "'DFS dives deep first,' Walker teaches. 'Then backtracks!'",
                "task": "Trace DFS from A in graph: A-B, A-C, B-D.",
                "starter_code": "# Graph: A-B, A-C, B-D\n# DFS from A visits: ",
                "expected_output": "A, B, D, C",
                "hints": ["Go A->B->D, backtrack, then C"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Fragmented Memory",
        "topic": "Memoization, Tabulation, Knapsack",
        "description": "Learn dynamic programming techniques.",
        "story_intro": "Memory fragments hold the key. Reuse computed results!",
        "character": "Memory Keeper",
        "character_quote": "Don't compute twice what you've solved once!",
        "icon": "database",
        "color": "#c0392b",
        "missions": [
            {
                "id": 728,
                "title": "Memoization",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Memoization",
                    "overview": "Cache results of function calls.",
                    "sections": [
                        {"heading": "Top-Down DP", "content": "Store results in a dictionary as you compute."},
                        {"heading": "Example", "content": "```python\ndef fib(n, memo={}):\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fib(n-1, memo) + fib(n-2, memo)\n    return memo[n]\n```"}
                    ]
                },
                "story": "'Remember what you've computed,' Keeper explains.",
                "task": "Implement memoized Fibonacci.",
                "starter_code": "def fib(n, memo={}):\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fib(n-1, memo) + fib(n-2, memo)\n    return memo[n]\n\nprint(fib(10))",
                "expected_output": "55",
                "hints": ["Store results in memo dict"]
            },
            {
                "id": 729,
                "title": "Tabulation",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Tabulation",
                    "overview": "Build solution bottom-up in a table.",
                    "sections": [
                        {"heading": "Bottom-Up DP", "content": "Start from base cases, build up to answer."},
                        {"heading": "Example", "content": "```python\ndef fib_tab(n):\n    if n <= 1:\n        return n\n    dp = [0] * (n + 1)\n    dp[1] = 1\n    for i in range(2, n + 1):\n        dp[i] = dp[i-1] + dp[i-2]\n    return dp[n]\n```"}
                    ]
                },
                "story": "'Build from the ground up,' Keeper teaches.",
                "task": "Implement tabulated Fibonacci.",
                "starter_code": "def fib_tab(n):\n    if n <= 1:\n        return n\n    dp = [0] * (n + 1)\n    dp[1] = 1\n    for i in range(2, n + 1):\n        dp[i] = dp[i-1] + dp[i-2]\n    return dp[n]\n\nprint(fib_tab(10))",
                "expected_output": "55",
                "hints": ["Build dp array from 0 to n"]
            },
            {
                "id": 730,
                "title": "Knapsack Problem",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "0/1 Knapsack",
                    "overview": "Classic DP problem: maximize value with weight limit.",
                    "sections": [
                        {"heading": "Problem", "content": "Given items with weights and values, maximize value without exceeding capacity."},
                        {"heading": "DP Approach", "content": "```python\ndef knapsack(W, weights, values):\n    n = len(weights)\n    dp = [[0] * (W + 1) for _ in range(n + 1)]\n    for i in range(1, n + 1):\n        for w in range(W + 1):\n            if weights[i-1] <= w:\n                dp[i][w] = max(dp[i-1][w], \n                              values[i-1] + dp[i-1][w-weights[i-1]])\n            else:\n                dp[i][w] = dp[i-1][w]\n    return dp[n][W]\n```"}
                    ]
                },
                "story": "'Choose wisely,' Keeper advises. 'Maximize value within limits!'",
                "task": "Solve: capacity=5, weights=[2,3,4], values=[3,4,5].",
                "starter_code": "# Knapsack: capacity=5\n# Items: weight=[2,3,4], value=[3,4,5]\n# Max value = ?",
                "expected_output": "7",
                "hints": ["Take items with weights 2 and 3 for values 3+4=7"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Final Trial",
        "topic": "Hard Mixed Problems, System Design Basics",
        "description": "Face the ultimate DSA challenge.",
        "story_intro": "The Final Trial tests everything you've learned. Are you ready?",
        "character": "Grand Arbiter",
        "character_quote": "Only the worthy pass the Final Trial!",
        "icon": "trophy",
        "color": "#ffd700",
        "missions": [
            {
                "id": 731,
                "title": "Mixed Challenge",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "Problem Solving Strategy",
                    "overview": "Combine multiple techniques to solve complex problems.",
                    "sections": [
                        {"heading": "Steps", "content": "1. Understand the problem\n2. Identify data structures needed\n3. Consider time/space trade-offs\n4. Start with brute force, optimize"},
                        {"heading": "Common Patterns", "content": "- Two pointers + sorting\n- BFS/DFS + memoization\n- Heap + sliding window"}
                    ]
                },
                "story": "'Combine your skills,' Arbiter challenges. 'Solve this!'",
                "task": "Find the kth largest element in an unsorted array.",
                "starter_code": "import heapq\n\ndef find_kth_largest(nums, k):\n    # Use a min heap of size k\n    pass\n\nprint(find_kth_largest([3, 2, 1, 5, 6, 4], 2))",
                "expected_output": "5",
                "hints": ["Min heap of size k, pop smallest, heap top is answer"]
            },
            {
                "id": 732,
                "title": "System Design Basics",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "System Design Introduction",
                    "overview": "Think about large-scale systems.",
                    "sections": [
                        {"heading": "Key Concepts", "content": "- Scalability: Handle growth\n- Load Balancing: Distribute traffic\n- Caching: Speed up reads\n- Database: SQL vs NoSQL"},
                        {"heading": "Design Process", "content": "1. Clarify requirements\n2. Estimate scale\n3. Define API\n4. Design data model\n5. High-level architecture\n6. Deep dive on components"}
                    ]
                },
                "story": "'Think big,' Arbiter instructs. 'Design for scale!'",
                "task": "Design a URL shortener: describe key components.",
                "starter_code": "# URL Shortener System Design\n# Components needed:\n# 1. \n# 2. \n# 3. ",
                "expected_output": None,
                "hints": ["Database, Hash function, Cache, Load balancer"]
            }
        ]
    }
]

REACT_ARCS = [
    {
        "id": 1,
        "name": "Portal of JSX",
        "topic": "JSX, Rendering Elements",
        "description": "Learn the magical syntax that blends HTML and JavaScript.",
        "story_intro": "Welcome to the Portal of Interfaces! Here, we craft magical windows for users to interact with the realm.",
        "character": "Interface Weaver",
        "character_quote": "JSX is the spell that creates what users see!",
        "icon": "code",
        "color": "#61dafb",
        "missions": [
            {
                "id": 801,
                "title": "JSX Syntax",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "JSX - JavaScript XML",
                    "overview": "JSX lets you write HTML-like syntax in JavaScript.",
                    "sections": [
                        {"heading": "What is JSX?", "content": "JSX is a syntax extension that looks like HTML but compiles to JavaScript function calls."},
                        {"heading": "Example", "content": "```jsx\nconst element = <h1>Hello, World!</h1>;\n\n// JSX with expressions\nconst name = 'Coder';\nconst greeting = <h1>Hello, {name}!</h1>;\n```"}
                    ]
                },
                "story": "'JSX looks like HTML but has the power of JavaScript,' Interface Weaver explains.",
                "task": "Create a JSX element that displays 'Welcome to React!'",
                "starter_code": "// Create a JSX heading element\nconst element = ",
                "expected_output": "<h1>Welcome to React!</h1>",
                "hints": ["Use angle brackets like HTML: <h1>text</h1>"]
            },
            {
                "id": 802,
                "title": "Rendering Elements",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Rendering to the DOM",
                    "overview": "React elements are rendered to a root DOM node.",
                    "sections": [
                        {"heading": "ReactDOM.render", "content": "Elements are rendered using ReactDOM.createRoot and root.render()."},
                        {"heading": "Example", "content": "```jsx\nimport { createRoot } from 'react-dom/client';\n\nconst root = createRoot(document.getElementById('root'));\nroot.render(<h1>Hello!</h1>);\n```"}
                    ]
                },
                "story": "'Elements appear in the DOM through rendering,' Weaver teaches.",
                "task": "Write the code to render a heading to the root element.",
                "starter_code": "// Render <h1>My App</h1> to the root\n",
                "expected_output": "root.render(<h1>My App</h1>)",
                "hints": ["Use root.render() with your JSX element"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Component Village",
        "topic": "Functional Components, Nesting",
        "description": "Build reusable UI pieces as components.",
        "story_intro": "In Component Village, every building block is a component that can be reused!",
        "character": "Builder Sage",
        "character_quote": "Components are the building blocks of React interfaces!",
        "icon": "box",
        "color": "#764abc",
        "missions": [
            {
                "id": 803,
                "title": "Functional Components",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Function Components",
                    "overview": "Components are JavaScript functions that return JSX.",
                    "sections": [
                        {"heading": "Creating Components", "content": "A component is a function that starts with a capital letter and returns JSX."},
                        {"heading": "Example", "content": "```jsx\nfunction Welcome() {\n  return <h1>Welcome!</h1>;\n}\n\n// Using the component\n<Welcome />\n```"}
                    ]
                },
                "story": "'Every component is a function that returns UI,' Builder Sage explains.",
                "task": "Create a Greeting component that returns 'Hello, Coder!'",
                "starter_code": "function Greeting() {\n  // Return a greeting\n}",
                "expected_output": "Hello, Coder!",
                "hints": ["Return JSX: return <p>Hello, Coder!</p>"]
            },
            {
                "id": 804,
                "title": "Nesting Components",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Component Composition",
                    "overview": "Components can contain other components.",
                    "sections": [
                        {"heading": "Nesting", "content": "Use components inside other components to build complex UIs."},
                        {"heading": "Example", "content": "```jsx\nfunction Header() {\n  return <h1>My App</h1>;\n}\n\nfunction App() {\n  return (\n    <div>\n      <Header />\n      <p>Content here</p>\n    </div>\n  );\n}\n```"}
                    ]
                },
                "story": "'Components inside components - that's composition!' Builder Sage reveals.",
                "task": "Create an App component that nests a Header and Footer component.",
                "starter_code": "function Header() { return <h1>Header</h1>; }\nfunction Footer() { return <p>Footer</p>; }\n\nfunction App() {\n  // Nest Header and Footer\n}",
                "expected_output": "<div><Header /><Footer /></div>",
                "hints": ["Return a div containing both components"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Prop Bridge",
        "topic": "Props, Destructuring, Children",
        "description": "Pass data between components using props.",
        "story_intro": "The Prop Bridge connects components, allowing data to flow between them!",
        "character": "Data Courier",
        "character_quote": "Props carry data from parent to child!",
        "icon": "arrow-right",
        "color": "#ff6b6b",
        "missions": [
            {
                "id": 805,
                "title": "Props Basics",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Passing Props",
                    "overview": "Props are how data flows from parent to child components.",
                    "sections": [
                        {"heading": "Props", "content": "Props are passed like HTML attributes and received as a function parameter."},
                        {"heading": "Example", "content": "```jsx\nfunction Welcome(props) {\n  return <h1>Hello, {props.name}!</h1>;\n}\n\n<Welcome name=\"Sakura\" />\n```"}
                    ]
                },
                "story": "'Props pass data down the component tree,' Data Courier explains.",
                "task": "Create a component that accepts a 'name' prop and displays it.",
                "starter_code": "function Hello(props) {\n  // Use props.name\n}\n\n// Usage: <Hello name=\"React\" />",
                "expected_output": "Hello, React!",
                "hints": ["Access with props.name inside curly braces"]
            },
            {
                "id": 806,
                "title": "Destructuring Props",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Props Destructuring",
                    "overview": "Destructure props for cleaner code.",
                    "sections": [
                        {"heading": "Destructuring", "content": "Extract props directly in the function parameter."},
                        {"heading": "Example", "content": "```jsx\nfunction Welcome({ name, age }) {\n  return <p>{name} is {age} years old</p>;\n}\n```"}
                    ]
                },
                "story": "'Destructure for cleaner, more readable code,' Courier teaches.",
                "task": "Rewrite a component using destructured props.",
                "starter_code": "// Destructure name and level from props\nfunction Player({ /* destructure here */ }) {\n  return <p>{name} - Level {level}</p>;\n}",
                "expected_output": "Sakura - Level 5",
                "hints": ["{ name, level } in the parameter"]
            },
            {
                "id": 807,
                "title": "Children Prop",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "The Children Prop",
                    "overview": "props.children contains nested content.",
                    "sections": [
                        {"heading": "Children", "content": "Content between opening and closing tags is passed as children."},
                        {"heading": "Example", "content": "```jsx\nfunction Card({ children }) {\n  return <div className=\"card\">{children}</div>;\n}\n\n<Card>\n  <h2>Title</h2>\n  <p>Content</p>\n</Card>\n```"}
                    ]
                },
                "story": "'Children lets you wrap content flexibly,' Courier reveals.",
                "task": "Create a Container component that renders its children.",
                "starter_code": "function Container({ children }) {\n  // Wrap children in a div\n}",
                "expected_output": "<div>{children}</div>",
                "hints": ["Return <div>{children}</div>"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Spark of State",
        "topic": "useState Hook, Event Handling",
        "description": "Add interactivity with state and events.",
        "story_intro": "The Spark of State brings your components to life with dynamic data!",
        "character": "State Guardian",
        "character_quote": "State makes your UI dynamic and responsive!",
        "icon": "zap",
        "color": "#feca57",
        "missions": [
            {
                "id": 808,
                "title": "useState Hook",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Managing State with useState",
                    "overview": "useState lets functional components have state.",
                    "sections": [
                        {"heading": "useState", "content": "Returns [currentValue, setterFunction]. State changes trigger re-renders."},
                        {"heading": "Example", "content": "```jsx\nimport { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  return <p>Count: {count}</p>;\n}\n```"}
                    ]
                },
                "story": "'useState is the hook that gives components memory,' State Guardian explains.",
                "task": "Create a counter with useState that starts at 0.",
                "starter_code": "import { useState } from 'react';\n\nfunction Counter() {\n  // Create count state\n  return <p>Count: {count}</p>;\n}",
                "expected_output": "Count: 0",
                "hints": ["const [count, setCount] = useState(0)"]
            },
            {
                "id": 809,
                "title": "Event Handling",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Handling Events",
                    "overview": "React events use camelCase and pass functions.",
                    "sections": [
                        {"heading": "Events", "content": "Use onClick, onChange, etc. Pass a function reference."},
                        {"heading": "Example", "content": "```jsx\nfunction Button() {\n  const [count, setCount] = useState(0);\n  \n  return (\n    <button onClick={() => setCount(count + 1)}>\n      Clicked {count} times\n    </button>\n  );\n}\n```"}
                    ]
                },
                "story": "'Events connect user actions to state changes,' Guardian teaches.",
                "task": "Add an onClick handler that increments a counter.",
                "starter_code": "function Counter() {\n  const [count, setCount] = useState(0);\n  \n  return (\n    <button onClick={/* handler */}>\n      {count}\n    </button>\n  );\n}",
                "expected_output": "onClick={() => setCount(count + 1)}",
                "hints": ["Arrow function that calls setCount"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Mirage of Render",
        "topic": "Conditional Rendering, Ternary Operators",
        "description": "Show different UI based on conditions.",
        "story_intro": "The Mirage of Render shows different views based on the state of reality!",
        "character": "Vision Keeper",
        "character_quote": "What you see depends on what is true!",
        "icon": "eye",
        "color": "#a55eea",
        "missions": [
            {
                "id": 810,
                "title": "Conditional Rendering",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Rendering Conditionally",
                    "overview": "Show different elements based on conditions.",
                    "sections": [
                        {"heading": "If Statements", "content": "Use if statements or && for conditional rendering."},
                        {"heading": "Example", "content": "```jsx\nfunction Greeting({ isLoggedIn }) {\n  if (isLoggedIn) {\n    return <h1>Welcome back!</h1>;\n  }\n  return <h1>Please log in.</h1>;\n}\n```"}
                    ]
                },
                "story": "'Render what matches the current truth,' Vision Keeper explains.",
                "task": "Render 'Loading...' if isLoading is true, else render 'Data loaded'.",
                "starter_code": "function Status({ isLoading }) {\n  // Conditional render\n}",
                "expected_output": "Loading... or Data loaded",
                "hints": ["if (isLoading) return <p>Loading...</p>"]
            },
            {
                "id": 811,
                "title": "Ternary Operators",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Inline Conditionals",
                    "overview": "Use ternary operators for inline conditions.",
                    "sections": [
                        {"heading": "Ternary", "content": "condition ? trueValue : falseValue"},
                        {"heading": "Example", "content": "```jsx\nfunction Status({ isOnline }) {\n  return (\n    <span>{isOnline ? 'Online' : 'Offline'}</span>\n  );\n}\n```"}
                    ]
                },
                "story": "'Ternary gives you inline power,' Vision Keeper teaches.",
                "task": "Use a ternary to show 'Active' or 'Inactive' based on isActive.",
                "starter_code": "function Badge({ isActive }) {\n  return <span>{/* ternary here */}</span>;\n}",
                "expected_output": "isActive ? 'Active' : 'Inactive'",
                "hints": ["condition ? 'Active' : 'Inactive'"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Magic List",
        "topic": "map(), key props, Filtering Lists",
        "description": "Render arrays of data dynamically.",
        "story_intro": "The Magic List conjures many elements from arrays of data!",
        "character": "List Mage",
        "character_quote": "Transform arrays into UI with the power of map!",
        "icon": "list",
        "color": "#00cec9",
        "missions": [
            {
                "id": 812,
                "title": "Using map()",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Rendering Lists with map",
                    "overview": "Use map() to render arrays as JSX elements.",
                    "sections": [
                        {"heading": "map()", "content": "Transform each array item into a JSX element."},
                        {"heading": "Example", "content": "```jsx\nconst items = ['Apple', 'Banana', 'Cherry'];\n\nfunction List() {\n  return (\n    <ul>\n      {items.map(item => <li>{item}</li>)}\n    </ul>\n  );\n}\n```"}
                    ]
                },
                "story": "'map transforms data into visible elements,' List Mage explains.",
                "task": "Render an array of names as list items.",
                "starter_code": "const names = ['Sakura', 'Yuki', 'Hana'];\n\nfunction NameList() {\n  return (\n    <ul>\n      {/* map names to li elements */}\n    </ul>\n  );\n}",
                "expected_output": "<li>Sakura</li><li>Yuki</li><li>Hana</li>",
                "hints": ["names.map(name => <li>{name}</li>)"]
            },
            {
                "id": 813,
                "title": "Key Props",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Keys in Lists",
                    "overview": "Keys help React identify which items changed.",
                    "sections": [
                        {"heading": "Why Keys?", "content": "Keys give elements a stable identity for efficient updates."},
                        {"heading": "Example", "content": "```jsx\n{items.map(item => (\n  <li key={item.id}>{item.name}</li>\n))}\n```"}
                    ]
                },
                "story": "'Keys identify each element uniquely,' List Mage teaches.",
                "task": "Add keys to a list of items with id properties.",
                "starter_code": "const users = [{id: 1, name: 'A'}, {id: 2, name: 'B'}];\n\n{users.map(user => (\n  <li /* add key */>{user.name}</li>\n))}",
                "expected_output": "key={user.id}",
                "hints": ["key={user.id} on the li element"]
            },
            {
                "id": 814,
                "title": "Filtering Lists",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Filter and Render",
                    "overview": "Combine filter() with map() for conditional lists.",
                    "sections": [
                        {"heading": "Filter + Map", "content": "First filter the array, then map the results."},
                        {"heading": "Example", "content": "```jsx\nconst items = [{name: 'A', active: true}, {name: 'B', active: false}];\n\n{items.filter(i => i.active).map(i => <li key={i.name}>{i.name}</li>)}\n```"}
                    ]
                },
                "story": "'Filter before mapping to show only what matters,' List Mage reveals.",
                "task": "Filter and display only completed tasks.",
                "starter_code": "const tasks = [\n  {id: 1, text: 'Learn React', done: true},\n  {id: 2, text: 'Build App', done: false}\n];\n\n// Filter done tasks, then map",
                "expected_output": "Learn React",
                "hints": ["tasks.filter(t => t.done).map(...)"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Ripple Effect",
        "topic": "useEffect Hook, API Fetching",
        "description": "Handle side effects and external data.",
        "story_intro": "The Ripple Effect connects your components to the outside world!",
        "character": "Effect Oracle",
        "character_quote": "Side effects ripple out from your components!",
        "icon": "activity",
        "color": "#6c5ce7",
        "missions": [
            {
                "id": 815,
                "title": "useEffect Hook",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Side Effects with useEffect",
                    "overview": "useEffect runs code after render for side effects.",
                    "sections": [
                        {"heading": "useEffect", "content": "Runs after every render by default. Use dependency array to control when."},
                        {"heading": "Example", "content": "```jsx\nimport { useEffect, useState } from 'react';\n\nfunction Timer() {\n  const [seconds, setSeconds] = useState(0);\n  \n  useEffect(() => {\n    document.title = `${seconds} seconds`;\n  }, [seconds]);\n  \n  return <p>{seconds}s</p>;\n}\n```"}
                    ]
                },
                "story": "'useEffect handles what happens after render,' Effect Oracle explains.",
                "task": "Use useEffect to log 'Component mounted' on first render.",
                "starter_code": "import { useEffect } from 'react';\n\nfunction App() {\n  // Log on mount\n  \n  return <p>Hello</p>;\n}",
                "expected_output": "useEffect(() => { console.log('Component mounted'); }, [])",
                "hints": ["Empty dependency array [] runs once on mount"]
            },
            {
                "id": 816,
                "title": "API Fetching",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Fetching Data",
                    "overview": "Use useEffect to fetch data from APIs.",
                    "sections": [
                        {"heading": "Fetch Pattern", "content": "Fetch in useEffect, store in state."},
                        {"heading": "Example", "content": "```jsx\nfunction Users() {\n  const [users, setUsers] = useState([]);\n  \n  useEffect(() => {\n    fetch('/api/users')\n      .then(res => res.json())\n      .then(data => setUsers(data));\n  }, []);\n  \n  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;\n}\n```"}
                    ]
                },
                "story": "'Fetch data from the realm beyond,' Effect Oracle teaches.",
                "task": "Fetch posts from an API and store in state.",
                "starter_code": "function Posts() {\n  const [posts, setPosts] = useState([]);\n  \n  useEffect(() => {\n    // Fetch from '/api/posts'\n  }, []);\n  \n  return <div>{posts.length} posts</div>;\n}",
                "expected_output": "fetch, then, setPosts",
                "hints": ["fetch('/api/posts').then(res => res.json()).then(setPosts)"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Reference Scroll",
        "topic": "useRef Hook, Accessing Elements",
        "description": "Access DOM elements directly.",
        "story_intro": "The Reference Scroll gives you direct access to DOM elements!",
        "character": "Ref Keeper",
        "character_quote": "References let you touch the DOM directly!",
        "icon": "target",
        "color": "#fd79a8",
        "missions": [
            {
                "id": 817,
                "title": "useRef Hook",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Creating References",
                    "overview": "useRef creates a mutable reference that persists across renders.",
                    "sections": [
                        {"heading": "useRef", "content": "Returns an object with a .current property."},
                        {"heading": "Example", "content": "```jsx\nimport { useRef } from 'react';\n\nfunction Counter() {\n  const renderCount = useRef(0);\n  renderCount.current++;\n  return <p>Renders: {renderCount.current}</p>;\n}\n```"}
                    ]
                },
                "story": "'useRef holds values without causing re-renders,' Ref Keeper explains.",
                "task": "Create a ref to track how many times a button was clicked.",
                "starter_code": "import { useRef } from 'react';\n\nfunction ClickTracker() {\n  const clicks = useRef(0);\n  \n  return <button onClick={() => /* increment */}>Clicks: {clicks.current}</button>;\n}",
                "expected_output": "clicks.current++",
                "hints": ["clicks.current++ in the onClick handler"]
            },
            {
                "id": 818,
                "title": "Accessing DOM Elements",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "DOM References",
                    "overview": "Attach refs to elements with the ref attribute.",
                    "sections": [
                        {"heading": "DOM Access", "content": "Use ref attribute to get direct DOM access."},
                        {"heading": "Example", "content": "```jsx\nfunction FocusInput() {\n  const inputRef = useRef(null);\n  \n  return (\n    <div>\n      <input ref={inputRef} />\n      <button onClick={() => inputRef.current.focus()}>\n        Focus\n      </button>\n    </div>\n  );\n}\n```"}
                    ]
                },
                "story": "'Attach refs to elements for direct control,' Ref Keeper teaches.",
                "task": "Create a button that focuses an input when clicked.",
                "starter_code": "function FocusInput() {\n  const inputRef = useRef(null);\n  \n  return (\n    <>\n      <input ref={/* attach ref */} />\n      <button onClick={/* focus */}>Focus</button>\n    </>\n  );\n}",
                "expected_output": "ref={inputRef}, inputRef.current.focus()",
                "hints": ["ref={inputRef} on input, onClick={() => inputRef.current.focus()}"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Collective Mana",
        "topic": "Context API, useContext",
        "description": "Share state across the component tree.",
        "story_intro": "Collective Mana flows through the entire tree, accessible everywhere!",
        "character": "Context Sage",
        "character_quote": "Context shares data without prop drilling!",
        "icon": "share-2",
        "color": "#00b894",
        "missions": [
            {
                "id": 819,
                "title": "Context API",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Creating Context",
                    "overview": "Context provides a way to share values without passing props.",
                    "sections": [
                        {"heading": "createContext", "content": "Create a context and Provider component."},
                        {"heading": "Example", "content": "```jsx\nimport { createContext } from 'react';\n\nconst ThemeContext = createContext('light');\n\nfunction App() {\n  return (\n    <ThemeContext.Provider value=\"dark\">\n      <Child />\n    </ThemeContext.Provider>\n  );\n}\n```"}
                    ]
                },
                "story": "'Context eliminates prop drilling,' Context Sage explains.",
                "task": "Create a UserContext and wrap your app with a Provider.",
                "starter_code": "import { createContext } from 'react';\n\n// Create context\nconst UserContext = \n\n// Wrap app with Provider",
                "expected_output": "createContext(null), <UserContext.Provider value={user}>",
                "hints": ["createContext(defaultValue)"]
            },
            {
                "id": 820,
                "title": "useContext Hook",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Consuming Context",
                    "overview": "useContext reads the current context value.",
                    "sections": [
                        {"heading": "useContext", "content": "Call useContext with the context object to get the value."},
                        {"heading": "Example", "content": "```jsx\nimport { useContext } from 'react';\n\nfunction ThemedButton() {\n  const theme = useContext(ThemeContext);\n  return <button className={theme}>Click</button>;\n}\n```"}
                    ]
                },
                "story": "'useContext retrieves the shared value,' Sage teaches.",
                "task": "Use useContext to get the current user from UserContext.",
                "starter_code": "import { useContext } from 'react';\n\nfunction Profile() {\n  // Get user from context\n  const user = \n  \n  return <p>Hello, {user.name}</p>;\n}",
                "expected_output": "useContext(UserContext)",
                "hints": ["useContext(YourContext)"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Custom Magic",
        "topic": "Writing Custom Hooks",
        "description": "Create your own reusable hooks.",
        "story_intro": "Custom Magic lets you craft your own powerful spells!",
        "character": "Hook Master",
        "character_quote": "Custom hooks extract and reuse logic!",
        "icon": "wand",
        "color": "#e17055",
        "missions": [
            {
                "id": 821,
                "title": "Custom Hooks Basics",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Creating Custom Hooks",
                    "overview": "Custom hooks are functions that use other hooks.",
                    "sections": [
                        {"heading": "Rules", "content": "- Start with 'use' prefix\n- Can use other hooks inside\n- Extract reusable logic"},
                        {"heading": "Example", "content": "```jsx\nfunction useCounter(initial = 0) {\n  const [count, setCount] = useState(initial);\n  const increment = () => setCount(c => c + 1);\n  return { count, increment };\n}\n\n// Usage\nfunction App() {\n  const { count, increment } = useCounter(0);\n  return <button onClick={increment}>{count}</button>;\n}\n```"}
                    ]
                },
                "story": "'Custom hooks encapsulate reusable logic,' Hook Master explains.",
                "task": "Create a useToggle hook that toggles between true and false.",
                "starter_code": "function useToggle(initial = false) {\n  // Create state and toggle function\n  \n  return [/* value */, /* toggle function */];\n}",
                "expected_output": "[value, toggle]",
                "hints": ["useState + function that calls setValue(!value)"]
            },
            {
                "id": 822,
                "title": "useLocalStorage Hook",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Practical Custom Hook",
                    "overview": "Build a hook that syncs state with localStorage.",
                    "sections": [
                        {"heading": "useLocalStorage", "content": "Persist state in localStorage."},
                        {"heading": "Example", "content": "```jsx\nfunction useLocalStorage(key, initial) {\n  const [value, setValue] = useState(() => {\n    const saved = localStorage.getItem(key);\n    return saved ? JSON.parse(saved) : initial;\n  });\n  \n  useEffect(() => {\n    localStorage.setItem(key, JSON.stringify(value));\n  }, [key, value]);\n  \n  return [value, setValue];\n}\n```"}
                    ]
                },
                "story": "'Persist data across sessions,' Hook Master teaches.",
                "task": "Implement a useLocalStorage hook.",
                "starter_code": "function useLocalStorage(key, initialValue) {\n  // Initialize from localStorage\n  // Sync to localStorage on change\n}",
                "expected_output": "useState, useEffect, localStorage",
                "hints": ["useState with lazy initializer, useEffect to save"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Road of Navigation",
        "topic": "React Router, Links, URL Params",
        "description": "Navigate between pages in your app.",
        "story_intro": "The Road of Navigation connects all the realms of your application!",
        "character": "Path Guide",
        "character_quote": "Routes lead users through your application!",
        "icon": "map",
        "color": "#0984e3",
        "missions": [
            {
                "id": 823,
                "title": "React Router Setup",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Setting Up Routes",
                    "overview": "React Router enables client-side navigation.",
                    "sections": [
                        {"heading": "Basic Setup", "content": "Wrap app in BrowserRouter, define Routes."},
                        {"heading": "Example", "content": "```jsx\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <Routes>\n        <Route path=\"/\" element={<Home />} />\n        <Route path=\"/about\" element={<About />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}\n```"}
                    ]
                },
                "story": "'Routes map URLs to components,' Path Guide explains.",
                "task": "Set up routes for Home (/) and Profile (/profile) pages.",
                "starter_code": "// Set up BrowserRouter with Routes\n",
                "expected_output": "<Route path='/' element={<Home />} />",
                "hints": ["BrowserRouter > Routes > Route"]
            },
            {
                "id": 824,
                "title": "Link Navigation",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Navigating with Links",
                    "overview": "Link component for client-side navigation.",
                    "sections": [
                        {"heading": "Link vs a", "content": "Link prevents full page reload."},
                        {"heading": "Example", "content": "```jsx\nimport { Link } from 'react-router-dom';\n\nfunction Nav() {\n  return (\n    <nav>\n      <Link to=\"/\">Home</Link>\n      <Link to=\"/about\">About</Link>\n    </nav>\n  );\n}\n```"}
                    ]
                },
                "story": "'Links navigate without reloading,' Path Guide teaches.",
                "task": "Create a navigation with Links to Home and About.",
                "starter_code": "import { Link } from 'react-router-dom';\n\nfunction Nav() {\n  return (\n    <nav>\n      {/* Add links */}\n    </nav>\n  );\n}",
                "expected_output": "<Link to='/'>Home</Link>",
                "hints": ["<Link to='/path'>Text</Link>"]
            },
            {
                "id": 825,
                "title": "URL Parameters",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Dynamic Routes",
                    "overview": "Use URL parameters for dynamic pages.",
                    "sections": [
                        {"heading": "useParams", "content": "Access URL parameters with useParams hook."},
                        {"heading": "Example", "content": "```jsx\nimport { useParams } from 'react-router-dom';\n\n// Route: <Route path=\"/user/:id\" element={<User />} />\n\nfunction User() {\n  const { id } = useParams();\n  return <p>User ID: {id}</p>;\n}\n```"}
                    ]
                },
                "story": "'URL parameters make routes dynamic,' Path Guide reveals.",
                "task": "Create a route /post/:postId and read the postId.",
                "starter_code": "// Route: <Route path='/post/:postId' element={<Post />} />\n\nfunction Post() {\n  // Get postId from URL\n  \n  return <p>Post: {postId}</p>;\n}",
                "expected_output": "useParams()",
                "hints": ["const { postId } = useParams()"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Grand Interface",
        "topic": "Building a full Kawaii Dashboard",
        "description": "Build a complete React application.",
        "story_intro": "The Grand Interface is your masterpiece - a complete application!",
        "character": "Grand Architect",
        "character_quote": "Combine all your skills to build something amazing!",
        "icon": "trophy",
        "color": "#ffd700",
        "missions": [
            {
                "id": 826,
                "title": "Dashboard Layout",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "Building the Dashboard",
                    "overview": "Combine components, routing, and state for a full app.",
                    "sections": [
                        {"heading": "Planning", "content": "1. Define routes\n2. Create layout components\n3. Add state management\n4. Connect to data"},
                        {"heading": "Structure", "content": "```\nApp\n├── Header\n├── Sidebar\n└── Routes\n    ├── Dashboard\n    ├── Profile\n    └── Settings\n```"}
                    ]
                },
                "story": "'Plan your architecture before coding,' Grand Architect advises.",
                "task": "Design the component structure for a dashboard with Header, Sidebar, and main content area.",
                "starter_code": "function App() {\n  return (\n    <div className=\"app\">\n      {/* Header, Sidebar, Routes */}\n    </div>\n  );\n}",
                "expected_output": None,
                "hints": ["Header at top, Sidebar on left, main content on right"]
            },
            {
                "id": 827,
                "title": "Final Integration",
                "difficulty": "hard",
                "xp": 100,
                "lesson": {
                    "title": "Putting It All Together",
                    "overview": "Integrate all React concepts into one project.",
                    "sections": [
                        {"heading": "Checklist", "content": "- Components with props\n- State management with useState\n- Side effects with useEffect\n- Context for global state\n- Routing for navigation"},
                        {"heading": "Best Practices", "content": "- Keep components small\n- Lift state up when needed\n- Use custom hooks for logic\n- Handle loading and errors"}
                    ]
                },
                "story": "'You are now a React Interface Weaver,' Grand Architect declares!",
                "task": "List all the React concepts you've learned and how they work together.",
                "starter_code": "// React concepts mastered:\n// 1. JSX and Components\n// 2. Props and State\n// 3. Hooks: useState, useEffect, useRef, useContext\n// 4. Lists and Conditional Rendering\n// 5. Custom Hooks\n// 6. React Router",
                "expected_output": None,
                "hints": ["Review all 12 arcs!"]
            }
        ]
    }
]

MONGODB_ARCS = [
    {
        "id": 1,
        "name": "The NoSQL Awakening",
        "topic": "What is NoSQL?, BSON vs JSON",
        "description": "Discover a different way to store data - flexible and document-based.",
        "story_intro": "Welcome to the Scroll of Infinite Documents! Here, data flows freely without rigid table structures.",
        "character": "Scroll Keeper",
        "character_quote": "NoSQL gives us freedom to shape our data as needed!",
        "icon": "book-open",
        "color": "#47a248",
        "missions": [
            {
                "id": 901,
                "title": "What is NoSQL?",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "NoSQL Databases",
                    "overview": "NoSQL databases store data differently than relational databases.",
                    "sections": [
                        {"heading": "NoSQL vs SQL", "content": "SQL uses tables with rows and columns. NoSQL uses flexible document structures, key-value pairs, or graphs."},
                        {"heading": "MongoDB", "content": "MongoDB is a document database - it stores data as JSON-like documents that can have varying structures."}
                    ]
                },
                "story": "'SQL puts data in rigid tables,' Scroll Keeper explains. 'NoSQL lets documents breathe freely!'",
                "task": "Explain one key difference between SQL and NoSQL databases.",
                "starter_code": "// SQL vs NoSQL difference:\n// ",
                "expected_output": "flexible schema",
                "hints": ["NoSQL doesn't require fixed schemas like SQL tables"]
            },
            {
                "id": 902,
                "title": "BSON vs JSON",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "BSON - Binary JSON",
                    "overview": "MongoDB stores data as BSON, a binary representation of JSON.",
                    "sections": [
                        {"heading": "JSON", "content": "JavaScript Object Notation - human readable text format with key-value pairs."},
                        {"heading": "BSON", "content": "Binary JSON - MongoDB's internal format. Adds types like Date, ObjectId, and is faster to parse."}
                    ]
                },
                "story": "'BSON is JSON's powerful cousin,' Scroll Keeper teaches.",
                "task": "What extra data types does BSON support that JSON doesn't?",
                "starter_code": "// BSON supports these types that JSON doesn't:\n// ",
                "expected_output": "Date, ObjectId",
                "hints": ["BSON has Date, ObjectId, Binary, and more"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Scroll Collection",
        "topic": "Databases, Collections, Documents",
        "description": "Learn how MongoDB organizes data into databases, collections, and documents.",
        "story_intro": "The great library is organized into sections, shelves, and individual scrolls!",
        "character": "Librarian Sage",
        "character_quote": "Organization is the key to finding your data!",
        "icon": "database",
        "color": "#3f9c35",
        "missions": [
            {
                "id": 903,
                "title": "Databases",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "MongoDB Databases",
                    "overview": "A database is a container for collections.",
                    "sections": [
                        {"heading": "Creating Databases", "content": "Databases are created automatically when you first store data in them."},
                        {"heading": "Commands", "content": "```javascript\nuse myDatabase    // Switch to database\nshow dbs          // List all databases\n```"}
                    ]
                },
                "story": "'Each database is like a section of the library,' Librarian Sage explains.",
                "task": "Write the command to switch to a database called 'kawaii_app'.",
                "starter_code": "// Switch to kawaii_app database\n",
                "expected_output": "use kawaii_app",
                "hints": ["use databaseName"]
            },
            {
                "id": 904,
                "title": "Collections",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Collections",
                    "overview": "Collections are groups of documents, like tables in SQL.",
                    "sections": [
                        {"heading": "What is a Collection?", "content": "A collection holds related documents. Unlike SQL tables, documents in a collection can have different structures."},
                        {"heading": "Commands", "content": "```javascript\ndb.createCollection('users')\nshow collections\n```"}
                    ]
                },
                "story": "'Collections are like shelves holding similar scrolls,' Sage teaches.",
                "task": "Write the command to show all collections in the current database.",
                "starter_code": "// Show all collections\n",
                "expected_output": "show collections",
                "hints": ["show collections"]
            },
            {
                "id": 905,
                "title": "Documents",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Documents",
                    "overview": "Documents are individual records stored as BSON objects.",
                    "sections": [
                        {"heading": "Document Structure", "content": "Documents are JSON-like objects with field-value pairs."},
                        {"heading": "Example", "content": "```javascript\n{\n  _id: ObjectId('...'),\n  name: 'Sakura',\n  level: 5,\n  skills: ['python', 'react']\n}\n```"}
                    ]
                },
                "story": "'Each document is a unique scroll with its own story,' Sage reveals.",
                "task": "What field does MongoDB automatically add to every document?",
                "starter_code": "// MongoDB auto-generates this field:\n",
                "expected_output": "_id",
                "hints": ["It's called _id and contains an ObjectId"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Scribe's First Entry",
        "topic": "insertOne(), insertMany()",
        "description": "Learn to write new documents to the database.",
        "story_intro": "The Scribe teaches you to create new scrolls and add them to the collection!",
        "character": "Master Scribe",
        "character_quote": "Every great database starts with a single insert!",
        "icon": "edit",
        "color": "#4db33d",
        "missions": [
            {
                "id": 906,
                "title": "insertOne()",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Inserting Single Documents",
                    "overview": "Use insertOne() to add a single document to a collection.",
                    "sections": [
                        {"heading": "Syntax", "content": "db.collection.insertOne({ field: value })"},
                        {"heading": "Example", "content": "```javascript\ndb.users.insertOne({\n  name: 'Yuki',\n  age: 22,\n  role: 'developer'\n})\n```"}
                    ]
                },
                "story": "'insertOne creates a single new scroll,' Master Scribe demonstrates.",
                "task": "Insert a document with name 'Hana' and level 1 into the players collection.",
                "starter_code": "db.players.insertOne(",
                "expected_output": "{ name: 'Hana', level: 1 }",
                "hints": ["insertOne({ name: 'Hana', level: 1 })"]
            },
            {
                "id": 907,
                "title": "insertMany()",
                "difficulty": "easy",
                "xp": 35,
                "lesson": {
                    "title": "Inserting Multiple Documents",
                    "overview": "Use insertMany() to add multiple documents at once.",
                    "sections": [
                        {"heading": "Syntax", "content": "db.collection.insertMany([doc1, doc2, ...])"},
                        {"heading": "Example", "content": "```javascript\ndb.items.insertMany([\n  { name: 'Sword', power: 10 },\n  { name: 'Shield', defense: 5 }\n])\n```"}
                    ]
                },
                "story": "'insertMany writes multiple scrolls at once,' Scribe explains.",
                "task": "Insert two items: a Potion with hp: 50 and an Elixir with mp: 30.",
                "starter_code": "db.items.insertMany([",
                "expected_output": "[{ name: 'Potion', hp: 50 }, { name: 'Elixir', mp: 30 }]",
                "hints": ["Pass an array of objects"]
            }
        ]
    },
    {
        "id": 4,
        "name": "The Seer's Vision",
        "topic": "find(), findOne(), Projections",
        "description": "Query documents from your collections.",
        "story_intro": "The Seer can look into the database and retrieve exactly what you need!",
        "character": "Oracle Seer",
        "character_quote": "Find what you seek with the power of queries!",
        "icon": "search",
        "color": "#59a14f",
        "missions": [
            {
                "id": 908,
                "title": "find()",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Finding Documents",
                    "overview": "Use find() to retrieve multiple documents from a collection.",
                    "sections": [
                        {"heading": "Basic find", "content": "db.collection.find() returns all documents. Add a filter to narrow results."},
                        {"heading": "Example", "content": "```javascript\ndb.users.find()           // All users\ndb.users.find({ age: 25 }) // Users aged 25\n```"}
                    ]
                },
                "story": "'find() reveals all matching scrolls,' Oracle Seer explains.",
                "task": "Find all documents in the players collection where level is 5.",
                "starter_code": "db.players.find(",
                "expected_output": "{ level: 5 }",
                "hints": ["find({ level: 5 })"]
            },
            {
                "id": 909,
                "title": "findOne()",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Finding One Document",
                    "overview": "Use findOne() to retrieve a single matching document.",
                    "sections": [
                        {"heading": "When to Use", "content": "findOne returns the first match - useful when you expect one result."},
                        {"heading": "Example", "content": "```javascript\ndb.users.findOne({ email: 'sakura@example.com' })\n```"}
                    ]
                },
                "story": "'findOne returns just the first matching scroll,' Seer teaches.",
                "task": "Find one player with the name 'Sakura'.",
                "starter_code": "db.players.findOne(",
                "expected_output": "{ name: 'Sakura' }",
                "hints": ["findOne({ name: 'Sakura' })"]
            },
            {
                "id": 910,
                "title": "Projections",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Projections - Selecting Fields",
                    "overview": "Projections let you specify which fields to include or exclude.",
                    "sections": [
                        {"heading": "Syntax", "content": "Second parameter to find: 1 to include, 0 to exclude."},
                        {"heading": "Example", "content": "```javascript\n// Only return name and level\ndb.players.find({}, { name: 1, level: 1 })\n\n// Exclude the password field\ndb.users.find({}, { password: 0 })\n```"}
                    ]
                },
                "story": "'Projections filter which fields you see,' Seer reveals.",
                "task": "Find all players but only return their name and score fields.",
                "starter_code": "db.players.find({}, ",
                "expected_output": "{ name: 1, score: 1 }",
                "hints": ["Second param: { name: 1, score: 1 }"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Filter of the Ancients",
        "topic": "$gt, $lt, $in, $and, $or",
        "description": "Master powerful query operators for precise filtering.",
        "story_intro": "The ancient filter operators give you precise control over your queries!",
        "character": "Filter Master",
        "character_quote": "With operators, you can find anything!",
        "icon": "filter",
        "color": "#2e8b57",
        "missions": [
            {
                "id": 911,
                "title": "Comparison Operators",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "$gt, $lt, $gte, $lte",
                    "overview": "Compare values with greater than, less than operators.",
                    "sections": [
                        {"heading": "Operators", "content": "$gt (>), $lt (<), $gte (>=), $lte (<=), $eq (=), $ne (!=)"},
                        {"heading": "Example", "content": "```javascript\n// Find players with level > 10\ndb.players.find({ level: { $gt: 10 } })\n\n// Find items with price between 5 and 20\ndb.items.find({ price: { $gte: 5, $lte: 20 } })\n```"}
                    ]
                },
                "story": "'$gt and $lt let you compare values,' Filter Master explains.",
                "task": "Find all players with score greater than 100.",
                "starter_code": "db.players.find({ score: ",
                "expected_output": "{ $gt: 100 }",
                "hints": ["Use $gt: 100"]
            },
            {
                "id": 912,
                "title": "$in Operator",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "The $in Operator",
                    "overview": "Match any value in an array of options.",
                    "sections": [
                        {"heading": "$in", "content": "Matches documents where the field equals any value in the array."},
                        {"heading": "Example", "content": "```javascript\n// Find players in specific roles\ndb.players.find({ role: { $in: ['warrior', 'mage'] } })\n```"}
                    ]
                },
                "story": "'$in matches any value from a list,' Filter Master teaches.",
                "task": "Find all items where type is either 'weapon' or 'armor'.",
                "starter_code": "db.items.find({ type: ",
                "expected_output": "{ $in: ['weapon', 'armor'] }",
                "hints": ["$in takes an array of values"]
            },
            {
                "id": 913,
                "title": "$and and $or",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Logical Operators",
                    "overview": "Combine multiple conditions with $and and $or.",
                    "sections": [
                        {"heading": "$and", "content": "All conditions must be true. Often implicit when using multiple fields."},
                        {"heading": "$or", "content": "At least one condition must be true."},
                        {"heading": "Example", "content": "```javascript\n// Active users OR admins\ndb.users.find({\n  $or: [\n    { active: true },\n    { role: 'admin' }\n  ]\n})\n```"}
                    ]
                },
                "story": "'$and and $or combine conditions logically,' Filter Master reveals.",
                "task": "Find players where level > 5 OR score > 1000.",
                "starter_code": "db.players.find({\n  $or: [",
                "expected_output": "$or: [{ level: { $gt: 5 } }, { score: { $gt: 1000 } }]",
                "hints": ["Array of conditions inside $or"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Transmutation Circle",
        "topic": "updateOne(), updateMany(), $set",
        "description": "Modify existing documents in your collections.",
        "story_intro": "The Transmutation Circle allows you to transform existing documents!",
        "character": "Alchemist",
        "character_quote": "Transform your data with the power of updates!",
        "icon": "edit-3",
        "color": "#228b22",
        "missions": [
            {
                "id": 914,
                "title": "updateOne()",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Updating Single Documents",
                    "overview": "Use updateOne() to modify the first matching document.",
                    "sections": [
                        {"heading": "Syntax", "content": "db.collection.updateOne(filter, update)"},
                        {"heading": "Example", "content": "```javascript\ndb.players.updateOne(\n  { name: 'Sakura' },\n  { $set: { level: 10 } }\n)\n```"}
                    ]
                },
                "story": "'updateOne modifies a single document,' Alchemist explains.",
                "task": "Update the player named 'Yuki' to have level 15.",
                "starter_code": "db.players.updateOne(\n  { name: 'Yuki' },\n  ",
                "expected_output": "{ $set: { level: 15 } }",
                "hints": ["Use $set to specify the new value"]
            },
            {
                "id": 915,
                "title": "updateMany()",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Updating Multiple Documents",
                    "overview": "Use updateMany() to modify all matching documents.",
                    "sections": [
                        {"heading": "When to Use", "content": "Update all documents that match the filter."},
                        {"heading": "Example", "content": "```javascript\n// Give all inactive users a status\ndb.users.updateMany(\n  { active: false },\n  { $set: { status: 'dormant' } }\n)\n```"}
                    ]
                },
                "story": "'updateMany transforms all matching scrolls,' Alchemist teaches.",
                "task": "Set active: true for all players where level > 10.",
                "starter_code": "db.players.updateMany(\n  { level: { $gt: 10 } },\n  ",
                "expected_output": "{ $set: { active: true } }",
                "hints": ["Same $set syntax, but affects many"]
            },
            {
                "id": 916,
                "title": "$set Operator",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "The $set Operator",
                    "overview": "$set modifies specific fields without replacing the whole document.",
                    "sections": [
                        {"heading": "Why $set?", "content": "Without $set, the entire document would be replaced. $set only changes specified fields."},
                        {"heading": "Other Operators", "content": "$inc (increment), $unset (remove field), $push (add to array)"}
                    ]
                },
                "story": "'$set changes only what you specify,' Alchemist reveals.",
                "task": "Increment a player's score by 50 using $inc.",
                "starter_code": "db.players.updateOne(\n  { name: 'Hana' },\n  { $inc: ",
                "expected_output": "{ score: 50 }",
                "hints": ["$inc: { score: 50 }"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Vanishing Act",
        "topic": "deleteOne(), deleteMany()",
        "description": "Remove documents from your collections.",
        "story_intro": "Sometimes scrolls must be removed from the archives!",
        "character": "Archivist",
        "character_quote": "With great power comes great responsibility to delete wisely!",
        "icon": "trash-2",
        "color": "#006400",
        "missions": [
            {
                "id": 917,
                "title": "deleteOne()",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Deleting Single Documents",
                    "overview": "Use deleteOne() to remove the first matching document.",
                    "sections": [
                        {"heading": "Syntax", "content": "db.collection.deleteOne(filter)"},
                        {"heading": "Example", "content": "```javascript\ndb.players.deleteOne({ name: 'OldPlayer' })\n```"}
                    ]
                },
                "story": "'deleteOne removes a single scroll carefully,' Archivist explains.",
                "task": "Delete the player with name 'GuestUser'.",
                "starter_code": "db.players.deleteOne(",
                "expected_output": "{ name: 'GuestUser' }",
                "hints": ["Pass a filter object"]
            },
            {
                "id": 918,
                "title": "deleteMany()",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Deleting Multiple Documents",
                    "overview": "Use deleteMany() to remove all matching documents.",
                    "sections": [
                        {"heading": "Caution", "content": "Be careful! deleteMany({}) removes ALL documents."},
                        {"heading": "Example", "content": "```javascript\n// Remove all inactive players\ndb.players.deleteMany({ active: false })\n```"}
                    ]
                },
                "story": "'deleteMany removes all matching scrolls - use wisely!' Archivist warns.",
                "task": "Delete all items where quantity is 0.",
                "starter_code": "db.items.deleteMany(",
                "expected_output": "{ quantity: 0 }",
                "hints": ["Filter for quantity: 0"]
            }
        ]
    },
    {
        "id": 8,
        "name": "The Speed-Runner's Path",
        "topic": "Creating Indexes, Performance basics",
        "description": "Optimize queries with indexes for faster performance.",
        "story_intro": "Indexes are the secret paths that make searching lightning fast!",
        "character": "Speed Sage",
        "character_quote": "Indexes turn slow searches into instant finds!",
        "icon": "zap",
        "color": "#32cd32",
        "missions": [
            {
                "id": 919,
                "title": "Creating Indexes",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Index Creation",
                    "overview": "Indexes speed up queries by creating sorted references to fields.",
                    "sections": [
                        {"heading": "Why Index?", "content": "Without indexes, MongoDB scans every document. With indexes, it jumps directly to matches."},
                        {"heading": "Syntax", "content": "```javascript\n// Create ascending index on name\ndb.players.createIndex({ name: 1 })\n\n// Create descending index on score\ndb.players.createIndex({ score: -1 })\n```"}
                    ]
                },
                "story": "'Indexes are like a book's table of contents,' Speed Sage explains.",
                "task": "Create an ascending index on the email field of the users collection.",
                "starter_code": "db.users.createIndex(",
                "expected_output": "{ email: 1 }",
                "hints": ["1 for ascending, -1 for descending"]
            },
            {
                "id": 920,
                "title": "Performance Basics",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Query Performance",
                    "overview": "Learn to analyze and improve query performance.",
                    "sections": [
                        {"heading": "explain()", "content": "Use explain() to see how MongoDB executes a query."},
                        {"heading": "Example", "content": "```javascript\ndb.players.find({ level: 5 }).explain('executionStats')\n\n// Look for:\n// - COLLSCAN (bad - full scan)\n// - IXSCAN (good - using index)\n```"}
                    ]
                },
                "story": "'explain() reveals how queries run,' Speed Sage teaches.",
                "task": "What type of scan indicates a query is using an index?",
                "starter_code": "// Index scan type: ",
                "expected_output": "IXSCAN",
                "hints": ["IXSCAN means index scan, COLLSCAN means full collection scan"]
            }
        ]
    },
    {
        "id": 9,
        "name": "The Alchemist's Pipe",
        "topic": "The Pipeline: $match, $group, $sort",
        "description": "Transform data with the aggregation pipeline.",
        "story_intro": "The aggregation pipeline transforms data through stages of magic!",
        "character": "Pipeline Mage",
        "character_quote": "Each stage transforms the data for the next!",
        "icon": "git-branch",
        "color": "#3cb371",
        "missions": [
            {
                "id": 921,
                "title": "$match Stage",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Filtering with $match",
                    "overview": "$match filters documents like find() but in a pipeline.",
                    "sections": [
                        {"heading": "Pipeline Intro", "content": "Aggregation pipelines are arrays of stages. Each stage transforms the data."},
                        {"heading": "Example", "content": "```javascript\ndb.players.aggregate([\n  { $match: { level: { $gt: 5 } } }\n])\n```"}
                    ]
                },
                "story": "'$match filters documents entering the pipeline,' Pipeline Mage explains.",
                "task": "Write a $match stage to filter players where active is true.",
                "starter_code": "db.players.aggregate([\n  { $match: ",
                "expected_output": "{ active: true }",
                "hints": ["$match uses the same syntax as find()"]
            },
            {
                "id": 922,
                "title": "$group Stage",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Grouping with $group",
                    "overview": "$group aggregates documents by a field and computes values.",
                    "sections": [
                        {"heading": "$group", "content": "_id specifies the grouping field. Add accumulators like $sum, $avg."},
                        {"heading": "Example", "content": "```javascript\ndb.orders.aggregate([\n  { $group: {\n    _id: '$category',\n    totalSales: { $sum: '$amount' }\n  }}\n])\n```"}
                    ]
                },
                "story": "'$group combines documents and calculates totals,' Mage teaches.",
                "task": "Group players by role and count how many in each role.",
                "starter_code": "{ $group: {\n  _id: '$role',\n  count: ",
                "expected_output": "{ $sum: 1 }",
                "hints": ["$sum: 1 counts documents"]
            },
            {
                "id": 923,
                "title": "$sort Stage",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Sorting with $sort",
                    "overview": "$sort orders documents in the pipeline.",
                    "sections": [
                        {"heading": "$sort", "content": "1 for ascending, -1 for descending."},
                        {"heading": "Example", "content": "```javascript\ndb.players.aggregate([\n  { $match: { active: true } },\n  { $sort: { score: -1 } }\n])\n```"}
                    ]
                },
                "story": "'$sort orders the results,' Pipeline Mage reveals.",
                "task": "Add a $sort stage to order by score descending.",
                "starter_code": "{ $sort: ",
                "expected_output": "{ score: -1 }",
                "hints": ["-1 for descending order"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Infinite Transformation",
        "topic": "$project, $limit, $unwind",
        "description": "Advanced pipeline stages for reshaping data.",
        "story_intro": "More powerful transformations await in the pipeline!",
        "character": "Transform Witch",
        "character_quote": "Reshape your data into exactly what you need!",
        "icon": "sliders",
        "color": "#2e8b57",
        "missions": [
            {
                "id": 924,
                "title": "$project Stage",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Reshaping with $project",
                    "overview": "$project includes, excludes, or transforms fields.",
                    "sections": [
                        {"heading": "$project", "content": "Similar to projections in find(), but can also compute new fields."},
                        {"heading": "Example", "content": "```javascript\ndb.players.aggregate([\n  { $project: {\n    name: 1,\n    doubleScore: { $multiply: ['$score', 2] }\n  }}\n])\n```"}
                    ]
                },
                "story": "'$project shapes the output fields,' Transform Witch explains.",
                "task": "Project only name and create a new field 'isHighLevel' that's true if level > 10.",
                "starter_code": "{ $project: {\n  name: 1,\n  isHighLevel: ",
                "expected_output": "{ $gt: ['$level', 10] }",
                "hints": ["Use comparison operators in expressions"]
            },
            {
                "id": 925,
                "title": "$limit Stage",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Limiting Results",
                    "overview": "$limit restricts the number of documents passed to the next stage.",
                    "sections": [
                        {"heading": "$limit", "content": "Often used with $sort for 'top N' queries."},
                        {"heading": "Example", "content": "```javascript\ndb.players.aggregate([\n  { $sort: { score: -1 } },\n  { $limit: 10 }\n])  // Top 10 players\n```"}
                    ]
                },
                "story": "'$limit caps how many results pass through,' Witch teaches.",
                "task": "Get the top 5 players by score.",
                "starter_code": "db.players.aggregate([\n  { $sort: { score: -1 } },\n  { $limit: ",
                "expected_output": "5",
                "hints": ["Just a number after $limit"]
            },
            {
                "id": 926,
                "title": "$unwind Stage",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Deconstructing Arrays",
                    "overview": "$unwind creates a document for each array element.",
                    "sections": [
                        {"heading": "$unwind", "content": "Expands array fields into separate documents."},
                        {"heading": "Example", "content": "```javascript\n// Document: { name: 'Sakura', skills: ['python', 'react'] }\n// After $unwind: { skills: 'python' } becomes separate from { skills: 'react' }\n\ndb.players.aggregate([\n  { $unwind: '$skills' }\n])\n```"}
                    ]
                },
                "story": "'$unwind splits arrays into individual documents,' Witch reveals.",
                "task": "Unwind the 'tags' array field.",
                "starter_code": "{ $unwind: ",
                "expected_output": "'$tags'",
                "hints": ["Use '$fieldName' syntax"]
            }
        ]
    },
    {
        "id": 11,
        "name": "The Bound Spirits",
        "topic": "Embedding vs. Referencing data",
        "description": "Learn when to embed documents vs reference them.",
        "story_intro": "Should spirits be bound together or linked from afar?",
        "character": "Design Oracle",
        "character_quote": "The right model depends on how you access your data!",
        "icon": "link",
        "color": "#228b22",
        "missions": [
            {
                "id": 927,
                "title": "Embedding Documents",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Embedded Documents",
                    "overview": "Store related data together in nested documents.",
                    "sections": [
                        {"heading": "When to Embed", "content": "- Data is always accessed together\n- One-to-few relationship\n- Data doesn't need to be queried independently"},
                        {"heading": "Example", "content": "```javascript\n{\n  name: 'Sakura',\n  address: {\n    city: 'Tokyo',\n    country: 'Japan'\n  }\n}\n```"}
                    ]
                },
                "story": "'Embed when data belongs together,' Design Oracle explains.",
                "task": "Give an example of data that should be embedded.",
                "starter_code": "// Good to embed: ",
                "expected_output": "address in user",
                "hints": ["User's address, blog post's comments (if few)"]
            },
            {
                "id": 928,
                "title": "Referencing Documents",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Document References",
                    "overview": "Store references (ObjectIds) to documents in other collections.",
                    "sections": [
                        {"heading": "When to Reference", "content": "- One-to-many with many items\n- Data accessed independently\n- Data changes frequently"},
                        {"heading": "Example", "content": "```javascript\n// users collection\n{ _id: ObjectId('user1'), name: 'Sakura' }\n\n// orders collection\n{ userId: ObjectId('user1'), item: 'Sword' }\n```"}
                    ]
                },
                "story": "'Reference when data is accessed separately,' Oracle teaches.",
                "task": "When should you use references instead of embedding?",
                "starter_code": "// Use references when: ",
                "expected_output": "one-to-many, independent access",
                "hints": ["Many related documents, or accessed separately"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Guardian of the Atlas",
        "topic": "Connecting to MongoDB Atlas (Cloud)",
        "description": "Deploy your database to the cloud with MongoDB Atlas.",
        "story_intro": "The Atlas holds databases in the clouds, accessible from anywhere!",
        "character": "Cloud Guardian",
        "character_quote": "Atlas brings your data to the world!",
        "icon": "cloud",
        "color": "#47a248",
        "missions": [
            {
                "id": 929,
                "title": "MongoDB Atlas",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Cloud Database with Atlas",
                    "overview": "MongoDB Atlas is MongoDB's cloud database service.",
                    "sections": [
                        {"heading": "What is Atlas?", "content": "A fully managed cloud database. No server setup needed."},
                        {"heading": "Connection String", "content": "```javascript\nmongodb+srv://username:password@cluster.mongodb.net/database\n\n// In Node.js:\nconst { MongoClient } = require('mongodb');\nconst client = new MongoClient(connectionString);\n```"}
                    ]
                },
                "story": "'Atlas runs your database in the cloud,' Cloud Guardian explains.",
                "task": "What protocol does a MongoDB Atlas connection string start with?",
                "starter_code": "// Atlas connection starts with: ",
                "expected_output": "mongodb+srv://",
                "hints": ["mongodb+srv:// for Atlas clusters"]
            },
            {
                "id": 930,
                "title": "Connection Mastery",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Connecting from Applications",
                    "overview": "Connect to Atlas from your application code.",
                    "sections": [
                        {"heading": "Steps", "content": "1. Create Atlas cluster\n2. Add IP to whitelist\n3. Create database user\n4. Get connection string\n5. Connect from code"},
                        {"heading": "Node.js Example", "content": "```javascript\nconst { MongoClient } = require('mongodb');\n\nasync function connect() {\n  const client = new MongoClient(process.env.MONGODB_URI);\n  await client.connect();\n  const db = client.db('myapp');\n  return db;\n}\n```"}
                    ]
                },
                "story": "'You are now a MongoDB Master!' Cloud Guardian declares.",
                "task": "What method connects the MongoClient to the database?",
                "starter_code": "// Connect method: await client.",
                "expected_output": "connect()",
                "hints": ["client.connect() is async"]
            }
        ]
    }
]

PHP_ARCS = [
    {
        "id": 1,
        "name": "Loom Setup",
        "topic": "Syntax, echo, Server environment",
        "description": "Set up your weaving loom and learn PHP basics.",
        "story_intro": "Welcome to the Web Weaver's Loom! Here you'll spin server-side magic that powers the web.",
        "character": "Loom Master",
        "character_quote": "PHP weaves the fabric of dynamic websites!",
        "icon": "settings",
        "color": "#777bb4",
        "missions": [
            {
                "id": 1001,
                "title": "PHP Syntax",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "PHP Basics",
                    "overview": "PHP code runs on the server and generates HTML for the browser.",
                    "sections": [
                        {"heading": "PHP Tags", "content": "PHP code is enclosed in <?php ?> tags. It can be embedded in HTML."},
                        {"heading": "Example", "content": "```php\n<?php\n  // PHP code here\n  $name = 'Sakura';\n?>\n```"}
                    ]
                },
                "story": "'PHP runs on the server before the page reaches the browser,' Loom Master explains.",
                "task": "Write PHP tags that define a variable $greeting with value 'Hello'.",
                "starter_code": "<?php\n  // Define greeting variable\n  \n?>",
                "expected_output": "$greeting = 'Hello'",
                "hints": ["$variableName = 'value';"]
            },
            {
                "id": 1002,
                "title": "Echo Output",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Outputting with echo",
                    "overview": "Use echo to output text to the browser.",
                    "sections": [
                        {"heading": "echo", "content": "echo outputs strings to the HTML response."},
                        {"heading": "Example", "content": "```php\n<?php\n  echo 'Hello, World!';\n  echo \"Welcome, $name\";  // Variables in double quotes\n?>\n```"}
                    ]
                },
                "story": "'echo sends your message to the browser,' Loom Master teaches.",
                "task": "Use echo to output 'Welcome to PHP!'",
                "starter_code": "<?php\n  // Output the message\n  \n?>",
                "expected_output": "Welcome to PHP!",
                "hints": ["echo 'Your message';"]
            },
            {
                "id": 1003,
                "title": "Server Environment",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Server Variables",
                    "overview": "Access server information through superglobals.",
                    "sections": [
                        {"heading": "$_SERVER", "content": "Contains server and execution environment information."},
                        {"heading": "Example", "content": "```php\n<?php\n  echo $_SERVER['PHP_SELF'];      // Current script\n  echo $_SERVER['SERVER_NAME'];   // Server hostname\n  echo $_SERVER['REQUEST_METHOD']; // GET or POST\n?>\n```"}
                    ]
                },
                "story": "'$_SERVER holds secrets about the request,' Loom Master reveals.",
                "task": "Echo the current request method using $_SERVER.",
                "starter_code": "<?php\n  // Output request method\n  echo ",
                "expected_output": "$_SERVER['REQUEST_METHOD']",
                "hints": ["$_SERVER['REQUEST_METHOD']"]
            }
        ]
    },
    {
        "id": 2,
        "name": "String Splicing",
        "topic": "Strings, Numbers, Operators",
        "description": "Work with PHP's data types and operators.",
        "story_intro": "Splice together the threads of data - strings, numbers, and more!",
        "character": "Data Weaver",
        "character_quote": "Data types are the threads we weave with!",
        "icon": "type",
        "color": "#8892be",
        "missions": [
            {
                "id": 1004,
                "title": "Strings",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Working with Strings",
                    "overview": "PHP has powerful string manipulation functions.",
                    "sections": [
                        {"heading": "String Functions", "content": "strlen(), strtoupper(), strtolower(), substr(), str_replace()"},
                        {"heading": "Example", "content": "```php\n<?php\n  $name = 'sakura';\n  echo strlen($name);        // 6\n  echo strtoupper($name);    // SAKURA\n  echo substr($name, 0, 3);  // sak\n?>\n```"}
                    ]
                },
                "story": "'Strings can be transformed in many ways,' Data Weaver explains.",
                "task": "Convert 'hello world' to uppercase using a string function.",
                "starter_code": "<?php\n  $text = 'hello world';\n  echo ",
                "expected_output": "strtoupper($text)",
                "hints": ["strtoupper() converts to uppercase"]
            },
            {
                "id": 1005,
                "title": "Numbers",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Numeric Types",
                    "overview": "PHP supports integers and floats.",
                    "sections": [
                        {"heading": "Types", "content": "Integers (whole numbers) and floats (decimals)."},
                        {"heading": "Example", "content": "```php\n<?php\n  $age = 25;        // integer\n  $price = 19.99;   // float\n  $sum = $age + 10; // 35\n?>\n```"}
                    ]
                },
                "story": "'Numbers power calculations,' Data Weaver teaches.",
                "task": "Calculate the total of price (29.99) plus tax (5.00).",
                "starter_code": "<?php\n  $price = 29.99;\n  $tax = 5.00;\n  $total = ",
                "expected_output": "$price + $tax",
                "hints": ["Simply add the two variables"]
            },
            {
                "id": 1006,
                "title": "Operators",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "PHP Operators",
                    "overview": "Arithmetic, comparison, and string operators.",
                    "sections": [
                        {"heading": "Operators", "content": "+ - * / % (arithmetic)\n== === != !== (comparison)\n. (string concatenation)"},
                        {"heading": "Example", "content": "```php\n<?php\n  $a = 5 + 3;              // 8\n  $greeting = 'Hello' . ' ' . 'World';  // Hello World\n  $equal = (5 === '5');    // false (strict)\n?>\n```"}
                    ]
                },
                "story": "'The dot operator joins strings together,' Weaver reveals.",
                "task": "Concatenate 'Hello' and 'PHP' with a space between.",
                "starter_code": "<?php\n  $result = 'Hello' . ",
                "expected_output": "' ' . 'PHP'",
                "hints": ["Use . to concatenate strings"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Decision Loom",
        "topic": "Logic, Loops (foreach)",
        "description": "Control the flow of your PHP code.",
        "story_intro": "The Decision Loom lets you choose different paths and repeat patterns!",
        "character": "Flow Controller",
        "character_quote": "Control structures guide the execution flow!",
        "icon": "git-branch",
        "color": "#6b70a0",
        "missions": [
            {
                "id": 1007,
                "title": "If/Else Logic",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Conditional Statements",
                    "overview": "Use if/else to make decisions.",
                    "sections": [
                        {"heading": "Syntax", "content": "if (condition) { } elseif (condition) { } else { }"},
                        {"heading": "Example", "content": "```php\n<?php\n  $age = 18;\n  if ($age >= 18) {\n    echo 'Adult';\n  } else {\n    echo 'Minor';\n  }\n?>\n```"}
                    ]
                },
                "story": "'If statements choose the path,' Flow Controller explains.",
                "task": "Write an if statement that echoes 'Pass' if $score >= 60.",
                "starter_code": "<?php\n  $score = 75;\n  // Check if passing\n  ",
                "expected_output": "if ($score >= 60) { echo 'Pass'; }",
                "hints": ["if ($score >= 60) { ... }"]
            },
            {
                "id": 1008,
                "title": "Foreach Loops",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Looping with foreach",
                    "overview": "foreach is perfect for iterating arrays.",
                    "sections": [
                        {"heading": "Syntax", "content": "foreach ($array as $value) { } or foreach ($array as $key => $value) { }"},
                        {"heading": "Example", "content": "```php\n<?php\n  $colors = ['red', 'green', 'blue'];\n  foreach ($colors as $color) {\n    echo $color . '<br>';\n  }\n?>\n```"}
                    ]
                },
                "story": "'foreach walks through every element,' Controller teaches.",
                "task": "Loop through $fruits array and echo each fruit.",
                "starter_code": "<?php\n  $fruits = ['apple', 'banana', 'cherry'];\n  // foreach loop\n  ",
                "expected_output": "foreach ($fruits as $fruit) { echo $fruit; }",
                "hints": ["foreach ($array as $item) { }"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Modular Weaving",
        "topic": "Scope, Return, Type hinting",
        "description": "Create reusable functions in PHP.",
        "story_intro": "Modular patterns can be woven once and reused many times!",
        "character": "Function Crafter",
        "character_quote": "Functions encapsulate reusable logic!",
        "icon": "package",
        "color": "#5c6299",
        "missions": [
            {
                "id": 1009,
                "title": "Functions and Scope",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Creating Functions",
                    "overview": "Functions have their own scope in PHP.",
                    "sections": [
                        {"heading": "Syntax", "content": "function name($params) { return value; }"},
                        {"heading": "Example", "content": "```php\n<?php\n  function greet($name) {\n    return 'Hello, ' . $name;\n  }\n  echo greet('Sakura');  // Hello, Sakura\n?>\n```"}
                    ]
                },
                "story": "'Functions create reusable blocks of code,' Function Crafter explains.",
                "task": "Create a function add that takes two numbers and returns their sum.",
                "starter_code": "<?php\n  function add($a, $b) {\n    // Return sum\n  }",
                "expected_output": "return $a + $b",
                "hints": ["return $a + $b;"]
            },
            {
                "id": 1010,
                "title": "Return Values",
                "difficulty": "medium",
                "xp": 30,
                "lesson": {
                    "title": "Returning Data",
                    "overview": "Functions can return values to the caller.",
                    "sections": [
                        {"heading": "Return", "content": "Use return to send a value back."},
                        {"heading": "Example", "content": "```php\n<?php\n  function square($n) {\n    return $n * $n;\n  }\n  $result = square(5);  // 25\n?>\n```"}
                    ]
                },
                "story": "'Return sends the result back,' Crafter teaches.",
                "task": "Create a function isEven that returns true if a number is even.",
                "starter_code": "<?php\n  function isEven($num) {\n    // Return true if even\n  }",
                "expected_output": "return $num % 2 === 0",
                "hints": ["Use modulo % 2 === 0"]
            },
            {
                "id": 1011,
                "title": "Type Hinting",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Type Declarations",
                    "overview": "PHP 7+ supports type hints for parameters and returns.",
                    "sections": [
                        {"heading": "Syntax", "content": "function name(type $param): returnType { }"},
                        {"heading": "Example", "content": "```php\n<?php\n  function add(int $a, int $b): int {\n    return $a + $b;\n  }\n  \n  function greet(string $name): string {\n    return 'Hello, ' . $name;\n  }\n?>\n```"}
                    ]
                },
                "story": "'Type hints make your code safer,' Crafter reveals.",
                "task": "Add type hints: function multiply takes two floats, returns float.",
                "starter_code": "<?php\n  function multiply(/* type hints */) {\n    return $a * $b;\n  }",
                "expected_output": "float $a, float $b): float",
                "hints": ["(float $a, float $b): float"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Vault of Records",
        "topic": "$_GET, $_POST, Form validation",
        "description": "Handle user input from forms.",
        "story_intro": "The Vault receives data submitted by users through magical forms!",
        "character": "Form Guardian",
        "character_quote": "Forms are the bridge between users and servers!",
        "icon": "inbox",
        "color": "#4f5488",
        "missions": [
            {
                "id": 1012,
                "title": "$_GET Requests",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "GET Parameters",
                    "overview": "$_GET contains URL query string parameters.",
                    "sections": [
                        {"heading": "$_GET", "content": "Parameters passed in the URL: page.php?name=value"},
                        {"heading": "Example", "content": "```php\n<?php\n  // URL: search.php?q=cats\n  $query = $_GET['q'];  // 'cats'\n  echo 'Searching for: ' . $query;\n?>\n```"}
                    ]
                },
                "story": "'GET data travels in the URL,' Form Guardian explains.",
                "task": "Get the 'id' parameter from the URL.",
                "starter_code": "<?php\n  // Get id from URL\n  $id = ",
                "expected_output": "$_GET['id']",
                "hints": ["$_GET['paramName']"]
            },
            {
                "id": 1013,
                "title": "$_POST Requests",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "POST Parameters",
                    "overview": "$_POST contains data from form submissions.",
                    "sections": [
                        {"heading": "$_POST", "content": "Data sent via POST method (form submissions)."},
                        {"heading": "Example", "content": "```php\n<?php\n  // From form: <input name=\"email\">\n  $email = $_POST['email'];\n  echo 'Email: ' . $email;\n?>\n```"}
                    ]
                },
                "story": "'POST data is hidden in the request body,' Guardian teaches.",
                "task": "Get the 'username' from a form POST submission.",
                "starter_code": "<?php\n  // Get username from form\n  $username = ",
                "expected_output": "$_POST['username']",
                "hints": ["$_POST['fieldName']"]
            },
            {
                "id": 1014,
                "title": "Form Validation",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Validating Input",
                    "overview": "Always validate and sanitize user input.",
                    "sections": [
                        {"heading": "Validation", "content": "Check if data exists and meets requirements."},
                        {"heading": "Example", "content": "```php\n<?php\n  if (empty($_POST['email'])) {\n    $error = 'Email is required';\n  } elseif (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {\n    $error = 'Invalid email format';\n  }\n?>\n```"}
                    ]
                },
                "story": "'Never trust user input!' Guardian warns.",
                "task": "Check if $_POST['name'] is empty and set an error message.",
                "starter_code": "<?php\n  if (/* check if empty */) {\n    $error = 'Name is required';\n  }",
                "expected_output": "empty($_POST['name'])",
                "hints": ["empty() checks if a value is empty"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Database Link",
        "topic": "PDO, Connecting to DB, Queries",
        "description": "Connect PHP to MySQL databases.",
        "story_intro": "The Database Link connects your code to persistent storage!",
        "character": "DB Connector",
        "character_quote": "PDO is the secure way to talk to databases!",
        "icon": "database",
        "color": "#424780",
        "missions": [
            {
                "id": 1015,
                "title": "PDO Connection",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "PHP Data Objects",
                    "overview": "PDO provides a secure interface to databases.",
                    "sections": [
                        {"heading": "Connecting", "content": "Create a PDO instance with connection string."},
                        {"heading": "Example", "content": "```php\n<?php\n  $dsn = 'mysql:host=localhost;dbname=myapp';\n  $pdo = new PDO($dsn, 'username', 'password');\n  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);\n?>\n```"}
                    ]
                },
                "story": "'PDO abstracts database connections,' DB Connector explains.",
                "task": "Create a PDO connection to database 'kawaii_db' on localhost.",
                "starter_code": "<?php\n  $dsn = 'mysql:host=localhost;dbname=",
                "expected_output": "kawaii_db",
                "hints": ["Complete the dbname parameter"]
            },
            {
                "id": 1016,
                "title": "Running Queries",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Executing SQL",
                    "overview": "Use prepared statements for safe queries.",
                    "sections": [
                        {"heading": "Prepared Statements", "content": "Prevent SQL injection with parameter binding."},
                        {"heading": "Example", "content": "```php\n<?php\n  $stmt = $pdo->prepare('SELECT * FROM users WHERE id = ?');\n  $stmt->execute([1]);\n  $user = $stmt->fetch();\n?>\n```"}
                    ]
                },
                "story": "'Prepared statements keep you safe,' Connector teaches.",
                "task": "Prepare a query to select a user by email.",
                "starter_code": "<?php\n  $stmt = $pdo->prepare('SELECT * FROM users WHERE email = ",
                "expected_output": "?')",
                "hints": ["Use ? as a placeholder"]
            },
            {
                "id": 1017,
                "title": "Fetching Results",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Getting Query Results",
                    "overview": "Fetch data from executed queries.",
                    "sections": [
                        {"heading": "Fetch Methods", "content": "fetch() - one row, fetchAll() - all rows"},
                        {"heading": "Example", "content": "```php\n<?php\n  $stmt = $pdo->query('SELECT * FROM products');\n  $products = $stmt->fetchAll(PDO::FETCH_ASSOC);\n  foreach ($products as $product) {\n    echo $product['name'];\n  }\n?>\n```"}
                    ]
                },
                "story": "'fetchAll gets all matching rows,' Connector reveals.",
                "task": "Fetch all rows as associative arrays.",
                "starter_code": "<?php\n  $users = $stmt->fetchAll(",
                "expected_output": "PDO::FETCH_ASSOC)",
                "hints": ["PDO::FETCH_ASSOC returns arrays with column names as keys"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Guard's Key",
        "topic": "Hashing passwords, SQL Injection",
        "description": "Secure your PHP applications.",
        "story_intro": "The Guard protects your application from attacks!",
        "character": "Security Guard",
        "character_quote": "Security is not optional - it's essential!",
        "icon": "shield",
        "color": "#363a6e",
        "missions": [
            {
                "id": 1018,
                "title": "Password Hashing",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Hashing Passwords",
                    "overview": "Never store plain text passwords!",
                    "sections": [
                        {"heading": "password_hash", "content": "Creates a secure hash of the password."},
                        {"heading": "Example", "content": "```php\n<?php\n  // Storing password\n  $hash = password_hash('mypassword', PASSWORD_DEFAULT);\n  \n  // Verifying password\n  if (password_verify('mypassword', $hash)) {\n    echo 'Password correct!';\n  }\n?>\n```"}
                    ]
                },
                "story": "'Always hash passwords before storing,' Security Guard insists.",
                "task": "Hash a password using PASSWORD_DEFAULT algorithm.",
                "starter_code": "<?php\n  $password = 'secret123';\n  $hash = ",
                "expected_output": "password_hash($password, PASSWORD_DEFAULT)",
                "hints": ["password_hash($password, PASSWORD_DEFAULT)"]
            },
            {
                "id": 1019,
                "title": "Preventing SQL Injection",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "SQL Injection Prevention",
                    "overview": "SQL injection is a critical vulnerability.",
                    "sections": [
                        {"heading": "The Problem", "content": "Inserting user input directly into SQL allows attacks."},
                        {"heading": "The Solution", "content": "```php\n<?php\n  // BAD - vulnerable!\n  $sql = \"SELECT * FROM users WHERE id = $id\";\n  \n  // GOOD - safe!\n  $stmt = $pdo->prepare('SELECT * FROM users WHERE id = ?');\n  $stmt->execute([$id]);\n?>\n```"}
                    ]
                },
                "story": "'Prepared statements are your shield,' Guard teaches.",
                "task": "Which is the secure way to include user input in a query?",
                "starter_code": "// Secure method: ",
                "expected_output": "prepared statements",
                "hints": ["Use prepare() and execute() with placeholders"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Identity Scrolls",
        "topic": "Cookies, Session management",
        "description": "Manage user sessions and state.",
        "story_intro": "Identity Scrolls remember who users are across requests!",
        "character": "Session Keeper",
        "character_quote": "Sessions maintain state in a stateless protocol!",
        "icon": "user-check",
        "color": "#2d3166",
        "missions": [
            {
                "id": 1020,
                "title": "Cookies",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Working with Cookies",
                    "overview": "Cookies store small data on the client.",
                    "sections": [
                        {"heading": "setcookie", "content": "Set cookies before any output."},
                        {"heading": "Example", "content": "```php\n<?php\n  // Set a cookie (expires in 1 hour)\n  setcookie('username', 'sakura', time() + 3600);\n  \n  // Read a cookie\n  $username = $_COOKIE['username'];\n?>\n```"}
                    ]
                },
                "story": "'Cookies persist data in the browser,' Session Keeper explains.",
                "task": "Set a cookie named 'theme' with value 'dark'.",
                "starter_code": "<?php\n  // Set theme cookie\n  ",
                "expected_output": "setcookie('theme', 'dark'",
                "hints": ["setcookie('name', 'value')"]
            },
            {
                "id": 1021,
                "title": "Session Management",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "PHP Sessions",
                    "overview": "Sessions store data on the server, linked by a session ID.",
                    "sections": [
                        {"heading": "Starting Sessions", "content": "Call session_start() at the beginning of your script."},
                        {"heading": "Example", "content": "```php\n<?php\n  session_start();\n  \n  // Store in session\n  $_SESSION['user_id'] = 123;\n  \n  // Read from session\n  $userId = $_SESSION['user_id'];\n  \n  // Destroy session (logout)\n  session_destroy();\n?>\n```"}
                    ]
                },
                "story": "'Sessions are more secure than cookies for sensitive data,' Keeper teaches.",
                "task": "Start a session and store 'logged_in' as true.",
                "starter_code": "<?php\n  // Start session and set logged_in\n  ",
                "expected_output": "session_start(); $_SESSION['logged_in'] = true",
                "hints": ["session_start() then $_SESSION['key'] = value"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Object Architects",
        "topic": "Classes, Namespaces, Interfaces",
        "description": "Object-oriented programming in PHP.",
        "story_intro": "Architects design blueprints (classes) for creating objects!",
        "character": "Class Designer",
        "character_quote": "OOP organizes code into reusable structures!",
        "icon": "box",
        "color": "#262959",
        "missions": [
            {
                "id": 1022,
                "title": "Classes",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Creating Classes",
                    "overview": "Classes are blueprints for objects.",
                    "sections": [
                        {"heading": "Syntax", "content": "class Name { properties; methods; }"},
                        {"heading": "Example", "content": "```php\n<?php\n  class User {\n    public $name;\n    \n    public function __construct($name) {\n      $this->name = $name;\n    }\n    \n    public function greet() {\n      return 'Hello, ' . $this->name;\n    }\n  }\n  \n  $user = new User('Sakura');\n  echo $user->greet();\n?>\n```"}
                    ]
                },
                "story": "'Classes define the structure of objects,' Class Designer explains.",
                "task": "Create a class Product with a public $name property.",
                "starter_code": "<?php\n  class Product {\n    // Add name property\n  }",
                "expected_output": "public $name",
                "hints": ["public $name; inside the class"]
            },
            {
                "id": 1023,
                "title": "Namespaces",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Organizing with Namespaces",
                    "overview": "Namespaces prevent naming conflicts.",
                    "sections": [
                        {"heading": "Declaring", "content": "namespace MyApp\\Models;"},
                        {"heading": "Example", "content": "```php\n<?php\n  namespace App\\Models;\n  \n  class User { }\n  \n  // Using the class\n  use App\\Models\\User;\n  $user = new User();\n?>\n```"}
                    ]
                },
                "story": "'Namespaces organize code into logical groups,' Designer teaches.",
                "task": "Declare a namespace for App\\Controllers.",
                "starter_code": "<?php\n  // Declare namespace\n  ",
                "expected_output": "namespace App\\Controllers",
                "hints": ["namespace Path\\To\\Namespace;"]
            },
            {
                "id": 1024,
                "title": "Interfaces",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Defining Contracts",
                    "overview": "Interfaces define method signatures that classes must implement.",
                    "sections": [
                        {"heading": "Interface", "content": "interface Name { public function method(); }"},
                        {"heading": "Example", "content": "```php\n<?php\n  interface Payable {\n    public function pay(float $amount): bool;\n  }\n  \n  class Order implements Payable {\n    public function pay(float $amount): bool {\n      return true;\n    }\n  }\n?>\n```"}
                    ]
                },
                "story": "'Interfaces ensure classes follow contracts,' Designer reveals.",
                "task": "Create an interface Printable with a print() method.",
                "starter_code": "<?php\n  interface Printable {\n    // Add print method\n  }",
                "expected_output": "public function print()",
                "hints": ["public function methodName();"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Package Courier",
        "topic": "Using libraries, Autoloading",
        "description": "Manage dependencies with Composer.",
        "story_intro": "The Package Courier delivers libraries from across the realm!",
        "character": "Courier Master",
        "character_quote": "Composer manages your dependencies automatically!",
        "icon": "truck",
        "color": "#1f224d",
        "missions": [
            {
                "id": 1025,
                "title": "Composer Basics",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Using Composer",
                    "overview": "Composer is PHP's dependency manager.",
                    "sections": [
                        {"heading": "Commands", "content": "composer init - create project\ncomposer require package - add dependency\ncomposer install - install dependencies"},
                        {"heading": "Example", "content": "```bash\n# Install a package\ncomposer require monolog/monolog\n\n# In PHP\nrequire 'vendor/autoload.php';\nuse Monolog\\Logger;\n```"}
                    ]
                },
                "story": "'Composer downloads packages from Packagist,' Courier Master explains.",
                "task": "What file does Composer create to track dependencies?",
                "starter_code": "// Composer config file: ",
                "expected_output": "composer.json",
                "hints": ["composer.json lists all dependencies"]
            },
            {
                "id": 1026,
                "title": "Autoloading",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "PSR-4 Autoloading",
                    "overview": "Autoloading loads classes automatically when needed.",
                    "sections": [
                        {"heading": "Setup", "content": "Include vendor/autoload.php once, classes load automatically."},
                        {"heading": "Example", "content": "```php\n<?php\n  // At the top of your app\n  require __DIR__ . '/vendor/autoload.php';\n  \n  // Classes are now autoloaded!\n  use App\\Models\\User;\n  $user = new User();\n?>\n```"}
                    ]
                },
                "story": "'Autoloading saves you from manual requires,' Courier teaches.",
                "task": "What file do you require to enable Composer autoloading?",
                "starter_code": "<?php\n  require ",
                "expected_output": "'vendor/autoload.php'",
                "hints": ["vendor/autoload.php"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Frame of the Realm",
        "topic": "Introduction to Laravel/MVC",
        "description": "Discover PHP frameworks and the MVC pattern.",
        "story_intro": "Frameworks provide structure for building large applications!",
        "character": "Framework Sage",
        "character_quote": "Frameworks accelerate development with proven patterns!",
        "icon": "layers",
        "color": "#191b40",
        "missions": [
            {
                "id": 1027,
                "title": "MVC Pattern",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Model-View-Controller",
                    "overview": "MVC separates concerns in your application.",
                    "sections": [
                        {"heading": "Components", "content": "Model - data and logic\nView - presentation\nController - handles requests, coordinates Model and View"},
                        {"heading": "Flow", "content": "Request -> Controller -> Model -> View -> Response"}
                    ]
                },
                "story": "'MVC keeps your code organized,' Framework Sage explains.",
                "task": "Which MVC component handles data and business logic?",
                "starter_code": "// Data and logic: ",
                "expected_output": "Model",
                "hints": ["Model handles data"]
            },
            {
                "id": 1028,
                "title": "Laravel Introduction",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Laravel Framework",
                    "overview": "Laravel is PHP's most popular framework.",
                    "sections": [
                        {"heading": "Features", "content": "Eloquent ORM, Blade templating, Artisan CLI, Authentication, Routing"},
                        {"heading": "Example Route", "content": "```php\n<?php\n  // routes/web.php\n  Route::get('/users', function () {\n    return view('users.index');\n  });\n  \n  Route::get('/users/{id}', [UserController::class, 'show']);\n?>\n```"}
                    ]
                },
                "story": "'Laravel makes PHP development elegant,' Sage teaches.",
                "task": "What command creates a new Laravel project?",
                "starter_code": "// Create Laravel project: composer ",
                "expected_output": "create-project laravel/laravel",
                "hints": ["composer create-project laravel/laravel projectname"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Master Weaver",
        "topic": "Building a dynamic Blog/CMS",
        "description": "Build a complete PHP application.",
        "story_intro": "The Master Weaver creates complete applications from scratch!",
        "character": "Grand Weaver",
        "character_quote": "Combine all your skills to build something amazing!",
        "icon": "trophy",
        "color": "#ff7f50",
        "missions": [
            {
                "id": 1029,
                "title": "Blog Structure",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Planning the Blog",
                    "overview": "A blog needs posts, users, and authentication.",
                    "sections": [
                        {"heading": "Components", "content": "1. Database: posts, users tables\n2. Authentication: login, register\n3. CRUD: Create, Read, Update, Delete posts\n4. Templates: Layout, post list, single post"},
                        {"heading": "Structure", "content": "```\n/public/index.php\n/src/Controllers/\n/src/Models/\n/templates/\n/config/database.php\n```"}
                    ]
                },
                "story": "'Plan your architecture before coding,' Grand Weaver advises.",
                "task": "What does CRUD stand for?",
                "starter_code": "// CRUD: ",
                "expected_output": "Create, Read, Update, Delete",
                "hints": ["Four basic database operations"]
            },
            {
                "id": 1030,
                "title": "PHP Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are Ready",
                    "overview": "You've learned the full PHP stack!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- PHP syntax and data types\n- Control structures and functions\n- Forms and validation\n- PDO and database access\n- Security best practices\n- Sessions and authentication\n- OOP and namespaces\n- Composer and autoloading\n- MVC and frameworks"},
                        {"heading": "Next Steps", "content": "Build real projects, learn Laravel deeply, explore APIs!"}
                    ]
                },
                "story": "'You are now a PHP Web Weaver!' Grand Weaver declares.",
                "task": "List three key security practices for PHP applications.",
                "starter_code": "// Security practices:\n// 1. ",
                "expected_output": "hash passwords, prepared statements, validate input",
                "hints": ["Password hashing, SQL injection prevention, input validation"]
            }
        ]
    }
]

DEVOPS_ARCS = [
    {
        "id": 1,
        "name": "The Save Point",
        "topic": "init, add, commit, log",
        "description": "Learn the basics of Git version control.",
        "story_intro": "Welcome to the Temporal Gates! Here you'll learn to save and travel through code history.",
        "character": "Time Keeper",
        "character_quote": "Git lets you save your progress at any point in time!",
        "icon": "save",
        "color": "#f05033",
        "missions": [
            {
                "id": 1101,
                "title": "Git Init",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Initializing a Repository",
                    "overview": "git init creates a new Git repository in your project.",
                    "sections": [
                        {"heading": "Creating a Repo", "content": "Run git init in any folder to start tracking changes."},
                        {"heading": "Example", "content": "```bash\nmkdir my-project\ncd my-project\ngit init\n# Creates .git folder\n```"}
                    ]
                },
                "story": "'Every journey begins with git init,' Time Keeper explains.",
                "task": "What command initializes a new Git repository?",
                "starter_code": "# Initialize repository:\n",
                "expected_output": "git init",
                "hints": ["git init"]
            },
            {
                "id": 1102,
                "title": "Git Add",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Staging Changes",
                    "overview": "git add stages files for the next commit.",
                    "sections": [
                        {"heading": "Staging", "content": "Stage specific files or all changes."},
                        {"heading": "Example", "content": "```bash\ngit add file.txt    # Stage one file\ngit add .           # Stage all changes\ngit add *.js        # Stage all JS files\n```"}
                    ]
                },
                "story": "'Staging prepares your changes for saving,' Time Keeper teaches.",
                "task": "What command stages all changed files?",
                "starter_code": "# Stage all changes:\n",
                "expected_output": "git add .",
                "hints": ["git add ."]
            },
            {
                "id": 1103,
                "title": "Git Commit",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Saving Changes",
                    "overview": "git commit saves your staged changes with a message.",
                    "sections": [
                        {"heading": "Committing", "content": "Each commit is a save point in history."},
                        {"heading": "Example", "content": "```bash\ngit commit -m \"Add login feature\"\ngit commit -m \"Fix bug in navigation\"\n```"}
                    ]
                },
                "story": "'Commits are save points in your timeline,' Time Keeper reveals.",
                "task": "Write a commit command with message 'Initial commit'.",
                "starter_code": "# Create commit:\n",
                "expected_output": "git commit -m \"Initial commit\"",
                "hints": ["git commit -m \"message\""]
            },
            {
                "id": 1104,
                "title": "Git Log",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Viewing History",
                    "overview": "git log shows the commit history.",
                    "sections": [
                        {"heading": "Log Options", "content": "View commits with various formats."},
                        {"heading": "Example", "content": "```bash\ngit log              # Full log\ngit log --oneline    # Compact view\ngit log -n 5         # Last 5 commits\n```"}
                    ]
                },
                "story": "'The log reveals all past save points,' Time Keeper explains.",
                "task": "What command shows a compact one-line commit history?",
                "starter_code": "# View compact log:\n",
                "expected_output": "git log --oneline",
                "hints": ["git log --oneline"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Branching Paths",
        "topic": "checkout, switch, branch logic",
        "description": "Create and navigate between branches.",
        "story_intro": "Branches let you explore different timelines without affecting the main path!",
        "character": "Branch Walker",
        "character_quote": "Branches are parallel universes for your code!",
        "icon": "git-branch",
        "color": "#e84d31",
        "missions": [
            {
                "id": 1105,
                "title": "Creating Branches",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Branch Basics",
                    "overview": "Branches let you work on features independently.",
                    "sections": [
                        {"heading": "Branch Commands", "content": "Create, list, and delete branches."},
                        {"heading": "Example", "content": "```bash\ngit branch feature-login  # Create branch\ngit branch                 # List branches\ngit branch -d old-branch   # Delete branch\n```"}
                    ]
                },
                "story": "'Create a new path with git branch,' Branch Walker explains.",
                "task": "Create a new branch called 'feature-auth'.",
                "starter_code": "# Create branch:\n",
                "expected_output": "git branch feature-auth",
                "hints": ["git branch branch-name"]
            },
            {
                "id": 1106,
                "title": "Switching Branches",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Checkout and Switch",
                    "overview": "Move between branches to work on different features.",
                    "sections": [
                        {"heading": "Switching", "content": "Use checkout or switch to change branches."},
                        {"heading": "Example", "content": "```bash\ngit checkout main           # Old way\ngit switch main             # New way\ngit switch -c new-feature   # Create and switch\n```"}
                    ]
                },
                "story": "'Switch moves you to a different timeline,' Branch Walker teaches.",
                "task": "Switch to the 'develop' branch using the modern command.",
                "starter_code": "# Switch to develop:\n",
                "expected_output": "git switch develop",
                "hints": ["git switch branch-name"]
            },
            {
                "id": 1107,
                "title": "Branch Logic",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Branching Strategy",
                    "overview": "Use branches strategically for features and fixes.",
                    "sections": [
                        {"heading": "Common Branches", "content": "main/master - production\ndevelop - integration\nfeature/* - new features\nhotfix/* - urgent fixes"},
                        {"heading": "Workflow", "content": "```\nmain\n  |\n  +-- develop\n        |\n        +-- feature/login\n        +-- feature/signup\n```"}
                    ]
                },
                "story": "'A good branching strategy keeps chaos at bay,' Branch Walker reveals.",
                "task": "What branch typically contains production-ready code?",
                "starter_code": "# Production branch:\n",
                "expected_output": "main",
                "hints": ["main or master"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Timeline Merging",
        "topic": "Merge, Rebase, Conflict resolution",
        "description": "Combine branches and resolve conflicts.",
        "story_intro": "Merging brings different timelines together into one!",
        "character": "Merge Master",
        "character_quote": "Merging unites parallel paths into a single timeline!",
        "icon": "git-merge",
        "color": "#d13f2f",
        "missions": [
            {
                "id": 1108,
                "title": "Git Merge",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Merging Branches",
                    "overview": "Merge combines changes from different branches.",
                    "sections": [
                        {"heading": "Merge", "content": "Merge brings another branch into your current branch."},
                        {"heading": "Example", "content": "```bash\ngit switch main\ngit merge feature-login\n# Feature changes now in main\n```"}
                    ]
                },
                "story": "'Merge combines two timelines,' Merge Master explains.",
                "task": "Merge the 'feature' branch into your current branch.",
                "starter_code": "# Merge feature:\n",
                "expected_output": "git merge feature",
                "hints": ["git merge branch-name"]
            },
            {
                "id": 1109,
                "title": "Git Rebase",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Rebasing",
                    "overview": "Rebase replays commits on top of another branch.",
                    "sections": [
                        {"heading": "Rebase vs Merge", "content": "Rebase creates a linear history, merge preserves branch structure."},
                        {"heading": "Example", "content": "```bash\ngit switch feature\ngit rebase main\n# Feature commits now on top of main\n```"}
                    ]
                },
                "story": "'Rebase rewrites history for a cleaner timeline,' Merge Master teaches.",
                "task": "Rebase your current branch onto main.",
                "starter_code": "# Rebase onto main:\n",
                "expected_output": "git rebase main",
                "hints": ["git rebase target-branch"]
            },
            {
                "id": 1110,
                "title": "Conflict Resolution",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Resolving Conflicts",
                    "overview": "Conflicts occur when the same lines are changed differently.",
                    "sections": [
                        {"heading": "Conflict Markers", "content": "<<<<<<< HEAD\nyour changes\n=======\ntheir changes\n>>>>>>> branch"},
                        {"heading": "Resolution", "content": "```bash\n# 1. Edit the file to resolve\n# 2. Remove conflict markers\n# 3. Stage the resolved file\ngit add resolved-file.txt\n# 4. Continue merge/rebase\ngit merge --continue\n```"}
                    ]
                },
                "story": "'Conflicts are just two timelines disagreeing,' Merge Master reveals.",
                "task": "After resolving a conflict, what command stages the fixed file?",
                "starter_code": "# Stage resolved file:\n",
                "expected_output": "git add",
                "hints": ["git add filename"]
            }
        ]
    },
    {
        "id": 4,
        "name": "The Cloud Archive",
        "topic": "Remotes, push, pull, clone",
        "description": "Work with remote repositories on GitHub.",
        "story_intro": "The Cloud Archive stores your code in the sky for all to access!",
        "character": "Cloud Archivist",
        "character_quote": "GitHub is where code lives in the cloud!",
        "icon": "cloud",
        "color": "#24292e",
        "missions": [
            {
                "id": 1111,
                "title": "Remote Repositories",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Git Remotes",
                    "overview": "Remotes are connections to repositories on servers like GitHub.",
                    "sections": [
                        {"heading": "Managing Remotes", "content": "Add, view, and remove remote connections."},
                        {"heading": "Example", "content": "```bash\ngit remote add origin https://github.com/user/repo.git\ngit remote -v    # List remotes\ngit remote remove origin\n```"}
                    ]
                },
                "story": "'Remotes connect your local repo to the cloud,' Cloud Archivist explains.",
                "task": "Add a remote called 'origin' pointing to a GitHub URL.",
                "starter_code": "# Add remote:\ngit remote add origin ",
                "expected_output": "https://github.com/user/repo.git",
                "hints": ["git remote add origin URL"]
            },
            {
                "id": 1112,
                "title": "Git Push",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Pushing Changes",
                    "overview": "Push sends your commits to the remote repository.",
                    "sections": [
                        {"heading": "Push", "content": "Upload local commits to the remote."},
                        {"heading": "Example", "content": "```bash\ngit push origin main        # Push to main\ngit push -u origin main     # Set upstream\ngit push                    # After upstream is set\n```"}
                    ]
                },
                "story": "'Push uploads your timeline to the cloud,' Cloud Archivist teaches.",
                "task": "Push your main branch to origin.",
                "starter_code": "# Push to remote:\n",
                "expected_output": "git push origin main",
                "hints": ["git push remote-name branch-name"]
            },
            {
                "id": 1113,
                "title": "Git Pull",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Pulling Changes",
                    "overview": "Pull downloads and merges remote changes.",
                    "sections": [
                        {"heading": "Pull", "content": "Fetch + merge in one command."},
                        {"heading": "Example", "content": "```bash\ngit pull origin main    # Pull from main\ngit pull                # Pull from upstream\ngit fetch               # Download without merging\n```"}
                    ]
                },
                "story": "'Pull brings the latest from the cloud,' Cloud Archivist reveals.",
                "task": "Pull the latest changes from origin main.",
                "starter_code": "# Pull from remote:\n",
                "expected_output": "git pull origin main",
                "hints": ["git pull origin main"]
            },
            {
                "id": 1114,
                "title": "Git Clone",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Cloning Repositories",
                    "overview": "Clone downloads an entire repository.",
                    "sections": [
                        {"heading": "Clone", "content": "Creates a complete copy of a remote repository."},
                        {"heading": "Example", "content": "```bash\ngit clone https://github.com/user/repo.git\ngit clone git@github.com:user/repo.git  # SSH\ngit clone URL folder-name               # Custom folder\n```"}
                    ]
                },
                "story": "'Clone copies an entire repository to your machine,' Archivist explains.",
                "task": "Clone a repository from a GitHub URL.",
                "starter_code": "# Clone repo:\ngit clone ",
                "expected_output": "https://github.com/",
                "hints": ["git clone URL"]
            }
        ]
    },
    {
        "id": 5,
        "name": "The Royal Decree",
        "topic": "PRs, Code Review, Forking",
        "description": "Collaborate using Pull Requests and forks.",
        "story_intro": "The Royal Decree governs how changes are proposed and approved!",
        "character": "Review Elder",
        "character_quote": "Pull Requests are proposals for change!",
        "icon": "git-pull-request",
        "color": "#6f42c1",
        "missions": [
            {
                "id": 1115,
                "title": "Pull Requests",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Creating PRs",
                    "overview": "Pull Requests propose merging one branch into another.",
                    "sections": [
                        {"heading": "PR Workflow", "content": "1. Create feature branch\n2. Make commits\n3. Push to remote\n4. Open PR on GitHub\n5. Review and merge"},
                        {"heading": "Best Practices", "content": "- Clear title and description\n- Reference issues\n- Keep PRs small and focused"}
                    ]
                },
                "story": "'PRs let others review before merging,' Review Elder explains.",
                "task": "What does PR stand for in GitHub?",
                "starter_code": "# PR stands for:\n",
                "expected_output": "Pull Request",
                "hints": ["Pull Request"]
            },
            {
                "id": 1116,
                "title": "Code Review",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Reviewing Code",
                    "overview": "Code review ensures quality and catches bugs.",
                    "sections": [
                        {"heading": "Review Process", "content": "1. Read the PR description\n2. Review changed files\n3. Leave comments/suggestions\n4. Approve, request changes, or comment"},
                        {"heading": "Good Reviews", "content": "- Be constructive\n- Explain your reasoning\n- Suggest improvements\n- Acknowledge good code"}
                    ]
                },
                "story": "'Reviews catch bugs and improve code quality,' Review Elder teaches.",
                "task": "What are the three review actions on GitHub?",
                "starter_code": "# Review actions:\n",
                "expected_output": "Approve, Request Changes, Comment",
                "hints": ["Approve, Request Changes, Comment"]
            },
            {
                "id": 1117,
                "title": "Forking",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Fork Workflow",
                    "overview": "Forks let you contribute to projects you don't own.",
                    "sections": [
                        {"heading": "Fork Process", "content": "1. Fork the repo on GitHub\n2. Clone your fork\n3. Make changes\n4. Push to your fork\n5. Open PR to original repo"},
                        {"heading": "Keeping Updated", "content": "```bash\ngit remote add upstream URL\ngit fetch upstream\ngit merge upstream/main\n```"}
                    ]
                },
                "story": "'Forks let anyone contribute to open source,' Review Elder reveals.",
                "task": "What is a fork in GitHub?",
                "starter_code": "# A fork is:\n",
                "expected_output": "A copy of a repository under your account",
                "hints": ["Your own copy of someone else's repository"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Command Command",
        "topic": "Terminal basics, Scripting",
        "description": "Master the command line and bash scripting.",
        "story_intro": "The Command Command center controls everything through text!",
        "character": "Terminal Sage",
        "character_quote": "The terminal is the most powerful interface!",
        "icon": "terminal",
        "color": "#4d4d4d",
        "missions": [
            {
                "id": 1118,
                "title": "Terminal Basics",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Essential Commands",
                    "overview": "Navigate and manipulate files from the command line.",
                    "sections": [
                        {"heading": "Navigation", "content": "ls - list files\ncd - change directory\npwd - print working directory\nmkdir - make directory"},
                        {"heading": "Example", "content": "```bash\nls -la          # List all with details\ncd projects     # Enter folder\npwd             # Where am I?\nmkdir new-app   # Create folder\n```"}
                    ]
                },
                "story": "'The terminal is your direct connection to the system,' Terminal Sage explains.",
                "task": "What command lists all files including hidden ones?",
                "starter_code": "# List all files:\n",
                "expected_output": "ls -la",
                "hints": ["ls -la or ls -a"]
            },
            {
                "id": 1119,
                "title": "Bash Scripting",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Writing Scripts",
                    "overview": "Bash scripts automate command sequences.",
                    "sections": [
                        {"heading": "Script Basics", "content": "Start with #!/bin/bash (shebang)\nMake executable with chmod +x"},
                        {"heading": "Example", "content": "```bash\n#!/bin/bash\necho \"Starting deployment...\"\ngit pull origin main\nnpm install\nnpm run build\necho \"Done!\"\n```"}
                    ]
                },
                "story": "'Scripts automate repetitive tasks,' Terminal Sage teaches.",
                "task": "What line should start every bash script?",
                "starter_code": "# Shebang line:\n",
                "expected_output": "#!/bin/bash",
                "hints": ["#!/bin/bash"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Automated Guard",
        "topic": "CI/CD, GitHub Actions, Testing pipes",
        "description": "Automate testing and deployment with CI/CD.",
        "story_intro": "The Automated Guard watches your code and tests it automatically!",
        "character": "Automation Spirit",
        "character_quote": "CI/CD automates your entire workflow!",
        "icon": "play-circle",
        "color": "#2088ff",
        "missions": [
            {
                "id": 1120,
                "title": "CI/CD Concepts",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Continuous Integration/Deployment",
                    "overview": "CI/CD automates building, testing, and deploying code.",
                    "sections": [
                        {"heading": "CI - Continuous Integration", "content": "Automatically build and test code on every push."},
                        {"heading": "CD - Continuous Deployment", "content": "Automatically deploy passing builds to production."}
                    ]
                },
                "story": "'CI/CD is the guardian that never sleeps,' Automation Spirit explains.",
                "task": "What does CI stand for?",
                "starter_code": "# CI means:\n",
                "expected_output": "Continuous Integration",
                "hints": ["Continuous Integration"]
            },
            {
                "id": 1121,
                "title": "GitHub Actions",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "GitHub Actions Basics",
                    "overview": "GitHub Actions runs workflows on GitHub events.",
                    "sections": [
                        {"heading": "Workflow File", "content": "Create .github/workflows/ci.yml"},
                        {"heading": "Example", "content": "```yaml\nname: CI\non: [push, pull_request]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - run: npm install\n      - run: npm test\n```"}
                    ]
                },
                "story": "'GitHub Actions runs your tests automatically,' Automation Spirit teaches.",
                "task": "Where do GitHub Actions workflow files go?",
                "starter_code": "# Workflow location:\n",
                "expected_output": ".github/workflows/",
                "hints": [".github/workflows/"]
            },
            {
                "id": 1122,
                "title": "Testing Pipelines",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Building Test Pipelines",
                    "overview": "Test pipelines run multiple checks on your code.",
                    "sections": [
                        {"heading": "Pipeline Stages", "content": "1. Lint - code style\n2. Unit tests\n3. Integration tests\n4. Build\n5. Deploy"},
                        {"heading": "Example", "content": "```yaml\njobs:\n  lint:\n    runs-on: ubuntu-latest\n    steps:\n      - run: npm run lint\n  test:\n    needs: lint\n    runs-on: ubuntu-latest\n    steps:\n      - run: npm test\n```"}
                    ]
                },
                "story": "'Pipelines ensure nothing breaks,' Automation Spirit reveals.",
                "task": "What keyword makes a job wait for another to complete?",
                "starter_code": "# Job dependency:\n",
                "expected_output": "needs",
                "hints": ["needs: job-name"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Magic Boxes",
        "topic": "Containers, Images, Dockerfile",
        "description": "Package applications with Docker.",
        "story_intro": "Magic Boxes contain entire environments that run anywhere!",
        "character": "Container Wizard",
        "character_quote": "Docker packages your app with everything it needs!",
        "icon": "box",
        "color": "#2496ed",
        "missions": [
            {
                "id": 1123,
                "title": "Container Concepts",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "What Are Containers",
                    "overview": "Containers package code with all dependencies.",
                    "sections": [
                        {"heading": "Containers vs VMs", "content": "Containers share the OS kernel - lighter than VMs.\nIsolated but efficient."},
                        {"heading": "Benefits", "content": "- Consistent environments\n- Easy deployment\n- Scalability\n- Isolation"}
                    ]
                },
                "story": "'Containers are portable environments,' Container Wizard explains.",
                "task": "What platform is most popular for containers?",
                "starter_code": "# Container platform:\n",
                "expected_output": "Docker",
                "hints": ["Docker"]
            },
            {
                "id": 1124,
                "title": "Docker Images",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Working with Images",
                    "overview": "Images are blueprints for containers.",
                    "sections": [
                        {"heading": "Image Commands", "content": "docker pull - download image\ndocker images - list images\ndocker run - create container from image"},
                        {"heading": "Example", "content": "```bash\ndocker pull node:18\ndocker images\ndocker run -it node:18 node -v\n```"}
                    ]
                },
                "story": "'Images are templates for containers,' Container Wizard teaches.",
                "task": "What command downloads a Docker image?",
                "starter_code": "# Download image:\n",
                "expected_output": "docker pull",
                "hints": ["docker pull image-name"]
            },
            {
                "id": 1125,
                "title": "Dockerfile",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Building Custom Images",
                    "overview": "Dockerfile defines how to build your image.",
                    "sections": [
                        {"heading": "Dockerfile Commands", "content": "FROM - base image\nWORKDIR - set directory\nCOPY - copy files\nRUN - execute commands\nCMD - default command"},
                        {"heading": "Example", "content": "```dockerfile\nFROM node:18\nWORKDIR /app\nCOPY package*.json ./\nRUN npm install\nCOPY . .\nCMD [\"npm\", \"start\"]\n```"}
                    ]
                },
                "story": "'Dockerfile is your image recipe,' Container Wizard reveals.",
                "task": "What Dockerfile instruction sets the base image?",
                "starter_code": "# Base image instruction:\n",
                "expected_output": "FROM",
                "hints": ["FROM image:tag"]
            }
        ]
    },
    {
        "id": 9,
        "name": "The Box Fleet",
        "topic": "Kubernetes basics, Pods",
        "description": "Orchestrate containers at scale with Kubernetes.",
        "story_intro": "The Box Fleet manages thousands of containers in harmony!",
        "character": "Fleet Commander",
        "character_quote": "Kubernetes orchestrates containers at any scale!",
        "icon": "layers",
        "color": "#326ce5",
        "missions": [
            {
                "id": 1126,
                "title": "Kubernetes Basics",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "What is Kubernetes",
                    "overview": "Kubernetes (K8s) manages containerized applications.",
                    "sections": [
                        {"heading": "K8s Features", "content": "- Auto-scaling\n- Self-healing\n- Load balancing\n- Rolling updates"},
                        {"heading": "Components", "content": "Cluster - collection of nodes\nNode - a machine (VM or physical)\nPod - smallest deployable unit"}
                    ]
                },
                "story": "'Kubernetes manages fleets of containers,' Fleet Commander explains.",
                "task": "What is K8s short for?",
                "starter_code": "# K8s means:\n",
                "expected_output": "Kubernetes",
                "hints": ["Kubernetes (K-8 letters-s)"]
            },
            {
                "id": 1127,
                "title": "Pods",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Working with Pods",
                    "overview": "Pods are the smallest unit in Kubernetes.",
                    "sections": [
                        {"heading": "Pod Basics", "content": "A Pod runs one or more containers.\nContainers in a Pod share networking and storage."},
                        {"heading": "kubectl Commands", "content": "```bash\nkubectl get pods         # List pods\nkubectl describe pod X   # Pod details\nkubectl logs pod-name    # View logs\nkubectl delete pod X     # Remove pod\n```"}
                    ]
                },
                "story": "'Pods are the atoms of Kubernetes,' Fleet Commander teaches.",
                "task": "What command lists all Kubernetes pods?",
                "starter_code": "# List pods:\n",
                "expected_output": "kubectl get pods",
                "hints": ["kubectl get pods"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Portal Casting",
        "topic": "Vercel, Heroku, or AWS basics",
        "description": "Deploy applications to cloud platforms.",
        "story_intro": "Portal Casting opens gateways to make your app accessible worldwide!",
        "character": "Cloud Mage",
        "character_quote": "Deployment platforms host your app for the world!",
        "icon": "globe",
        "color": "#ff6b35",
        "missions": [
            {
                "id": 1128,
                "title": "Deployment Platforms",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Cloud Hosting Options",
                    "overview": "Various platforms host web applications.",
                    "sections": [
                        {"heading": "Platform Types", "content": "PaaS - Vercel, Heroku, Netlify (easy)\nIaaS - AWS, GCP, Azure (flexible)\nServerless - AWS Lambda, Vercel Functions"},
                        {"heading": "Choosing", "content": "- Vercel/Netlify: Frontend/Jamstack\n- Heroku: Full-stack apps\n- AWS: Enterprise, complex needs"}
                    ]
                },
                "story": "'Different platforms suit different needs,' Cloud Mage explains.",
                "task": "What type of platform is Vercel?",
                "starter_code": "# Vercel is a:\n",
                "expected_output": "PaaS",
                "hints": ["Platform as a Service (PaaS)"]
            },
            {
                "id": 1129,
                "title": "Vercel Deployment",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Deploying to Vercel",
                    "overview": "Vercel makes frontend deployment simple.",
                    "sections": [
                        {"heading": "Vercel Features", "content": "- Git integration\n- Automatic deployments\n- Preview deployments\n- Edge network"},
                        {"heading": "Deployment", "content": "```bash\n# Install CLI\nnpm i -g vercel\n# Deploy\nvercel\n# Production deploy\nvercel --prod\n```"}
                    ]
                },
                "story": "'Vercel deploys on every git push,' Cloud Mage teaches.",
                "task": "What command deploys to Vercel production?",
                "starter_code": "# Production deploy:\n",
                "expected_output": "vercel --prod",
                "hints": ["vercel --prod"]
            },
            {
                "id": 1130,
                "title": "AWS Basics",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "AWS Overview",
                    "overview": "AWS offers hundreds of cloud services.",
                    "sections": [
                        {"heading": "Key Services", "content": "EC2 - Virtual servers\nS3 - Object storage\nRDS - Managed databases\nLambda - Serverless functions"},
                        {"heading": "Getting Started", "content": "1. Create AWS account\n2. Use IAM for security\n3. Start with free tier services"}
                    ]
                },
                "story": "'AWS powers much of the internet,' Cloud Mage reveals.",
                "task": "What AWS service provides virtual servers?",
                "starter_code": "# Virtual servers:\n",
                "expected_output": "EC2",
                "hints": ["Elastic Compute Cloud (EC2)"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Watcher's Eye",
        "topic": "Logging, Error tracking",
        "description": "Monitor applications and track errors.",
        "story_intro": "The Watcher's Eye sees all that happens in your application!",
        "character": "Watchful Guardian",
        "character_quote": "Monitoring reveals what's happening in production!",
        "icon": "eye",
        "color": "#9b59b6",
        "missions": [
            {
                "id": 1131,
                "title": "Logging",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Application Logging",
                    "overview": "Logs record what happens in your application.",
                    "sections": [
                        {"heading": "Log Levels", "content": "DEBUG - development details\nINFO - general information\nWARN - potential issues\nERROR - failures"},
                        {"heading": "Best Practices", "content": "- Use structured logging (JSON)\n- Include context (user ID, request ID)\n- Don't log sensitive data\n- Use log aggregation tools"}
                    ]
                },
                "story": "'Logs are your application's diary,' Watchful Guardian explains.",
                "task": "What log level indicates a potential problem?",
                "starter_code": "# Potential problem:\n",
                "expected_output": "WARN",
                "hints": ["WARN or WARNING"]
            },
            {
                "id": 1132,
                "title": "Error Tracking",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Tracking Production Errors",
                    "overview": "Error tracking services catch and report production bugs.",
                    "sections": [
                        {"heading": "Tools", "content": "- Sentry\n- Bugsnag\n- Rollbar\n- New Relic"},
                        {"heading": "Features", "content": "- Stack traces\n- User context\n- Release tracking\n- Alerting"}
                    ]
                },
                "story": "'Error tracking catches bugs before users report them,' Guardian teaches.",
                "task": "Name a popular error tracking service.",
                "starter_code": "# Error tracking service:\n",
                "expected_output": "Sentry",
                "hints": ["Sentry, Bugsnag, or Rollbar"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Time Lord",
        "topic": "Setting up a Full Deployment Pipeline",
        "description": "Build a complete CI/CD deployment pipeline.",
        "story_intro": "The Time Lord commands the entire flow from code to production!",
        "character": "Grand Architect",
        "character_quote": "A full pipeline automates everything from push to production!",
        "icon": "trophy",
        "color": "#f1c40f",
        "missions": [
            {
                "id": 1133,
                "title": "Pipeline Design",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Full Pipeline Architecture",
                    "overview": "A complete pipeline automates the entire delivery process.",
                    "sections": [
                        {"heading": "Pipeline Stages", "content": "1. Code Push\n2. Build\n3. Lint & Test\n4. Security Scan\n5. Build Docker Image\n6. Deploy to Staging\n7. Integration Tests\n8. Deploy to Production\n9. Monitor"},
                        {"heading": "Tools", "content": "Git + GitHub Actions + Docker + Kubernetes + Sentry"}
                    ]
                },
                "story": "'A full pipeline is the ultimate automation,' Grand Architect explains.",
                "task": "What comes after testing in a typical pipeline?",
                "starter_code": "# After testing:\n",
                "expected_output": "Deploy",
                "hints": ["Build or Deploy"]
            },
            {
                "id": 1134,
                "title": "DevOps Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are Ready",
                    "overview": "You've mastered Git and DevOps fundamentals!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- Git version control\n- Branching and merging\n- GitHub collaboration\n- Command line\n- CI/CD with GitHub Actions\n- Docker containers\n- Kubernetes basics\n- Cloud deployment\n- Monitoring"},
                        {"heading": "Next Steps", "content": "Build real pipelines, explore advanced K8s, learn infrastructure as code!"}
                    ]
                },
                "story": "'You are now a Time Lord of DevOps!' Grand Architect declares.",
                "task": "List three key components of a DevOps pipeline.",
                "starter_code": "# Pipeline components:\n",
                "expected_output": "CI, Docker, Deployment",
                "hints": ["Version control, CI/CD, containers, deployment"]
            }
        ]
    }
]

ML_ARCS = [
    {
        "id": 1,
        "name": "The Alchemist's Math",
        "topic": "Linear Algebra, Calculus basics",
        "description": "Learn the mathematical foundations of machine learning.",
        "story_intro": "Welcome to the Mind of the Machine! First, you must master the sacred math that powers AI.",
        "character": "Math Alchemist",
        "character_quote": "Math is the language machines use to think!",
        "icon": "calculator",
        "color": "#ff6f00",
        "missions": [
            {
                "id": 1201,
                "title": "Linear Algebra Basics",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Vectors and Matrices",
                    "overview": "Linear algebra is the foundation of ML computations.",
                    "sections": [
                        {"heading": "Vectors", "content": "Vectors are arrays of numbers representing points or directions.\nv = [1, 2, 3] is a 3D vector"},
                        {"heading": "Matrices", "content": "Matrices are 2D arrays used for transformations.\n```python\nimport numpy as np\nA = np.array([[1, 2], [3, 4]])\n```"}
                    ]
                },
                "story": "'Vectors and matrices are how machines see data,' Math Alchemist explains.",
                "task": "Create a 2x2 numpy matrix with values [[1,2],[3,4]].",
                "starter_code": "import numpy as np\n\n# Create matrix\nA = ",
                "expected_output": "np.array([[1, 2], [3, 4]])",
                "hints": ["np.array([[1, 2], [3, 4]])"]
            },
            {
                "id": 1202,
                "title": "Matrix Operations",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Matrix Math",
                    "overview": "Operations on matrices power neural networks.",
                    "sections": [
                        {"heading": "Operations", "content": "Addition, multiplication, transpose, dot product"},
                        {"heading": "Example", "content": "```python\nA = np.array([[1, 2], [3, 4]])\nB = np.array([[5, 6], [7, 8]])\nC = np.dot(A, B)  # Matrix multiplication\nD = A.T           # Transpose\n```"}
                    ]
                },
                "story": "'Matrix multiplication is how layers connect,' Alchemist teaches.",
                "task": "Compute the dot product of matrices A and B.",
                "starter_code": "import numpy as np\nA = np.array([[1, 2], [3, 4]])\nB = np.array([[5, 6], [7, 8]])\n\nresult = ",
                "expected_output": "np.dot(A, B)",
                "hints": ["np.dot(A, B)"]
            },
            {
                "id": 1203,
                "title": "Calculus Basics",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Derivatives for ML",
                    "overview": "Derivatives measure how functions change - essential for optimization.",
                    "sections": [
                        {"heading": "Gradient", "content": "The gradient points in the direction of steepest increase.\nML uses gradients to minimize error."},
                        {"heading": "Chain Rule", "content": "d/dx f(g(x)) = f'(g(x)) * g'(x)\nThis is how backpropagation works!"}
                    ]
                },
                "story": "'Gradients tell the machine which way to improve,' Alchemist reveals.",
                "task": "What does gradient descent minimize in ML?",
                "starter_code": "# Gradient descent minimizes the:\n",
                "expected_output": "loss function",
                "hints": ["loss function or cost function"]
            }
        ]
    },
    {
        "id": 2,
        "name": "The Scrying Glass",
        "topic": "NumPy, Pandas, Matplotlib",
        "description": "Master the essential data science libraries.",
        "story_intro": "The Scrying Glass reveals patterns in data through visualization!",
        "character": "Data Seer",
        "character_quote": "See the patterns hidden in the numbers!",
        "icon": "eye",
        "color": "#ff8f00",
        "missions": [
            {
                "id": 1204,
                "title": "NumPy Arrays",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "NumPy Fundamentals",
                    "overview": "NumPy provides fast numerical operations.",
                    "sections": [
                        {"heading": "Creating Arrays", "content": "```python\nimport numpy as np\narr = np.array([1, 2, 3, 4, 5])\nzeros = np.zeros((3, 3))\nones = np.ones((2, 4))\n```"},
                        {"heading": "Operations", "content": "Arrays support element-wise operations:\narr * 2, arr + 10, np.sqrt(arr)"}
                    ]
                },
                "story": "'NumPy is the foundation of scientific Python,' Data Seer explains.",
                "task": "Create a numpy array of zeros with shape (3, 3).",
                "starter_code": "import numpy as np\n\nzeros = ",
                "expected_output": "np.zeros((3, 3))",
                "hints": ["np.zeros((rows, cols))"]
            },
            {
                "id": 1205,
                "title": "Pandas DataFrames",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Working with Pandas",
                    "overview": "Pandas provides DataFrames for tabular data.",
                    "sections": [
                        {"heading": "DataFrames", "content": "```python\nimport pandas as pd\ndf = pd.DataFrame({\n    'name': ['Alice', 'Bob'],\n    'age': [25, 30]\n})\n```"},
                        {"heading": "Operations", "content": "df.head(), df.describe(), df['column'], df.loc[0]"}
                    ]
                },
                "story": "'Pandas makes data manipulation intuitive,' Data Seer teaches.",
                "task": "Read a CSV file into a pandas DataFrame.",
                "starter_code": "import pandas as pd\n\ndf = ",
                "expected_output": "pd.read_csv('data.csv')",
                "hints": ["pd.read_csv('filename.csv')"]
            },
            {
                "id": 1206,
                "title": "Matplotlib Plotting",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Data Visualization",
                    "overview": "Matplotlib creates charts and plots.",
                    "sections": [
                        {"heading": "Basic Plots", "content": "```python\nimport matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3], [1, 4, 9])\nplt.xlabel('X axis')\nplt.ylabel('Y axis')\nplt.title('My Plot')\nplt.show()\n```"},
                        {"heading": "Types", "content": "plt.scatter(), plt.bar(), plt.hist(), plt.pie()"}
                    ]
                },
                "story": "'Visualization reveals what numbers hide,' Data Seer reveals.",
                "task": "Create a scatter plot of x and y data.",
                "starter_code": "import matplotlib.pyplot as plt\nx = [1, 2, 3, 4]\ny = [1, 4, 9, 16]\n\nplt.",
                "expected_output": "scatter(x, y)",
                "hints": ["plt.scatter(x, y)"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Purifying the Stream",
        "topic": "Cleaning data, Handling missing values",
        "description": "Prepare raw data for machine learning.",
        "story_intro": "Raw data is like muddy water - it must be purified before use!",
        "character": "Data Cleanser",
        "character_quote": "Clean data is the foundation of good models!",
        "icon": "filter",
        "color": "#ffab00",
        "missions": [
            {
                "id": 1207,
                "title": "Cleaning Data",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Data Cleaning Techniques",
                    "overview": "Real data is messy - learn to clean it.",
                    "sections": [
                        {"heading": "Common Issues", "content": "- Duplicates\n- Incorrect formats\n- Outliers\n- Inconsistent values"},
                        {"heading": "Cleaning", "content": "```python\ndf.drop_duplicates()\ndf['col'] = df['col'].str.lower()\ndf = df[df['age'] > 0]  # Remove invalid\n```"}
                    ]
                },
                "story": "'Garbage in, garbage out,' Data Cleanser warns.",
                "task": "Remove duplicate rows from a DataFrame.",
                "starter_code": "import pandas as pd\ndf = pd.DataFrame({'a': [1, 1, 2], 'b': [3, 3, 4]})\n\ndf_clean = df.",
                "expected_output": "drop_duplicates()",
                "hints": ["df.drop_duplicates()"]
            },
            {
                "id": 1208,
                "title": "Handling Missing Values",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Missing Data Strategies",
                    "overview": "Missing values must be handled carefully.",
                    "sections": [
                        {"heading": "Detecting", "content": "df.isnull().sum() - count missing per column"},
                        {"heading": "Handling", "content": "```python\n# Drop rows with missing values\ndf.dropna()\n\n# Fill with a value\ndf.fillna(0)\ndf.fillna(df.mean())  # Fill with column mean\n```"}
                    ]
                },
                "story": "'Missing data can ruin predictions,' Cleanser teaches.",
                "task": "Fill missing values with the column mean.",
                "starter_code": "import pandas as pd\ndf = pd.DataFrame({'a': [1, None, 3]})\n\ndf_filled = df.fillna(",
                "expected_output": "df.mean())",
                "hints": ["df.fillna(df.mean())"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Line of Sight",
        "topic": "Simple Linear Regression",
        "description": "Learn your first predictive algorithm.",
        "story_intro": "The Line of Sight draws a straight path through the data!",
        "character": "Regression Mage",
        "character_quote": "Find the line that best fits the data!",
        "icon": "trending-up",
        "color": "#ffc400",
        "missions": [
            {
                "id": 1209,
                "title": "Linear Regression Concept",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Understanding Linear Regression",
                    "overview": "Linear regression finds the best-fit line through data.",
                    "sections": [
                        {"heading": "The Line", "content": "y = mx + b\nm = slope, b = intercept"},
                        {"heading": "Goal", "content": "Minimize the sum of squared errors between predictions and actual values."}
                    ]
                },
                "story": "'The line reveals the relationship,' Regression Mage explains.",
                "task": "What is the equation of a line in linear regression?",
                "starter_code": "# Equation: ",
                "expected_output": "y = mx + b",
                "hints": ["y = mx + b"]
            },
            {
                "id": 1210,
                "title": "Implementing Linear Regression",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Sklearn Linear Regression",
                    "overview": "Use scikit-learn to build regression models.",
                    "sections": [
                        {"heading": "Steps", "content": "1. Import model\n2. Create instance\n3. Fit to data\n4. Predict"},
                        {"heading": "Code", "content": "```python\nfrom sklearn.linear_model import LinearRegression\n\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\npredictions = model.predict(X_test)\n```"}
                    ]
                },
                "story": "'Sklearn makes ML accessible,' Regression Mage teaches.",
                "task": "Fit a LinearRegression model to X_train and y_train.",
                "starter_code": "from sklearn.linear_model import LinearRegression\n\nmodel = LinearRegression()\nmodel.",
                "expected_output": "fit(X_train, y_train)",
                "hints": ["model.fit(X_train, y_train)"]
            }
        ]
    },
    {
        "id": 5,
        "name": "The Multi-Path",
        "topic": "Multiple & Polynomial Regression",
        "description": "Handle multiple features and curved relationships.",
        "story_intro": "The Multi-Path sees beyond simple lines to complex patterns!",
        "character": "Polynomial Sage",
        "character_quote": "Some relationships are curved, not straight!",
        "icon": "share-2",
        "color": "#ffd740",
        "missions": [
            {
                "id": 1211,
                "title": "Multiple Regression",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Multiple Features",
                    "overview": "Use multiple input features for better predictions.",
                    "sections": [
                        {"heading": "Equation", "content": "y = b0 + b1*x1 + b2*x2 + ... + bn*xn"},
                        {"heading": "Example", "content": "Predicting house price using:\n- Square footage\n- Number of bedrooms\n- Location score"}
                    ]
                },
                "story": "'More features can mean better predictions,' Polynomial Sage explains.",
                "task": "How many coefficients does a model with 3 features have?",
                "starter_code": "# Number of coefficients (including intercept):\n",
                "expected_output": "4",
                "hints": ["3 features + 1 intercept = 4"]
            },
            {
                "id": 1212,
                "title": "Polynomial Regression",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Curved Relationships",
                    "overview": "Polynomial regression fits curves to data.",
                    "sections": [
                        {"heading": "Concept", "content": "Transform features: x -> [x, x^2, x^3, ...]"},
                        {"heading": "Code", "content": "```python\nfrom sklearn.preprocessing import PolynomialFeatures\n\npoly = PolynomialFeatures(degree=2)\nX_poly = poly.fit_transform(X)\nmodel.fit(X_poly, y)\n```"}
                    ]
                },
                "story": "'Polynomials capture curves in the data,' Sage teaches.",
                "task": "Create polynomial features of degree 2.",
                "starter_code": "from sklearn.preprocessing import PolynomialFeatures\n\npoly = PolynomialFeatures(",
                "expected_output": "degree=2)",
                "hints": ["PolynomialFeatures(degree=2)"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Sorting Gate",
        "topic": "Logistic Regression, K-NN",
        "description": "Learn classification algorithms.",
        "story_intro": "The Sorting Gate decides which category each item belongs to!",
        "character": "Classifier Guardian",
        "character_quote": "Classification assigns labels to data!",
        "icon": "check-square",
        "color": "#ffea00",
        "missions": [
            {
                "id": 1213,
                "title": "Logistic Regression",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Binary Classification",
                    "overview": "Logistic regression predicts probabilities for classification.",
                    "sections": [
                        {"heading": "Sigmoid", "content": "Outputs probability between 0 and 1.\nIf P > 0.5, predict class 1, else class 0"},
                        {"heading": "Code", "content": "```python\nfrom sklearn.linear_model import LogisticRegression\n\nmodel = LogisticRegression()\nmodel.fit(X_train, y_train)\npredictions = model.predict(X_test)\n```"}
                    ]
                },
                "story": "'Logistic regression gives probabilities,' Classifier Guardian explains.",
                "task": "Create a LogisticRegression model.",
                "starter_code": "from sklearn.linear_model import LogisticRegression\n\nmodel = ",
                "expected_output": "LogisticRegression()",
                "hints": ["LogisticRegression()"]
            },
            {
                "id": 1214,
                "title": "K-Nearest Neighbors",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "KNN Classification",
                    "overview": "KNN classifies based on nearby data points.",
                    "sections": [
                        {"heading": "Concept", "content": "Find the K nearest neighbors.\nAssign the most common class among them."},
                        {"heading": "Code", "content": "```python\nfrom sklearn.neighbors import KNeighborsClassifier\n\nknn = KNeighborsClassifier(n_neighbors=5)\nknn.fit(X_train, y_train)\n```"}
                    ]
                },
                "story": "'Birds of a feather flock together,' Guardian teaches.",
                "task": "Create a KNN classifier with 3 neighbors.",
                "starter_code": "from sklearn.neighbors import KNeighborsClassifier\n\nknn = KNeighborsClassifier(",
                "expected_output": "n_neighbors=3)",
                "hints": ["KNeighborsClassifier(n_neighbors=3)"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Wisdom Tree",
        "topic": "Decision Trees, Random Forests",
        "description": "Master tree-based algorithms.",
        "story_intro": "The Wisdom Tree makes decisions by asking questions!",
        "character": "Tree Elder",
        "character_quote": "Trees make decisions through a series of questions!",
        "icon": "git-branch",
        "color": "#c6ff00",
        "missions": [
            {
                "id": 1215,
                "title": "Decision Trees",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Tree-Based Learning",
                    "overview": "Decision trees split data based on features.",
                    "sections": [
                        {"heading": "How It Works", "content": "Each node asks a question about a feature.\nData flows down until reaching a leaf (prediction)."},
                        {"heading": "Code", "content": "```python\nfrom sklearn.tree import DecisionTreeClassifier\n\ntree = DecisionTreeClassifier(max_depth=3)\ntree.fit(X_train, y_train)\n```"}
                    ]
                },
                "story": "'Trees ask questions to classify,' Tree Elder explains.",
                "task": "Create a DecisionTreeClassifier with max_depth=5.",
                "starter_code": "from sklearn.tree import DecisionTreeClassifier\n\ntree = DecisionTreeClassifier(",
                "expected_output": "max_depth=5)",
                "hints": ["DecisionTreeClassifier(max_depth=5)"]
            },
            {
                "id": 1216,
                "title": "Random Forests",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Ensemble Learning",
                    "overview": "Random forests combine many trees for better predictions.",
                    "sections": [
                        {"heading": "Concept", "content": "Train multiple trees on random subsets of data.\nCombine their predictions by voting."},
                        {"heading": "Code", "content": "```python\nfrom sklearn.ensemble import RandomForestClassifier\n\nrf = RandomForestClassifier(n_estimators=100)\nrf.fit(X_train, y_train)\n```"}
                    ]
                },
                "story": "'Many trees are wiser than one,' Tree Elder teaches.",
                "task": "Create a RandomForestClassifier with 50 trees.",
                "starter_code": "from sklearn.ensemble import RandomForestClassifier\n\nrf = RandomForestClassifier(",
                "expected_output": "n_estimators=50)",
                "hints": ["n_estimators=50"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Grouping Spirits",
        "topic": "K-Means Clustering",
        "description": "Discover natural groupings in data.",
        "story_intro": "Grouping Spirits find hidden clusters in unlabeled data!",
        "character": "Cluster Spirit",
        "character_quote": "Unsupervised learning finds patterns without labels!",
        "icon": "target",
        "color": "#76ff03",
        "missions": [
            {
                "id": 1217,
                "title": "K-Means Concept",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Clustering Basics",
                    "overview": "K-Means groups similar data points together.",
                    "sections": [
                        {"heading": "Algorithm", "content": "1. Choose K cluster centers\n2. Assign points to nearest center\n3. Update centers to mean of assigned points\n4. Repeat until convergence"},
                        {"heading": "Use Cases", "content": "Customer segmentation, image compression, anomaly detection"}
                    ]
                },
                "story": "'K-Means finds hidden groups,' Cluster Spirit explains.",
                "task": "What does K represent in K-Means?",
                "starter_code": "# K represents:\n",
                "expected_output": "number of clusters",
                "hints": ["The number of clusters to create"]
            },
            {
                "id": 1218,
                "title": "Implementing K-Means",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "K-Means in Sklearn",
                    "overview": "Use scikit-learn for clustering.",
                    "sections": [
                        {"heading": "Code", "content": "```python\nfrom sklearn.cluster import KMeans\n\nkmeans = KMeans(n_clusters=3)\nkmeans.fit(X)\nlabels = kmeans.labels_\ncenters = kmeans.cluster_centers_\n```"},
                        {"heading": "Elbow Method", "content": "Plot inertia for different K values to find optimal clusters."}
                    ]
                },
                "story": "'Sklearn makes clustering easy,' Cluster Spirit teaches.",
                "task": "Create a KMeans model with 4 clusters.",
                "starter_code": "from sklearn.cluster import KMeans\n\nkmeans = KMeans(",
                "expected_output": "n_clusters=4)",
                "hints": ["KMeans(n_clusters=4)"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Soul Compression",
        "topic": "PCA (Principal Component Analysis)",
        "description": "Reduce data dimensions while preserving information.",
        "story_intro": "Soul Compression distills data to its essential form!",
        "character": "Dimension Walker",
        "character_quote": "Reduce complexity while keeping the essence!",
        "icon": "minimize-2",
        "color": "#00e676",
        "missions": [
            {
                "id": 1219,
                "title": "PCA Concept",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Dimensionality Reduction",
                    "overview": "PCA finds the most important directions in data.",
                    "sections": [
                        {"heading": "Why PCA", "content": "- Reduce noise\n- Speed up training\n- Visualize high-dimensional data"},
                        {"heading": "How", "content": "Find principal components - directions of maximum variance.\nProject data onto fewer dimensions."}
                    ]
                },
                "story": "'PCA finds the directions that matter most,' Dimension Walker explains.",
                "task": "What does PCA stand for?",
                "starter_code": "# PCA means:\n",
                "expected_output": "Principal Component Analysis",
                "hints": ["Principal Component Analysis"]
            },
            {
                "id": 1220,
                "title": "Implementing PCA",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "PCA in Sklearn",
                    "overview": "Use PCA to reduce dimensions.",
                    "sections": [
                        {"heading": "Code", "content": "```python\nfrom sklearn.decomposition import PCA\n\npca = PCA(n_components=2)\nX_reduced = pca.fit_transform(X)\n\n# Explained variance\nprint(pca.explained_variance_ratio_)\n```"},
                        {"heading": "Choosing Components", "content": "Keep enough components to explain 95% of variance."}
                    ]
                },
                "story": "'Reduce dimensions without losing meaning,' Dimension Walker teaches.",
                "task": "Create PCA that reduces data to 3 components.",
                "starter_code": "from sklearn.decomposition import PCA\n\npca = PCA(",
                "expected_output": "n_components=3)",
                "hints": ["PCA(n_components=3)"]
            }
        ]
    },
    {
        "id": 10,
        "name": "The Neural Web",
        "topic": "Perceptrons, Neural Network layers",
        "description": "Enter the world of deep learning.",
        "story_intro": "The Neural Web mimics the connections of a living brain!",
        "character": "Neural Architect",
        "character_quote": "Neural networks learn complex patterns layer by layer!",
        "icon": "zap",
        "color": "#1de9b6",
        "missions": [
            {
                "id": 1221,
                "title": "Perceptrons",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "The Simplest Neural Unit",
                    "overview": "A perceptron is a single artificial neuron.",
                    "sections": [
                        {"heading": "Structure", "content": "Inputs -> Weights -> Sum -> Activation -> Output"},
                        {"heading": "Math", "content": "output = activation(sum(weights * inputs) + bias)\nActivations: sigmoid, ReLU, tanh"}
                    ]
                },
                "story": "'The perceptron is the atom of neural networks,' Neural Architect explains.",
                "task": "What function introduces non-linearity in neural networks?",
                "starter_code": "# Non-linearity comes from:\n",
                "expected_output": "activation function",
                "hints": ["activation function"]
            },
            {
                "id": 1222,
                "title": "Neural Network Layers",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Building Networks",
                    "overview": "Networks stack layers of neurons.",
                    "sections": [
                        {"heading": "Layer Types", "content": "Input layer - receives data\nHidden layers - learn features\nOutput layer - makes predictions"},
                        {"heading": "Code", "content": "```python\nfrom sklearn.neural_network import MLPClassifier\n\nmlp = MLPClassifier(hidden_layer_sizes=(100, 50))\nmlp.fit(X_train, y_train)\n```"}
                    ]
                },
                "story": "'Deeper networks learn more complex patterns,' Architect teaches.",
                "task": "Create an MLP with hidden layers of size 64 and 32.",
                "starter_code": "from sklearn.neural_network import MLPClassifier\n\nmlp = MLPClassifier(hidden_layer_sizes=",
                "expected_output": "(64, 32))",
                "hints": ["hidden_layer_sizes=(64, 32)"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Vision of the Golem",
        "topic": "CNNs (Convolutional Neural Nets)",
        "description": "Teach machines to see with computer vision.",
        "story_intro": "The Vision of the Golem grants sight to machines!",
        "character": "Vision Master",
        "character_quote": "CNNs see patterns in images just like eyes!",
        "icon": "image",
        "color": "#00bcd4",
        "missions": [
            {
                "id": 1223,
                "title": "CNN Concepts",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Convolutional Networks",
                    "overview": "CNNs are specialized for image data.",
                    "sections": [
                        {"heading": "Key Layers", "content": "Convolutional - detect features (edges, shapes)\nPooling - reduce size, keep important info\nFully Connected - final classification"},
                        {"heading": "Filters", "content": "Small matrices that slide over images detecting patterns."}
                    ]
                },
                "story": "'CNNs detect visual features automatically,' Vision Master explains.",
                "task": "What layer type detects features like edges in CNNs?",
                "starter_code": "# Feature detection layer:\n",
                "expected_output": "Convolutional",
                "hints": ["Convolutional layer"]
            },
            {
                "id": 1224,
                "title": "Building a CNN",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "CNN with Keras",
                    "overview": "Build CNNs with TensorFlow/Keras.",
                    "sections": [
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense\n\nmodel = Sequential([\n    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),\n    MaxPooling2D((2,2)),\n    Flatten(),\n    Dense(10, activation='softmax')\n])\n```"},
                        {"heading": "Training", "content": "model.compile(optimizer='adam', loss='categorical_crossentropy')\nmodel.fit(X_train, y_train, epochs=10)"}
                    ]
                },
                "story": "'Keras makes deep learning accessible,' Vision Master teaches.",
                "task": "What activation function is commonly used for multi-class output?",
                "starter_code": "# Multi-class activation:\n",
                "expected_output": "softmax",
                "hints": ["softmax"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Oracle Awakening",
        "topic": "Building a Predictive AI model",
        "description": "Build a complete machine learning pipeline.",
        "story_intro": "The Oracle combines all skills to predict the future!",
        "character": "Grand Oracle",
        "character_quote": "You are now ready to build intelligent systems!",
        "icon": "trophy",
        "color": "#e91e63",
        "missions": [
            {
                "id": 1225,
                "title": "ML Pipeline",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "End-to-End ML",
                    "overview": "A complete ML pipeline from data to deployment.",
                    "sections": [
                        {"heading": "Steps", "content": "1. Data collection\n2. Data cleaning\n3. Feature engineering\n4. Train/test split\n5. Model selection\n6. Training\n7. Evaluation\n8. Deployment"},
                        {"heading": "Evaluation", "content": "Accuracy, Precision, Recall, F1-Score, Confusion Matrix"}
                    ]
                },
                "story": "'The full pipeline brings it all together,' Grand Oracle explains.",
                "task": "What function splits data into training and test sets?",
                "starter_code": "from sklearn.model_selection import ",
                "expected_output": "train_test_split",
                "hints": ["train_test_split"]
            },
            {
                "id": 1226,
                "title": "ML Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are Ready",
                    "overview": "You've mastered machine learning fundamentals!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- Math foundations\n- Data manipulation\n- Data visualization\n- Regression models\n- Classification models\n- Clustering\n- Dimensionality reduction\n- Neural networks\n- Computer vision basics"},
                        {"heading": "Next Steps", "content": "- Deep learning with TensorFlow/PyTorch\n- Natural Language Processing\n- Reinforcement Learning\n- Deploy models to production"}
                    ]
                },
                "story": "'You have awakened the Oracle within!' Grand Oracle declares.",
                "task": "Name three evaluation metrics for classification.",
                "starter_code": "# Classification metrics:\n",
                "expected_output": "Accuracy, Precision, Recall",
                "hints": ["Accuracy, Precision, Recall, F1-Score"]
            }
        ]
    }
]

DL_ARCS = [
    {
        "id": 1,
        "name": "Spark of the Neuron",
        "topic": "Perceptrons, Activation Functions (Sigmoid, ReLU)",
        "description": "Learn the fundamental building blocks of neural networks.",
        "story_intro": "Welcome to the Neural Nexus! First, understand how a single neuron works.",
        "character": "Neuron Sage",
        "character_quote": "Every great network starts with a single spark!",
        "icon": "zap",
        "color": "#9c27b0",
        "missions": [
            {
                "id": 1301,
                "title": "The Perceptron",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Understanding Perceptrons",
                    "overview": "A perceptron is the simplest form of a neural network.",
                    "sections": [
                        {"heading": "Structure", "content": "A perceptron takes inputs, multiplies by weights, adds bias, and applies activation.\noutput = activation(sum(weights * inputs) + bias)"},
                        {"heading": "Learning", "content": "Perceptrons learn by adjusting weights based on errors.\nThis is the foundation of neural network training."}
                    ]
                },
                "story": "'The perceptron mimics a single brain cell,' Neuron Sage explains.",
                "task": "What are the three main components of a perceptron?",
                "starter_code": "# Three components:\n",
                "expected_output": "weights, bias, activation",
                "hints": ["weights, bias, activation function"]
            },
            {
                "id": 1302,
                "title": "Sigmoid Activation",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "The Sigmoid Function",
                    "overview": "Sigmoid squashes values between 0 and 1.",
                    "sections": [
                        {"heading": "Formula", "content": "sigmoid(x) = 1 / (1 + e^(-x))"},
                        {"heading": "Properties", "content": "- Output range: (0, 1)\n- Smooth gradient\n- Used for probability outputs\n- Problem: vanishing gradients for extreme values"}
                    ]
                },
                "story": "'Sigmoid turns any number into a probability,' Sage teaches.",
                "task": "What is the output range of the sigmoid function?",
                "starter_code": "# Sigmoid output range:\n",
                "expected_output": "0 to 1",
                "hints": ["Between 0 and 1"]
            },
            {
                "id": 1303,
                "title": "ReLU Activation",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Rectified Linear Unit",
                    "overview": "ReLU is the most popular activation function in deep learning.",
                    "sections": [
                        {"heading": "Formula", "content": "ReLU(x) = max(0, x)\nIf x > 0, return x. Otherwise, return 0."},
                        {"heading": "Advantages", "content": "- Simple and fast\n- Reduces vanishing gradient problem\n- Sparse activation (many zeros)\n- Standard choice for hidden layers"}
                    ]
                },
                "story": "'ReLU is simple but powerful,' Neuron Sage reveals.",
                "task": "What does ReLU return for negative inputs?",
                "starter_code": "# ReLU of negative numbers:\n",
                "expected_output": "0",
                "hints": ["ReLU returns 0 for any negative input"]
            }
        ]
    },
    {
        "id": 2,
        "name": "The Layered Labyrinth",
        "topic": "Multi-Layer Perceptrons (MLP), Dense Layers",
        "description": "Build networks with multiple layers.",
        "story_intro": "Navigate the Layered Labyrinth where neurons connect in complex patterns!",
        "character": "Layer Architect",
        "character_quote": "Depth gives networks their power!",
        "icon": "layers",
        "color": "#ab47bc",
        "missions": [
            {
                "id": 1304,
                "title": "Multi-Layer Perceptrons",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Building MLPs",
                    "overview": "MLPs stack multiple layers of neurons.",
                    "sections": [
                        {"heading": "Architecture", "content": "Input Layer -> Hidden Layer(s) -> Output Layer\nEach layer is 'fully connected' to the next."},
                        {"heading": "Why Layers", "content": "More layers = ability to learn more complex patterns.\nThis is what makes 'deep' learning deep!"}
                    ]
                },
                "story": "'Multiple layers learn hierarchical features,' Layer Architect explains.",
                "task": "What connects the input layer to the output layer in an MLP?",
                "starter_code": "# Between input and output:\n",
                "expected_output": "hidden layers",
                "hints": ["Hidden layer(s)"]
            },
            {
                "id": 1305,
                "title": "Dense Layers",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Fully Connected Layers",
                    "overview": "Dense layers connect every neuron to every neuron in the next layer.",
                    "sections": [
                        {"heading": "Dense/Fully Connected", "content": "Each neuron receives input from ALL neurons in previous layer.\nParameters = (input_size * output_size) + output_size (bias)"},
                        {"heading": "Keras Code", "content": "```python\nfrom tensorflow.keras.layers import Dense\n\nmodel.add(Dense(64, activation='relu'))\nmodel.add(Dense(32, activation='relu'))\nmodel.add(Dense(10, activation='softmax'))\n```"}
                    ]
                },
                "story": "'Dense layers are the workhorses of deep learning,' Architect teaches.",
                "task": "Create a Dense layer with 128 neurons and ReLU activation.",
                "starter_code": "from tensorflow.keras.layers import Dense\n\nlayer = Dense(",
                "expected_output": "128, activation='relu')",
                "hints": ["Dense(128, activation='relu')"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Alchemist's Optimizer",
        "topic": "Backpropagation, Gradient Descent, Adam/SGD",
        "description": "Learn how neural networks learn.",
        "story_intro": "The Alchemist reveals the secret of how networks improve themselves!",
        "character": "Optimization Alchemist",
        "character_quote": "Learning is the art of adjusting weights!",
        "icon": "settings",
        "color": "#ba68c8",
        "missions": [
            {
                "id": 1306,
                "title": "Backpropagation",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "The Learning Algorithm",
                    "overview": "Backpropagation calculates gradients for all weights.",
                    "sections": [
                        {"heading": "Forward Pass", "content": "Data flows forward through the network to produce output."},
                        {"heading": "Backward Pass", "content": "Error flows backward, calculating gradients using the chain rule.\nEach weight learns how much it contributed to the error."}
                    ]
                },
                "story": "'Backprop is the magic that makes learning possible,' Alchemist reveals.",
                "task": "What mathematical rule does backpropagation use?",
                "starter_code": "# Backprop uses the:\n",
                "expected_output": "chain rule",
                "hints": ["The chain rule from calculus"]
            },
            {
                "id": 1307,
                "title": "Gradient Descent",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Optimizing Weights",
                    "overview": "Gradient descent updates weights to minimize loss.",
                    "sections": [
                        {"heading": "Update Rule", "content": "new_weight = old_weight - learning_rate * gradient"},
                        {"heading": "Intuition", "content": "Imagine rolling downhill to find the lowest point.\nThe gradient tells you which direction is 'down'."}
                    ]
                },
                "story": "'Follow the gradient to find the best weights,' Alchemist teaches.",
                "task": "In gradient descent, we subtract or add the gradient to weights?",
                "starter_code": "# We _____ the gradient:\n",
                "expected_output": "subtract",
                "hints": ["We subtract to go downhill on the loss surface"]
            },
            {
                "id": 1308,
                "title": "Adam and SGD Optimizers",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Modern Optimizers",
                    "overview": "Adam and SGD are popular optimization algorithms.",
                    "sections": [
                        {"heading": "SGD", "content": "Stochastic Gradient Descent - updates weights on small batches.\nSimple but may oscillate."},
                        {"heading": "Adam", "content": "Adaptive Moment Estimation - adapts learning rate per parameter.\nCombines momentum and RMSprop. Often the default choice."}
                    ]
                },
                "story": "'Adam adapts to each weight individually,' Alchemist explains.",
                "task": "Which optimizer adapts learning rate per parameter?",
                "starter_code": "# Adaptive optimizer:\n",
                "expected_output": "Adam",
                "hints": ["Adam (Adaptive Moment Estimation)"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Shield of Stability",
        "topic": "Dropout, Batch Normalization, Overfitting",
        "description": "Prevent overfitting and stabilize training.",
        "story_intro": "The Shield protects your models from learning too much noise!",
        "character": "Stability Guardian",
        "character_quote": "A model that memorizes is not one that understands!",
        "icon": "shield",
        "color": "#ce93d8",
        "missions": [
            {
                "id": 1309,
                "title": "Understanding Overfitting",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "When Models Memorize",
                    "overview": "Overfitting means the model memorizes training data instead of learning patterns.",
                    "sections": [
                        {"heading": "Symptoms", "content": "- High training accuracy, low test accuracy\n- Model 'memorizes' noise in training data\n- Poor generalization to new data"},
                        {"heading": "Solutions", "content": "- More data\n- Regularization (dropout, L2)\n- Early stopping\n- Simpler model"}
                    ]
                },
                "story": "'Overfitting is when your model cheats by memorizing answers,' Guardian warns.",
                "task": "What happens to test accuracy when a model overfits?",
                "starter_code": "# Test accuracy when overfitting:\n",
                "expected_output": "decreases",
                "hints": ["It goes down while training accuracy stays high"]
            },
            {
                "id": 1310,
                "title": "Dropout Regularization",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Random Neuron Dropping",
                    "overview": "Dropout randomly disables neurons during training.",
                    "sections": [
                        {"heading": "How It Works", "content": "During training, randomly set some neurons to 0.\nThis prevents neurons from co-adapting too much."},
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.layers import Dropout\n\nmodel.add(Dense(128, activation='relu'))\nmodel.add(Dropout(0.5))  # Drop 50% of neurons\n```"}
                    ]
                },
                "story": "'Dropout forces the network to be robust,' Guardian teaches.",
                "task": "Add a Dropout layer that drops 30% of neurons.",
                "starter_code": "from tensorflow.keras.layers import Dropout\n\nlayer = Dropout(",
                "expected_output": "0.3)",
                "hints": ["Dropout(0.3)"]
            },
            {
                "id": 1311,
                "title": "Batch Normalization",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Normalizing Layer Inputs",
                    "overview": "Batch normalization stabilizes and speeds up training.",
                    "sections": [
                        {"heading": "What It Does", "content": "Normalizes inputs to each layer to have mean=0, variance=1.\nReduces internal covariate shift."},
                        {"heading": "Benefits", "content": "- Faster training\n- Higher learning rates possible\n- Some regularization effect\n- Reduces sensitivity to initialization"}
                    ]
                },
                "story": "'BatchNorm keeps the data flowing smoothly,' Guardian reveals.",
                "task": "Where is BatchNormalization typically placed in a network?",
                "starter_code": "# BatchNorm is placed:\n",
                "expected_output": "after Dense layer, before activation",
                "hints": ["After the dense layer, before or after activation"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Eye of the Pattern",
        "topic": "Convolutional Layers, Pooling, Filters",
        "description": "Master convolutional neural networks for images.",
        "story_intro": "The Eye of the Pattern sees shapes and textures in visual data!",
        "character": "Vision Weaver",
        "character_quote": "Convolutions detect patterns at every location!",
        "icon": "eye",
        "color": "#7b1fa2",
        "missions": [
            {
                "id": 1312,
                "title": "Convolutional Layers",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Detecting Patterns",
                    "overview": "Convolutional layers slide filters across images to detect patterns.",
                    "sections": [
                        {"heading": "How It Works", "content": "A small filter (e.g., 3x3) slides across the image.\nAt each position, element-wise multiplication + sum = one output value."},
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.layers import Conv2D\n\nmodel.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))\n```"}
                    ]
                },
                "story": "'Each filter learns to detect a specific pattern,' Vision Weaver explains.",
                "task": "Create a Conv2D layer with 64 filters of size 3x3.",
                "starter_code": "from tensorflow.keras.layers import Conv2D\n\nlayer = Conv2D(",
                "expected_output": "64, (3, 3), activation='relu')",
                "hints": ["Conv2D(64, (3, 3), activation='relu')"]
            },
            {
                "id": 1313,
                "title": "Pooling Layers",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Downsampling",
                    "overview": "Pooling reduces spatial dimensions while keeping important information.",
                    "sections": [
                        {"heading": "Max Pooling", "content": "Takes the maximum value in each window.\nReduces size by 2x if using (2,2) pool size."},
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.layers import MaxPooling2D\n\nmodel.add(MaxPooling2D((2, 2)))\n```"}
                    ]
                },
                "story": "'Pooling keeps the essence, discards the noise,' Weaver teaches.",
                "task": "What does MaxPooling2D((2, 2)) do to image dimensions?",
                "starter_code": "# Effect on dimensions:\n",
                "expected_output": "halves them",
                "hints": ["Reduces height and width by half"]
            },
            {
                "id": 1314,
                "title": "Understanding Filters",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "What Filters Learn",
                    "overview": "Filters learn to detect specific features.",
                    "sections": [
                        {"heading": "Early Layers", "content": "Detect simple patterns: edges, corners, colors"},
                        {"heading": "Deeper Layers", "content": "Combine simple patterns into complex features:\nEyes, wheels, textures, faces"}
                    ]
                },
                "story": "'Early filters see edges, later filters see objects,' Weaver reveals.",
                "task": "What do early convolutional layers typically detect?",
                "starter_code": "# Early layers detect:\n",
                "expected_output": "edges",
                "hints": ["Edges, simple patterns, corners"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Echoes of Time",
        "topic": "Recurrent Neural Networks, Sequence data",
        "description": "Process sequential data with memory.",
        "story_intro": "The Echoes remember what came before to predict what comes next!",
        "character": "Sequence Oracle",
        "character_quote": "The past informs the future!",
        "icon": "repeat",
        "color": "#6a1b9a",
        "missions": [
            {
                "id": 1315,
                "title": "Recurrent Neural Networks",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Networks with Memory",
                    "overview": "RNNs maintain hidden state across sequence steps.",
                    "sections": [
                        {"heading": "Structure", "content": "At each time step:\n- Take input + previous hidden state\n- Produce output + new hidden state\nThis creates 'memory' of past inputs."},
                        {"heading": "Uses", "content": "- Text generation\n- Machine translation\n- Speech recognition\n- Time series prediction"}
                    ]
                },
                "story": "'RNNs remember the sequence they've seen,' Sequence Oracle explains.",
                "task": "What does an RNN maintain across time steps?",
                "starter_code": "# RNNs maintain:\n",
                "expected_output": "hidden state",
                "hints": ["Hidden state (memory)"]
            },
            {
                "id": 1316,
                "title": "Sequence Data",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Working with Sequences",
                    "overview": "Sequential data has order that matters.",
                    "sections": [
                        {"heading": "Examples", "content": "- Text (sequence of words)\n- Audio (sequence of samples)\n- Stock prices (sequence of values)\n- Video (sequence of frames)"},
                        {"heading": "Shape", "content": "Sequence data shape: (batch_size, sequence_length, features)"}
                    ]
                },
                "story": "'Order matters in sequence data,' Oracle teaches.",
                "task": "Give an example of sequence data.",
                "starter_code": "# Example:\n",
                "expected_output": "text",
                "hints": ["Text, audio, time series, video"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Time-Turner Scrolls",
        "topic": "LSTMs, GRUs, Long-term dependencies",
        "description": "Handle long sequences with advanced memory cells.",
        "story_intro": "The Time-Turner Scrolls preserve memories across vast distances of time!",
        "character": "Memory Keeper",
        "character_quote": "LSTMs never forget what matters!",
        "icon": "clock",
        "color": "#4a148c",
        "missions": [
            {
                "id": 1317,
                "title": "Long Short-Term Memory",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "LSTM Architecture",
                    "overview": "LSTMs solve the vanishing gradient problem in RNNs.",
                    "sections": [
                        {"heading": "Gates", "content": "- Forget gate: what to throw away\n- Input gate: what to add\n- Output gate: what to output\nGates control information flow."},
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.layers import LSTM\n\nmodel.add(LSTM(128, return_sequences=True))\n```"}
                    ]
                },
                "story": "'LSTM gates control what to remember and forget,' Memory Keeper explains.",
                "task": "How many gates does an LSTM cell have?",
                "starter_code": "# Number of gates:\n",
                "expected_output": "3",
                "hints": ["Three: forget, input, output"]
            },
            {
                "id": 1318,
                "title": "Gated Recurrent Units",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "GRUs - Simplified LSTMs",
                    "overview": "GRUs are simpler than LSTMs but often equally effective.",
                    "sections": [
                        {"heading": "Simplification", "content": "GRUs have only 2 gates (update and reset).\nFewer parameters, faster to train."},
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.layers import GRU\n\nmodel.add(GRU(128))\n```"}
                    ]
                },
                "story": "'GRUs are LSTMs with less complexity,' Keeper teaches.",
                "task": "How many gates does a GRU have?",
                "starter_code": "# GRU gates:\n",
                "expected_output": "2",
                "hints": ["Two: update gate and reset gate"]
            },
            {
                "id": 1319,
                "title": "Long-term Dependencies",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Remembering Distant Past",
                    "overview": "LSTM/GRU can connect information across many time steps.",
                    "sections": [
                        {"heading": "Problem", "content": "Vanilla RNNs struggle to learn long-range dependencies.\nGradients vanish over many time steps."},
                        {"heading": "Solution", "content": "LSTM's cell state acts as a 'highway' for gradients.\nInformation can flow unchanged across many steps."}
                    ]
                },
                "story": "'The cell state carries memories through time,' Keeper reveals.",
                "task": "What problem do LSTMs solve that vanilla RNNs have?",
                "starter_code": "# LSTMs solve:\n",
                "expected_output": "vanishing gradient",
                "hints": ["Vanishing gradient problem"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Ritual of Attention",
        "topic": "Self-Attention, Key/Query/Value concepts",
        "description": "Learn the attention mechanism that powers transformers.",
        "story_intro": "The Ritual of Attention reveals what truly matters in the data!",
        "character": "Attention Master",
        "character_quote": "Attention focuses on what's important!",
        "icon": "crosshair",
        "color": "#311b92",
        "missions": [
            {
                "id": 1320,
                "title": "Self-Attention Mechanism",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Attending to Everything",
                    "overview": "Self-attention lets each position attend to all other positions.",
                    "sections": [
                        {"heading": "Concept", "content": "Unlike RNNs that process sequentially, attention can look at the entire sequence at once.\nEach word can directly connect to any other word."},
                        {"heading": "Formula", "content": "Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) * V"}
                    ]
                },
                "story": "'Self-attention connects every element to every other,' Attention Master explains.",
                "task": "What can self-attention do that RNNs cannot?",
                "starter_code": "# Self-attention can:\n",
                "expected_output": "attend to all positions at once",
                "hints": ["Look at all positions simultaneously"]
            },
            {
                "id": 1321,
                "title": "Keys, Queries, and Values",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "The KQV Framework",
                    "overview": "Attention uses three projections: Key, Query, Value.",
                    "sections": [
                        {"heading": "Analogy", "content": "Query = what you're looking for\nKey = what each item offers\nValue = the actual content\nLike searching a database!"},
                        {"heading": "Process", "content": "1. Compare Query to all Keys (similarity scores)\n2. Softmax scores to get weights\n3. Weighted sum of Values = output"}
                    ]
                },
                "story": "'Query asks, Key answers, Value delivers,' Master teaches.",
                "task": "What do we compare to compute attention weights?",
                "starter_code": "# We compare:\n",
                "expected_output": "Query and Key",
                "hints": ["Query and Key vectors"]
            }
        ]
    },
    {
        "id": 9,
        "name": "The Transformer Tower",
        "topic": "Multi-head attention, Encoder-Decoder",
        "description": "Master the transformer architecture.",
        "story_intro": "The Transformer Tower is the most powerful structure in the Neural Nexus!",
        "character": "Transformer Sage",
        "character_quote": "Transformers transformed everything!",
        "icon": "git-merge",
        "color": "#1a237e",
        "missions": [
            {
                "id": 1322,
                "title": "Multi-Head Attention",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Multiple Attention Patterns",
                    "overview": "Multi-head attention runs several attention mechanisms in parallel.",
                    "sections": [
                        {"heading": "Why Multiple Heads", "content": "Different heads can learn different relationships.\nOne head might focus on syntax, another on semantics."},
                        {"heading": "Process", "content": "1. Split into h heads\n2. Apply attention to each\n3. Concatenate results\n4. Linear projection"}
                    ]
                },
                "story": "'Multiple heads see multiple patterns,' Transformer Sage explains.",
                "task": "Why use multiple attention heads instead of one?",
                "starter_code": "# Multiple heads allow:\n",
                "expected_output": "learning different relationships",
                "hints": ["Different heads learn different types of relationships"]
            },
            {
                "id": 1323,
                "title": "Encoder-Decoder Architecture",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Transforming Sequences",
                    "overview": "The encoder-decoder structure is used for sequence-to-sequence tasks.",
                    "sections": [
                        {"heading": "Encoder", "content": "Processes input sequence.\nBuilds a rich representation of the input."},
                        {"heading": "Decoder", "content": "Generates output sequence.\nAttends to encoder output while generating."},
                        {"heading": "Applications", "content": "Translation, summarization, question answering"}
                    ]
                },
                "story": "'Encoder understands, Decoder generates,' Sage teaches.",
                "task": "What does the encoder produce for the decoder?",
                "starter_code": "# Encoder produces:\n",
                "expected_output": "representations",
                "hints": ["Hidden representations/encodings of the input"]
            }
        ]
    },
    {
        "id": 10,
        "name": "The Generative Forge",
        "topic": "GANs (Generative Adversarial Nets), VAEs",
        "description": "Create models that generate new data.",
        "story_intro": "The Generative Forge creates entirely new content from learned patterns!",
        "character": "Genesis Artificer",
        "character_quote": "GANs create what has never existed!",
        "icon": "sparkles",
        "color": "#0d47a1",
        "missions": [
            {
                "id": 1324,
                "title": "Generative Adversarial Networks",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "The GAN Game",
                    "overview": "GANs pit two networks against each other.",
                    "sections": [
                        {"heading": "Components", "content": "Generator: Creates fake data from noise.\nDiscriminator: Tries to distinguish real from fake."},
                        {"heading": "Training", "content": "Generator tries to fool discriminator.\nDiscriminator tries to catch fakes.\nBoth improve through competition."}
                    ]
                },
                "story": "'Generator and Discriminator compete to improve,' Artificer explains.",
                "task": "What are the two networks in a GAN?",
                "starter_code": "# Two networks:\n",
                "expected_output": "Generator and Discriminator",
                "hints": ["Generator and Discriminator"]
            },
            {
                "id": 1325,
                "title": "Variational Autoencoders",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Learning Latent Spaces",
                    "overview": "VAEs learn a compressed representation of data.",
                    "sections": [
                        {"heading": "Structure", "content": "Encoder: Data -> Latent space (mean, variance)\nDecoder: Latent space -> Reconstructed data"},
                        {"heading": "Generation", "content": "Sample from latent space.\nDecode to generate new data.\nSmooth, continuous latent space allows interpolation."}
                    ]
                },
                "story": "'VAEs learn the essence of data,' Artificer teaches.",
                "task": "What does a VAE encoder output?",
                "starter_code": "# VAE encoder outputs:\n",
                "expected_output": "mean and variance",
                "hints": ["Mean and variance of latent distribution"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Hyperparameter Heights",
        "topic": "Learning rates, Epochs, Transfer Learning",
        "description": "Fine-tune models for optimal performance.",
        "story_intro": "Climb the Hyperparameter Heights to perfect your models!",
        "character": "Tuning Sage",
        "character_quote": "The right hyperparameters make all the difference!",
        "icon": "sliders",
        "color": "#01579b",
        "missions": [
            {
                "id": 1326,
                "title": "Learning Rate",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "The Most Important Hyperparameter",
                    "overview": "Learning rate controls how fast weights update.",
                    "sections": [
                        {"heading": "Too High", "content": "Overshoots the optimal weights.\nLoss may oscillate or diverge."},
                        {"heading": "Too Low", "content": "Takes forever to converge.\nMay get stuck in local minima."},
                        {"heading": "Typical Values", "content": "Start with 0.001 or 0.01.\nUse learning rate schedulers to decrease over time."}
                    ]
                },
                "story": "'Learning rate is the first thing to tune,' Tuning Sage explains.",
                "task": "What happens if learning rate is too high?",
                "starter_code": "# If learning rate too high:\n",
                "expected_output": "overshoots",
                "hints": ["Overshoots optimal weights, may diverge"]
            },
            {
                "id": 1327,
                "title": "Epochs and Batch Size",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Training Iterations",
                    "overview": "Epochs and batch size control training duration and updates.",
                    "sections": [
                        {"heading": "Epoch", "content": "One complete pass through the training data.\nMore epochs = more learning (but risk overfitting)."},
                        {"heading": "Batch Size", "content": "Number of samples per gradient update.\nLarger batches = more stable gradients, slower training.\nSmaller batches = noisier gradients, faster updates."}
                    ]
                },
                "story": "'Balance epochs and batch size for best results,' Sage teaches.",
                "task": "What is one epoch?",
                "starter_code": "# One epoch is:\n",
                "expected_output": "one pass through all training data",
                "hints": ["One complete pass through the training dataset"]
            },
            {
                "id": 1328,
                "title": "Transfer Learning",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Standing on Giants",
                    "overview": "Use pre-trained models as starting points.",
                    "sections": [
                        {"heading": "Concept", "content": "Take a model trained on large dataset.\nFine-tune on your smaller dataset.\nLeverages learned features!"},
                        {"heading": "Process", "content": "1. Load pre-trained model (e.g., VGG, BERT)\n2. Freeze early layers\n3. Replace final layer for your task\n4. Train on your data"}
                    ]
                },
                "story": "'Why start from scratch when giants have paved the way?' Sage reveals.",
                "task": "What do we typically freeze in transfer learning?",
                "starter_code": "# We freeze:\n",
                "expected_output": "early layers",
                "hints": ["Early layers (they contain general features)"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Lord of the Nexus",
        "topic": "Final Project: Building a Handwritten Digit Recognizer",
        "description": "Build a complete deep learning project.",
        "story_intro": "The Lord of the Nexus challenges you to prove your mastery!",
        "character": "Nexus Lord",
        "character_quote": "Show me everything you've learned!",
        "icon": "trophy",
        "color": "#e91e63",
        "missions": [
            {
                "id": 1329,
                "title": "Building the Model",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "MNIST Digit Recognizer",
                    "overview": "Build a CNN to recognize handwritten digits.",
                    "sections": [
                        {"heading": "Architecture", "content": "```python\nmodel = Sequential([\n    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),\n    MaxPooling2D((2,2)),\n    Conv2D(64, (3,3), activation='relu'),\n    MaxPooling2D((2,2)),\n    Flatten(),\n    Dense(128, activation='relu'),\n    Dropout(0.5),\n    Dense(10, activation='softmax')\n])\n```"},
                        {"heading": "Compile", "content": "model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])"}
                    ]
                },
                "story": "'Build a network that can read numbers!' Nexus Lord challenges.",
                "task": "What activation function should the output layer use for multi-class classification?",
                "starter_code": "# Output activation:\n",
                "expected_output": "softmax",
                "hints": ["softmax for multi-class"]
            },
            {
                "id": 1330,
                "title": "Deep Learning Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Master",
                    "overview": "You've conquered the Neural Nexus!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- Perceptrons & Activations\n- MLPs & Dense Layers\n- Backpropagation & Optimizers\n- Regularization\n- CNNs\n- RNNs, LSTMs, GRUs\n- Attention & Transformers\n- GANs & VAEs\n- Hyperparameter Tuning"},
                        {"heading": "Next Steps", "content": "- Deploy models to production\n- Explore NLP with BERT/GPT\n- Try reinforcement learning\n- Contribute to open source AI"}
                    ]
                },
                "story": "'You have become the Lord of the Neural Nexus!' The realm celebrates!",
                "task": "Name three types of neural network layers you learned.",
                "starter_code": "# Three layer types:\n",
                "expected_output": "Dense, Conv2D, LSTM",
                "hints": ["Dense, Conv2D, LSTM, GRU, Dropout, etc."]
            }
        ]
    }
]

CV_ARCS = [
    {
        "id": 1,
        "name": "Visionary's Lens",
        "topic": "Pixels, RGB vs. Grayscale, OpenCV intro",
        "description": "Learn the fundamentals of digital images.",
        "story_intro": "Welcome to the Prism Gazer's realm! First, understand how machines see images.",
        "character": "Vision Sage",
        "character_quote": "Every image is just a grid of numbers!",
        "icon": "image",
        "color": "#00bcd4",
        "missions": [
            {
                "id": 1401,
                "title": "Understanding Pixels",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "The Building Blocks of Images",
                    "overview": "Pixels are the smallest units of digital images.",
                    "sections": [
                        {"heading": "What is a Pixel", "content": "A pixel (picture element) is a single point in an image.\nImages are 2D grids of pixels with width x height dimensions."},
                        {"heading": "Resolution", "content": "A 1920x1080 image has 1920 columns and 1080 rows = 2,073,600 pixels."}
                    ]
                },
                "story": "'Each pixel holds a tiny piece of the visual world,' Vision Sage explains.",
                "task": "What is the total number of pixels in a 640x480 image?",
                "starter_code": "# Total pixels:\n",
                "expected_output": "307200",
                "hints": ["640 * 480 = 307,200"]
            },
            {
                "id": 1402,
                "title": "RGB vs Grayscale",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Color Representation",
                    "overview": "Images can be color (RGB) or grayscale.",
                    "sections": [
                        {"heading": "RGB", "content": "Red, Green, Blue - 3 channels per pixel.\nEach channel has values 0-255.\n(255, 0, 0) = pure red"},
                        {"heading": "Grayscale", "content": "Single channel per pixel (0-255).\n0 = black, 255 = white.\nUsed for edge detection, simplifying computations."}
                    ]
                },
                "story": "'Color adds depth, grayscale reveals structure,' Sage teaches.",
                "task": "How many channels does an RGB image have?",
                "starter_code": "# RGB channels:\n",
                "expected_output": "3",
                "hints": ["Red, Green, Blue = 3"]
            },
            {
                "id": 1403,
                "title": "OpenCV Introduction",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "The Vision Library",
                    "overview": "OpenCV is the standard library for computer vision.",
                    "sections": [
                        {"heading": "Reading Images", "content": "```python\nimport cv2\n\nimg = cv2.imread('image.jpg')\nprint(img.shape)  # (height, width, channels)\n```"},
                        {"heading": "Key Functions", "content": "cv2.imread() - read image\ncv2.imshow() - display image\ncv2.cvtColor() - convert colors\ncv2.imwrite() - save image"}
                    ]
                },
                "story": "'OpenCV gives your code eyes,' Vision Sage reveals.",
                "task": "What function reads an image in OpenCV?",
                "starter_code": "import cv2\n\nimg = cv2.",
                "expected_output": "imread('image.jpg')",
                "hints": ["cv2.imread()"]
            }
        ]
    },
    {
        "id": 2,
        "name": "The Filter Forest",
        "topic": "Blurring, Sharpening, Morphological Ops",
        "description": "Apply filters to enhance and transform images.",
        "story_intro": "Enter the Filter Forest where images are transformed and refined!",
        "character": "Filter Weaver",
        "character_quote": "Filters reveal what the raw image hides!",
        "icon": "sliders",
        "color": "#26c6da",
        "missions": [
            {
                "id": 1404,
                "title": "Blurring Images",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Smoothing Techniques",
                    "overview": "Blurring reduces noise and detail.",
                    "sections": [
                        {"heading": "Gaussian Blur", "content": "Uses a Gaussian kernel to smooth the image.\n```python\nblurred = cv2.GaussianBlur(img, (5, 5), 0)\n```"},
                        {"heading": "Other Blurs", "content": "- cv2.blur() - simple average\n- cv2.medianBlur() - good for salt-and-pepper noise\n- cv2.bilateralFilter() - preserves edges"}
                    ]
                },
                "story": "'Blurring removes noise while keeping the essence,' Filter Weaver explains.",
                "task": "Apply Gaussian blur with a 5x5 kernel.",
                "starter_code": "import cv2\nimg = cv2.imread('image.jpg')\n\nblurred = cv2.GaussianBlur(img, ",
                "expected_output": "(5, 5), 0)",
                "hints": ["cv2.GaussianBlur(img, (5, 5), 0)"]
            },
            {
                "id": 1405,
                "title": "Sharpening Images",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Enhancing Edges",
                    "overview": "Sharpening makes edges more pronounced.",
                    "sections": [
                        {"heading": "Kernel", "content": "```python\nimport numpy as np\nkernel = np.array([[-1,-1,-1],\n                   [-1, 9,-1],\n                   [-1,-1,-1]])\nsharpened = cv2.filter2D(img, -1, kernel)\n```"},
                        {"heading": "Concept", "content": "Sharpening subtracts a blurred version from the original, enhancing high-frequency details."}
                    ]
                },
                "story": "'Sharpening reveals hidden details,' Weaver teaches.",
                "task": "What value is at the center of a typical sharpening kernel?",
                "starter_code": "# Center value:\n",
                "expected_output": "9",
                "hints": ["A positive value larger than the sum of negatives, often 9"]
            },
            {
                "id": 1406,
                "title": "Morphological Operations",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Shape-Based Processing",
                    "overview": "Morphological ops process shapes in binary images.",
                    "sections": [
                        {"heading": "Erosion", "content": "Shrinks white regions. Useful for removing small noise.\ncv2.erode(img, kernel, iterations=1)"},
                        {"heading": "Dilation", "content": "Expands white regions. Fills small holes.\ncv2.dilate(img, kernel, iterations=1)"},
                        {"heading": "Opening/Closing", "content": "Opening = erosion then dilation (removes noise)\nClosing = dilation then erosion (fills holes)"}
                    ]
                },
                "story": "'Morphology shapes the image at a structural level,' Weaver reveals.",
                "task": "What morphological operation removes small noise spots?",
                "starter_code": "# To remove noise:\n",
                "expected_output": "opening",
                "hints": ["Opening (erosion followed by dilation)"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Edge of Discovery",
        "topic": "Canny Edge Detection, Sobel Filters",
        "description": "Detect edges and boundaries in images.",
        "story_intro": "At the Edge of Discovery, boundaries reveal themselves!",
        "character": "Edge Seeker",
        "character_quote": "Edges are where the information lives!",
        "icon": "maximize",
        "color": "#4dd0e1",
        "missions": [
            {
                "id": 1407,
                "title": "Sobel Filters",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Gradient-Based Edge Detection",
                    "overview": "Sobel filters detect edges by computing gradients.",
                    "sections": [
                        {"heading": "How It Works", "content": "Sobel computes derivatives in x and y directions.\nHigh gradient = edge."},
                        {"heading": "Code", "content": "```python\nsobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # x direction\nsobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # y direction\nedges = cv2.magnitude(sobelx, sobely)\n```"}
                    ]
                },
                "story": "'Sobel measures how rapidly brightness changes,' Edge Seeker explains.",
                "task": "What does Sobel filter compute to detect edges?",
                "starter_code": "# Sobel computes:\n",
                "expected_output": "gradients",
                "hints": ["Image gradients/derivatives"]
            },
            {
                "id": 1408,
                "title": "Canny Edge Detection",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The Best Edge Detector",
                    "overview": "Canny is the most popular edge detection algorithm.",
                    "sections": [
                        {"heading": "Steps", "content": "1. Gaussian blur\n2. Gradient calculation\n3. Non-maximum suppression\n4. Double thresholding\n5. Edge tracking by hysteresis"},
                        {"heading": "Code", "content": "```python\nedges = cv2.Canny(gray, threshold1=100, threshold2=200)\n```"}
                    ]
                },
                "story": "'Canny finds edges with precision and accuracy,' Seeker teaches.",
                "task": "Apply Canny edge detection with thresholds 50 and 150.",
                "starter_code": "import cv2\ngray = cv2.imread('image.jpg', 0)\n\nedges = cv2.Canny(gray, ",
                "expected_output": "50, 150)",
                "hints": ["cv2.Canny(gray, 50, 150)"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Shape-Shifter's Circle",
        "topic": "Finding shapes, Bounding boxes, Area",
        "description": "Detect and analyze shapes in images.",
        "story_intro": "The Shape-Shifter reveals hidden forms within images!",
        "character": "Shape Master",
        "character_quote": "Every object has a shape waiting to be found!",
        "icon": "square",
        "color": "#80deea",
        "missions": [
            {
                "id": 1409,
                "title": "Finding Contours",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Shape Detection",
                    "overview": "Contours are curves joining continuous points along a boundary.",
                    "sections": [
                        {"heading": "Finding Contours", "content": "```python\ncontours, hierarchy = cv2.findContours(\n    binary_img,\n    cv2.RETR_EXTERNAL,\n    cv2.CHAIN_APPROX_SIMPLE\n)\n```"},
                        {"heading": "Drawing", "content": "cv2.drawContours(img, contours, -1, (0,255,0), 2)"}
                    ]
                },
                "story": "'Contours trace the boundaries of objects,' Shape Master explains.",
                "task": "What function finds contours in OpenCV?",
                "starter_code": "contours, _ = cv2.",
                "expected_output": "findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)",
                "hints": ["cv2.findContours()"]
            },
            {
                "id": 1410,
                "title": "Bounding Boxes",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Enclosing Shapes",
                    "overview": "Bounding boxes enclose detected objects.",
                    "sections": [
                        {"heading": "Rectangle", "content": "```python\nx, y, w, h = cv2.boundingRect(contour)\ncv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)\n```"},
                        {"heading": "Rotated Rectangle", "content": "cv2.minAreaRect() - finds the smallest rotated rectangle"}
                    ]
                },
                "story": "'Bounding boxes localize objects in space,' Master teaches.",
                "task": "What does cv2.boundingRect() return?",
                "starter_code": "# Returns:\n",
                "expected_output": "x, y, width, height",
                "hints": ["x, y, w, h"]
            },
            {
                "id": 1411,
                "title": "Contour Properties",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Analyzing Shapes",
                    "overview": "Extract useful properties from contours.",
                    "sections": [
                        {"heading": "Area", "content": "area = cv2.contourArea(contour)"},
                        {"heading": "Perimeter", "content": "perimeter = cv2.arcLength(contour, True)"},
                        {"heading": "Centroid", "content": "M = cv2.moments(contour)\ncx = int(M['m10']/M['m00'])\ncy = int(M['m01']/M['m00'])"}
                    ]
                },
                "story": "'Measure shapes to understand them,' Master reveals.",
                "task": "What function calculates contour area?",
                "starter_code": "area = cv2.",
                "expected_output": "contourArea(contour)",
                "hints": ["cv2.contourArea()"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Feature Finder's Path",
        "topic": "SIFT, SURF, ORB (Interest points)",
        "description": "Detect distinctive features in images.",
        "story_intro": "The Feature Finder discovers unique landmarks in every image!",
        "character": "Feature Scout",
        "character_quote": "Features are the fingerprints of images!",
        "icon": "map-pin",
        "color": "#00acc1",
        "missions": [
            {
                "id": 1412,
                "title": "SIFT Features",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Scale-Invariant Feature Transform",
                    "overview": "SIFT detects features that are robust to scale and rotation.",
                    "sections": [
                        {"heading": "Properties", "content": "- Scale invariant\n- Rotation invariant\n- Distinctive descriptors\n- Used for matching images"},
                        {"heading": "Code", "content": "```python\nsift = cv2.SIFT_create()\nkeypoints, descriptors = sift.detectAndCompute(gray, None)\n```"}
                    ]
                },
                "story": "'SIFT finds features that persist across transformations,' Feature Scout explains.",
                "task": "What does SIFT stand for?",
                "starter_code": "# SIFT means:\n",
                "expected_output": "Scale-Invariant Feature Transform",
                "hints": ["Scale-Invariant Feature Transform"]
            },
            {
                "id": 1413,
                "title": "ORB Features",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Oriented FAST and Rotated BRIEF",
                    "overview": "ORB is a fast, free alternative to SIFT.",
                    "sections": [
                        {"heading": "Advantages", "content": "- Much faster than SIFT\n- Patent-free\n- Good for real-time applications"},
                        {"heading": "Code", "content": "```python\norb = cv2.ORB_create()\nkeypoints, descriptors = orb.detectAndCompute(gray, None)\n```"}
                    ]
                },
                "story": "'ORB is fast and free,' Scout teaches.",
                "task": "Create an ORB detector.",
                "starter_code": "import cv2\n\norb = cv2.",
                "expected_output": "ORB_create()",
                "hints": ["cv2.ORB_create()"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Neural Gaze",
        "topic": "CNNs for Image Classification",
        "description": "Use deep learning for image understanding.",
        "story_intro": "The Neural Gaze sees images through trained neural pathways!",
        "character": "Neural Visionary",
        "character_quote": "CNNs learn to see patterns humans define!",
        "icon": "cpu",
        "color": "#0097a7",
        "missions": [
            {
                "id": 1414,
                "title": "CNNs for Classification",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Deep Learning Vision",
                    "overview": "CNNs learn hierarchical visual features.",
                    "sections": [
                        {"heading": "Architecture", "content": "Conv layers -> Pooling -> More Conv -> Flatten -> Dense -> Output"},
                        {"heading": "Why CNNs", "content": "- Learn features automatically\n- Translation invariant\n- State-of-the-art accuracy\n- Powers modern computer vision"}
                    ]
                },
                "story": "'CNNs revolutionized how machines see,' Neural Visionary explains.",
                "task": "What layer type is essential for image classification CNNs?",
                "starter_code": "# Essential layer:\n",
                "expected_output": "Convolutional",
                "hints": ["Convolutional layers"]
            },
            {
                "id": 1415,
                "title": "Building an Image Classifier",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Classification with Keras",
                    "overview": "Build a CNN for image classification.",
                    "sections": [
                        {"heading": "Architecture", "content": "```python\nmodel = Sequential([\n    Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),\n    MaxPooling2D((2,2)),\n    Conv2D(64, (3,3), activation='relu'),\n    MaxPooling2D((2,2)),\n    Flatten(),\n    Dense(128, activation='relu'),\n    Dense(num_classes, activation='softmax')\n])\n```"},
                        {"heading": "Training", "content": "model.compile(optimizer='adam', loss='categorical_crossentropy')\nmodel.fit(X_train, y_train, epochs=10)"}
                    ]
                },
                "story": "'Build your own image classifier,' Visionary teaches.",
                "task": "What activation function is used in the output layer for multi-class classification?",
                "starter_code": "# Output activation:\n",
                "expected_output": "softmax",
                "hints": ["softmax"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Royal Portrait Hall",
        "topic": "Face Detection (Haar Cascades), Landmarks",
        "description": "Detect faces and facial features.",
        "story_intro": "Enter the Royal Portrait Hall where faces are recognized!",
        "character": "Face Oracle",
        "character_quote": "Every face tells a story!",
        "icon": "user",
        "color": "#00838f",
        "missions": [
            {
                "id": 1416,
                "title": "Haar Cascade Face Detection",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Classical Face Detection",
                    "overview": "Haar cascades use hand-crafted features for detection.",
                    "sections": [
                        {"heading": "How It Works", "content": "Trained on positive (faces) and negative (non-faces) images.\nUses edge/line features at multiple scales."},
                        {"heading": "Code", "content": "```python\nface_cascade = cv2.CascadeClassifier(\n    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'\n)\nfaces = face_cascade.detectMultiScale(gray, 1.1, 4)\nfor (x, y, w, h) in faces:\n    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)\n```"}
                    ]
                },
                "story": "'Haar cascades were the first fast face detectors,' Face Oracle explains.",
                "task": "What method detects faces at multiple scales?",
                "starter_code": "faces = face_cascade.",
                "expected_output": "detectMultiScale(gray, 1.1, 4)",
                "hints": ["detectMultiScale()"]
            },
            {
                "id": 1417,
                "title": "Facial Landmarks",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Detecting Face Features",
                    "overview": "Landmarks identify key points on faces.",
                    "sections": [
                        {"heading": "Key Points", "content": "- Eyes, eyebrows\n- Nose tip\n- Mouth corners\n- Jawline\nTypically 68 or 5 landmark points"},
                        {"heading": "Uses", "content": "- Face alignment\n- Emotion detection\n- Face filters (Snapchat-style)\n- Gaze tracking"}
                    ]
                },
                "story": "'Landmarks map the geography of a face,' Oracle teaches.",
                "task": "How many landmark points are commonly used for detailed face analysis?",
                "starter_code": "# Common landmark count:\n",
                "expected_output": "68",
                "hints": ["68 landmarks"]
            }
        ]
    },
    {
        "id": 8,
        "name": "The Hunter's Mark",
        "topic": "YOLO (You Only Look Once), SSD basics",
        "description": "Detect multiple objects in real-time.",
        "story_intro": "The Hunter's Mark spots all objects in a single glance!",
        "character": "Detection Hunter",
        "character_quote": "YOLO sees everything at once!",
        "icon": "target",
        "color": "#006064",
        "missions": [
            {
                "id": 1418,
                "title": "YOLO Object Detection",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "You Only Look Once",
                    "overview": "YOLO detects objects in a single forward pass.",
                    "sections": [
                        {"heading": "How It Works", "content": "- Divides image into grid\n- Each cell predicts bounding boxes and class probabilities\n- Single neural network pass = real-time detection"},
                        {"heading": "Advantages", "content": "- Extremely fast (30-155 FPS)\n- Sees global context\n- Good for real-time applications"}
                    ]
                },
                "story": "'YOLO revolutionized real-time detection,' Detection Hunter explains.",
                "task": "What does YOLO stand for?",
                "starter_code": "# YOLO means:\n",
                "expected_output": "You Only Look Once",
                "hints": ["You Only Look Once"]
            },
            {
                "id": 1419,
                "title": "SSD Basics",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Single Shot MultiBox Detector",
                    "overview": "SSD detects objects at multiple scales in one pass.",
                    "sections": [
                        {"heading": "Architecture", "content": "- Uses feature maps at multiple resolutions\n- Detects small objects with early layers, large with later\n- No region proposal step needed"},
                        {"heading": "vs YOLO", "content": "SSD handles multiple scales better.\nYOLO is typically faster.\nBoth are single-shot detectors."}
                    ]
                },
                "story": "'SSD balances speed and accuracy,' Hunter teaches.",
                "task": "What type of detector are both YOLO and SSD?",
                "starter_code": "# Both are:\n",
                "expected_output": "single-shot detectors",
                "hints": ["Single-shot detectors"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Map of Many Colors",
        "topic": "Semantic vs. Instance Segmentation (Mask R-CNN)",
        "description": "Classify every pixel in an image.",
        "story_intro": "The Map of Many Colors labels every pixel with meaning!",
        "character": "Segmentation Sage",
        "character_quote": "Every pixel belongs to something!",
        "icon": "grid",
        "color": "#004d40",
        "missions": [
            {
                "id": 1420,
                "title": "Semantic Segmentation",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Pixel-wise Classification",
                    "overview": "Semantic segmentation labels every pixel with a class.",
                    "sections": [
                        {"heading": "Concept", "content": "Each pixel gets a class label (road, sky, person, car...).\nAll instances of a class share the same label."},
                        {"heading": "Architectures", "content": "- FCN (Fully Convolutional Networks)\n- U-Net\n- DeepLab"}
                    ]
                },
                "story": "'Semantic segmentation sees what each pixel is,' Segmentation Sage explains.",
                "task": "Does semantic segmentation distinguish between different instances of the same class?",
                "starter_code": "# Different instances:\n",
                "expected_output": "No",
                "hints": ["No, all cars are labeled as 'car'"]
            },
            {
                "id": 1421,
                "title": "Instance Segmentation",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Distinguishing Instances",
                    "overview": "Instance segmentation identifies each object separately.",
                    "sections": [
                        {"heading": "vs Semantic", "content": "Semantic: all people = 'person'\nInstance: person 1, person 2, person 3..."},
                        {"heading": "Mask R-CNN", "content": "Extends Faster R-CNN with a mask branch.\nOutputs bounding box + class + pixel mask per instance."}
                    ]
                },
                "story": "'Instance segmentation knows each object individually,' Sage teaches.",
                "task": "What model combines detection with instance segmentation?",
                "starter_code": "# Detection + segmentation model:\n",
                "expected_output": "Mask R-CNN",
                "hints": ["Mask R-CNN"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Mirror of Motion",
        "topic": "Optical Flow, Frame Differencing, Tracking",
        "description": "Analyze motion in video.",
        "story_intro": "The Mirror of Motion reveals movement through time!",
        "character": "Motion Tracker",
        "character_quote": "Motion tells the story of change!",
        "icon": "activity",
        "color": "#00695c",
        "missions": [
            {
                "id": 1422,
                "title": "Optical Flow",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Tracking Motion",
                    "overview": "Optical flow estimates motion between frames.",
                    "sections": [
                        {"heading": "Concept", "content": "Computes how pixels move from frame to frame.\nUsed for motion estimation, video stabilization."},
                        {"heading": "Types", "content": "- Dense: Flow for every pixel\n- Sparse: Flow for specific points\ncv2.calcOpticalFlowFarneback() - dense\ncv2.calcOpticalFlowPyrLK() - sparse"}
                    ]
                },
                "story": "'Optical flow sees the invisible currents of motion,' Motion Tracker explains.",
                "task": "What does optical flow estimate between video frames?",
                "starter_code": "# Optical flow estimates:\n",
                "expected_output": "pixel motion",
                "hints": ["How pixels move between frames"]
            },
            {
                "id": 1423,
                "title": "Frame Differencing",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Simple Motion Detection",
                    "overview": "Subtract frames to find what changed.",
                    "sections": [
                        {"heading": "Method", "content": "```python\ndiff = cv2.absdiff(frame1, frame2)\ngray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)\n_, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)\n```"},
                        {"heading": "Uses", "content": "- Motion detection in security cameras\n- Background subtraction\n- Activity detection"}
                    ]
                },
                "story": "'Differences reveal what moves,' Tracker teaches.",
                "task": "What function computes absolute difference between frames?",
                "starter_code": "diff = cv2.",
                "expected_output": "absdiff(frame1, frame2)",
                "hints": ["cv2.absdiff()"]
            },
            {
                "id": 1424,
                "title": "Object Tracking",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Following Objects Through Video",
                    "overview": "Tracking maintains object identity across frames.",
                    "sections": [
                        {"heading": "Trackers", "content": "OpenCV trackers:\n- KCF - good speed/accuracy balance\n- CSRT - more accurate, slower\n- MOSSE - fastest"},
                        {"heading": "Code", "content": "```python\ntracker = cv2.TrackerKCF_create()\ntracker.init(frame, bbox)\nsuccess, bbox = tracker.update(new_frame)\n```"}
                    ]
                },
                "story": "'Trackers follow objects through the river of time,' Tracker reveals.",
                "task": "Name one OpenCV tracker algorithm.",
                "starter_code": "# Tracker:\n",
                "expected_output": "KCF",
                "hints": ["KCF, CSRT, or MOSSE"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Wisdom Transfer",
        "topic": "Using Pre-trained models (ResNet, VGG)",
        "description": "Leverage pre-trained models for your tasks.",
        "story_intro": "The Wisdom Transfer shares knowledge from models trained on millions of images!",
        "character": "Transfer Sage",
        "character_quote": "Stand on the shoulders of giants!",
        "icon": "download",
        "color": "#26a69a",
        "missions": [
            {
                "id": 1425,
                "title": "Using VGG",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "VGGNet for Transfer Learning",
                    "overview": "VGG is a classic deep CNN architecture.",
                    "sections": [
                        {"heading": "Architecture", "content": "- Very deep (16-19 layers)\n- Small 3x3 convolutions throughout\n- Pre-trained on ImageNet (1000 classes)"},
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.applications import VGG16\n\nbase_model = VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3))\nbase_model.trainable = False\n```"}
                    ]
                },
                "story": "'VGG's deep layers learned rich visual features,' Transfer Sage explains.",
                "task": "What dataset are ImageNet models pre-trained on?",
                "starter_code": "# Pre-trained on:\n",
                "expected_output": "ImageNet",
                "hints": ["ImageNet (1.2 million images, 1000 classes)"]
            },
            {
                "id": 1426,
                "title": "Using ResNet",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Residual Networks",
                    "overview": "ResNet uses skip connections for very deep networks.",
                    "sections": [
                        {"heading": "Skip Connections", "content": "Allow gradients to flow directly through the network.\nEnables training networks with 100+ layers."},
                        {"heading": "Code", "content": "```python\nfrom tensorflow.keras.applications import ResNet50\n\nbase_model = ResNet50(weights='imagenet', include_top=False)\nbase_model.trainable = False\n# Add your own classification layers\n```"}
                    ]
                },
                "story": "'ResNet's skip connections broke the depth barrier,' Sage teaches.",
                "task": "What architectural feature allows ResNet to train very deep networks?",
                "starter_code": "# ResNet uses:\n",
                "expected_output": "skip connections",
                "hints": ["Skip connections / residual connections"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Master of the Prism",
        "topic": "Final Project: Building a Real-time Object Scanner",
        "description": "Build a complete computer vision application.",
        "story_intro": "Become the Master of the Prism by creating your own vision system!",
        "character": "Prism Lord",
        "character_quote": "You now see as the machines see!",
        "icon": "trophy",
        "color": "#e91e63",
        "missions": [
            {
                "id": 1427,
                "title": "Building an Object Scanner",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Real-time Vision System",
                    "overview": "Combine all skills to build a complete application.",
                    "sections": [
                        {"heading": "Components", "content": "1. Capture video from camera\n2. Preprocess frames\n3. Detect/classify objects\n4. Draw results\n5. Display in real-time"},
                        {"heading": "Pipeline", "content": "```python\ncap = cv2.VideoCapture(0)\nwhile True:\n    ret, frame = cap.read()\n    # Process frame\n    # Detect objects\n    # Draw boxes\n    cv2.imshow('Scanner', frame)\n    if cv2.waitKey(1) & 0xFF == ord('q'):\n        break\n```"}
                    ]
                },
                "story": "'Build a system that sees and understands!' Prism Lord challenges.",
                "task": "What function captures video from a camera in OpenCV?",
                "starter_code": "cap = cv2.",
                "expected_output": "VideoCapture(0)",
                "hints": ["cv2.VideoCapture()"]
            },
            {
                "id": 1428,
                "title": "Computer Vision Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Master",
                    "overview": "You've mastered computer vision!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- Image fundamentals\n- Filtering and processing\n- Edge detection\n- Contour analysis\n- Feature detection\n- Deep learning for vision\n- Face detection\n- Object detection\n- Segmentation\n- Motion analysis\n- Transfer learning"},
                        {"heading": "Next Steps", "content": "- 3D computer vision\n- Medical imaging\n- Autonomous vehicles\n- AR/VR applications\n- Deploy vision models to edge devices"}
                    ]
                },
                "story": "'You have become the Master of the Prism!' The realm sees through your eyes!",
                "task": "Name three computer vision applications you can now build.",
                "starter_code": "# Three applications:\n",
                "expected_output": "face detection, object detection, image classification",
                "hints": ["Face detection, object detection, image classifier, etc."]
            }
        ]
    }
]

NLP_ARCS = [
    {
        "id": 1,
        "name": "The Scribe's Ink",
        "topic": "Tokenization, Case folding, Regex",
        "description": "Learn the fundamentals of text preprocessing.",
        "story_intro": "Welcome to the Script-Weaver's domain! First, learn to prepare text for analysis.",
        "character": "Text Scribe",
        "character_quote": "Every word must be properly prepared before it reveals its meaning!",
        "icon": "file-text",
        "color": "#e91e63",
        "missions": [
            {
                "id": 1501,
                "title": "Tokenization",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Breaking Text into Pieces",
                    "overview": "Tokenization splits text into individual units (tokens).",
                    "sections": [
                        {"heading": "What is Tokenization", "content": "Tokenization breaks text into words, sentences, or subwords.\n'Hello world!' -> ['Hello', 'world', '!']"},
                        {"heading": "Types", "content": "- Word tokenization: split by words\n- Sentence tokenization: split by sentences\n- Subword tokenization: BPE, WordPiece (used in BERT)"}
                    ]
                },
                "story": "'Text must be split into tokens before we can understand it,' Text Scribe explains.",
                "task": "What is the process of splitting text into individual words called?",
                "starter_code": "# Process name:\n",
                "expected_output": "tokenization",
                "hints": ["Tokenization"]
            },
            {
                "id": 1502,
                "title": "Case Folding",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Normalizing Text Case",
                    "overview": "Case folding converts text to a uniform case.",
                    "sections": [
                        {"heading": "Why Case Fold", "content": "'Hello' and 'hello' should be treated as the same word.\nConvert all text to lowercase for consistency."},
                        {"heading": "Code", "content": "```python\ntext = 'Hello World'\nlower_text = text.lower()  # 'hello world'\n```"}
                    ]
                },
                "story": "'Uniformity in case brings clarity,' Scribe teaches.",
                "task": "Convert 'MACHINE LEARNING' to lowercase.",
                "starter_code": "text = 'MACHINE LEARNING'\nresult = text.",
                "expected_output": "lower()",
                "hints": [".lower()"]
            },
            {
                "id": 1503,
                "title": "Regular Expressions",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Pattern Matching with Regex",
                    "overview": "Regex helps find and manipulate text patterns.",
                    "sections": [
                        {"heading": "Basic Patterns", "content": "\\d - digit, \\w - word character, \\s - whitespace\n. - any character, * - zero or more, + - one or more"},
                        {"heading": "Code", "content": "```python\nimport re\ntext = 'Email: user@example.com'\nemail = re.findall(r'[\\w.-]+@[\\w.-]+', text)\n```"}
                    ]
                },
                "story": "'Regex patterns unlock hidden text structures,' Scribe reveals.",
                "task": "What regex pattern matches one or more digits?",
                "starter_code": "import re\npattern = r'",
                "expected_output": "\\d+'",
                "hints": ["\\d+ matches one or more digits"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Word-Whirlpool",
        "topic": "Stopwords, Stemming, Lemmatization",
        "description": "Clean and normalize text for analysis.",
        "story_intro": "The Word-Whirlpool refines raw text into its essential form!",
        "character": "Word Purifier",
        "character_quote": "Remove the noise to find the signal!",
        "icon": "filter",
        "color": "#f06292",
        "missions": [
            {
                "id": 1504,
                "title": "Stopwords Removal",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Filtering Common Words",
                    "overview": "Stopwords are common words that add little meaning.",
                    "sections": [
                        {"heading": "What are Stopwords", "content": "Words like 'the', 'is', 'at', 'which' are stopwords.\nThey appear frequently but carry little semantic meaning."},
                        {"heading": "Code", "content": "```python\nfrom nltk.corpus import stopwords\nstop_words = set(stopwords.words('english'))\nfiltered = [w for w in words if w.lower() not in stop_words]\n```"}
                    ]
                },
                "story": "'Remove the noise to hear the message,' Word Purifier explains.",
                "task": "What do we call common words like 'the', 'is', 'and' that are often removed?",
                "starter_code": "# These words are called:\n",
                "expected_output": "stopwords",
                "hints": ["Stopwords"]
            },
            {
                "id": 1505,
                "title": "Stemming",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Reducing Words to Roots",
                    "overview": "Stemming chops words to their base form.",
                    "sections": [
                        {"heading": "How It Works", "content": "'running' -> 'run', 'flies' -> 'fli'\nSimple rule-based approach, may not produce real words."},
                        {"heading": "Code", "content": "```python\nfrom nltk.stem import PorterStemmer\nstemmer = PorterStemmer()\nstemmer.stem('running')  # 'run'\n```"}
                    ]
                },
                "story": "'Stemming finds the root of words,' Purifier teaches.",
                "task": "What is the stem of 'running' using Porter Stemmer?",
                "starter_code": "# Stem of 'running':\n",
                "expected_output": "run",
                "hints": ["run"]
            },
            {
                "id": 1506,
                "title": "Lemmatization",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Finding Dictionary Forms",
                    "overview": "Lemmatization finds the proper dictionary form.",
                    "sections": [
                        {"heading": "vs Stemming", "content": "Lemmatization uses vocabulary and morphological analysis.\n'better' -> 'good', 'running' -> 'run'\nProduces real words unlike stemming."},
                        {"heading": "Code", "content": "```python\nfrom nltk.stem import WordNetLemmatizer\nlemmatizer = WordNetLemmatizer()\nlemmatizer.lemmatize('better', pos='a')  # 'good'\n```"}
                    ]
                },
                "story": "'Lemmatization reveals the true form of words,' Purifier reveals.",
                "task": "What is the difference between stemming and lemmatization?",
                "starter_code": "# Key difference:\n",
                "expected_output": "lemmatization produces real words",
                "hints": ["Lemmatization produces real dictionary words"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Weight of Words",
        "topic": "Bag of Words, TF-IDF, N-grams",
        "description": "Convert text into numerical representations.",
        "story_intro": "At the Weight of Words, text becomes numbers!",
        "character": "Vector Sage",
        "character_quote": "Numbers reveal what words hide!",
        "icon": "bar-chart",
        "color": "#ec407a",
        "missions": [
            {
                "id": 1507,
                "title": "Bag of Words",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Simple Text Vectorization",
                    "overview": "Bag of Words counts word occurrences.",
                    "sections": [
                        {"heading": "Concept", "content": "Each document becomes a vector of word counts.\nIgnores word order, only considers frequency."},
                        {"heading": "Code", "content": "```python\nfrom sklearn.feature_extraction.text import CountVectorizer\nvectorizer = CountVectorizer()\nX = vectorizer.fit_transform(documents)\n```"}
                    ]
                },
                "story": "'Count words to measure meaning,' Vector Sage explains.",
                "task": "What vectorization method counts word occurrences in documents?",
                "starter_code": "# Method name:\n",
                "expected_output": "Bag of Words",
                "hints": ["Bag of Words"]
            },
            {
                "id": 1508,
                "title": "TF-IDF",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Term Frequency-Inverse Document Frequency",
                    "overview": "TF-IDF weighs words by importance.",
                    "sections": [
                        {"heading": "Formula", "content": "TF = term frequency in document\nIDF = log(total docs / docs containing term)\nTF-IDF = TF * IDF\nRare words get higher scores."},
                        {"heading": "Code", "content": "```python\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nvectorizer = TfidfVectorizer()\nX = vectorizer.fit_transform(documents)\n```"}
                    ]
                },
                "story": "'TF-IDF reveals truly important words,' Sage teaches.",
                "task": "What does IDF stand for?",
                "starter_code": "# IDF means:\n",
                "expected_output": "Inverse Document Frequency",
                "hints": ["Inverse Document Frequency"]
            },
            {
                "id": 1509,
                "title": "N-grams",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Capturing Word Sequences",
                    "overview": "N-grams capture sequences of n consecutive words.",
                    "sections": [
                        {"heading": "Types", "content": "Unigram: single words\nBigram: pairs ('machine learning')\nTrigram: triplets ('natural language processing')"},
                        {"heading": "Code", "content": "```python\nvectorizer = CountVectorizer(ngram_range=(1, 2))  # unigrams and bigrams\n```"}
                    ]
                },
                "story": "'N-grams capture word relationships,' Sage reveals.",
                "task": "What is a sequence of 2 consecutive words called?",
                "starter_code": "# Two-word sequence:\n",
                "expected_output": "bigram",
                "hints": ["Bigram"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Emotion Ocean",
        "topic": "Sentiment Analysis, Naive Bayes for text",
        "description": "Classify text by emotion and sentiment.",
        "story_intro": "The Emotion Ocean reads the feelings behind words!",
        "character": "Sentiment Reader",
        "character_quote": "Every text carries an emotional signature!",
        "icon": "heart",
        "color": "#d81b60",
        "missions": [
            {
                "id": 1510,
                "title": "Sentiment Analysis",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Detecting Emotions in Text",
                    "overview": "Sentiment analysis determines if text is positive, negative, or neutral.",
                    "sections": [
                        {"heading": "Applications", "content": "- Product reviews\n- Social media monitoring\n- Customer feedback\n- Brand reputation"},
                        {"heading": "Approaches", "content": "1. Lexicon-based: use sentiment word lists\n2. Machine learning: train classifiers\n3. Deep learning: use neural networks"}
                    ]
                },
                "story": "'Read the emotions hidden in words,' Sentiment Reader explains.",
                "task": "What are the three main sentiment categories?",
                "starter_code": "# Three categories:\n",
                "expected_output": "positive, negative, neutral",
                "hints": ["Positive, negative, neutral"]
            },
            {
                "id": 1511,
                "title": "Naive Bayes for Text",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Probabilistic Text Classification",
                    "overview": "Naive Bayes is a simple but effective text classifier.",
                    "sections": [
                        {"heading": "How It Works", "content": "Uses Bayes' theorem with 'naive' independence assumption.\nP(class|text) proportional to P(class) * P(word1|class) * P(word2|class) * ..."},
                        {"heading": "Code", "content": "```python\nfrom sklearn.naive_bayes import MultinomialNB\nclassifier = MultinomialNB()\nclassifier.fit(X_train, y_train)\npredictions = classifier.predict(X_test)\n```"}
                    ]
                },
                "story": "'Naive Bayes classifies with probability,' Reader teaches.",
                "task": "What assumption makes Naive Bayes 'naive'?",
                "starter_code": "# The naive assumption:\n",
                "expected_output": "feature independence",
                "hints": ["Features are independent of each other"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Soul-Sense Links",
        "topic": "Word2Vec, GloVe, Contextual meaning",
        "description": "Learn dense word representations.",
        "story_intro": "The Soul-Sense Links reveal deep connections between words!",
        "character": "Embedding Master",
        "character_quote": "Words with similar meanings live close together!",
        "icon": "link",
        "color": "#c2185b",
        "missions": [
            {
                "id": 1512,
                "title": "Word2Vec",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Learning Word Vectors",
                    "overview": "Word2Vec learns dense vector representations of words.",
                    "sections": [
                        {"heading": "Architectures", "content": "CBOW: Predict word from context\nSkip-gram: Predict context from word\nBoth learn meaningful word vectors."},
                        {"heading": "Magic", "content": "king - man + woman = queen\nWords with similar meanings have similar vectors."}
                    ]
                },
                "story": "'Word2Vec captures the essence of words,' Embedding Master explains.",
                "task": "What famous Word2Vec equation shows semantic relationships?",
                "starter_code": "# Famous equation:\n",
                "expected_output": "king - man + woman = queen",
                "hints": ["king - man + woman = queen"]
            },
            {
                "id": 1513,
                "title": "GloVe Embeddings",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Global Vectors for Word Representation",
                    "overview": "GloVe learns from word co-occurrence statistics.",
                    "sections": [
                        {"heading": "vs Word2Vec", "content": "Word2Vec: local context windows\nGloVe: global co-occurrence matrix\nBoth produce similar quality embeddings."},
                        {"heading": "Pre-trained", "content": "GloVe comes with pre-trained vectors:\n- Wikipedia + Gigaword\n- Common Crawl\n- Twitter"}
                    ]
                },
                "story": "'GloVe sees the big picture of word relationships,' Master teaches.",
                "task": "What does GloVe stand for?",
                "starter_code": "# GloVe means:\n",
                "expected_output": "Global Vectors",
                "hints": ["Global Vectors for Word Representation"]
            },
            {
                "id": 1514,
                "title": "Contextual Embeddings",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Words in Context",
                    "overview": "Contextual embeddings give different vectors based on context.",
                    "sections": [
                        {"heading": "The Problem", "content": "'bank' in 'river bank' vs 'bank account'\nStatic embeddings give the same vector.\nContextual embeddings give different vectors!"},
                        {"heading": "Models", "content": "ELMo, BERT, GPT produce contextual embeddings.\nThey understand word meaning from surrounding context."}
                    ]
                },
                "story": "'Context changes meaning,' Master reveals.",
                "task": "Why are contextual embeddings better than static embeddings?",
                "starter_code": "# Key advantage:\n",
                "expected_output": "same word gets different vectors based on context",
                "hints": ["Different vectors based on context"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Sequential Song",
        "topic": "LSTMs for text generation and completion",
        "description": "Generate and complete text with neural networks.",
        "story_intro": "The Sequential Song weaves words into new tales!",
        "character": "Text Weaver",
        "character_quote": "Sequences hold the rhythm of language!",
        "icon": "music",
        "color": "#ad1457",
        "missions": [
            {
                "id": 1515,
                "title": "LSTMs for Text",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Remembering Long Sequences",
                    "overview": "LSTMs process text while remembering context.",
                    "sections": [
                        {"heading": "Why LSTMs", "content": "Text has long-range dependencies.\n'The cat that sat on the mat was hungry'\nLSTMs remember 'cat' when predicting 'was'."},
                        {"heading": "Architecture", "content": "Input gate, forget gate, output gate.\nCell state carries information across long sequences."}
                    ]
                },
                "story": "'LSTMs remember the distant past,' Text Weaver explains.",
                "task": "What problem do LSTMs solve that basic RNNs cannot?",
                "starter_code": "# LSTMs solve:\n",
                "expected_output": "long-range dependencies",
                "hints": ["Long-range dependencies / vanishing gradient"]
            },
            {
                "id": 1516,
                "title": "Text Generation",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Creating New Text",
                    "overview": "Train models to generate text character by character or word by word.",
                    "sections": [
                        {"heading": "Process", "content": "1. Train on text corpus\n2. Feed seed text\n3. Predict next character/word\n4. Add to sequence, repeat"},
                        {"heading": "Temperature", "content": "Low temperature: conservative, repetitive\nHigh temperature: creative, chaotic\nBalance creativity and coherence."}
                    ]
                },
                "story": "'Generate new stories from learned patterns,' Weaver teaches.",
                "task": "What does high temperature in text generation produce?",
                "starter_code": "# High temperature produces:\n",
                "expected_output": "more creative/diverse text",
                "hints": ["More creative, diverse, sometimes chaotic output"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Identity Archives",
        "topic": "Named Entity Recognition (NER), POS Tagging",
        "description": "Extract entities and understand grammar.",
        "story_intro": "The Identity Archives reveal who and what in every text!",
        "character": "Entity Keeper",
        "character_quote": "Every name has a story!",
        "icon": "user-check",
        "color": "#880e4f",
        "missions": [
            {
                "id": 1517,
                "title": "Named Entity Recognition",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Finding Names in Text",
                    "overview": "NER identifies and classifies named entities.",
                    "sections": [
                        {"heading": "Entity Types", "content": "PERSON: 'Albert Einstein'\nORG: 'Google', 'NASA'\nLOC: 'Paris', 'Mount Everest'\nDATE: 'January 1, 2024'\nMONEY: '$1 million'"},
                        {"heading": "Code", "content": "```python\nimport spacy\nnlp = spacy.load('en_core_web_sm')\ndoc = nlp('Apple is looking at buying U.K. startup')\nfor ent in doc.ents:\n    print(ent.text, ent.label_)\n```"}
                    ]
                },
                "story": "'NER finds the who, what, where in text,' Entity Keeper explains.",
                "task": "What entity type is 'Google' classified as?",
                "starter_code": "# Entity type:\n",
                "expected_output": "ORG",
                "hints": ["ORG (Organization)"]
            },
            {
                "id": 1518,
                "title": "POS Tagging",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Part-of-Speech Tagging",
                    "overview": "POS tagging identifies grammatical roles of words.",
                    "sections": [
                        {"heading": "Common Tags", "content": "NN: noun, VB: verb, JJ: adjective\nRB: adverb, DT: determiner, IN: preposition"},
                        {"heading": "Code", "content": "```python\nimport nltk\ntext = 'The quick brown fox jumps'\ntokens = nltk.word_tokenize(text)\ntagged = nltk.pos_tag(tokens)\n# [('The', 'DT'), ('quick', 'JJ'), ...]\n```"}
                    ]
                },
                "story": "'Know the role of every word,' Keeper teaches.",
                "task": "What POS tag does 'quickly' (an adverb) receive?",
                "starter_code": "# Adverb tag:\n",
                "expected_output": "RB",
                "hints": ["RB"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Bridge of Tongues",
        "topic": "Seq2Seq models, Encoder-Decoder basics",
        "description": "Translate between languages.",
        "story_intro": "The Bridge of Tongues connects languages across realms!",
        "character": "Translation Oracle",
        "character_quote": "Every language can speak to another!",
        "icon": "globe",
        "color": "#7b1fa2",
        "missions": [
            {
                "id": 1519,
                "title": "Seq2Seq Models",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Sequence to Sequence Learning",
                    "overview": "Seq2Seq transforms one sequence into another.",
                    "sections": [
                        {"heading": "Applications", "content": "- Machine translation\n- Summarization\n- Chatbots\n- Question answering"},
                        {"heading": "Architecture", "content": "Encoder reads input sequence -> context vector\nDecoder generates output sequence from context"}
                    ]
                },
                "story": "'Seq2Seq bridges input to output,' Translation Oracle explains.",
                "task": "What are the two main components of a Seq2Seq model?",
                "starter_code": "# Two components:\n",
                "expected_output": "encoder and decoder",
                "hints": ["Encoder and Decoder"]
            },
            {
                "id": 1520,
                "title": "Encoder-Decoder Architecture",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "The Translation Pipeline",
                    "overview": "Encoder compresses, decoder expands.",
                    "sections": [
                        {"heading": "Encoder", "content": "Processes input sequence word by word.\nProduces a fixed-size context vector.\nCaptures the meaning of the input."},
                        {"heading": "Decoder", "content": "Takes context vector as initial state.\nGenerates output one word at a time.\nUses previous output as next input."}
                    ]
                },
                "story": "'Encode meaning, decode into new language,' Oracle teaches.",
                "task": "What does the encoder produce that the decoder uses?",
                "starter_code": "# Encoder produces:\n",
                "expected_output": "context vector",
                "hints": ["Context vector / hidden state"]
            }
        ]
    },
    {
        "id": 9,
        "name": "The Attention Ritual",
        "topic": "Scaled Dot-Product Attention, Transformers",
        "description": "Master the attention mechanism.",
        "story_intro": "The Attention Ritual focuses on what matters most!",
        "character": "Attention Priest",
        "character_quote": "Focus on what matters, ignore the rest!",
        "icon": "target",
        "color": "#6a1b9a",
        "missions": [
            {
                "id": 1521,
                "title": "Scaled Dot-Product Attention",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "The Core Attention Mechanism",
                    "overview": "Attention weighs the importance of different parts of input.",
                    "sections": [
                        {"heading": "Formula", "content": "Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) * V\nQ: Query, K: Key, V: Value\nScale factor prevents large dot products."},
                        {"heading": "Intuition", "content": "Query asks 'what am I looking for?'\nKeys say 'this is what I contain'\nValues provide the actual information."}
                    ]
                },
                "story": "'Attention focuses on relevant information,' Attention Priest explains.",
                "task": "What are the three components in the attention formula?",
                "starter_code": "# Three components:\n",
                "expected_output": "Query, Key, Value",
                "hints": ["Query (Q), Key (K), Value (V)"]
            },
            {
                "id": 1522,
                "title": "Transformers Architecture",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Attention Is All You Need",
                    "overview": "Transformers use only attention, no recurrence.",
                    "sections": [
                        {"heading": "Key Features", "content": "- Multi-head attention: attend to different aspects\n- Positional encoding: inject sequence order\n- Layer normalization\n- Parallel processing (faster than RNNs)"},
                        {"heading": "Impact", "content": "Transformers power BERT, GPT, T5, and all modern LLMs.\nRevolutionized NLP in 2017."}
                    ]
                },
                "story": "'Transformers changed everything,' Priest reveals.",
                "task": "What famous paper introduced the Transformer architecture?",
                "starter_code": "# Paper title:\n",
                "expected_output": "Attention Is All You Need",
                "hints": ["Attention Is All You Need"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Legend of the BERT",
        "topic": "BERT, RoBERTa, Hugging Face Library",
        "description": "Use pre-trained language models.",
        "story_intro": "The Legend of BERT unlocks the power of pre-trained knowledge!",
        "character": "BERT Master",
        "character_quote": "Pre-training gives you a head start!",
        "icon": "book-open",
        "color": "#4a148c",
        "missions": [
            {
                "id": 1523,
                "title": "BERT",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Bidirectional Encoder Representations",
                    "overview": "BERT reads text in both directions simultaneously.",
                    "sections": [
                        {"heading": "Pre-training", "content": "Masked Language Model: predict [MASK] tokens\nNext Sentence Prediction: are sentences related?\nTrained on Wikipedia + BookCorpus."},
                        {"heading": "Fine-tuning", "content": "Add task-specific layer on top.\nFine-tune for classification, NER, QA, etc.\nMuch less data needed than training from scratch."}
                    ]
                },
                "story": "'BERT understands context from both sides,' BERT Master explains.",
                "task": "What does BERT stand for?",
                "starter_code": "# BERT means:\n",
                "expected_output": "Bidirectional Encoder Representations from Transformers",
                "hints": ["Bidirectional Encoder Representations from Transformers"]
            },
            {
                "id": 1524,
                "title": "RoBERTa and Variants",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "BERT's Successors",
                    "overview": "RoBERTa improved BERT's training process.",
                    "sections": [
                        {"heading": "Improvements", "content": "- More data, longer training\n- Removed Next Sentence Prediction\n- Dynamic masking\n- Larger batch sizes"},
                        {"heading": "Other Variants", "content": "ALBERT: parameter-efficient\nDistilBERT: smaller, faster\nXLNet: permutation language modeling"}
                    ]
                },
                "story": "'RoBERTa shows training matters,' Master teaches.",
                "task": "What did RoBERTa remove from BERT's pre-training?",
                "starter_code": "# Removed task:\n",
                "expected_output": "Next Sentence Prediction",
                "hints": ["Next Sentence Prediction"]
            },
            {
                "id": 1525,
                "title": "Hugging Face Library",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The Model Hub",
                    "overview": "Hugging Face makes using transformers easy.",
                    "sections": [
                        {"heading": "Transformers Library", "content": "```python\nfrom transformers import pipeline\nclassifier = pipeline('sentiment-analysis')\nresult = classifier('I love this product!')\n```"},
                        {"heading": "Model Hub", "content": "Thousands of pre-trained models.\nOne-line download and use.\nCommunity contributions."}
                    ]
                },
                "story": "'Hugging Face democratizes NLP,' Master reveals.",
                "task": "What library from Hugging Face makes using transformers easy?",
                "starter_code": "from transformers import ",
                "expected_output": "pipeline",
                "hints": ["pipeline"]
            }
        ]
    },
    {
        "id": 11,
        "name": "The Prompt Portal",
        "topic": "GPT architecture, Zero-shot learning",
        "description": "Explore generative language models.",
        "story_intro": "The Prompt Portal opens doors to generative AI!",
        "character": "GPT Guardian",
        "character_quote": "Ask and you shall receive!",
        "icon": "zap",
        "color": "#311b92",
        "missions": [
            {
                "id": 1526,
                "title": "GPT Architecture",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Generative Pre-trained Transformers",
                    "overview": "GPT generates text by predicting the next token.",
                    "sections": [
                        {"heading": "vs BERT", "content": "BERT: bidirectional, encoder-only\nGPT: unidirectional, decoder-only\nGPT is autoregressive: generates left to right."},
                        {"heading": "Scaling", "content": "GPT-2: 1.5B parameters\nGPT-3: 175B parameters\nGPT-4: rumored trillions\nBigger = more capable."}
                    ]
                },
                "story": "'GPT generates language like magic,' GPT Guardian explains.",
                "task": "Is GPT an encoder or decoder model?",
                "starter_code": "# GPT is:\n",
                "expected_output": "decoder",
                "hints": ["Decoder-only model"]
            },
            {
                "id": 1527,
                "title": "Zero-Shot Learning",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "No Training Required",
                    "overview": "Zero-shot models perform tasks without task-specific training.",
                    "sections": [
                        {"heading": "Concept", "content": "Zero-shot: no examples\nFew-shot: a few examples in prompt\nIn-context learning: model learns from prompt context."},
                        {"heading": "Example", "content": "Prompt: 'Classify this review as positive or negative: I hated this movie.'\nGPT answers: 'negative'\nNo training on movie reviews needed!"}
                    ]
                },
                "story": "'Zero-shot means no training examples,' Guardian teaches.",
                "task": "What is it called when we provide a few examples in the prompt?",
                "starter_code": "# With few examples:\n",
                "expected_output": "few-shot learning",
                "hints": ["Few-shot learning"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Arch-Scribe of the Realm",
        "topic": "Final Project: Building an Anime Story Generator",
        "description": "Build a complete NLP application.",
        "story_intro": "Become the Arch-Scribe by creating your own language AI!",
        "character": "Arch-Scribe",
        "character_quote": "You now command the power of language!",
        "icon": "trophy",
        "color": "#ff4081",
        "missions": [
            {
                "id": 1528,
                "title": "Building a Story Generator",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Generating Creative Text",
                    "overview": "Combine all NLP skills to build a story generator.",
                    "sections": [
                        {"heading": "Components", "content": "1. Text preprocessing\n2. Choose model (GPT, fine-tuned LSTM)\n3. Prompt engineering\n4. Temperature control\n5. Post-processing"},
                        {"heading": "Approach", "content": "```python\nfrom transformers import pipeline\ngenerator = pipeline('text-generation', model='gpt2')\nstory = generator('Once upon a time in an anime world,', max_length=200)\n```"}
                    ]
                },
                "story": "'Build a system that writes stories!' Arch-Scribe challenges.",
                "task": "What Hugging Face pipeline is used for story generation?",
                "starter_code": "generator = pipeline('",
                "expected_output": "text-generation')",
                "hints": ["text-generation"]
            },
            {
                "id": 1529,
                "title": "NLP Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Script-Weaver",
                    "overview": "You've mastered Natural Language Processing!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- Text preprocessing\n- Vectorization (BoW, TF-IDF)\n- Sentiment analysis\n- Word embeddings\n- RNNs and LSTMs\n- NER and POS tagging\n- Seq2Seq and attention\n- Transformers and BERT\n- GPT and zero-shot learning"},
                        {"heading": "Next Steps", "content": "- Fine-tune models for specific domains\n- Build chatbots and assistants\n- Explore multilingual NLP\n- Deploy NLP models to production"}
                    ]
                },
                "story": "'You have become the Arch-Scribe of the Realm!' Language bends to your will!",
                "task": "Name three NLP applications you can now build.",
                "starter_code": "# Three applications:\n",
                "expected_output": "chatbot, sentiment analyzer, text generator",
                "hints": ["Chatbot, sentiment analyzer, translator, summarizer, etc."]
            }
        ]
    }
]

AI_ARCS = [
    {
        "id": 1,
        "name": "Chronicles of the Golem",
        "topic": "Turing Test, Symbolic AI vs. Connectionism",
        "description": "Learn the history and foundations of AI.",
        "story_intro": "Welcome to the Grand Design! First, understand how the Great Golem came to be.",
        "character": "Historian Sage",
        "character_quote": "To understand AI's future, we must know its past!",
        "icon": "book",
        "color": "#673ab7",
        "missions": [
            {
                "id": 1601,
                "title": "The Turing Test",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Can Machines Think?",
                    "overview": "The Turing Test measures machine intelligence.",
                    "sections": [
                        {"heading": "Alan Turing's Question", "content": "In 1950, Alan Turing asked 'Can machines think?'\nHe proposed the Imitation Game: if a human can't tell if they're talking to a machine or human, the machine is intelligent."},
                        {"heading": "The Test", "content": "A human judge converses with a human and a machine.\nIf the judge can't reliably distinguish them, the machine passes.\nNo machine has definitively passed the full Turing Test."}
                    ]
                },
                "story": "'The Turing Test is the foundation of AI philosophy,' Historian Sage explains.",
                "task": "Who proposed the Turing Test and in what year?",
                "starter_code": "# Answer:\n",
                "expected_output": "Alan Turing, 1950",
                "hints": ["Alan Turing proposed it in 1950"]
            },
            {
                "id": 1602,
                "title": "Symbolic AI",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "The Logic Approach",
                    "overview": "Symbolic AI uses rules and logic to represent knowledge.",
                    "sections": [
                        {"heading": "GOFAI", "content": "Good Old-Fashioned AI (GOFAI) uses:\n- Explicit rules and logic\n- Knowledge bases\n- Expert systems\n- Symbol manipulation"},
                        {"heading": "Example", "content": "IF patient has fever AND cough THEN diagnose flu\nKnowledge is explicitly programmed by humans."}
                    ]
                },
                "story": "'Symbolic AI writes knowledge as rules,' Sage teaches.",
                "task": "What does GOFAI stand for?",
                "starter_code": "# GOFAI means:\n",
                "expected_output": "Good Old-Fashioned AI",
                "hints": ["Good Old-Fashioned AI"]
            },
            {
                "id": 1603,
                "title": "Connectionism",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "The Neural Approach",
                    "overview": "Connectionism uses neural networks to learn patterns.",
                    "sections": [
                        {"heading": "The Idea", "content": "Instead of programming rules, let machines learn from data.\nInspired by biological neurons in the brain.\nNeural networks learn patterns through examples."},
                        {"heading": "vs Symbolic", "content": "Symbolic: explicit rules, interpretable, brittle\nConnectionist: learned patterns, black-box, robust\nModern AI combines both approaches."}
                    ]
                },
                "story": "'Connectionism lets machines learn like brains,' Sage reveals.",
                "task": "What is the main difference between Symbolic AI and Connectionism?",
                "starter_code": "# Key difference:\n",
                "expected_output": "rules vs learning from data",
                "hints": ["Symbolic uses rules, Connectionism learns from data"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Path of the Seeker",
        "topic": "Uninformed Search (BFS, DFS, Uniform Cost)",
        "description": "Master blind search algorithms.",
        "story_intro": "The Path of the Seeker teaches you to find solutions without guidance!",
        "character": "Blind Navigator",
        "character_quote": "Search systematically when you have no map!",
        "icon": "search",
        "color": "#7c4dff",
        "missions": [
            {
                "id": 1604,
                "title": "Breadth-First Search",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Exploring Level by Level",
                    "overview": "BFS explores all nodes at current depth before going deeper.",
                    "sections": [
                        {"heading": "Algorithm", "content": "Use a queue (FIFO)\n1. Start with initial node\n2. Expand all neighbors\n3. Add unexplored to queue\n4. Repeat until goal found"},
                        {"heading": "Properties", "content": "Complete: Yes (finds solution if exists)\nOptimal: Yes (for uniform cost)\nTime: O(b^d), Space: O(b^d)\nb=branching, d=depth"}
                    ]
                },
                "story": "'BFS explores layer by layer,' Blind Navigator explains.",
                "task": "What data structure does BFS use?",
                "starter_code": "# Data structure:\n",
                "expected_output": "queue",
                "hints": ["Queue (FIFO)"]
            },
            {
                "id": 1605,
                "title": "Depth-First Search",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Going Deep First",
                    "overview": "DFS explores as deep as possible before backtracking.",
                    "sections": [
                        {"heading": "Algorithm", "content": "Use a stack (LIFO)\n1. Start with initial node\n2. Go to first unexplored child\n3. Keep going deeper\n4. Backtrack when stuck"},
                        {"heading": "Properties", "content": "Complete: No (can get stuck in infinite paths)\nOptimal: No\nTime: O(b^m), Space: O(bm)\nm=max depth"}
                    ]
                },
                "story": "'DFS dives deep before exploring wide,' Navigator teaches.",
                "task": "What data structure does DFS use?",
                "starter_code": "# Data structure:\n",
                "expected_output": "stack",
                "hints": ["Stack (LIFO)"]
            },
            {
                "id": 1606,
                "title": "Uniform Cost Search",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Finding Cheapest Paths",
                    "overview": "UCS expands the node with lowest path cost.",
                    "sections": [
                        {"heading": "Algorithm", "content": "Use a priority queue ordered by path cost.\nAlways expand the cheapest unexpanded node.\nGuarantees optimal solution for positive costs."},
                        {"heading": "vs BFS", "content": "BFS: treats all edges as equal cost\nUCS: considers actual edge costs\nUCS is Dijkstra's algorithm for search."}
                    ]
                },
                "story": "'UCS finds the cheapest path,' Navigator reveals.",
                "task": "What data structure does Uniform Cost Search use?",
                "starter_code": "# Data structure:\n",
                "expected_output": "priority queue",
                "hints": ["Priority queue ordered by cost"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Seer's Shortcut",
        "topic": "Informed Search (A*, Heuristics)",
        "description": "Use knowledge to search smarter.",
        "story_intro": "The Seer's Shortcut uses wisdom to find paths faster!",
        "character": "Oracle Pathfinder",
        "character_quote": "Let heuristics guide your search!",
        "icon": "compass",
        "color": "#651fff",
        "missions": [
            {
                "id": 1607,
                "title": "Heuristics",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Educated Guesses",
                    "overview": "Heuristics estimate the cost to reach the goal.",
                    "sections": [
                        {"heading": "What is a Heuristic", "content": "h(n) = estimated cost from n to goal\nMust be:\n- Admissible: never overestimate\n- Consistent: h(n) <= cost(n,n') + h(n')"},
                        {"heading": "Examples", "content": "Straight-line distance (Euclidean)\nManhattan distance (grid)\nMisplaced tiles (puzzles)"}
                    ]
                },
                "story": "'Heuristics are educated guesses about distance,' Oracle Pathfinder explains.",
                "task": "What property must a heuristic have to guarantee optimal solutions?",
                "starter_code": "# Required property:\n",
                "expected_output": "admissible",
                "hints": ["Admissible - never overestimates"]
            },
            {
                "id": 1608,
                "title": "A* Search",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "The Best of Both Worlds",
                    "overview": "A* combines path cost and heuristic for optimal search.",
                    "sections": [
                        {"heading": "Formula", "content": "f(n) = g(n) + h(n)\ng(n) = cost from start to n\nh(n) = estimated cost from n to goal\nExpand node with lowest f(n)"},
                        {"heading": "Properties", "content": "Complete: Yes\nOptimal: Yes (if h is admissible)\nThe most popular pathfinding algorithm in games and robotics."}
                    ]
                },
                "story": "'A* is the crown jewel of search algorithms,' Pathfinder teaches.",
                "task": "What is the formula A* uses to evaluate nodes?",
                "starter_code": "# A* formula:\n",
                "expected_output": "f(n) = g(n) + h(n)",
                "hints": ["f(n) = g(n) + h(n)"]
            }
        ]
    },
    {
        "id": 4,
        "name": "The Duelist's Gambit",
        "topic": "Adversarial Search (Minimax, Alpha-Beta Pruning)",
        "description": "Master game-playing AI.",
        "story_intro": "The Duelist's Gambit teaches you to outsmart opponents!",
        "character": "Game Master",
        "character_quote": "Think ahead and anticipate your opponent!",
        "icon": "swords",
        "color": "#536dfe",
        "missions": [
            {
                "id": 1609,
                "title": "Minimax Algorithm",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Thinking Like Your Opponent",
                    "overview": "Minimax assumes optimal play from both sides.",
                    "sections": [
                        {"heading": "The Idea", "content": "MAX player tries to maximize score.\nMIN player tries to minimize score.\nAlternate between maximizing and minimizing at each level."},
                        {"heading": "Process", "content": "1. Build game tree to terminal states\n2. Evaluate terminal states\n3. Propagate values up:\n   - MAX nodes: take maximum\n   - MIN nodes: take minimum"}
                    ]
                },
                "story": "'Minimax assumes your opponent plays perfectly,' Game Master explains.",
                "task": "In Minimax, what does the MAX player try to do?",
                "starter_code": "# MAX player:\n",
                "expected_output": "maximize the score",
                "hints": ["Maximize the score/utility"]
            },
            {
                "id": 1610,
                "title": "Alpha-Beta Pruning",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Pruning the Game Tree",
                    "overview": "Alpha-Beta eliminates branches that can't affect the decision.",
                    "sections": [
                        {"heading": "The Optimization", "content": "Alpha: best value for MAX so far\nBeta: best value for MIN so far\nPrune when alpha >= beta"},
                        {"heading": "Benefit", "content": "Same result as Minimax.\nMuch faster: O(b^(d/2)) instead of O(b^d)\nEffective depth doubles!"}
                    ]
                },
                "story": "'Alpha-Beta prunes unnecessary branches,' Master teaches.",
                "task": "When does Alpha-Beta pruning occur?",
                "starter_code": "# Prune when:\n",
                "expected_output": "alpha >= beta",
                "hints": ["When alpha >= beta"]
            }
        ]
    },
    {
        "id": 5,
        "name": "The Puzzle Key",
        "topic": "Constraint Satisfaction Problems (CSPs)",
        "description": "Solve puzzles with constraints.",
        "story_intro": "The Puzzle Key unlocks solutions through constraints!",
        "character": "Constraint Keeper",
        "character_quote": "Constraints are not limitations, they are guides!",
        "icon": "puzzle",
        "color": "#448aff",
        "missions": [
            {
                "id": 1611,
                "title": "CSP Fundamentals",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Variables, Domains, and Constraints",
                    "overview": "CSPs define problems as variables with constraints.",
                    "sections": [
                        {"heading": "Components", "content": "Variables: X1, X2, ... Xn\nDomains: possible values for each variable\nConstraints: rules that must be satisfied"},
                        {"heading": "Examples", "content": "Sudoku: each cell is a variable\nMap coloring: each region is a variable\nScheduling: each task is a variable"}
                    ]
                },
                "story": "'CSPs break problems into variables and constraints,' Constraint Keeper explains.",
                "task": "What are the three components of a CSP?",
                "starter_code": "# Three components:\n",
                "expected_output": "variables, domains, constraints",
                "hints": ["Variables, Domains, Constraints"]
            },
            {
                "id": 1612,
                "title": "Backtracking Search",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Solving CSPs",
                    "overview": "Backtracking assigns values and backtracks on failure.",
                    "sections": [
                        {"heading": "Algorithm", "content": "1. Select unassigned variable\n2. Try a value from domain\n3. Check constraints\n4. If valid, recurse\n5. If fail, backtrack and try next value"},
                        {"heading": "Optimizations", "content": "- MRV: Most Restricted Variable first\n- Arc consistency: prune domains early\n- Forward checking"}
                    ]
                },
                "story": "'Backtracking explores and retreats when stuck,' Keeper teaches.",
                "task": "What does MRV stand for in CSP solving?",
                "starter_code": "# MRV means:\n",
                "expected_output": "Most Restricted Variable",
                "hints": ["Most Restricted Variable / Minimum Remaining Values"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Logic Link",
        "topic": "Propositional & First-Order Logic",
        "description": "Reason with formal logic.",
        "story_intro": "The Logic Link connects facts through reasoning!",
        "character": "Logic Weaver",
        "character_quote": "From premises, truth emerges!",
        "icon": "git-branch",
        "color": "#40c4ff",
        "missions": [
            {
                "id": 1613,
                "title": "Propositional Logic",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Logic of Propositions",
                    "overview": "Propositional logic deals with true/false statements.",
                    "sections": [
                        {"heading": "Operators", "content": "AND: A ^ B (both true)\nOR: A v B (at least one true)\nNOT: ~A (negation)\nIMPLIES: A -> B (if A then B)"},
                        {"heading": "Inference", "content": "Modus Ponens: A, A->B therefore B\nResolution: combine clauses to derive new facts"}
                    ]
                },
                "story": "'Propositional logic is the foundation of reasoning,' Logic Weaver explains.",
                "task": "What inference rule says: if A is true and A->B, then B is true?",
                "starter_code": "# Inference rule:\n",
                "expected_output": "Modus Ponens",
                "hints": ["Modus Ponens"]
            },
            {
                "id": 1614,
                "title": "First-Order Logic",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Logic with Quantifiers",
                    "overview": "First-order logic adds variables and quantifiers.",
                    "sections": [
                        {"heading": "Quantifiers", "content": "Universal: ForAll x, P(x) - for every x\nExistential: Exists x, P(x) - there exists an x"},
                        {"heading": "Example", "content": "ForAll x, Human(x) -> Mortal(x)\nHuman(Socrates)\nTherefore: Mortal(Socrates)"}
                    ]
                },
                "story": "'First-order logic reasons about all things,' Weaver teaches.",
                "task": "What are the two main quantifiers in first-order logic?",
                "starter_code": "# Two quantifiers:\n",
                "expected_output": "universal and existential",
                "hints": ["Universal (ForAll) and Existential (Exists)"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Oracle's Probability",
        "topic": "Bayesian Networks, Probabilistic Reasoning",
        "description": "Reason under uncertainty.",
        "story_intro": "The Oracle's Probability reveals truth through chance!",
        "character": "Probability Sage",
        "character_quote": "Certainty is rare, probability is everywhere!",
        "icon": "percent",
        "color": "#18ffff",
        "missions": [
            {
                "id": 1615,
                "title": "Bayes' Theorem",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Updating Beliefs",
                    "overview": "Bayes' theorem updates probability based on evidence.",
                    "sections": [
                        {"heading": "Formula", "content": "P(A|B) = P(B|A) * P(A) / P(B)\nPosterior = Likelihood * Prior / Evidence"},
                        {"heading": "Example", "content": "Disease test:\nP(Disease|Positive) depends on:\n- How accurate the test is\n- How common the disease is"}
                    ]
                },
                "story": "'Bayes updates beliefs with evidence,' Probability Sage explains.",
                "task": "In Bayes' theorem, what is P(A|B) called?",
                "starter_code": "# P(A|B) is the:\n",
                "expected_output": "posterior probability",
                "hints": ["Posterior probability"]
            },
            {
                "id": 1616,
                "title": "Bayesian Networks",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Graphical Probability Models",
                    "overview": "Bayesian networks represent probabilistic dependencies.",
                    "sections": [
                        {"heading": "Structure", "content": "Directed acyclic graph (DAG)\nNodes = random variables\nEdges = probabilistic dependencies\nEach node has conditional probability table"},
                        {"heading": "Inference", "content": "Can compute any conditional probability.\nUsed for diagnosis, prediction, reasoning."}
                    ]
                },
                "story": "'Bayesian networks model uncertain worlds,' Sage teaches.",
                "task": "What type of graph structure do Bayesian networks use?",
                "starter_code": "# Graph type:\n",
                "expected_output": "directed acyclic graph",
                "hints": ["DAG / Directed Acyclic Graph"]
            }
        ]
    },
    {
        "id": 8,
        "name": "The Planning Chamber",
        "topic": "Automated Planning, Goal-oriented action",
        "description": "Plan sequences of actions to achieve goals.",
        "story_intro": "The Planning Chamber turns goals into action sequences!",
        "character": "Strategy Architect",
        "character_quote": "Every goal needs a plan!",
        "icon": "map",
        "color": "#64ffda",
        "missions": [
            {
                "id": 1617,
                "title": "Automated Planning",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "From Goals to Actions",
                    "overview": "Planning finds action sequences to achieve goals.",
                    "sections": [
                        {"heading": "STRIPS Representation", "content": "State: set of facts (predicates)\nGoal: desired state conditions\nActions: preconditions and effects\nFind sequence: initial -> goal"},
                        {"heading": "Example", "content": "Initial: At(Home), ~Have(Milk)\nGoal: Have(Milk)\nActions: Go(Store), Buy(Milk)\nPlan: Go(Store), Buy(Milk)"}
                    ]
                },
                "story": "'Planning bridges current state to goals,' Strategy Architect explains.",
                "task": "What does STRIPS define for each action?",
                "starter_code": "# STRIPS actions have:\n",
                "expected_output": "preconditions and effects",
                "hints": ["Preconditions and effects"]
            },
            {
                "id": 1618,
                "title": "Goal-Oriented Action",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "GOAP in Games",
                    "overview": "Goal-Oriented Action Planning is used in game AI.",
                    "sections": [
                        {"heading": "GOAP", "content": "Goals have priority and conditions.\nActions have costs and effects.\nPlanner finds cheapest action sequence.\nUsed in games like F.E.A.R., Fallout"},
                        {"heading": "Process", "content": "1. Agent has current goal\n2. Planner searches for action sequence\n3. Execute actions\n4. Replan if world changes"}
                    ]
                },
                "story": "'GOAP makes game NPCs feel alive,' Architect teaches.",
                "task": "What famous game first used GOAP for AI?",
                "starter_code": "# Famous game:\n",
                "expected_output": "F.E.A.R.",
                "hints": ["F.E.A.R."]
            }
        ]
    },
    {
        "id": 9,
        "name": "Rite of Reinforcement",
        "topic": "Agent-Environment loop, Q-Learning basics",
        "description": "Learn through trial and error.",
        "story_intro": "The Rite of Reinforcement teaches learning by doing!",
        "character": "Reward Seeker",
        "character_quote": "Every action has consequences - learn from them!",
        "icon": "refresh-cw",
        "color": "#69f0ae",
        "missions": [
            {
                "id": 1619,
                "title": "Agent-Environment Loop",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "The RL Framework",
                    "overview": "An agent learns by interacting with an environment.",
                    "sections": [
                        {"heading": "Components", "content": "Agent: the learner/decision maker\nEnvironment: the world\nState: current situation\nAction: what agent can do\nReward: feedback signal"},
                        {"heading": "Loop", "content": "1. Agent observes state\n2. Agent takes action\n3. Environment returns reward and new state\n4. Agent learns from experience"}
                    ]
                },
                "story": "'RL agents learn through interaction,' Reward Seeker explains.",
                "task": "What are the five key components of reinforcement learning?",
                "starter_code": "# Five components:\n",
                "expected_output": "agent, environment, state, action, reward",
                "hints": ["Agent, Environment, State, Action, Reward"]
            },
            {
                "id": 1620,
                "title": "Q-Learning",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Learning Action Values",
                    "overview": "Q-Learning learns the value of state-action pairs.",
                    "sections": [
                        {"heading": "Q-Value", "content": "Q(s,a) = expected future reward for action a in state s\nBellman equation:\nQ(s,a) = r + gamma * max Q(s',a')"},
                        {"heading": "Algorithm", "content": "1. Initialize Q-table\n2. Take action (epsilon-greedy)\n3. Observe reward and new state\n4. Update Q(s,a)\n5. Repeat until convergence"}
                    ]
                },
                "story": "'Q-Learning discovers optimal policies,' Seeker teaches.",
                "task": "What does Q(s,a) represent in Q-Learning?",
                "starter_code": "# Q(s,a) represents:\n",
                "expected_output": "expected future reward",
                "hints": ["Expected future reward for taking action a in state s"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Mirror of Ethics",
        "topic": "AI Bias, Fairness, Safety, Hallucinations",
        "description": "Understand AI's responsibilities.",
        "story_intro": "The Mirror of Ethics reflects AI's impact on society!",
        "character": "Ethics Guardian",
        "character_quote": "With great power comes great responsibility!",
        "icon": "shield",
        "color": "#b2ff59",
        "missions": [
            {
                "id": 1621,
                "title": "AI Bias and Fairness",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Unintended Discrimination",
                    "overview": "AI systems can perpetuate or amplify human biases.",
                    "sections": [
                        {"heading": "Sources of Bias", "content": "- Training data reflects historical biases\n- Feature selection can encode discrimination\n- Feedback loops amplify inequalities"},
                        {"heading": "Examples", "content": "- Hiring algorithms discriminating by gender\n- Facial recognition failing on dark skin\n- Loan algorithms disadvantaging minorities"}
                    ]
                },
                "story": "'AI can inherit our biases,' Ethics Guardian explains.",
                "task": "Name one source of bias in AI systems.",
                "starter_code": "# Source of bias:\n",
                "expected_output": "training data",
                "hints": ["Biased training data, feature selection, feedback loops"]
            },
            {
                "id": 1622,
                "title": "AI Safety",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Ensuring Safe AI",
                    "overview": "AI systems must be aligned with human values.",
                    "sections": [
                        {"heading": "Concerns", "content": "- Value alignment: AI goals match human intentions\n- Robustness: safe under distribution shift\n- Interpretability: understanding AI decisions\n- Control: ability to correct or stop AI"},
                        {"heading": "Approaches", "content": "- RLHF: Reinforcement Learning from Human Feedback\n- Constitutional AI: rules and principles\n- Red teaming: adversarial testing"}
                    ]
                },
                "story": "'AI must serve humanity safely,' Guardian teaches.",
                "task": "What does RLHF stand for?",
                "starter_code": "# RLHF means:\n",
                "expected_output": "Reinforcement Learning from Human Feedback",
                "hints": ["Reinforcement Learning from Human Feedback"]
            },
            {
                "id": 1623,
                "title": "AI Hallucinations",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "When AI Makes Things Up",
                    "overview": "LLMs can generate confident but false information.",
                    "sections": [
                        {"heading": "The Problem", "content": "AI generates plausible-sounding but incorrect facts.\nCan cite non-existent sources.\nConfidence doesn't indicate accuracy."},
                        {"heading": "Mitigation", "content": "- Retrieval augmented generation (RAG)\n- Fact-checking and verification\n- Uncertainty quantification\n- Human oversight"}
                    ]
                },
                "story": "'AI can confidently be wrong,' Guardian reveals.",
                "task": "What technique helps reduce hallucinations by grounding responses in retrieved documents?",
                "starter_code": "# Technique:\n",
                "expected_output": "RAG",
                "hints": ["RAG / Retrieval Augmented Generation"]
            }
        ]
    },
    {
        "id": 11,
        "name": "The Golem's Dream",
        "topic": "Multi-modal AI, AGI concepts, LLMs",
        "description": "Explore cutting-edge AI.",
        "story_intro": "The Golem's Dream reveals the future of AI!",
        "character": "Visionary Sage",
        "character_quote": "The future of AI is more than we can imagine!",
        "icon": "sparkles",
        "color": "#eeff41",
        "missions": [
            {
                "id": 1624,
                "title": "Multi-Modal AI",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "AI That Sees and Speaks",
                    "overview": "Multi-modal AI processes multiple types of data.",
                    "sections": [
                        {"heading": "Modalities", "content": "Text, images, audio, video, code.\nCombine understanding across modalities.\nExamples: GPT-4V, Gemini, Claude"},
                        {"heading": "Applications", "content": "- Image captioning\n- Visual question answering\n- Video understanding\n- Cross-modal search"}
                    ]
                },
                "story": "'Multi-modal AI perceives the world fully,' Visionary Sage explains.",
                "task": "Name three modalities that multi-modal AI can process.",
                "starter_code": "# Three modalities:\n",
                "expected_output": "text, images, audio",
                "hints": ["Text, images, audio, video, code"]
            },
            {
                "id": 1625,
                "title": "Large Language Models",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The LLM Revolution",
                    "overview": "LLMs have transformed AI capabilities.",
                    "sections": [
                        {"heading": "Key Concepts", "content": "Pre-training on massive text corpora.\nEmergent abilities at scale.\nIn-context learning.\nInstruction following."},
                        {"heading": "Examples", "content": "GPT-4, Claude, Gemini, LLaMA\nBillions of parameters.\nCan code, reason, create."}
                    ]
                },
                "story": "'LLMs are reshaping what AI can do,' Sage teaches.",
                "task": "What is the ability of LLMs to learn from examples in the prompt called?",
                "starter_code": "# Learning ability:\n",
                "expected_output": "in-context learning",
                "hints": ["In-context learning"]
            },
            {
                "id": 1626,
                "title": "AGI Concepts",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Artificial General Intelligence",
                    "overview": "AGI is AI that can do any intellectual task a human can.",
                    "sections": [
                        {"heading": "vs Narrow AI", "content": "Narrow AI: excels at specific tasks\nAGI: general-purpose intelligence\nASI: superintelligence beyond human level"},
                        {"heading": "Debate", "content": "When will AGI arrive? Years? Decades?\nWhat are the risks and benefits?\nHow do we ensure it's aligned with human values?"}
                    ]
                },
                "story": "'AGI is the ultimate goal and challenge,' Sage reveals.",
                "task": "What is the difference between AGI and narrow AI?",
                "starter_code": "# Key difference:\n",
                "expected_output": "AGI is general-purpose, narrow AI is task-specific",
                "hints": ["AGI is general-purpose, narrow AI is specialized"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Architect of Infinity",
        "topic": "Final Project: Designing an Intelligent Game Agent",
        "description": "Build a complete AI agent.",
        "story_intro": "Become the Architect of Infinity by creating your own intelligent agent!",
        "character": "Grand Architect",
        "character_quote": "You now command the wisdom to create intelligence!",
        "icon": "trophy",
        "color": "#ffd740",
        "missions": [
            {
                "id": 1627,
                "title": "Designing a Game Agent",
                "difficulty": "hard",
                "xp": 60,
                "lesson": {
                    "title": "Building an Intelligent Player",
                    "overview": "Combine AI techniques to create a game-playing agent.",
                    "sections": [
                        {"heading": "Components", "content": "1. State representation\n2. Search algorithm (Minimax or MCTS)\n3. Evaluation function / Heuristic\n4. Learning component (optional)"},
                        {"heading": "Approach", "content": "Choose a game (Tic-tac-toe, Connect4)\nImplement game logic\nAdd search with alpha-beta\nOptimize with good heuristics"}
                    ]
                },
                "story": "'Design an agent that thinks ahead!' Grand Architect challenges.",
                "task": "What search algorithm would you use for a two-player game?",
                "starter_code": "# Search algorithm:\n",
                "expected_output": "Minimax",
                "hints": ["Minimax with Alpha-Beta pruning"]
            },
            {
                "id": 1628,
                "title": "AI Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Grand Architect",
                    "overview": "You've mastered the foundations of Artificial Intelligence!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- AI history and philosophy\n- Search algorithms (BFS, DFS, A*)\n- Game playing (Minimax, Alpha-Beta)\n- Constraint satisfaction\n- Logic and reasoning\n- Probability and Bayesian networks\n- Planning\n- Reinforcement learning\n- AI ethics and safety\n- Modern AI and LLMs"},
                        {"heading": "Next Steps", "content": "- Build more complex agents\n- Explore specialized AI domains\n- Contribute to AI safety research\n- Create AI that benefits humanity"}
                    ]
                },
                "story": "'You have become the Grand Architect!' The Great Golem recognizes your wisdom!",
                "task": "Name three AI search algorithms you've learned.",
                "starter_code": "# Three algorithms:\n",
                "expected_output": "BFS, DFS, A*",
                "hints": ["BFS, DFS, A*, Uniform Cost, Minimax"]
            }
        ]
    }
]

EXCEL_ARCS = [
    {
        "id": 1,
        "name": "The Scribe's Basics",
        "topic": "Cells, Ranges, Formatting, Shortcuts",
        "description": "Master the fundamentals of spreadsheet navigation.",
        "story_intro": "Welcome to the Excel Grimoire! First, learn the basic incantations of the spreadsheet realm.",
        "character": "Scribe Master",
        "character_quote": "Every great sorcerer begins with the basics!",
        "icon": "grid",
        "color": "#217346",
        "missions": [
            {
                "id": 1701,
                "title": "Cells and Ranges",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "The Building Blocks",
                    "overview": "Cells are the foundation of every spreadsheet.",
                    "sections": [
                        {"heading": "Cell Basics", "content": "A cell is the intersection of a row and column.\nCell address: Column letter + Row number (e.g., A1, B5)\nA range is a group of cells (e.g., A1:C5)."},
                        {"heading": "Selecting", "content": "Click a cell to select it.\nDrag to select a range.\nCtrl+Click for non-adjacent cells.\nShift+Click for continuous range."}
                    ]
                },
                "story": "'Each cell holds a piece of the realm's data,' Scribe Master explains.",
                "task": "What is the cell address for column B, row 3?",
                "starter_code": "# Cell address:\n",
                "expected_output": "B3",
                "hints": ["Column letter followed by row number"]
            },
            {
                "id": 1702,
                "title": "Formatting Cells",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Making Data Beautiful",
                    "overview": "Formatting makes data readable and professional.",
                    "sections": [
                        {"heading": "Number Formats", "content": "Currency: $1,234.56\nPercentage: 75%\nDate: 12/25/2024\nCustom formats for special needs."},
                        {"heading": "Visual Formatting", "content": "Bold, Italic, Underline\nFill color and font color\nBorders and alignment\nMerge cells for headers"}
                    ]
                },
                "story": "'Presentation matters as much as data,' Master teaches.",
                "task": "What format would you use to display 0.75 as 75%?",
                "starter_code": "# Format type:\n",
                "expected_output": "percentage",
                "hints": ["Percentage format"]
            },
            {
                "id": 1703,
                "title": "Essential Shortcuts",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Speed Through Sorcery",
                    "overview": "Keyboard shortcuts make you faster.",
                    "sections": [
                        {"heading": "Navigation", "content": "Ctrl+Home: Go to A1\nCtrl+End: Go to last used cell\nCtrl+Arrow: Jump to edge of data"},
                        {"heading": "Editing", "content": "Ctrl+C: Copy\nCtrl+V: Paste\nCtrl+Z: Undo\nCtrl+S: Save\nF2: Edit cell"}
                    ]
                },
                "story": "'True masters never touch the mouse,' Master reveals.",
                "task": "What shortcut goes to the beginning of the spreadsheet (cell A1)?",
                "starter_code": "# Shortcut:\n",
                "expected_output": "Ctrl+Home",
                "hints": ["Ctrl+Home"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Incantation of Sums",
        "topic": "SUM, AVERAGE, COUNT, MIN/MAX",
        "description": "Learn the basic mathematical formulas.",
        "story_intro": "The Incantation of Sums teaches you to perform calculations with ease!",
        "character": "Math Mage",
        "character_quote": "Numbers obey those who know the formulas!",
        "icon": "calculator",
        "color": "#2e7d32",
        "missions": [
            {
                "id": 1704,
                "title": "SUM Function",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Adding Numbers",
                    "overview": "SUM adds up all values in a range.",
                    "sections": [
                        {"heading": "Syntax", "content": "=SUM(number1, [number2], ...)\n=SUM(A1:A10) adds cells A1 through A10\n=SUM(A1, B1, C1) adds specific cells"},
                        {"heading": "Tips", "content": "Alt+= is a shortcut for AutoSum.\nSUM ignores text and empty cells.\nCan sum multiple ranges: =SUM(A1:A10, C1:C10)"}
                    ]
                },
                "story": "'SUM is the most used formula in all the realm,' Math Mage explains.",
                "task": "Write a formula to sum cells A1 through A10.",
                "starter_code": "# Formula:\n",
                "expected_output": "=SUM(A1:A10)",
                "hints": ["=SUM(range)"]
            },
            {
                "id": 1705,
                "title": "AVERAGE Function",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Finding the Mean",
                    "overview": "AVERAGE calculates the arithmetic mean.",
                    "sections": [
                        {"heading": "Syntax", "content": "=AVERAGE(number1, [number2], ...)\n=AVERAGE(B1:B20) averages the range\nIgnores empty cells and text."},
                        {"heading": "Example", "content": "If B1:B5 contains 10, 20, 30, 40, 50\n=AVERAGE(B1:B5) returns 30"}
                    ]
                },
                "story": "'AVERAGE finds the center of your data,' Mage teaches.",
                "task": "Write a formula to find the average of cells B1 through B20.",
                "starter_code": "# Formula:\n",
                "expected_output": "=AVERAGE(B1:B20)",
                "hints": ["=AVERAGE(range)"]
            },
            {
                "id": 1706,
                "title": "COUNT Function",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Counting Numbers",
                    "overview": "COUNT counts cells containing numbers.",
                    "sections": [
                        {"heading": "COUNT vs COUNTA", "content": "COUNT: counts cells with numbers only\nCOUNTA: counts all non-empty cells\nCOUNTBLANK: counts empty cells"},
                        {"heading": "Example", "content": "If A1:A5 has: 1, 'text', 3, '', 5\nCOUNT returns 3\nCOUNTA returns 4"}
                    ]
                },
                "story": "'COUNT reveals how many numbers you have,' Mage reveals.",
                "task": "Which function counts ALL non-empty cells including text?",
                "starter_code": "# Function:\n",
                "expected_output": "COUNTA",
                "hints": ["COUNTA counts all non-empty cells"]
            },
            {
                "id": 1707,
                "title": "MIN and MAX",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Finding Extremes",
                    "overview": "MIN and MAX find the smallest and largest values.",
                    "sections": [
                        {"heading": "Syntax", "content": "=MIN(range) - returns smallest value\n=MAX(range) - returns largest value\nBoth ignore text and empty cells."},
                        {"heading": "Example", "content": "If C1:C5 contains 10, 5, 25, 15, 20\n=MIN(C1:C5) returns 5\n=MAX(C1:C5) returns 25"}
                    ]
                },
                "story": "'MIN and MAX find the boundaries of your data,' Mage teaches.",
                "task": "Write a formula to find the largest value in C1:C100.",
                "starter_code": "# Formula:\n",
                "expected_output": "=MAX(C1:C100)",
                "hints": ["=MAX(range)"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Logic Mirror",
        "topic": "IF, AND, OR, Nested IFs",
        "description": "Make decisions with conditional formulas.",
        "story_intro": "The Logic Mirror reflects the truth through conditions!",
        "character": "Logic Oracle",
        "character_quote": "Every decision follows a pattern of logic!",
        "icon": "git-branch",
        "color": "#388e3c",
        "missions": [
            {
                "id": 1708,
                "title": "IF Function",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Making Decisions",
                    "overview": "IF returns different values based on a condition.",
                    "sections": [
                        {"heading": "Syntax", "content": "=IF(logical_test, value_if_true, value_if_false)\nExample: =IF(A1>10, 'High', 'Low')\nReturns 'High' if A1>10, otherwise 'Low'"},
                        {"heading": "Comparisons", "content": "= Equal\n<> Not equal\n> Greater than\n< Less than\n>= Greater or equal\n<= Less or equal"}
                    ]
                },
                "story": "'IF is the gateway to decision-making,' Logic Oracle explains.",
                "task": "Write an IF formula that returns 'Pass' if B1>=60, otherwise 'Fail'.",
                "starter_code": "# Formula:\n",
                "expected_output": "=IF(B1>=60,\"Pass\",\"Fail\")",
                "hints": ["=IF(condition, true_value, false_value)"]
            },
            {
                "id": 1709,
                "title": "AND Function",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Multiple Conditions - All Must Be True",
                    "overview": "AND returns TRUE only if all conditions are true.",
                    "sections": [
                        {"heading": "Syntax", "content": "=AND(condition1, condition2, ...)\nReturns TRUE if ALL conditions are true.\nReturns FALSE if ANY condition is false."},
                        {"heading": "With IF", "content": "=IF(AND(A1>0, A1<100), 'Valid', 'Invalid')\nChecks if A1 is between 0 and 100."}
                    ]
                },
                "story": "'AND demands all conditions be met,' Oracle teaches.",
                "task": "Write a formula using AND to check if A1>10 AND B1<20.",
                "starter_code": "# Formula:\n",
                "expected_output": "=AND(A1>10,B1<20)",
                "hints": ["=AND(condition1, condition2)"]
            },
            {
                "id": 1710,
                "title": "OR Function",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Multiple Conditions - Any Can Be True",
                    "overview": "OR returns TRUE if any condition is true.",
                    "sections": [
                        {"heading": "Syntax", "content": "=OR(condition1, condition2, ...)\nReturns TRUE if ANY condition is true.\nReturns FALSE only if ALL are false."},
                        {"heading": "With IF", "content": "=IF(OR(A1='Red', A1='Blue'), 'Primary', 'Other')\nChecks if A1 is Red or Blue."}
                    ]
                },
                "story": "'OR accepts any single truth,' Oracle reveals.",
                "task": "Write a formula using OR to check if C1='Yes' OR C1='Y'.",
                "starter_code": "# Formula:\n",
                "expected_output": "=OR(C1=\"Yes\",C1=\"Y\")",
                "hints": ["=OR(condition1, condition2)"]
            },
            {
                "id": 1711,
                "title": "Nested IFs",
                "difficulty": "hard",
                "xp": 45,
                "lesson": {
                    "title": "Multiple Outcomes",
                    "overview": "Nested IFs handle multiple conditions and outcomes.",
                    "sections": [
                        {"heading": "Structure", "content": "=IF(test1, result1, IF(test2, result2, result3))\nEach IF is nested in the false branch.\nCan nest up to 64 levels (but don't!)."},
                        {"heading": "Example", "content": "Grade formula:\n=IF(A1>=90,'A',IF(A1>=80,'B',IF(A1>=70,'C','F')))\nIFS function is cleaner for multiple conditions."}
                    ]
                },
                "story": "'Nested IFs create complex decision trees,' Oracle teaches.",
                "task": "What function is a cleaner alternative to deeply nested IFs?",
                "starter_code": "# Function:\n",
                "expected_output": "IFS",
                "hints": ["IFS function handles multiple conditions more cleanly"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Search for the Hidden",
        "topic": "VLOOKUP, HLOOKUP, XLOOKUP",
        "description": "Find data across tables.",
        "story_intro": "Search for the Hidden reveals data across the realm's many tables!",
        "character": "Data Seeker",
        "character_quote": "No data can hide from a true seeker!",
        "icon": "search",
        "color": "#43a047",
        "missions": [
            {
                "id": 1712,
                "title": "VLOOKUP Function",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Vertical Lookup",
                    "overview": "VLOOKUP searches vertically in the first column.",
                    "sections": [
                        {"heading": "Syntax", "content": "=VLOOKUP(lookup_value, table_array, col_index, [range_lookup])\nlookup_value: what to find\ntable_array: where to search\ncol_index: which column to return\nrange_lookup: FALSE for exact match"},
                        {"heading": "Example", "content": "=VLOOKUP('Apple', A1:C10, 3, FALSE)\nFinds 'Apple' in column A, returns value from column C."}
                    ]
                },
                "story": "'VLOOKUP is the classic search spell,' Data Seeker explains.",
                "task": "In VLOOKUP, what does the 4th argument FALSE mean?",
                "starter_code": "# FALSE means:\n",
                "expected_output": "exact match",
                "hints": ["FALSE means exact match, TRUE means approximate"]
            },
            {
                "id": 1713,
                "title": "HLOOKUP Function",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Horizontal Lookup",
                    "overview": "HLOOKUP searches horizontally in the first row.",
                    "sections": [
                        {"heading": "Syntax", "content": "=HLOOKUP(lookup_value, table_array, row_index, [range_lookup])\nSame as VLOOKUP but searches across rows.\nrow_index specifies which row to return."},
                        {"heading": "When to Use", "content": "Use HLOOKUP when your data is arranged horizontally.\nHeaders in the first row, data below.\nLess common than VLOOKUP."}
                    ]
                },
                "story": "'HLOOKUP searches across instead of down,' Seeker teaches.",
                "task": "What is the main difference between VLOOKUP and HLOOKUP?",
                "starter_code": "# Difference:\n",
                "expected_output": "vertical vs horizontal search",
                "hints": ["VLOOKUP searches down columns, HLOOKUP searches across rows"]
            },
            {
                "id": 1714,
                "title": "XLOOKUP Function",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The Modern Lookup",
                    "overview": "XLOOKUP replaces VLOOKUP with more power.",
                    "sections": [
                        {"heading": "Syntax", "content": "=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])\nCan look left or right.\nBuilt-in error handling."},
                        {"heading": "Advantages", "content": "- Can return values from any column (left or right)\n- Better error handling\n- Simpler syntax\n- Can search from bottom up"}
                    ]
                },
                "story": "'XLOOKUP is the future of lookups,' Seeker reveals.",
                "task": "What advantage does XLOOKUP have over VLOOKUP?",
                "starter_code": "# Advantage:\n",
                "expected_output": "can look left or right",
                "hints": ["XLOOKUP can look left, VLOOKUP cannot"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Purifying the Ink",
        "topic": "Text-to-Columns, Flash Fill, Duplicates",
        "description": "Clean and transform messy data.",
        "story_intro": "Purifying the Ink teaches you to cleanse corrupted data!",
        "character": "Data Alchemist",
        "character_quote": "Dirty data leads to false conclusions!",
        "icon": "filter",
        "color": "#4caf50",
        "missions": [
            {
                "id": 1715,
                "title": "Text to Columns",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Splitting Data",
                    "overview": "Split one column into multiple based on delimiter.",
                    "sections": [
                        {"heading": "How It Works", "content": "Data tab > Text to Columns\nDelimited: split by comma, tab, space, etc.\nFixed width: split at specific positions."},
                        {"heading": "Common Uses", "content": "Split full names into first/last.\nSplit dates into day/month/year.\nSplit addresses into components."}
                    ]
                },
                "story": "'Text to Columns separates the combined,' Data Alchemist explains.",
                "task": "Where do you find Text to Columns in Excel?",
                "starter_code": "# Location:\n",
                "expected_output": "Data tab",
                "hints": ["Data tab > Text to Columns"]
            },
            {
                "id": 1716,
                "title": "Flash Fill",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Pattern Recognition",
                    "overview": "Flash Fill detects patterns and fills automatically.",
                    "sections": [
                        {"heading": "How to Use", "content": "Type the pattern you want in the first cell.\nPress Ctrl+E or Data > Flash Fill.\nExcel detects the pattern and fills the rest."},
                        {"heading": "Examples", "content": "Extract first name from 'John Smith' -> 'John'\nFormat phone: 1234567890 -> (123) 456-7890\nCombine data: 'John' + 'Smith' -> 'John Smith'"}
                    ]
                },
                "story": "'Flash Fill learns your patterns,' Alchemist teaches.",
                "task": "What is the keyboard shortcut for Flash Fill?",
                "starter_code": "# Shortcut:\n",
                "expected_output": "Ctrl+E",
                "hints": ["Ctrl+E"]
            },
            {
                "id": 1717,
                "title": "Removing Duplicates",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Eliminating Redundancy",
                    "overview": "Remove duplicate rows from your data.",
                    "sections": [
                        {"heading": "How to Remove", "content": "Data tab > Remove Duplicates\nSelect which columns to check.\nKeeps first occurrence, removes others."},
                        {"heading": "Caution", "content": "Always make a backup first!\nThis action cannot be undone easily.\nUse conditional formatting to highlight first."}
                    ]
                },
                "story": "'Duplicates corrupt the truth of data,' Alchemist reveals.",
                "task": "Where is Remove Duplicates located in Excel?",
                "starter_code": "# Location:\n",
                "expected_output": "Data tab",
                "hints": ["Data tab > Remove Duplicates"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Pivot Portal",
        "topic": "Creating Pivot Tables, Field Settings",
        "description": "Aggregate and summarize data powerfully.",
        "story_intro": "The Pivot Portal transforms raw data into insights!",
        "character": "Pivot Master",
        "character_quote": "Pivot Tables reveal patterns hidden in chaos!",
        "icon": "layers",
        "color": "#66bb6a",
        "missions": [
            {
                "id": 1718,
                "title": "Creating Pivot Tables",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Building Your First Pivot",
                    "overview": "Pivot Tables summarize large datasets instantly.",
                    "sections": [
                        {"heading": "How to Create", "content": "Select your data (including headers).\nInsert tab > PivotTable.\nChoose where to place it.\nDrag fields to Rows, Columns, Values."},
                        {"heading": "Field Areas", "content": "Rows: Categories down the left.\nColumns: Categories across the top.\nValues: Numbers to summarize.\nFilters: Overall data filters."}
                    ]
                },
                "story": "'Pivot Tables are the most powerful summarization tool,' Pivot Master explains.",
                "task": "What are the four areas where you can drag fields in a Pivot Table?",
                "starter_code": "# Four areas:\n",
                "expected_output": "Rows, Columns, Values, Filters",
                "hints": ["Rows, Columns, Values, Filters"]
            },
            {
                "id": 1719,
                "title": "Field Settings",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Customizing Calculations",
                    "overview": "Change how Pivot Tables calculate values.",
                    "sections": [
                        {"heading": "Value Field Settings", "content": "Right-click a value > Value Field Settings.\nSummarize by: Sum, Count, Average, Max, Min.\nShow Values As: % of total, Running total, Rank."},
                        {"heading": "Tips", "content": "Text fields default to Count.\nNumber fields default to Sum.\nChange the number format here too."}
                    ]
                },
                "story": "'Field settings control the magic of aggregation,' Master teaches.",
                "task": "What is the default summarization for number fields in a Pivot Table?",
                "starter_code": "# Default:\n",
                "expected_output": "Sum",
                "hints": ["Sum is the default for numbers"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Alchemist's Slicer",
        "topic": "Slicers, Timelines, Pivot Charts",
        "description": "Make Pivot Tables interactive.",
        "story_intro": "The Alchemist's Slicer creates interactive data exploration!",
        "character": "Visual Enchanter",
        "character_quote": "Interactive visuals tell stories data cannot!",
        "icon": "sliders",
        "color": "#81c784",
        "missions": [
            {
                "id": 1720,
                "title": "Using Slicers",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Visual Filters",
                    "overview": "Slicers are visual buttons to filter Pivot Tables.",
                    "sections": [
                        {"heading": "How to Add", "content": "Click in Pivot Table.\nPivotTable Analyze > Insert Slicer.\nSelect fields to create slicers for.\nClick slicer buttons to filter."},
                        {"heading": "Tips", "content": "Hold Ctrl to select multiple items.\nClear filter button in top right.\nSlicers can control multiple Pivot Tables."}
                    ]
                },
                "story": "'Slicers make filtering visual and intuitive,' Visual Enchanter explains.",
                "task": "How do you select multiple items in a Slicer?",
                "starter_code": "# Method:\n",
                "expected_output": "Hold Ctrl and click",
                "hints": ["Hold Ctrl while clicking"]
            },
            {
                "id": 1721,
                "title": "Timelines",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Filtering by Date",
                    "overview": "Timelines filter date fields visually.",
                    "sections": [
                        {"heading": "How to Add", "content": "Click in Pivot Table with date field.\nPivotTable Analyze > Insert Timeline.\nSelect the date field.\nDrag timeline to filter by period."},
                        {"heading": "Features", "content": "Filter by Years, Quarters, Months, Days.\nDrag to select date ranges.\nWorks like slicers but for dates."}
                    ]
                },
                "story": "'Timelines reveal trends across time,' Enchanter teaches.",
                "task": "What types of periods can you filter by in a Timeline?",
                "starter_code": "# Periods:\n",
                "expected_output": "Years, Quarters, Months, Days",
                "hints": ["Years, Quarters, Months, Days"]
            },
            {
                "id": 1722,
                "title": "Pivot Charts",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Visualizing Pivot Data",
                    "overview": "Pivot Charts are charts linked to Pivot Tables.",
                    "sections": [
                        {"heading": "How to Create", "content": "Click in Pivot Table.\nPivotTable Analyze > PivotChart.\nChoose chart type.\nChart updates when Pivot Table changes."},
                        {"heading": "Benefits", "content": "Automatically updates with data.\nInteractive filtering with field buttons.\nCombines analysis and visualization."}
                    ]
                },
                "story": "'Pivot Charts bring data to life,' Enchanter reveals.",
                "task": "What happens to a Pivot Chart when you filter the Pivot Table?",
                "starter_code": "# Result:\n",
                "expected_output": "chart updates automatically",
                "hints": ["The chart updates to reflect the filter"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Power Query Awakening",
        "topic": "Importing data, Power Query Editor",
        "description": "Import and transform data from anywhere.",
        "story_intro": "Power Query Awakening unlocks data from across realms!",
        "character": "Query Wizard",
        "character_quote": "Power Query connects all data sources!",
        "icon": "database",
        "color": "#a5d6a7",
        "missions": [
            {
                "id": 1723,
                "title": "Importing Data",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Connecting to Sources",
                    "overview": "Power Query imports data from many sources.",
                    "sections": [
                        {"heading": "Data Sources", "content": "Data tab > Get Data\nFrom File: Excel, CSV, XML, JSON\nFrom Database: SQL Server, Access\nFrom Web: websites, APIs"},
                        {"heading": "Process", "content": "1. Select data source\n2. Connect and preview\n3. Transform in Power Query\n4. Load to Excel"}
                    ]
                },
                "story": "'Power Query imports from any source,' Query Wizard explains.",
                "task": "Where do you find Get Data in Excel?",
                "starter_code": "# Location:\n",
                "expected_output": "Data tab",
                "hints": ["Data tab > Get Data"]
            },
            {
                "id": 1724,
                "title": "Power Query Editor",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The Transformation Workshop",
                    "overview": "Power Query Editor transforms data with clicks.",
                    "sections": [
                        {"heading": "Interface", "content": "Query Settings pane on right.\nApplied Steps shows your transformations.\nPreview shows data changes in real-time.\nFormula bar shows M code."},
                        {"heading": "Common Actions", "content": "Remove columns\nChange data types\nFilter rows\nSplit columns\nReplace values"}
                    ]
                },
                "story": "'The Editor records every transformation,' Wizard teaches.",
                "task": "What language does Power Query use internally?",
                "starter_code": "# Language:\n",
                "expected_output": "M",
                "hints": ["M language / Power Query Formula Language"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Transmutation Stream",
        "topic": "Merging, Appending, Unpivoting data",
        "description": "Advanced data transformations.",
        "story_intro": "The Transmutation Stream reshapes data completely!",
        "character": "Transform Sage",
        "character_quote": "Data takes any shape you need!",
        "icon": "shuffle",
        "color": "#c8e6c9",
        "missions": [
            {
                "id": 1725,
                "title": "Merging Queries",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Joining Tables",
                    "overview": "Merge combines tables based on matching columns.",
                    "sections": [
                        {"heading": "How to Merge", "content": "Home > Merge Queries.\nSelect tables and matching columns.\nChoose join type.\nExpand the merged column."},
                        {"heading": "Join Types", "content": "Left Outer: all from first, matches from second\nRight Outer: all from second, matches from first\nFull Outer: all from both\nInner: only matching rows"}
                    ]
                },
                "story": "'Merging combines data from multiple sources,' Transform Sage explains.",
                "task": "Which join type keeps ALL rows from both tables?",
                "starter_code": "# Join type:\n",
                "expected_output": "Full Outer",
                "hints": ["Full Outer Join keeps all rows"]
            },
            {
                "id": 1726,
                "title": "Appending Queries",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Stacking Tables",
                    "overview": "Append stacks tables on top of each other.",
                    "sections": [
                        {"heading": "How to Append", "content": "Home > Append Queries.\nSelect tables to combine.\nColumns matched by name.\nMissing columns filled with null."},
                        {"heading": "Use Cases", "content": "Combine monthly reports.\nStack data from multiple regions.\nUnion similar datasets."}
                    ]
                },
                "story": "'Appending stacks data vertically,' Sage teaches.",
                "task": "What is the difference between Merge and Append?",
                "starter_code": "# Difference:\n",
                "expected_output": "Merge joins sideways, Append stacks vertically",
                "hints": ["Merge is horizontal (join), Append is vertical (stack)"]
            },
            {
                "id": 1727,
                "title": "Unpivoting Data",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Reshaping Wide to Long",
                    "overview": "Unpivot transforms columns into rows.",
                    "sections": [
                        {"heading": "Why Unpivot", "content": "Wide data: Jan, Feb, Mar as columns\nLong data: Month column with values\nPivot Tables work better with long data."},
                        {"heading": "How to Unpivot", "content": "Select columns to unpivot.\nTransform > Unpivot Columns.\nCreates Attribute and Value columns.\nRename as needed."}
                    ]
                },
                "story": "'Unpivoting reshapes data for analysis,' Sage reveals.",
                "task": "What two columns does Unpivot create?",
                "starter_code": "# Two columns:\n",
                "expected_output": "Attribute and Value",
                "hints": ["Attribute and Value columns"]
            }
        ]
    },
    {
        "id": 10,
        "name": "The Artist's Canvas",
        "topic": "Conditional Formatting, Sparklines, Charts",
        "description": "Visualize data beautifully.",
        "story_intro": "The Artist's Canvas paints data with meaning!",
        "character": "Visual Artist",
        "character_quote": "Colors and shapes reveal what numbers hide!",
        "icon": "palette",
        "color": "#e8f5e9",
        "missions": [
            {
                "id": 1728,
                "title": "Conditional Formatting",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Rules-Based Colors",
                    "overview": "Format cells based on their values.",
                    "sections": [
                        {"heading": "Types", "content": "Highlight Cell Rules: greater than, less than, between\nTop/Bottom Rules: top 10, bottom 10%\nData Bars: in-cell bar charts\nColor Scales: gradient colors\nIcon Sets: symbols based on value"},
                        {"heading": "How to Apply", "content": "Select cells.\nHome > Conditional Formatting.\nChoose rule type.\nSet conditions and format."}
                    ]
                },
                "story": "'Conditional formatting makes patterns visible,' Visual Artist explains.",
                "task": "Name one type of conditional formatting that shows in-cell bar charts.",
                "starter_code": "# Type:\n",
                "expected_output": "Data Bars",
                "hints": ["Data Bars"]
            },
            {
                "id": 1729,
                "title": "Sparklines",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Mini Charts in Cells",
                    "overview": "Sparklines are tiny charts that fit in a cell.",
                    "sections": [
                        {"heading": "Types", "content": "Line: trend over time\nColumn: comparison bars\nWin/Loss: positive/negative values"},
                        {"heading": "How to Create", "content": "Insert > Sparklines.\nSelect data range.\nSelect location cell.\nCustomize with Sparkline tab."}
                    ]
                },
                "story": "'Sparklines show trends at a glance,' Artist teaches.",
                "task": "What are the three types of Sparklines?",
                "starter_code": "# Three types:\n",
                "expected_output": "Line, Column, Win/Loss",
                "hints": ["Line, Column, Win/Loss"]
            },
            {
                "id": 1730,
                "title": "Creating Charts",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Full Visualizations",
                    "overview": "Charts communicate data stories powerfully.",
                    "sections": [
                        {"heading": "Chart Types", "content": "Column/Bar: compare categories\nLine: show trends over time\nPie: show parts of whole\nScatter: show relationships"},
                        {"heading": "How to Create", "content": "Select data including headers.\nInsert > Recommended Charts.\nOr choose specific chart type.\nCustomize with Chart Tools."}
                    ]
                },
                "story": "'The right chart tells the right story,' Artist reveals.",
                "task": "Which chart type is best for showing trends over time?",
                "starter_code": "# Chart type:\n",
                "expected_output": "Line",
                "hints": ["Line chart for trends"]
            }
        ]
    },
    {
        "id": 11,
        "name": "Clockwork Automation",
        "topic": "Recording Macros, Basic VBA Intro",
        "description": "Automate repetitive tasks.",
        "story_intro": "Clockwork Automation teaches you to make Excel work for you!",
        "character": "Automation Smith",
        "character_quote": "Never do the same task twice manually!",
        "icon": "settings",
        "color": "#1b5e20",
        "missions": [
            {
                "id": 1731,
                "title": "Recording Macros",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Capturing Actions",
                    "overview": "Record your actions to replay them later.",
                    "sections": [
                        {"heading": "How to Record", "content": "View > Macros > Record Macro.\nGive it a name and shortcut.\nPerform your actions.\nStop recording when done."},
                        {"heading": "Tips", "content": "Plan your steps before recording.\nUse keyboard navigation (more reliable).\nStore in Personal Macro Workbook for all files.\nTest the macro after recording."}
                    ]
                },
                "story": "'Macros capture your actions perfectly,' Automation Smith explains.",
                "task": "Where do you store a macro to make it available in all workbooks?",
                "starter_code": "# Storage location:\n",
                "expected_output": "Personal Macro Workbook",
                "hints": ["Personal Macro Workbook"]
            },
            {
                "id": 1732,
                "title": "Basic VBA Intro",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Behind the Macros",
                    "overview": "VBA is the programming language behind macros.",
                    "sections": [
                        {"heading": "VBA Basics", "content": "VBA = Visual Basic for Applications.\nAlt+F11 opens the VBA Editor.\nMacros are stored as VBA code.\nYou can edit and enhance recorded macros."},
                        {"heading": "Simple Structure", "content": "Sub MacroName()\n    ' Your code here\n    Range('A1').Value = 'Hello'\nEnd Sub"}
                    ]
                },
                "story": "'VBA is the language of Excel automation,' Smith teaches.",
                "task": "What keyboard shortcut opens the VBA Editor?",
                "starter_code": "# Shortcut:\n",
                "expected_output": "Alt+F11",
                "hints": ["Alt+F11"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Master Ledger",
        "topic": "Building a complete Realm Finance Dashboard",
        "description": "Create a professional dashboard.",
        "story_intro": "Become Master of the Ledger by building a complete finance dashboard!",
        "character": "Grand Treasurer",
        "character_quote": "You now command the full power of spreadsheet sorcery!",
        "icon": "trophy",
        "color": "#004d40",
        "missions": [
            {
                "id": 1733,
                "title": "Dashboard Design",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Planning Your Dashboard",
                    "overview": "Great dashboards need great planning.",
                    "sections": [
                        {"heading": "Components", "content": "1. Data source (Power Query connection)\n2. Pivot Tables for calculations\n3. Charts for visualization\n4. Slicers for interactivity\n5. Summary KPIs at the top"},
                        {"heading": "Layout Tips", "content": "Keep it on one page.\nMost important info at top-left.\nUse consistent colors.\nAlign everything perfectly."}
                    ]
                },
                "story": "'A dashboard tells a story at a glance,' Grand Treasurer explains.",
                "task": "Where should the most important information appear on a dashboard?",
                "starter_code": "# Location:\n",
                "expected_output": "top-left",
                "hints": ["Top-left (people read left to right, top to bottom)"]
            },
            {
                "id": 1734,
                "title": "Excel Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Master Scribe",
                    "overview": "You've mastered the Excel Grimoire!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- Navigation and formatting\n- Essential formulas (SUM, AVERAGE, COUNT)\n- Logic (IF, AND, OR)\n- Lookups (VLOOKUP, XLOOKUP)\n- Data cleaning\n- Pivot Tables and Charts\n- Power Query\n- Automation with Macros"},
                        {"heading": "Next Steps", "content": "- Explore Power Pivot for data modeling\n- Learn DAX for advanced calculations\n- Master VBA for full automation\n- Connect to live data sources"}
                    ]
                },
                "story": "'You have become a true Spreadsheet Sorcerer!' The Grand Treasurer bows!",
                "task": "Name three lookup functions you've learned.",
                "starter_code": "# Three functions:\n",
                "expected_output": "VLOOKUP, HLOOKUP, XLOOKUP",
                "hints": ["VLOOKUP, HLOOKUP, XLOOKUP"]
            }
        ]
    }
]

POWERBI_ARCS = [
    {
        "id": 1,
        "name": "The Prism Interface",
        "topic": "Power BI/Tableau Desktop, Data sources",
        "description": "Learn the interfaces of modern BI tools.",
        "story_intro": "Welcome to the Visionary Lens! Learn to see data through crystal clarity.",
        "character": "Vision Keeper",
        "character_quote": "The dashboard reveals what eyes cannot see!",
        "icon": "monitor",
        "color": "#f2c811",
        "missions": [
            {
                "id": 1801,
                "title": "Power BI Desktop Interface",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "Your First Crystal Ball",
                    "overview": "Power BI Desktop is where you build dashboards.",
                    "sections": [
                        {"heading": "Key Areas", "content": "Report View: Design your dashboard\nData View: See and edit your data\nModel View: Define relationships\nFields Pane: All your columns and measures"},
                        {"heading": "Getting Started", "content": "Download Power BI Desktop (free)\nConnect to data sources\nBuild visualizations\nPublish to Power BI Service"}
                    ]
                },
                "story": "'Power BI Desktop is your crafting table,' Vision Keeper explains.",
                "task": "What are the three main views in Power BI Desktop?",
                "starter_code": "# Three views:\n",
                "expected_output": "Report, Data, Model",
                "hints": ["Report View, Data View, Model View"]
            },
            {
                "id": 1802,
                "title": "Tableau Desktop Interface",
                "difficulty": "easy",
                "xp": 25,
                "lesson": {
                    "title": "The Alternative Crystal",
                    "overview": "Tableau is another powerful BI tool.",
                    "sections": [
                        {"heading": "Key Areas", "content": "Data Source Page: Connect and prepare data\nWorksheet: Build individual charts\nDashboard: Combine multiple worksheets\nStory: Create presentation narratives"},
                        {"heading": "Key Concepts", "content": "Dimensions: Categorical fields (blue)\nMeasures: Numerical fields (green)\nShelves: Where you drag fields\nMarks Card: Control appearance"}
                    ]
                },
                "story": "'Tableau sees dimensions and measures differently,' Keeper teaches.",
                "task": "In Tableau, what color represents dimensions?",
                "starter_code": "# Color:\n",
                "expected_output": "blue",
                "hints": ["Dimensions are blue, Measures are green"]
            },
            {
                "id": 1803,
                "title": "Data Sources Overview",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Where Data Lives",
                    "overview": "BI tools connect to many data sources.",
                    "sections": [
                        {"heading": "Common Sources", "content": "Files: Excel, CSV, JSON\nDatabases: SQL Server, MySQL, PostgreSQL\nCloud: Azure, Salesforce, Google Analytics\nWeb: APIs, SharePoint"},
                        {"heading": "Connection Types", "content": "Import: Data copied into the tool\nDirect Query/Live: Real-time connection\nImport is faster, Live is always current"}
                    ]
                },
                "story": "'Data flows from many realms into our crystal,' Keeper reveals.",
                "task": "What connection type keeps data always current but may be slower?",
                "starter_code": "# Connection type:\n",
                "expected_output": "Direct Query",
                "hints": ["Direct Query or Live connection"]
            }
        ]
    },
    {
        "id": 2,
        "name": "Forge of Connections",
        "topic": "Connecting to SQL, Excel, and Web APIs",
        "description": "Connect to various data sources.",
        "story_intro": "The Forge of Connections teaches you to draw data from any source!",
        "character": "Data Smith",
        "character_quote": "Every source has a story to tell!",
        "icon": "link",
        "color": "#ffb300",
        "missions": [
            {
                "id": 1804,
                "title": "Connecting to SQL",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Database Connections",
                    "overview": "SQL databases are common enterprise sources.",
                    "sections": [
                        {"heading": "Steps in Power BI", "content": "Get Data > SQL Server\nEnter server name and database\nChoose Import or DirectQuery\nSelect tables or write custom query"},
                        {"heading": "Authentication", "content": "Windows: Use your Windows login\nDatabase: SQL username/password\nAzure AD: Microsoft account"}
                    ]
                },
                "story": "'SQL holds the kingdom's deepest records,' Data Smith explains.",
                "task": "What are the two main data connectivity modes for SQL in Power BI?",
                "starter_code": "# Two modes:\n",
                "expected_output": "Import and DirectQuery",
                "hints": ["Import and DirectQuery"]
            },
            {
                "id": 1805,
                "title": "Connecting to Excel",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Spreadsheet Data",
                    "overview": "Excel is the most common data source.",
                    "sections": [
                        {"heading": "Best Practices", "content": "Format data as a Table in Excel\nUse clear column headers\nNo merged cells\nNo blank rows in the middle"},
                        {"heading": "Connection", "content": "Get Data > Excel Workbook\nSelect file location\nChoose sheets or tables to import\nData automatically refreshes"}
                    ]
                },
                "story": "'Excel remains the universal language of data,' Smith teaches.",
                "task": "Why should you format Excel data as a Table before importing?",
                "starter_code": "# Reason:\n",
                "expected_output": "automatic column headers and range expansion",
                "hints": ["Tables auto-expand and have clear headers"]
            },
            {
                "id": 1806,
                "title": "Connecting to Web APIs",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Live Web Data",
                    "overview": "APIs provide real-time external data.",
                    "sections": [
                        {"heading": "Power BI", "content": "Get Data > Web\nEnter API URL\nPower Query parses JSON/XML\nMay need authentication headers"},
                        {"heading": "Common APIs", "content": "REST APIs return JSON\nCurrency exchange rates\nWeather data\nSocial media metrics"}
                    ]
                },
                "story": "'APIs bring live data from across the realms,' Smith reveals.",
                "task": "What data format do most REST APIs return?",
                "starter_code": "# Format:\n",
                "expected_output": "JSON",
                "hints": ["JSON"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Model Constellation",
        "topic": "Star Schema, Snowflake Schema, Joins",
        "description": "Build proper data models.",
        "story_intro": "The Model Constellation teaches the patterns of data relationships!",
        "character": "Schema Sage",
        "character_quote": "A good model is the foundation of great analytics!",
        "icon": "git-merge",
        "color": "#ffa000",
        "missions": [
            {
                "id": 1807,
                "title": "Star Schema",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "The Classic Pattern",
                    "overview": "Star schema is the gold standard for BI.",
                    "sections": [
                        {"heading": "Structure", "content": "Fact Table: Contains measures (sales, counts)\nDimension Tables: Contain attributes (date, product, customer)\nFacts connect to multiple dimensions\nLooks like a star when visualized"},
                        {"heading": "Benefits", "content": "Simple to understand\nFast query performance\nEasy to extend\nBest for Power BI/Tableau"}
                    ]
                },
                "story": "'The Star Schema shines brightest in analytics,' Schema Sage explains.",
                "task": "What type of table contains the measures (like sales amounts)?",
                "starter_code": "# Table type:\n",
                "expected_output": "Fact Table",
                "hints": ["Fact Table"]
            },
            {
                "id": 1808,
                "title": "Snowflake Schema",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "The Normalized Star",
                    "overview": "Snowflake normalizes dimensions further.",
                    "sections": [
                        {"heading": "Structure", "content": "Dimensions are split into sub-dimensions\nProduct -> Category -> Department\nReduces data redundancy\nMore complex joins"},
                        {"heading": "Trade-offs", "content": "Saves storage space\nSlower query performance\nMore complex to maintain\nStar schema usually preferred for BI"}
                    ]
                },
                "story": "'Snowflake spreads dimensions into branches,' Sage teaches.",
                "task": "Which schema is generally preferred for BI tools: Star or Snowflake?",
                "starter_code": "# Preferred:\n",
                "expected_output": "Star",
                "hints": ["Star schema is preferred for performance"]
            },
            {
                "id": 1809,
                "title": "Relationships and Joins",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Connecting Tables",
                    "overview": "Relationships link your tables together.",
                    "sections": [
                        {"heading": "Cardinality", "content": "One-to-Many (1:*): Most common\nOne-to-One (1:1): Rare, for splitting tables\nMany-to-Many (*:*): Requires bridge table"},
                        {"heading": "Cross-Filter Direction", "content": "Single: Filter flows one way\nBoth: Filter flows both ways\nSingle is safer, Both can cause issues"}
                    ]
                },
                "story": "'Relationships define how data flows,' Sage reveals.",
                "task": "What is the most common cardinality type in data models?",
                "starter_code": "# Cardinality:\n",
                "expected_output": "One-to-Many",
                "hints": ["One-to-Many (1:*)"]
            }
        ]
    },
    {
        "id": 4,
        "name": "The DAX Cipher",
        "topic": "Measures vs. Columns, SUM, COUNT",
        "description": "Learn DAX calculations.",
        "story_intro": "The DAX Cipher unlocks the power of dynamic calculations!",
        "character": "DAX Mage",
        "character_quote": "DAX transforms raw numbers into insights!",
        "icon": "code",
        "color": "#ff8f00",
        "missions": [
            {
                "id": 1810,
                "title": "Measures vs Calculated Columns",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Two Types of Calculations",
                    "overview": "Understand when to use each.",
                    "sections": [
                        {"heading": "Calculated Columns", "content": "Computed row by row\nStored in the model\nUse for categorization\nExample: IF([Sales]>1000, 'High', 'Low')"},
                        {"heading": "Measures", "content": "Computed at query time\nRespond to filter context\nUse for aggregations\nExample: Total Sales = SUM(Sales[Amount])"}
                    ]
                },
                "story": "'Measures and Columns serve different purposes,' DAX Mage explains.",
                "task": "Which one responds to filter context: Measures or Calculated Columns?",
                "starter_code": "# Answer:\n",
                "expected_output": "Measures",
                "hints": ["Measures respond to filters"]
            },
            {
                "id": 1811,
                "title": "SUM and SUMX",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Aggregating Values",
                    "overview": "Different ways to sum in DAX.",
                    "sections": [
                        {"heading": "SUM", "content": "SUM(Table[Column])\nSimply adds up all values\nFast and efficient\nTotal Sales = SUM(Sales[Amount])"},
                        {"heading": "SUMX", "content": "SUMX(Table, Expression)\nIterates row by row\nCan calculate before summing\nRevenue = SUMX(Sales, Sales[Qty] * Sales[Price])"}
                    ]
                },
                "story": "'SUM is simple, SUMX is powerful,' DAX Mage teaches.",
                "task": "Which DAX function would you use to sum (Quantity * Price) for each row?",
                "starter_code": "# Function:\n",
                "expected_output": "SUMX",
                "hints": ["SUMX iterates and can calculate expressions"]
            },
            {
                "id": 1812,
                "title": "COUNT Functions",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Counting in DAX",
                    "overview": "Multiple ways to count things.",
                    "sections": [
                        {"heading": "COUNT Functions", "content": "COUNT: counts numbers only\nCOUNTA: counts non-blank values\nCOUNTBLANK: counts blanks\nCOUNTROWS: counts table rows\nDISTINCTCOUNT: counts unique values"},
                        {"heading": "Examples", "content": "Order Count = COUNTROWS(Orders)\nCustomers = DISTINCTCOUNT(Sales[CustomerID])"}
                    ]
                },
                "story": "'Counting seems simple but has many forms,' Mage reveals.",
                "task": "Which COUNT function counts unique values?",
                "starter_code": "# Function:\n",
                "expected_output": "DISTINCTCOUNT",
                "hints": ["DISTINCTCOUNT"]
            }
        ]
    },
    {
        "id": 5,
        "name": "Filter of Destiny",
        "topic": "Bar charts, Pie charts, Tree maps",
        "description": "Create basic visualizations.",
        "story_intro": "The Filter of Destiny reveals patterns through visuals!",
        "character": "Chart Weaver",
        "character_quote": "Each chart type tells a different story!",
        "icon": "bar-chart",
        "color": "#ff6f00",
        "missions": [
            {
                "id": 1813,
                "title": "Bar and Column Charts",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Comparing Categories",
                    "overview": "The most common chart types.",
                    "sections": [
                        {"heading": "When to Use", "content": "Comparing categories\nShowing rankings\nTime series (column)\nHorizontal bar for long labels"},
                        {"heading": "Best Practices", "content": "Start axis at zero\nSort meaningfully\nLimit categories (top 10)\nUse consistent colors"}
                    ]
                },
                "story": "'Bar charts are the workhorses of visualization,' Chart Weaver explains.",
                "task": "Should the axis of a bar chart start at zero?",
                "starter_code": "# Answer:\n",
                "expected_output": "yes",
                "hints": ["Yes, to avoid misleading comparisons"]
            },
            {
                "id": 1814,
                "title": "Pie Charts",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Parts of a Whole",
                    "overview": "Pie charts show proportions.",
                    "sections": [
                        {"heading": "When to Use", "content": "Showing parts of 100%\nLimited categories (2-5 max)\nWhen proportions matter\nDoughnut variant for aesthetics"},
                        {"heading": "When NOT to Use", "content": "Many categories\nComparing across groups\nWhen precision matters\nTime series data"}
                    ]
                },
                "story": "'Pie charts reveal the whole picture,' Weaver teaches.",
                "task": "What is the maximum number of categories recommended for a pie chart?",
                "starter_code": "# Maximum:\n",
                "expected_output": "5",
                "hints": ["2-5 categories maximum"]
            },
            {
                "id": 1815,
                "title": "Tree Maps",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Hierarchical Proportions",
                    "overview": "Tree maps show hierarchical data.",
                    "sections": [
                        {"heading": "Structure", "content": "Rectangles sized by value\nCan show hierarchy (nested)\nColor can show another measure\nGood for many categories"},
                        {"heading": "Use Cases", "content": "Budget allocation\nDisk space usage\nSales by region and product\nPortfolio analysis"}
                    ]
                },
                "story": "'Tree maps pack information densely,' Weaver reveals.",
                "task": "What determines the size of rectangles in a tree map?",
                "starter_code": "# Determines size:\n",
                "expected_output": "value",
                "hints": ["The measure value determines rectangle size"]
            }
        ]
    },
    {
        "id": 6,
        "name": "The Map of Realms",
        "topic": "Creating Maps and Scatter plots",
        "description": "Geospatial and correlation visuals.",
        "story_intro": "The Map of Realms reveals patterns across geography and dimensions!",
        "character": "Geo Seer",
        "character_quote": "Location tells stories numbers cannot!",
        "icon": "map",
        "color": "#e65100",
        "missions": [
            {
                "id": 1816,
                "title": "Creating Maps",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Geographic Visualization",
                    "overview": "Maps show data by location.",
                    "sections": [
                        {"heading": "Map Types", "content": "Filled Map: Colors regions\nBubble Map: Sized circles on locations\nShape Map: Custom shapes\nArcGIS: Advanced mapping"},
                        {"heading": "Requirements", "content": "Location data (city, state, country)\nLatitude/Longitude for precision\nBing Maps integration (Power BI)\nMapbox (Tableau)"}
                    ]
                },
                "story": "'Maps reveal geographic patterns instantly,' Geo Seer explains.",
                "task": "What two fields can you use for precise map locations?",
                "starter_code": "# Two fields:\n",
                "expected_output": "Latitude and Longitude",
                "hints": ["Latitude and Longitude"]
            },
            {
                "id": 1817,
                "title": "Scatter Plots",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Correlation Analysis",
                    "overview": "Scatter plots show relationships.",
                    "sections": [
                        {"heading": "Structure", "content": "X-axis: One measure\nY-axis: Another measure\nEach point is a data item\nCan add size and color"},
                        {"heading": "Patterns", "content": "Positive correlation: upward trend\nNegative correlation: downward trend\nNo correlation: random scatter\nClusters: groups of similar items"}
                    ]
                },
                "story": "'Scatter plots reveal hidden relationships,' Seer teaches.",
                "task": "What pattern indicates a positive correlation in a scatter plot?",
                "starter_code": "# Pattern:\n",
                "expected_output": "upward trend",
                "hints": ["Points trending upward from left to right"]
            }
        ]
    },
    {
        "id": 7,
        "name": "Time-Traveler's Lens",
        "topic": "YTD, MTD, SamePeriodLastYear (DAX)",
        "description": "Time intelligence calculations.",
        "story_intro": "The Time-Traveler's Lens peers through time to compare periods!",
        "character": "Chrono Analyst",
        "character_quote": "Time is the dimension that reveals growth!",
        "icon": "clock",
        "color": "#d84315",
        "missions": [
            {
                "id": 1818,
                "title": "Year-To-Date (YTD)",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Cumulative Yearly Totals",
                    "overview": "YTD shows cumulative values from year start.",
                    "sections": [
                        {"heading": "DAX Formula", "content": "Sales YTD = TOTALYTD(SUM(Sales[Amount]), Dates[Date])\nOr: CALCULATE(SUM(Sales[Amount]), DATESYTD(Dates[Date]))\nRequires a proper Date table"},
                        {"heading": "Requirements", "content": "Mark as Date Table\nContinuous dates (no gaps)\nUnique date values\nRelationship to fact table"}
                    ]
                },
                "story": "'YTD accumulates from January 1st forward,' Chrono Analyst explains.",
                "task": "What DAX function calculates Year-To-Date totals?",
                "starter_code": "# Function:\n",
                "expected_output": "TOTALYTD",
                "hints": ["TOTALYTD or DATESYTD"]
            },
            {
                "id": 1819,
                "title": "Month-To-Date (MTD)",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Cumulative Monthly Totals",
                    "overview": "MTD shows cumulative values from month start.",
                    "sections": [
                        {"heading": "DAX Formula", "content": "Sales MTD = TOTALMTD(SUM(Sales[Amount]), Dates[Date])\nResets at the start of each month\nUseful for tracking monthly progress"},
                        {"heading": "QTD Also Available", "content": "Sales QTD = TOTALQTD(SUM(Sales[Amount]), Dates[Date])\nQuarter-To-Date calculations\nResets each quarter"}
                    ]
                },
                "story": "'MTD resets with each new month,' Analyst teaches.",
                "task": "What DAX function calculates Quarter-To-Date totals?",
                "starter_code": "# Function:\n",
                "expected_output": "TOTALQTD",
                "hints": ["TOTALQTD"]
            },
            {
                "id": 1820,
                "title": "Same Period Last Year",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Year-Over-Year Comparison",
                    "overview": "Compare to the same period last year.",
                    "sections": [
                        {"heading": "DAX Formula", "content": "Sales LY = CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR(Dates[Date]))\nShifts the date context back one year\nGreat for YoY comparisons"},
                        {"heading": "Growth Calculation", "content": "YoY Growth = DIVIDE([Sales] - [Sales LY], [Sales LY])\nFormat as percentage\nShows year-over-year change"}
                    ]
                },
                "story": "'Comparing to last year reveals true growth,' Analyst reveals.",
                "task": "What DAX function shifts dates back one year?",
                "starter_code": "# Function:\n",
                "expected_output": "SAMEPERIODLASTYEAR",
                "hints": ["SAMEPERIODLASTYEAR"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Interaction Ritual",
        "topic": "Tooltips, Drill-throughs, Bookmarks",
        "description": "Make dashboards interactive.",
        "story_intro": "The Interaction Ritual brings dashboards to life!",
        "character": "UX Enchanter",
        "character_quote": "Interactivity makes data exploration magical!",
        "icon": "mouse-pointer",
        "color": "#bf360c",
        "missions": [
            {
                "id": 1821,
                "title": "Custom Tooltips",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Hover Information",
                    "overview": "Tooltips show details on hover.",
                    "sections": [
                        {"heading": "Default Tooltips", "content": "Automatically show field values\nCustomize which fields appear\nFormat numbers and dates"},
                        {"heading": "Report Page Tooltips", "content": "Create a separate tooltip page\nAdd any visuals you want\nSet page as tooltip in format\nRich, visual tooltips on hover"}
                    ]
                },
                "story": "'Tooltips reveal hidden details,' UX Enchanter explains.",
                "task": "What type of tooltip lets you show a full mini-dashboard on hover?",
                "starter_code": "# Type:\n",
                "expected_output": "Report Page Tooltip",
                "hints": ["Report Page Tooltip"]
            },
            {
                "id": 1822,
                "title": "Drill-Through Pages",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Detailed Analysis",
                    "overview": "Drill-through navigates to detail pages.",
                    "sections": [
                        {"heading": "How It Works", "content": "Create a detail page\nAdd drill-through filters\nRight-click data point > Drill through\nSee full details for that item"},
                        {"heading": "Use Cases", "content": "Customer details from summary\nProduct deep-dive\nRegion analysis\nTransaction history"}
                    ]
                },
                "story": "'Drill-through reveals the story behind numbers,' Enchanter teaches.",
                "task": "How do you navigate to a drill-through page?",
                "starter_code": "# Method:\n",
                "expected_output": "right-click and select drill through",
                "hints": ["Right-click on a data point"]
            },
            {
                "id": 1823,
                "title": "Bookmarks",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Saved Views",
                    "overview": "Bookmarks save the state of your report.",
                    "sections": [
                        {"heading": "What's Saved", "content": "Current filters and slicers\nVisibility of visuals\nSort order\nSelected page"},
                        {"heading": "Use Cases", "content": "Toggle between views\nCreate guided navigation\nShow/hide detail sections\nPresentation mode states"}
                    ]
                },
                "story": "'Bookmarks capture moments in your dashboard,' Enchanter reveals.",
                "task": "What can bookmarks be used to toggle?",
                "starter_code": "# Can toggle:\n",
                "expected_output": "visibility of visuals",
                "hints": ["Show/hide visuals, filters, states"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Realm-Wide Broadcast",
        "topic": "Power BI Service, Workspaces, Sharing",
        "description": "Publish and share dashboards.",
        "story_intro": "The Realm-Wide Broadcast spreads your insights across the kingdom!",
        "character": "Herald of Data",
        "character_quote": "Sharing is how insights become actions!",
        "icon": "share-2",
        "color": "#9e9d24",
        "missions": [
            {
                "id": 1824,
                "title": "Power BI Service",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Cloud Dashboards",
                    "overview": "Power BI Service hosts your reports online.",
                    "sections": [
                        {"heading": "Key Features", "content": "Access reports from anywhere\nSchedule data refresh\nCreate dashboards (pinned tiles)\nSet up alerts on data changes"},
                        {"heading": "Publishing", "content": "Publish button in Desktop\nChoose workspace\nReport appears in Service\nSet up refresh schedule"}
                    ]
                },
                "story": "'The Service makes dashboards available everywhere,' Herald explains.",
                "task": "Where do you click to send a report from Desktop to Service?",
                "starter_code": "# Button:\n",
                "expected_output": "Publish",
                "hints": ["Publish button"]
            },
            {
                "id": 1825,
                "title": "Workspaces",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Organizing Content",
                    "overview": "Workspaces organize reports and datasets.",
                    "sections": [
                        {"heading": "Workspace Types", "content": "My Workspace: Personal content\nShared Workspaces: Team collaboration\nPremium: Advanced features\nEach has its own content"},
                        {"heading": "Roles", "content": "Admin: Full control\nMember: Edit content\nContributor: Add content\nViewer: View only"}
                    ]
                },
                "story": "'Workspaces organize the kingdom's data assets,' Herald teaches.",
                "task": "What workspace role can only view content but not edit?",
                "starter_code": "# Role:\n",
                "expected_output": "Viewer",
                "hints": ["Viewer role"]
            },
            {
                "id": 1826,
                "title": "Sharing Options",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Getting Reports to Users",
                    "overview": "Multiple ways to share content.",
                    "sections": [
                        {"heading": "Sharing Methods", "content": "Direct share: To specific users\nApps: Packaged content bundles\nEmbed: In websites or SharePoint\nPublish to web: Public URL (careful!)"},
                        {"heading": "Best Practice", "content": "Use Apps for wide distribution\nDirect share for small groups\nNever publish sensitive data to web"}
                    ]
                },
                "story": "'Choose your sharing method wisely,' Herald reveals.",
                "task": "What sharing method creates a public URL that anyone can access?",
                "starter_code": "# Method:\n",
                "expected_output": "Publish to web",
                "hints": ["Publish to web"]
            }
        ]
    },
    {
        "id": 10,
        "name": "Security Seal",
        "topic": "Row-Level Security (RLS), Gateways",
        "description": "Secure your data.",
        "story_intro": "The Security Seal protects sensitive kingdom data!",
        "character": "Guardian of Secrets",
        "character_quote": "Not all eyes should see all data!",
        "icon": "shield",
        "color": "#827717",
        "missions": [
            {
                "id": 1827,
                "title": "Row-Level Security",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Filtering by User",
                    "overview": "RLS restricts data based on who's viewing.",
                    "sections": [
                        {"heading": "How It Works", "content": "Create roles in Desktop\nDefine DAX filters (Region = 'East')\nAssign users to roles in Service\nUsers only see their allowed data"},
                        {"heading": "Dynamic RLS", "content": "Use USERPRINCIPALNAME() in DAX\nFilter based on logged-in user\nSales[SalesRep] = USERPRINCIPALNAME()\nScales to many users automatically"}
                    ]
                },
                "story": "'RLS ensures each user sees only their realm,' Guardian explains.",
                "task": "What DAX function returns the email of the current user?",
                "starter_code": "# Function:\n",
                "expected_output": "USERPRINCIPALNAME()",
                "hints": ["USERPRINCIPALNAME()"]
            },
            {
                "id": 1828,
                "title": "Data Gateways",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Connecting to On-Premises Data",
                    "overview": "Gateways bridge cloud and local data.",
                    "sections": [
                        {"heading": "Gateway Types", "content": "Personal: One user, one machine\nEnterprise: Shared, multiple sources\nInstall on machine with data access\nSecure tunnel to cloud"},
                        {"heading": "When Needed", "content": "On-premises SQL Server\nLocal file shares\nAnalysis Services\nAny non-cloud data source"}
                    ]
                },
                "story": "'Gateways bridge the realm to the cloud,' Guardian teaches.",
                "task": "What type of gateway is shared across multiple users?",
                "starter_code": "# Type:\n",
                "expected_output": "Enterprise",
                "hints": ["Enterprise gateway"]
            }
        ]
    },
    {
        "id": 11,
        "name": "The Advanced Alchemist",
        "topic": "What-if Analysis, Field Parameters",
        "description": "Advanced analytical features.",
        "story_intro": "The Advanced Alchemist teaches powerful analytical techniques!",
        "character": "Grand Alchemist",
        "character_quote": "What-if scenarios predict possible futures!",
        "icon": "sliders",
        "color": "#558b2f",
        "missions": [
            {
                "id": 1829,
                "title": "What-If Parameters",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Scenario Analysis",
                    "overview": "Let users adjust assumptions.",
                    "sections": [
                        {"heading": "Creating Parameters", "content": "Modeling > New Parameter\nSet min, max, increment\nCreates a slicer automatically\nParameter value usable in measures"},
                        {"heading": "Use Cases", "content": "Price sensitivity analysis\nGrowth rate scenarios\nDiscount impact modeling\nBudget variance analysis"}
                    ]
                },
                "story": "'What-if parameters let users explore scenarios,' Grand Alchemist explains.",
                "task": "Where do you create a What-If parameter in Power BI?",
                "starter_code": "# Location:\n",
                "expected_output": "Modeling tab",
                "hints": ["Modeling > New Parameter"]
            },
            {
                "id": 1830,
                "title": "Field Parameters",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Dynamic Field Selection",
                    "overview": "Let users choose which fields to display.",
                    "sections": [
                        {"heading": "What They Do", "content": "Users switch between measures\nOne visual, many perspectives\nSlicer controls which field shows\nGreat for flexible dashboards"},
                        {"heading": "Creating", "content": "Modeling > New Parameter > Fields\nSelect fields to include\nAdd to visual as value\nAdd slicer for selection"}
                    ]
                },
                "story": "'Field parameters give users control,' Alchemist teaches.",
                "task": "What do field parameters let users dynamically change?",
                "starter_code": "# What they change:\n",
                "expected_output": "which fields to display",
                "hints": ["The fields/measures shown in visuals"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Oracle's Dashboard",
        "topic": "Building a Kingdom Population & Resource Tracker",
        "description": "Build a complete dashboard.",
        "story_intro": "Become the Oracle by building a complete kingdom tracker!",
        "character": "Supreme Oracle",
        "character_quote": "You now command the full power of visualization!",
        "icon": "trophy",
        "color": "#33691e",
        "missions": [
            {
                "id": 1831,
                "title": "Dashboard Planning",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Designing the Oracle's View",
                    "overview": "Great dashboards need great planning.",
                    "sections": [
                        {"heading": "Key Questions", "content": "Who is the audience?\nWhat decisions will they make?\nWhat data is available?\nHow often will it refresh?"},
                        {"heading": "Layout Principles", "content": "KPIs at the top\nFilters accessible\nLogical flow (overview to detail)\nConsistent visual language"}
                    ]
                },
                "story": "'Planning prevents poor dashboards,' Supreme Oracle explains.",
                "task": "Where should KPIs appear on a dashboard?",
                "starter_code": "# Location:\n",
                "expected_output": "at the top",
                "hints": ["Top of the dashboard"]
            },
            {
                "id": 1832,
                "title": "Power BI/Tableau Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Oracle",
                    "overview": "You've mastered the Visionary Lens!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- Connecting to data sources\n- Building data models\n- DAX calculations\n- All chart types\n- Time intelligence\n- Interactivity features\n- Publishing and sharing\n- Security and governance"},
                        {"heading": "Next Steps", "content": "- Explore advanced DAX patterns\n- Learn Power Automate integration\n- Master composite models\n- Explore Paginated Reports"}
                    ]
                },
                "story": "'You have become a true Data Oracle!' The Supreme Oracle bows!",
                "task": "Name three time intelligence DAX functions you learned.",
                "starter_code": "# Three functions:\n",
                "expected_output": "TOTALYTD, TOTALMTD, SAMEPERIODLASTYEAR",
                "hints": ["TOTALYTD, TOTALMTD, TOTALQTD, SAMEPERIODLASTYEAR"]
            }
        ]
    }
]

DATAENG_ARCS = [
    {
        "id": 1,
        "name": "Architecture of Mana",
        "topic": "ETL vs. ELT, Batch vs. Streaming",
        "description": "Learn the foundational patterns of data engineering.",
        "story_intro": "Welcome to the Great Pipeline! Learn how Mana flows through the realm.",
        "character": "Pipeline Architect",
        "character_quote": "Every great system starts with solid foundations!",
        "icon": "layers",
        "color": "#00acc1",
        "missions": [
            {
                "id": 1901,
                "title": "ETL vs ELT",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Two Paradigms",
                    "overview": "ETL and ELT are two approaches to data transformation.",
                    "sections": [
                        {"heading": "ETL (Extract-Transform-Load)", "content": "Transform data BEFORE loading to warehouse\nGood for: Legacy systems, data cleaning\nTools: Informatica, Talend, SSIS\nCompute happens in staging area"},
                        {"heading": "ELT (Extract-Load-Transform)", "content": "Load raw data FIRST, transform in warehouse\nGood for: Cloud warehouses, big data\nTools: dbt, Snowflake, BigQuery\nLeverages warehouse compute power"}
                    ]
                },
                "story": "'ETL and ELT shape how data flows,' Pipeline Architect explains.",
                "task": "Which approach transforms data IN the warehouse after loading?",
                "starter_code": "# Approach:\n",
                "expected_output": "ELT",
                "hints": ["ELT transforms after loading"]
            },
            {
                "id": 1902,
                "title": "Batch Processing",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Processing in Groups",
                    "overview": "Batch processing handles data in scheduled chunks.",
                    "sections": [
                        {"heading": "What is Batch?", "content": "Process data at scheduled intervals\nDaily, hourly, weekly runs\nGood for: Reports, analytics, backups\nLatency: Minutes to hours"},
                        {"heading": "Characteristics", "content": "High throughput\nCost efficient\nEasier to implement\nExamples: Nightly ETL, monthly reports"}
                    ]
                },
                "story": "'Batch processing gathers data like waves,' Architect teaches.",
                "task": "What is a typical latency for batch processing?",
                "starter_code": "# Latency:\n",
                "expected_output": "minutes to hours",
                "hints": ["Minutes to hours"]
            },
            {
                "id": 1903,
                "title": "Streaming Processing",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Real-Time Data",
                    "overview": "Streaming processes data as it arrives.",
                    "sections": [
                        {"heading": "What is Streaming?", "content": "Process data continuously as it arrives\nReal-time or near-real-time\nGood for: Fraud detection, live dashboards\nLatency: Milliseconds to seconds"},
                        {"heading": "Characteristics", "content": "Lower latency\nMore complex architecture\nHigher infrastructure cost\nExamples: Stock prices, IoT sensors"}
                    ]
                },
                "story": "'Streaming flows like an endless river,' Architect reveals.",
                "task": "What is a typical latency for streaming processing?",
                "starter_code": "# Latency:\n",
                "expected_output": "milliseconds to seconds",
                "hints": ["Milliseconds to seconds"]
            }
        ]
    },
    {
        "id": 2,
        "name": "The Storage Vaults",
        "topic": "Data Lakes vs. Data Warehouses",
        "description": "Understand different storage paradigms.",
        "story_intro": "The Storage Vaults hold the realm's most precious Mana!",
        "character": "Vault Keeper",
        "character_quote": "Where you store data matters as much as what you store!",
        "icon": "hard-drive",
        "color": "#0097a7",
        "missions": [
            {
                "id": 1904,
                "title": "Data Warehouses",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Structured Storage",
                    "overview": "Data warehouses store processed, structured data.",
                    "sections": [
                        {"heading": "Characteristics", "content": "Schema-on-write (define before loading)\nOptimized for SQL queries\nStructured, cleaned data\nExamples: Snowflake, Redshift, BigQuery"},
                        {"heading": "Use Cases", "content": "Business intelligence\nReporting and dashboards\nHistorical analysis\nKPIs and metrics"}
                    ]
                },
                "story": "'Warehouses organize data for quick answers,' Vault Keeper explains.",
                "task": "Is a data warehouse schema-on-write or schema-on-read?",
                "starter_code": "# Type:\n",
                "expected_output": "schema-on-write",
                "hints": ["Schema-on-write"]
            },
            {
                "id": 1905,
                "title": "Data Lakes",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Raw Storage",
                    "overview": "Data lakes store raw, unprocessed data.",
                    "sections": [
                        {"heading": "Characteristics", "content": "Schema-on-read (define when reading)\nStore any format (JSON, CSV, Parquet)\nRaw, unprocessed data\nExamples: S3, Azure Data Lake, GCS"},
                        {"heading": "Use Cases", "content": "Machine learning training\nData exploration\nArchiving raw data\nAdvanced analytics"}
                    ]
                },
                "story": "'Lakes hold raw Mana in its purest form,' Keeper teaches.",
                "task": "Is a data lake schema-on-write or schema-on-read?",
                "starter_code": "# Type:\n",
                "expected_output": "schema-on-read",
                "hints": ["Schema-on-read"]
            },
            {
                "id": 1906,
                "title": "Data Lakehouse",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "The Best of Both",
                    "overview": "Lakehouses combine lake and warehouse features.",
                    "sections": [
                        {"heading": "Concept", "content": "Raw storage with warehouse features\nACID transactions on lake data\nExamples: Databricks, Delta Lake, Apache Iceberg"},
                        {"heading": "Benefits", "content": "Single source of truth\nSupports both BI and ML\nReduced data duplication\nCost effective"}
                    ]
                },
                "story": "'The Lakehouse unites both worlds,' Keeper reveals.",
                "task": "Name one popular lakehouse technology.",
                "starter_code": "# Technology:\n",
                "expected_output": "Delta Lake",
                "hints": ["Delta Lake, Databricks, Apache Iceberg"]
            }
        ]
    },
    {
        "id": 3,
        "name": "The Flow of Airflow",
        "topic": "Airflow Basics, DAGs, Tasks",
        "description": "Learn Apache Airflow fundamentals.",
        "story_intro": "The Flow of Airflow orchestrates all data movement!",
        "character": "Flow Master",
        "character_quote": "Orchestration brings order to chaos!",
        "icon": "wind",
        "color": "#00838f",
        "missions": [
            {
                "id": 1907,
                "title": "Airflow Basics",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "What is Airflow?",
                    "overview": "Apache Airflow orchestrates complex data pipelines.",
                    "sections": [
                        {"heading": "Core Concept", "content": "Workflow orchestration tool\nDefine pipelines as Python code\nSchedule and monitor jobs\nCreated by Airbnb, now Apache project"},
                        {"heading": "Components", "content": "Scheduler: Triggers workflows\nExecutor: Runs tasks\nWebserver: UI for monitoring\nMetadata DB: Stores state"}
                    ]
                },
                "story": "'Airflow conducts the symphony of data,' Flow Master explains.",
                "task": "What company originally created Apache Airflow?",
                "starter_code": "# Company:\n",
                "expected_output": "Airbnb",
                "hints": ["Airbnb"]
            },
            {
                "id": 1908,
                "title": "DAGs Explained",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Directed Acyclic Graphs",
                    "overview": "DAGs define your pipeline structure.",
                    "sections": [
                        {"heading": "What is a DAG?", "content": "Directed: Has a direction (flow)\nAcyclic: No circular dependencies\nGraph: Collection of nodes and edges\nNodes = Tasks, Edges = Dependencies"},
                        {"heading": "In Airflow", "content": "DAG = Your pipeline definition\nWritten in Python\nSpecifies task order\nExample: Extract >> Transform >> Load"}
                    ]
                },
                "story": "'DAGs map the flow of your data,' Master teaches.",
                "task": "What does the 'A' in DAG stand for?",
                "starter_code": "# A stands for:\n",
                "expected_output": "Acyclic",
                "hints": ["Acyclic - no cycles allowed"]
            },
            {
                "id": 1909,
                "title": "Tasks and Operators",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Building Blocks",
                    "overview": "Tasks are the units of work in Airflow.",
                    "sections": [
                        {"heading": "Tasks", "content": "Individual units of work\nDefined using Operators\nHave upstream/downstream dependencies\nCan pass data via XCom"},
                        {"heading": "Common Operators", "content": "PythonOperator: Run Python functions\nBashOperator: Run shell commands\nSQLOperator: Execute SQL\nSensor: Wait for conditions"}
                    ]
                },
                "story": "'Tasks are the workers of your pipeline,' Master reveals.",
                "task": "Which operator runs Python functions in Airflow?",
                "starter_code": "# Operator:\n",
                "expected_output": "PythonOperator",
                "hints": ["PythonOperator"]
            }
        ]
    },
    {
        "id": 4,
        "name": "Guardian of Schedules",
        "topic": "Scheduling, Backfilling, Operators",
        "description": "Master Airflow scheduling and advanced features.",
        "story_intro": "The Guardian of Schedules controls time in the pipeline realm!",
        "character": "Time Warden",
        "character_quote": "Timing is everything in data engineering!",
        "icon": "calendar",
        "color": "#006064",
        "missions": [
            {
                "id": 1910,
                "title": "Scheduling DAGs",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "When to Run",
                    "overview": "Schedule your DAGs to run automatically.",
                    "sections": [
                        {"heading": "Schedule Interval", "content": "Cron expressions: '0 0 * * *' (daily at midnight)\nPresets: @daily, @hourly, @weekly\nNone: Manual trigger only\nTimedelta objects also work"},
                        {"heading": "Key Concepts", "content": "execution_date: Logical date being processed\nstart_date: When DAG becomes active\ncatchup: Whether to run past dates"}
                    ]
                },
                "story": "'Schedules automate your workflows,' Time Warden explains.",
                "task": "What Airflow preset runs a DAG once per day?",
                "starter_code": "# Preset:\n",
                "expected_output": "@daily",
                "hints": ["@daily"]
            },
            {
                "id": 1911,
                "title": "Backfilling",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Processing Historical Data",
                    "overview": "Backfilling runs DAGs for past dates.",
                    "sections": [
                        {"heading": "What is Backfilling?", "content": "Run DAG for historical dates\nUseful for: Fixing data, new pipelines\nCatchup=True enables automatic backfill\nCLI: airflow dags backfill"},
                        {"heading": "Best Practices", "content": "Set catchup=False for most DAGs\nUse idempotent tasks\nBe mindful of resource usage\nTest on small date ranges first"}
                    ]
                },
                "story": "'Backfilling lets you rewrite history,' Warden teaches.",
                "task": "What parameter controls automatic backfilling in Airflow?",
                "starter_code": "# Parameter:\n",
                "expected_output": "catchup",
                "hints": ["catchup parameter"]
            },
            {
                "id": 1912,
                "title": "Advanced Operators",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Specialized Workers",
                    "overview": "Use specialized operators for different tasks.",
                    "sections": [
                        {"heading": "Transfer Operators", "content": "S3ToRedshiftOperator\nGoogleCloudStorageToBigQueryOperator\nMove data between systems"},
                        {"heading": "Sensors", "content": "Wait for external conditions\nFileSensor: Wait for file\nHttpSensor: Wait for API\nExternalTaskSensor: Wait for other DAGs"}
                    ]
                },
                "story": "'Operators specialize in different magics,' Warden reveals.",
                "task": "What type of operator waits for external conditions to be met?",
                "starter_code": "# Operator type:\n",
                "expected_output": "Sensor",
                "hints": ["Sensor operators"]
            }
        ]
    },
    {
        "id": 5,
        "name": "The Spark Forge",
        "topic": "Apache Spark, RDDs, DataFrames",
        "description": "Learn Apache Spark fundamentals.",
        "story_intro": "The Spark Forge processes massive amounts of Mana!",
        "character": "Spark Smith",
        "character_quote": "Spark transforms big data into insights at scale!",
        "icon": "zap",
        "color": "#e65100",
        "missions": [
            {
                "id": 1913,
                "title": "Apache Spark Basics",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "What is Spark?",
                    "overview": "Apache Spark is a fast big data processing engine.",
                    "sections": [
                        {"heading": "Core Concept", "content": "Distributed computing framework\n100x faster than Hadoop MapReduce\nIn-memory processing\nSupports batch and streaming"},
                        {"heading": "Components", "content": "Spark Core: Base engine\nSpark SQL: Structured data\nSpark Streaming: Real-time\nMLlib: Machine learning"}
                    ]
                },
                "story": "'Spark processes data at incredible speeds,' Spark Smith explains.",
                "task": "How much faster is Spark compared to Hadoop MapReduce?",
                "starter_code": "# Times faster:\n",
                "expected_output": "100x",
                "hints": ["100x faster"]
            },
            {
                "id": 1914,
                "title": "RDDs",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Resilient Distributed Datasets",
                    "overview": "RDDs are Spark's fundamental data structure.",
                    "sections": [
                        {"heading": "What are RDDs?", "content": "Resilient: Fault-tolerant\nDistributed: Spread across cluster\nDataset: Collection of elements\nImmutable and partitioned"},
                        {"heading": "Operations", "content": "Transformations: map, filter, flatMap (lazy)\nActions: collect, count, reduce (trigger execution)\nRDDs are the low-level API"}
                    ]
                },
                "story": "'RDDs are Spark's original building blocks,' Smith teaches.",
                "task": "Are RDD transformations executed immediately or lazily?",
                "starter_code": "# Execution:\n",
                "expected_output": "lazily",
                "hints": ["Lazily - only when an action is called"]
            },
            {
                "id": 1915,
                "title": "DataFrames",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Structured Data API",
                    "overview": "DataFrames are the preferred Spark API.",
                    "sections": [
                        {"heading": "What are DataFrames?", "content": "Distributed table with named columns\nSimilar to pandas DataFrame\nOptimized with Catalyst engine\nSchema enforcement"},
                        {"heading": "Advantages", "content": "Easier to use than RDDs\nAutomatic optimization\nInteroperable with SQL\nBetter performance in most cases"}
                    ]
                },
                "story": "'DataFrames make Spark accessible,' Smith reveals.",
                "task": "What optimization engine does Spark use for DataFrames?",
                "starter_code": "# Engine:\n",
                "expected_output": "Catalyst",
                "hints": ["Catalyst optimizer"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Distributed Magic",
        "topic": "Spark SQL, PySpark, Cluster Computing",
        "description": "Advanced Spark concepts.",
        "story_intro": "Distributed Magic harnesses the power of clusters!",
        "character": "Cluster Mage",
        "character_quote": "Distribute your work, multiply your power!",
        "icon": "server",
        "color": "#bf360c",
        "missions": [
            {
                "id": 1916,
                "title": "Spark SQL",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "SQL on Spark",
                    "overview": "Run SQL queries on distributed data.",
                    "sections": [
                        {"heading": "Using Spark SQL", "content": "df.createOrReplaceTempView('table')\nspark.sql('SELECT * FROM table')\nFull SQL support\nIntegrates with Hive"},
                        {"heading": "Benefits", "content": "Familiar SQL syntax\nOptimized execution\nJoin with DataFrames\nGreat for analysts"}
                    ]
                },
                "story": "'SQL works on any scale with Spark,' Cluster Mage explains.",
                "task": "What method creates a temporary view for SQL queries?",
                "starter_code": "# Method:\n",
                "expected_output": "createOrReplaceTempView",
                "hints": ["createOrReplaceTempView"]
            },
            {
                "id": 1917,
                "title": "PySpark",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Python + Spark",
                    "overview": "Use Python to write Spark applications.",
                    "sections": [
                        {"heading": "PySpark Basics", "content": "from pyspark.sql import SparkSession\nspark = SparkSession.builder.getOrCreate()\ndf = spark.read.csv('data.csv')\ndf.show()"},
                        {"heading": "Common Operations", "content": "select(), filter(), groupBy()\njoin(), agg(), orderBy()\nwrite.parquet(), write.csv()\nSimilar to pandas syntax"}
                    ]
                },
                "story": "'PySpark brings Python to big data,' Mage teaches.",
                "task": "What object do you create first when starting a PySpark application?",
                "starter_code": "# Object:\n",
                "expected_output": "SparkSession",
                "hints": ["SparkSession"]
            },
            {
                "id": 1918,
                "title": "Cluster Computing",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Distributed Architecture",
                    "overview": "Understand how Spark distributes work.",
                    "sections": [
                        {"heading": "Architecture", "content": "Driver: Coordinates execution\nExecutors: Run tasks on workers\nCluster Manager: Allocates resources\nModes: Standalone, YARN, Kubernetes"},
                        {"heading": "Partitioning", "content": "Data split into partitions\nEach partition processed in parallel\nrepartition() to change partitions\nKey to performance tuning"}
                    ]
                },
                "story": "'Clusters multiply computing power,' Mage reveals.",
                "task": "What component coordinates Spark job execution?",
                "starter_code": "# Component:\n",
                "expected_output": "Driver",
                "hints": ["Driver program"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Stream of Souls",
        "topic": "Apache Kafka, Producers, Consumers",
        "description": "Learn Apache Kafka basics.",
        "story_intro": "The Stream of Souls carries real-time Mana!",
        "character": "Stream Keeper",
        "character_quote": "Kafka enables real-time data flow!",
        "icon": "activity",
        "color": "#231f20",
        "missions": [
            {
                "id": 1919,
                "title": "Apache Kafka Basics",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "What is Kafka?",
                    "overview": "Apache Kafka is a distributed streaming platform.",
                    "sections": [
                        {"heading": "Core Concept", "content": "Distributed event streaming\nHigh throughput, low latency\nDurable message storage\nCreated by LinkedIn, now Apache project"},
                        {"heading": "Use Cases", "content": "Real-time analytics\nEvent sourcing\nLog aggregation\nMicroservices communication"}
                    ]
                },
                "story": "'Kafka streams events across systems,' Stream Keeper explains.",
                "task": "What company originally created Apache Kafka?",
                "starter_code": "# Company:\n",
                "expected_output": "LinkedIn",
                "hints": ["LinkedIn"]
            },
            {
                "id": 1920,
                "title": "Producers",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Sending Messages",
                    "overview": "Producers write data to Kafka topics.",
                    "sections": [
                        {"heading": "What are Producers?", "content": "Applications that send messages\nWrite to specific topics\nChoose partition (or let Kafka decide)\nCan be synchronous or async"},
                        {"heading": "Key Concepts", "content": "Key: Optional, for partitioning\nValue: The actual message\nAcks: Delivery confirmation level\nCompression: Reduce network usage"}
                    ]
                },
                "story": "'Producers feed the stream,' Keeper teaches.",
                "task": "What do Kafka producers write to?",
                "starter_code": "# Write to:\n",
                "expected_output": "topics",
                "hints": ["Topics"]
            },
            {
                "id": 1921,
                "title": "Consumers",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Reading Messages",
                    "overview": "Consumers read data from Kafka topics.",
                    "sections": [
                        {"heading": "What are Consumers?", "content": "Applications that read messages\nSubscribe to topics\nTrack position with offsets\nCan form consumer groups"},
                        {"heading": "Consumer Groups", "content": "Multiple consumers share work\nEach partition read by one consumer\nLoad balancing built-in\nFault tolerance through reassignment"}
                    ]
                },
                "story": "'Consumers drink from the stream,' Keeper reveals.",
                "task": "What tracks a consumer's position in a Kafka topic?",
                "starter_code": "# Tracks position:\n",
                "expected_output": "offset",
                "hints": ["Offset"]
            }
        ]
    },
    {
        "id": 8,
        "name": "The Topic Nexus",
        "topic": "Kafka Topics, Partitions, Real-time Flow",
        "description": "Deep dive into Kafka architecture.",
        "story_intro": "The Topic Nexus is where all streams converge!",
        "character": "Nexus Guardian",
        "character_quote": "Topics and partitions are the heart of Kafka!",
        "icon": "git-branch",
        "color": "#424242",
        "missions": [
            {
                "id": 1922,
                "title": "Kafka Topics",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Message Categories",
                    "overview": "Topics organize messages in Kafka.",
                    "sections": [
                        {"heading": "What are Topics?", "content": "Named categories of messages\nLike a table in a database\nRetain messages for configurable time\nCan have many producers/consumers"},
                        {"heading": "Topic Config", "content": "retention.ms: How long to keep data\ncleanup.policy: delete or compact\nreplication.factor: Copies for durability\npartitions: Parallelism level"}
                    ]
                },
                "story": "'Topics organize the stream,' Nexus Guardian explains.",
                "task": "What config controls how long Kafka keeps messages?",
                "starter_code": "# Config:\n",
                "expected_output": "retention.ms",
                "hints": ["retention.ms"]
            },
            {
                "id": 1923,
                "title": "Partitions",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Parallel Processing",
                    "overview": "Partitions enable parallel data processing.",
                    "sections": [
                        {"heading": "What are Partitions?", "content": "Topics split into partitions\nEach partition is ordered\nMessages have unique offset per partition\nEnable parallel processing"},
                        {"heading": "Partitioning Strategy", "content": "By key: Same key = same partition\nRound-robin: If no key\nCustom: Your own logic\nMore partitions = more parallelism"}
                    ]
                },
                "story": "'Partitions multiply throughput,' Guardian teaches.",
                "task": "Are messages within a single partition ordered?",
                "starter_code": "# Ordered:\n",
                "expected_output": "yes",
                "hints": ["Yes, ordering is guaranteed within a partition"]
            },
            {
                "id": 1924,
                "title": "Real-Time Streaming",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Stream Processing",
                    "overview": "Process data as it flows through Kafka.",
                    "sections": [
                        {"heading": "Kafka Streams", "content": "Client library for stream processing\nStateless: filter, map, branch\nStateful: aggregations, joins\nExactly-once processing support"},
                        {"heading": "ksqlDB", "content": "SQL interface for Kafka\nCREATE STREAM for real-time queries\nNo coding required\nGreat for rapid development"}
                    ]
                },
                "story": "'Real-time processing unlocks instant insights,' Guardian reveals.",
                "task": "What SQL-like tool can query Kafka streams?",
                "starter_code": "# Tool:\n",
                "expected_output": "ksqlDB",
                "hints": ["ksqlDB"]
            }
        ]
    },
    {
        "id": 9,
        "name": "Cloud Foundry",
        "topic": "Snowflake, BigQuery, AWS Glue basics",
        "description": "Cloud data engineering platforms.",
        "story_intro": "Cloud Foundry houses the modern data platforms!",
        "character": "Cloud Sage",
        "character_quote": "The cloud scales infinitely for your data needs!",
        "icon": "cloud",
        "color": "#1976d2",
        "missions": [
            {
                "id": 1925,
                "title": "Snowflake",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The Data Cloud",
                    "overview": "Snowflake is a cloud-native data warehouse.",
                    "sections": [
                        {"heading": "Key Features", "content": "Separate storage and compute\nAuto-scaling compute clusters\nNear-zero maintenance\nSupports semi-structured data"},
                        {"heading": "Unique Concepts", "content": "Virtual Warehouses: Compute clusters\nTime Travel: Query historical data\nData Sharing: Share without copying\nSnowpipe: Continuous data loading"}
                    ]
                },
                "story": "'Snowflake redefines data warehousing,' Cloud Sage explains.",
                "task": "What Snowflake feature lets you query data from the past?",
                "starter_code": "# Feature:\n",
                "expected_output": "Time Travel",
                "hints": ["Time Travel"]
            },
            {
                "id": 1926,
                "title": "BigQuery",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Google's Warehouse",
                    "overview": "BigQuery is Google's serverless data warehouse.",
                    "sections": [
                        {"heading": "Key Features", "content": "Serverless (no infrastructure)\nPay per query (scan-based pricing)\nBuilt-in ML (BigQuery ML)\nIntegrated with GCP ecosystem"},
                        {"heading": "Best Practices", "content": "Use partitioning to reduce costs\nCluster on frequently filtered columns\nLimit SELECT * queries\nUse slot reservations for predictable costs"}
                    ]
                },
                "story": "'BigQuery handles petabytes effortlessly,' Sage teaches.",
                "task": "How does BigQuery charge for queries?",
                "starter_code": "# Charging:\n",
                "expected_output": "per query based on data scanned",
                "hints": ["Pay per query/data scanned"]
            },
            {
                "id": 1927,
                "title": "AWS Glue",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Serverless ETL",
                    "overview": "AWS Glue is a managed ETL service.",
                    "sections": [
                        {"heading": "Components", "content": "Data Catalog: Metadata repository\nCrawlers: Auto-discover schemas\nETL Jobs: Spark-based transformations\nStudio: Visual job authoring"},
                        {"heading": "Use Cases", "content": "S3 to Redshift pipelines\nData lake organization\nSchema discovery\nData preparation for ML"}
                    ]
                },
                "story": "'Glue connects AWS data services,' Sage reveals.",
                "task": "What AWS Glue component automatically discovers data schemas?",
                "starter_code": "# Component:\n",
                "expected_output": "Crawlers",
                "hints": ["Crawlers"]
            }
        ]
    },
    {
        "id": 10,
        "name": "The Transform Tablet",
        "topic": "DBT (Data Build Tool), SQL Models",
        "description": "Learn dbt for transformations.",
        "story_intro": "The Transform Tablet holds the secrets of dbt!",
        "character": "Transform Master",
        "character_quote": "dbt brings software engineering to analytics!",
        "icon": "code",
        "color": "#ff6f00",
        "missions": [
            {
                "id": 1928,
                "title": "What is dbt?",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The T in ELT",
                    "overview": "dbt transforms data in your warehouse.",
                    "sections": [
                        {"heading": "Core Concept", "content": "Transform data using SQL\nVersion control your transformations\nTest data quality\nDocument data models"},
                        {"heading": "How it Works", "content": "Write SQL SELECT statements\ndbt handles CREATE/INSERT\nBuilds dependency graph\nRuns in your warehouse"}
                    ]
                },
                "story": "'dbt revolutionizes data transformation,' Transform Master explains.",
                "task": "What type of SQL statement do you write in dbt models?",
                "starter_code": "# Statement:\n",
                "expected_output": "SELECT",
                "hints": ["SELECT statements"]
            },
            {
                "id": 1929,
                "title": "dbt Models",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Building Models",
                    "overview": "Models are the core of dbt.",
                    "sections": [
                        {"heading": "Model Types", "content": "Staging: Clean raw data\nIntermediate: Business logic\nMart: Final analytics tables\nUse ref() to reference other models"},
                        {"heading": "Materialization", "content": "view: Virtual table (default)\ntable: Physical table\nincremental: Only new/changed rows\nephemeral: Not materialized (CTE)"}
                    ]
                },
                "story": "'Models build on each other,' Master teaches.",
                "task": "What dbt function references another model?",
                "starter_code": "# Function:\n",
                "expected_output": "ref()",
                "hints": ["ref()"]
            },
            {
                "id": 1930,
                "title": "dbt Tests",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Data Quality",
                    "overview": "dbt tests validate your data.",
                    "sections": [
                        {"heading": "Built-in Tests", "content": "unique: No duplicates\nnot_null: No null values\naccepted_values: Only allowed values\nrelationships: Foreign key check"},
                        {"heading": "Custom Tests", "content": "Write SQL that returns failures\nTest complex business rules\nRun with dbt test\nFail pipeline on test failure"}
                    ]
                },
                "story": "'Tests catch data problems early,' Master reveals.",
                "task": "What dbt test checks for no duplicate values?",
                "starter_code": "# Test:\n",
                "expected_output": "unique",
                "hints": ["unique"]
            }
        ]
    },
    {
        "id": 11,
        "name": "The Iron Container",
        "topic": "Docker for DE, Testing Pipelines",
        "description": "Containerization and testing.",
        "story_intro": "The Iron Container ensures reliability!",
        "character": "Container Smith",
        "character_quote": "Containers make pipelines portable and reliable!",
        "icon": "box",
        "color": "#0db7ed",
        "missions": [
            {
                "id": 1931,
                "title": "Docker for Data Engineering",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Containerized Pipelines",
                    "overview": "Docker ensures consistent environments.",
                    "sections": [
                        {"heading": "Why Docker for DE?", "content": "Consistent environments\nEasy dependency management\nPortable across cloud/local\nReproducible pipelines"},
                        {"heading": "Common Uses", "content": "Airflow in containers\nSpark applications\nCustom ETL scripts\nLocal development environments"}
                    ]
                },
                "story": "'Docker packages your pipelines perfectly,' Container Smith explains.",
                "task": "What does Docker provide for pipeline environments?",
                "starter_code": "# Provides:\n",
                "expected_output": "consistency",
                "hints": ["Consistent environments"]
            },
            {
                "id": 1932,
                "title": "Testing Data Pipelines",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Quality Assurance",
                    "overview": "Test your pipelines for reliability.",
                    "sections": [
                        {"heading": "Test Types", "content": "Unit tests: Test functions\nIntegration tests: Test connections\nData quality tests: Validate data\nEnd-to-end tests: Full pipeline"},
                        {"heading": "Tools", "content": "pytest for Python tests\nGreat Expectations for data\ndbt tests for SQL\nMock external dependencies"}
                    ]
                },
                "story": "'Testing prevents data disasters,' Smith teaches.",
                "task": "What Python framework is commonly used for testing data pipelines?",
                "starter_code": "# Framework:\n",
                "expected_output": "pytest",
                "hints": ["pytest"]
            }
        ]
    },
    {
        "id": 12,
        "name": "Architect of Infinity",
        "topic": "Building an End-to-End Real-time Sales Pipeline",
        "description": "Build a complete data pipeline.",
        "story_intro": "Become the Architect of Infinity!",
        "character": "Grand Architect",
        "character_quote": "You now command the full power of data engineering!",
        "icon": "trophy",
        "color": "#00796b",
        "missions": [
            {
                "id": 1933,
                "title": "Pipeline Architecture",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "Designing the Pipeline",
                    "overview": "Plan a complete real-time pipeline.",
                    "sections": [
                        {"heading": "Components", "content": "Source: Kafka producers (sales events)\nIngestion: Kafka topics\nProcessing: Spark Streaming\nStorage: Data lakehouse\nServing: dbt models to Snowflake"},
                        {"heading": "Orchestration", "content": "Airflow for batch portions\nKafka for real-time flow\nMonitoring and alerting\nData quality checks"}
                    ]
                },
                "story": "'Design before you build,' Grand Architect explains.",
                "task": "What tool would you use for the real-time portion of the pipeline?",
                "starter_code": "# Tool:\n",
                "expected_output": "Kafka",
                "hints": ["Kafka for streaming"]
            },
            {
                "id": 1934,
                "title": "Data Engineering Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Architect",
                    "overview": "You've mastered the Great Pipeline!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- ETL/ELT paradigms\n- Data warehouses and lakes\n- Apache Airflow orchestration\n- Apache Spark processing\n- Apache Kafka streaming\n- Cloud platforms\n- dbt transformations\n- Testing and reliability"},
                        {"heading": "Next Steps", "content": "- Explore Databricks\n- Learn Flink for streaming\n- Master Kubernetes for scaling\n- Study data mesh architecture"}
                    ]
                },
                "story": "'You have become a true Data Engineer!' The Grand Architect bows.",
                "task": "Name the three Apache projects you learned: one for orchestration, one for batch, one for streaming.",
                "starter_code": "# Three projects:\n",
                "expected_output": "Airflow, Spark, Kafka",
                "hints": ["Airflow, Spark, Kafka"]
            }
        ]
    }
]

BA_ARCS = [
    {
        "id": 1,
        "name": "The Counselor's Invitation",
        "topic": "The BA Role, SDLC (Software Life Cycle), BABOK Basics",
        "description": "Learn the foundations of business analysis.",
        "story_intro": "Welcome to the Royal Counselor's Path! Learn the art of bridging realms.",
        "character": "Chief Counselor",
        "character_quote": "A great BA bridges the gap between vision and reality!",
        "icon": "user-check",
        "color": "#7b1fa2",
        "missions": [
            {
                "id": 2001,
                "title": "The BA Role",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "What is a Business Analyst?",
                    "overview": "Business Analysts translate business needs into solutions.",
                    "sections": [
                        {"heading": "Core Responsibilities", "content": "Elicit requirements from stakeholders\nDocument and analyze requirements\nBridge business and technical teams\nEnsure solutions meet business needs"},
                        {"heading": "Key Skills", "content": "Communication and listening\nAnalytical thinking\nProblem solving\nDocumentation and organization"}
                    ]
                },
                "story": "'The BA is the bridge between worlds,' Chief Counselor explains.",
                "task": "What is the primary role of a Business Analyst?",
                "starter_code": "# Role:\n",
                "expected_output": "translate business needs into solutions",
                "hints": ["Bridge between business and tech"]
            },
            {
                "id": 2002,
                "title": "SDLC Overview",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Software Development Life Cycle",
                    "overview": "SDLC defines phases of software development.",
                    "sections": [
                        {"heading": "SDLC Phases", "content": "1. Planning - Define scope and goals\n2. Analysis - Gather requirements\n3. Design - Create solution architecture\n4. Development - Build the solution\n5. Testing - Verify quality\n6. Deployment - Release to users\n7. Maintenance - Ongoing support"},
                        {"heading": "BA in SDLC", "content": "Most active in Planning and Analysis\nSupports Design and Testing\nHelps validate during UAT\nEnsures traceability throughout"}
                    ]
                },
                "story": "'The SDLC guides all projects,' Counselor teaches.",
                "task": "In which SDLC phase does the BA gather requirements?",
                "starter_code": "# Phase:\n",
                "expected_output": "Analysis",
                "hints": ["Analysis phase"]
            },
            {
                "id": 2003,
                "title": "BABOK Basics",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Business Analysis Body of Knowledge",
                    "overview": "BABOK is the global standard for BA practices.",
                    "sections": [
                        {"heading": "What is BABOK?", "content": "Published by IIBA\nDefines BA knowledge areas\nGlobal standard for the profession\nUsed for CBAP certification"},
                        {"heading": "Six Knowledge Areas", "content": "1. Business Analysis Planning\n2. Elicitation & Collaboration\n3. Requirements Life Cycle Management\n4. Strategy Analysis\n5. Requirements Analysis & Design\n6. Solution Evaluation"}
                    ]
                },
                "story": "'BABOK is the counselor's sacred text,' Counselor reveals.",
                "task": "What organization publishes BABOK?",
                "starter_code": "# Organization:\n",
                "expected_output": "IIBA",
                "hints": ["IIBA - International Institute of Business Analysis"]
            }
        ]
    },
    {
        "id": 2,
        "name": "The Gathering of Lords",
        "topic": "Stakeholder ID, Analysis Matrix, Management Plans",
        "description": "Master stakeholder management.",
        "story_intro": "The Lords of the realm gather - learn to understand their needs!",
        "character": "Diplomat Sage",
        "character_quote": "Know your stakeholders, know your project's fate!",
        "icon": "users",
        "color": "#6a1b9a",
        "missions": [
            {
                "id": 2004,
                "title": "Stakeholder Identification",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Finding Stakeholders",
                    "overview": "Identify everyone affected by the project.",
                    "sections": [
                        {"heading": "Who are Stakeholders?", "content": "Anyone affected by the project\nIncludes: Sponsors, Users, Developers\nInternal and external parties\nDirect and indirect stakeholders"},
                        {"heading": "Identification Techniques", "content": "Review org charts\nInterview project sponsors\nBrainstorm with team\nAnalyze process documentation"}
                    ]
                },
                "story": "'Every lord has a voice,' Diplomat Sage explains.",
                "task": "What is a stakeholder?",
                "starter_code": "# Definition:\n",
                "expected_output": "anyone affected by the project",
                "hints": ["Anyone affected by or interested in the project"]
            },
            {
                "id": 2005,
                "title": "Stakeholder Analysis Matrix",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Power-Interest Grid",
                    "overview": "Categorize stakeholders by power and interest.",
                    "sections": [
                        {"heading": "The Matrix", "content": "High Power, High Interest: Manage Closely\nHigh Power, Low Interest: Keep Satisfied\nLow Power, High Interest: Keep Informed\nLow Power, Low Interest: Monitor"},
                        {"heading": "Using the Matrix", "content": "Plot each stakeholder\nDetermine engagement strategy\nPrioritize communication\nUpdate as project evolves"}
                    ]
                },
                "story": "'The matrix reveals who needs your attention,' Sage teaches.",
                "task": "How should you treat stakeholders with High Power and High Interest?",
                "starter_code": "# Strategy:\n",
                "expected_output": "Manage Closely",
                "hints": ["Manage Closely"]
            },
            {
                "id": 2006,
                "title": "Management Plans",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Stakeholder Management Plan",
                    "overview": "Document how to engage stakeholders.",
                    "sections": [
                        {"heading": "Plan Contents", "content": "Stakeholder register\nCommunication preferences\nEngagement approach\nRoles and responsibilities"},
                        {"heading": "Best Practices", "content": "Keep it updated\nAlign with project charter\nShare with team\nReview regularly"}
                    ]
                },
                "story": "'A plan ensures no lord is forgotten,' Sage reveals.",
                "task": "What document lists all stakeholders and their info?",
                "starter_code": "# Document:\n",
                "expected_output": "Stakeholder Register",
                "hints": ["Stakeholder Register"]
            }
        ]
    },
    {
        "id": 3,
        "name": "Whispers of the Realm",
        "topic": "Interviews, Workshops, Surveys, Observation",
        "description": "Master elicitation techniques.",
        "story_intro": "Listen to the whispers of the realm to understand its needs!",
        "character": "Oracle Listener",
        "character_quote": "The best requirements come from active listening!",
        "icon": "message-circle",
        "color": "#5e35b1",
        "missions": [
            {
                "id": 2007,
                "title": "Interviews",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "One-on-One Elicitation",
                    "overview": "Interviews gather detailed requirements from individuals.",
                    "sections": [
                        {"heading": "Interview Types", "content": "Structured: Predefined questions\nUnstructured: Open conversation\nSemi-structured: Mix of both\nBest for: In-depth understanding"},
                        {"heading": "Best Practices", "content": "Prepare questions in advance\nUse open-ended questions\nTake detailed notes\nFollow up on unclear points"}
                    ]
                },
                "story": "'Interviews reveal the deepest truths,' Oracle Listener explains.",
                "task": "What interview type uses predefined questions?",
                "starter_code": "# Type:\n",
                "expected_output": "Structured",
                "hints": ["Structured interviews"]
            },
            {
                "id": 2008,
                "title": "Workshops",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Group Sessions",
                    "overview": "Workshops gather requirements from multiple stakeholders.",
                    "sections": [
                        {"heading": "Workshop Benefits", "content": "Gather diverse perspectives\nBuild consensus quickly\nIdentify conflicts early\nFoster collaboration"},
                        {"heading": "Facilitation Tips", "content": "Set clear objectives\nCreate safe environment\nManage dominant voices\nDocument decisions immediately"}
                    ]
                },
                "story": "'Workshops unite many voices,' Listener teaches.",
                "task": "What is a key benefit of workshops over interviews?",
                "starter_code": "# Benefit:\n",
                "expected_output": "gather diverse perspectives",
                "hints": ["Multiple perspectives at once"]
            },
            {
                "id": 2009,
                "title": "Surveys",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Collecting Broad Input",
                    "overview": "Surveys gather data from many stakeholders.",
                    "sections": [
                        {"heading": "When to Use", "content": "Large stakeholder groups\nGeographically dispersed users\nQuantitative data needed\nTime or access constraints"},
                        {"heading": "Survey Design", "content": "Keep it short and focused\nMix closed and open questions\nUse clear language\nPilot test before distribution"}
                    ]
                },
                "story": "'Surveys reach across the realm,' Listener reveals.",
                "task": "When are surveys most useful?",
                "starter_code": "# Best for:\n",
                "expected_output": "large stakeholder groups",
                "hints": ["Large groups, geographically dispersed"]
            },
            {
                "id": 2010,
                "title": "Observation",
                "difficulty": "medium",
                "xp": 35,
                "lesson": {
                    "title": "Watching Work Happen",
                    "overview": "Observation reveals unstated requirements.",
                    "sections": [
                        {"heading": "Types", "content": "Active: Ask questions while observing\nPassive: Watch without interrupting\nJob shadowing: Follow users for a day\nContextual inquiry: Interview during work"},
                        {"heading": "Benefits", "content": "Reveals workarounds and pain points\nUncovers tacit knowledge\nValidates stated requirements\nBuilds empathy with users"}
                    ]
                },
                "story": "'Observation reveals what words cannot,' Listener explains.",
                "task": "What does observation help uncover that interviews might miss?",
                "starter_code": "# Uncovers:\n",
                "expected_output": "tacit knowledge",
                "hints": ["Tacit/unstated knowledge, workarounds"]
            }
        ]
    },
    {
        "id": 4,
        "name": "The Blueprint Scribes",
        "topic": "BRD (Business Requirements), FRD (Functional), SRS",
        "description": "Master requirements documentation.",
        "story_intro": "The Scribes preserve requirements for all to understand!",
        "character": "Master Scribe",
        "character_quote": "Good documentation is the foundation of success!",
        "icon": "file-text",
        "color": "#512da8",
        "missions": [
            {
                "id": 2011,
                "title": "Business Requirements Document",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "The BRD",
                    "overview": "BRD captures high-level business needs.",
                    "sections": [
                        {"heading": "BRD Contents", "content": "Executive summary\nBusiness objectives\nScope and boundaries\nStakeholder list\nHigh-level requirements"},
                        {"heading": "Purpose", "content": "Defines WHAT the business needs\nNot HOW it will be built\nApproved by business stakeholders\nGuides project direction"}
                    ]
                },
                "story": "'The BRD captures the kingdom's vision,' Master Scribe explains.",
                "task": "Does the BRD focus on WHAT or HOW?",
                "starter_code": "# Focus:\n",
                "expected_output": "WHAT",
                "hints": ["WHAT the business needs"]
            },
            {
                "id": 2012,
                "title": "Functional Requirements Document",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "The FRD",
                    "overview": "FRD details system functionality.",
                    "sections": [
                        {"heading": "FRD Contents", "content": "Functional requirements\nUse cases or user stories\nBusiness rules\nData requirements\nInterface requirements"},
                        {"heading": "Characteristics", "content": "More detailed than BRD\nDefines system behavior\nUsed by development team\nTestable requirements"}
                    ]
                },
                "story": "'The FRD details system capabilities,' Scribe teaches.",
                "task": "Who primarily uses the FRD?",
                "starter_code": "# Used by:\n",
                "expected_output": "development team",
                "hints": ["Development/technical team"]
            },
            {
                "id": 2013,
                "title": "Software Requirements Specification",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "The SRS",
                    "overview": "SRS is the complete technical specification.",
                    "sections": [
                        {"heading": "SRS Contents", "content": "Functional requirements\nNon-functional requirements (performance, security)\nSystem interfaces\nConstraints and assumptions\nDependencies"},
                        {"heading": "IEEE 830 Standard", "content": "Industry standard for SRS\nDefines structure and content\nEnsures completeness\nWidely used in contracts"}
                    ]
                },
                "story": "'The SRS is the complete blueprint,' Scribe reveals.",
                "task": "What standard defines SRS structure?",
                "starter_code": "# Standard:\n",
                "expected_output": "IEEE 830",
                "hints": ["IEEE 830"]
            }
        ]
    },
    {
        "id": 5,
        "name": "The Kingdom's Logic",
        "topic": "BPMN 2.0, Flowcharts, Use Case Diagrams",
        "description": "Learn process modeling techniques.",
        "story_intro": "Map the logic that governs the kingdom's processes!",
        "character": "Process Cartographer",
        "character_quote": "A picture is worth a thousand requirements!",
        "icon": "git-merge",
        "color": "#4527a0",
        "missions": [
            {
                "id": 2014,
                "title": "BPMN 2.0",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Business Process Model and Notation",
                    "overview": "BPMN is the standard for process modeling.",
                    "sections": [
                        {"heading": "Core Elements", "content": "Events: Start, End, Intermediate (circles)\nActivities: Tasks and sub-processes (rounded rectangles)\nGateways: Decision points (diamonds)\nFlows: Sequence and message flows (arrows)"},
                        {"heading": "Benefits", "content": "Industry standard notation\nUnderstood by business and IT\nExecutable in BPM tools\nDetailed process documentation"}
                    ]
                },
                "story": "'BPMN maps the kingdom's workflows,' Process Cartographer explains.",
                "task": "What shape represents decision points in BPMN?",
                "starter_code": "# Shape:\n",
                "expected_output": "diamond",
                "hints": ["Diamond (gateways)"]
            },
            {
                "id": 2015,
                "title": "Flowcharts",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Simple Process Diagrams",
                    "overview": "Flowcharts visualize step-by-step processes.",
                    "sections": [
                        {"heading": "Basic Shapes", "content": "Oval: Start/End\nRectangle: Process step\nDiamond: Decision\nArrows: Flow direction"},
                        {"heading": "When to Use", "content": "Simple processes\nQuick documentation\nNon-technical audiences\nTraining materials"}
                    ]
                },
                "story": "'Flowcharts make logic visible,' Cartographer teaches.",
                "task": "What shape represents a decision in flowcharts?",
                "starter_code": "# Shape:\n",
                "expected_output": "diamond",
                "hints": ["Diamond"]
            },
            {
                "id": 2016,
                "title": "Use Case Diagrams",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "UML Use Cases",
                    "overview": "Use cases show system interactions.",
                    "sections": [
                        {"heading": "Components", "content": "Actor: User or external system (stick figure)\nUse Case: System function (oval)\nSystem Boundary: Scope of system (rectangle)\nRelationships: Include, Extend, Generalization"},
                        {"heading": "Purpose", "content": "Define system scope\nIdentify actors and functions\nBasis for requirements\nCommunicate with stakeholders"}
                    ]
                },
                "story": "'Use cases define what the system does,' Cartographer reveals.",
                "task": "What symbol represents an actor in use case diagrams?",
                "starter_code": "# Symbol:\n",
                "expected_output": "stick figure",
                "hints": ["Stick figure"]
            }
        ]
    },
    {
        "id": 6,
        "name": "Sorting the Scroll",
        "topic": "Requirements Prioritization (MoSCoW), Gap Analysis",
        "description": "Learn to analyze and prioritize requirements.",
        "story_intro": "Sort the scrolls to find what matters most!",
        "character": "Priority Master",
        "character_quote": "Not all requirements are created equal!",
        "icon": "filter",
        "color": "#311b92",
        "missions": [
            {
                "id": 2017,
                "title": "MoSCoW Prioritization",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Prioritization Framework",
                    "overview": "MoSCoW categorizes requirements by importance.",
                    "sections": [
                        {"heading": "Categories", "content": "Must Have: Critical for success\nShould Have: Important but not critical\nCould Have: Nice to have\nWon't Have: Out of scope for now"},
                        {"heading": "Using MoSCoW", "content": "Collaborate with stakeholders\nBe realistic about Must Haves\nDocument rationale\nReview as scope changes"}
                    ]
                },
                "story": "'MoSCoW separates the essential from the optional,' Priority Master explains.",
                "task": "What does the 'M' in MoSCoW stand for?",
                "starter_code": "# M stands for:\n",
                "expected_output": "Must Have",
                "hints": ["Must Have"]
            },
            {
                "id": 2018,
                "title": "Gap Analysis",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Current vs Future State",
                    "overview": "Gap analysis identifies what needs to change.",
                    "sections": [
                        {"heading": "The Process", "content": "1. Document current state (As-Is)\n2. Define future state (To-Be)\n3. Identify gaps between them\n4. Create action plan to bridge gaps"},
                        {"heading": "Deliverables", "content": "As-Is process maps\nTo-Be process maps\nGap analysis matrix\nRecommendations for closing gaps"}
                    ]
                },
                "story": "'Gap analysis reveals the journey ahead,' Master teaches.",
                "task": "What is the current state called in gap analysis?",
                "starter_code": "# Current state:\n",
                "expected_output": "As-Is",
                "hints": ["As-Is"]
            },
            {
                "id": 2019,
                "title": "Other Prioritization Methods",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Beyond MoSCoW",
                    "overview": "Alternative prioritization techniques.",
                    "sections": [
                        {"heading": "Techniques", "content": "Kano Model: Delight vs Basic needs\n100-Dollar Method: Allocate points\nValue vs Complexity: 2x2 matrix\nWeighted Scoring: Numeric criteria"},
                        {"heading": "Choosing a Method", "content": "Consider stakeholder preferences\nMatch to project context\nCombine methods if needed\nDocument the approach used"}
                    ]
                },
                "story": "'Many paths lead to good priorities,' Master reveals.",
                "task": "Which method gives stakeholders points to allocate?",
                "starter_code": "# Method:\n",
                "expected_output": "100-Dollar Method",
                "hints": ["100-Dollar Method"]
            }
        ]
    },
    {
        "id": 7,
        "name": "The Royal Decree",
        "topic": "User Stories, Acceptance Criteria, Backlog Grooming",
        "description": "Master Agile BA practices.",
        "story_intro": "The Royal Decree brings Agile to the kingdom!",
        "character": "Agile Champion",
        "character_quote": "In Agile, requirements evolve with understanding!",
        "icon": "repeat",
        "color": "#1a237e",
        "missions": [
            {
                "id": 2020,
                "title": "User Stories",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Agile Requirements",
                    "overview": "User stories capture requirements from user perspective.",
                    "sections": [
                        {"heading": "Format", "content": "As a [role]\nI want [feature]\nSo that [benefit]\nKeep them small and focused\nINVEST criteria: Independent, Negotiable, Valuable, Estimable, Small, Testable"},
                        {"heading": "Examples", "content": "As a customer\nI want to view my order history\nSo that I can track past purchases"}
                    ]
                },
                "story": "'User stories speak the user's language,' Agile Champion explains.",
                "task": "What are the three parts of a user story format?",
                "starter_code": "# Parts:\n",
                "expected_output": "role, feature, benefit",
                "hints": ["As a [role], I want [feature], So that [benefit]"]
            },
            {
                "id": 2021,
                "title": "Acceptance Criteria",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Definition of Done",
                    "overview": "Acceptance criteria define when a story is complete.",
                    "sections": [
                        {"heading": "Gherkin Format", "content": "Given [context]\nWhen [action]\nThen [expected result]\nUsed in BDD testing\nClear and testable"},
                        {"heading": "Best Practices", "content": "Write before development starts\nCollaborate with team and stakeholders\nKeep specific and measurable\nInclude edge cases"}
                    ]
                },
                "story": "'Acceptance criteria prove success,' Champion teaches.",
                "task": "What is the 'Given-When-Then' format called?",
                "starter_code": "# Format:\n",
                "expected_output": "Gherkin",
                "hints": ["Gherkin format"]
            },
            {
                "id": 2022,
                "title": "Backlog Grooming",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Refinement Sessions",
                    "overview": "Keep the backlog healthy and ready.",
                    "sections": [
                        {"heading": "Activities", "content": "Clarify requirements\nEstimate stories (story points)\nSplit large stories\nPrioritize items\nRemove obsolete items"},
                        {"heading": "BA Role", "content": "Prepare stories before grooming\nAnswer team questions\nFacilitate discussions\nUpdate stories with decisions"}
                    ]
                },
                "story": "'Grooming keeps the backlog battle-ready,' Champion reveals.",
                "task": "What is another name for backlog grooming?",
                "starter_code": "# Also called:\n",
                "expected_output": "Refinement",
                "hints": ["Backlog Refinement"]
            }
        ]
    },
    {
        "id": 8,
        "name": "Market Mystic's Vision",
        "topic": "SWOT Analysis, Business Case, ROI Calculation",
        "description": "Learn strategic analysis techniques.",
        "story_intro": "The Market Mystic reveals the kingdom's strategic future!",
        "character": "Strategy Oracle",
        "character_quote": "Strategy turns vision into reality!",
        "icon": "target",
        "color": "#0d47a1",
        "missions": [
            {
                "id": 2023,
                "title": "SWOT Analysis",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Strategic Assessment",
                    "overview": "SWOT evaluates internal and external factors.",
                    "sections": [
                        {"heading": "The Framework", "content": "Strengths: Internal positives\nWeaknesses: Internal negatives\nOpportunities: External positives\nThreats: External negatives"},
                        {"heading": "Using SWOT", "content": "Brainstorm each quadrant\nBe honest and specific\nPrioritize key factors\nDevelop action strategies"}
                    ]
                },
                "story": "'SWOT reveals the kingdom's position,' Strategy Oracle explains.",
                "task": "Are Opportunities internal or external factors?",
                "starter_code": "# Type:\n",
                "expected_output": "external",
                "hints": ["External factors"]
            },
            {
                "id": 2024,
                "title": "Business Case",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Justifying the Investment",
                    "overview": "Business cases justify project investment.",
                    "sections": [
                        {"heading": "Key Components", "content": "Problem statement\nProposed solution\nBenefits (quantified)\nCosts and resources\nRisks and mitigation\nTimeline and milestones"},
                        {"heading": "Purpose", "content": "Secure funding and approval\nAlign stakeholders\nProvide decision framework\nBaseline for success measurement"}
                    ]
                },
                "story": "'A business case wins the king's approval,' Oracle teaches.",
                "task": "What document justifies project investment?",
                "starter_code": "# Document:\n",
                "expected_output": "Business Case",
                "hints": ["Business Case"]
            },
            {
                "id": 2025,
                "title": "ROI Calculation",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Return on Investment",
                    "overview": "ROI measures project value.",
                    "sections": [
                        {"heading": "The Formula", "content": "ROI = (Gain - Cost) / Cost x 100%\nGain: Total benefits\nCost: Total investment\nResult: Percentage return"},
                        {"heading": "Example", "content": "Gain: $150,000\nCost: $100,000\nROI = (150,000 - 100,000) / 100,000 x 100%\nROI = 50%"}
                    ]
                },
                "story": "'ROI proves the value of your vision,' Oracle reveals.",
                "task": "If gain is $200,000 and cost is $100,000, what is the ROI?",
                "starter_code": "# ROI:\n",
                "expected_output": "100%",
                "hints": ["(200,000 - 100,000) / 100,000 x 100% = 100%"]
            }
        ]
    },
    {
        "id": 9,
        "name": "The Mirror of Reality",
        "topic": "Prototyping basics, Figma/Balsamiq for BA",
        "description": "Learn wireframing and prototyping.",
        "story_intro": "The Mirror of Reality shows the future before it's built!",
        "character": "Vision Weaver",
        "character_quote": "A prototype is worth a thousand meetings!",
        "icon": "layout",
        "color": "#1565c0",
        "missions": [
            {
                "id": 2026,
                "title": "Prototyping Basics",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Visualizing Solutions",
                    "overview": "Prototypes make requirements tangible.",
                    "sections": [
                        {"heading": "Prototype Fidelity", "content": "Low-fidelity: Sketches, paper mockups\nMedium-fidelity: Wireframes\nHigh-fidelity: Interactive mockups\nChoose based on audience and purpose"},
                        {"heading": "Benefits", "content": "Gather early feedback\nReduce misunderstandings\nValidate requirements\nEngage stakeholders visually"}
                    ]
                },
                "story": "'Prototypes bridge imagination and reality,' Vision Weaver explains.",
                "task": "What is a paper sketch prototype called?",
                "starter_code": "# Fidelity:\n",
                "expected_output": "low-fidelity",
                "hints": ["Low-fidelity prototype"]
            },
            {
                "id": 2027,
                "title": "Figma for BAs",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Modern Design Tool",
                    "overview": "Figma creates professional wireframes and prototypes.",
                    "sections": [
                        {"heading": "Key Features", "content": "Browser-based (no install)\nReal-time collaboration\nComponent libraries\nInteractive prototyping"},
                        {"heading": "BA Use Cases", "content": "Create wireframes\nDocument UI requirements\nGather stakeholder feedback\nHandoff to design/dev teams"}
                    ]
                },
                "story": "'Figma brings visions to life,' Weaver teaches.",
                "task": "What is a key benefit of Figma being browser-based?",
                "starter_code": "# Benefit:\n",
                "expected_output": "no install needed",
                "hints": ["No installation required, accessible anywhere"]
            },
            {
                "id": 2028,
                "title": "Balsamiq for BAs",
                "difficulty": "easy",
                "xp": 30,
                "lesson": {
                    "title": "Quick Wireframing",
                    "overview": "Balsamiq creates sketch-style wireframes.",
                    "sections": [
                        {"heading": "Key Features", "content": "Sketch-style look (intentionally rough)\nDrag-and-drop components\nFast wireframe creation\nLow-fidelity focus"},
                        {"heading": "Why Sketch Style?", "content": "Focuses on functionality, not design\nPrevents design debates\nEncourages feedback\nClear it's a work in progress"}
                    ]
                },
                "story": "'Balsamiq keeps focus on function,' Weaver reveals.",
                "task": "Why does Balsamiq use a sketch style?",
                "starter_code": "# Reason:\n",
                "expected_output": "focuses on functionality not design",
                "hints": ["Prevents design debates, focuses on function"]
            }
        ]
    },
    {
        "id": 10,
        "name": "The User's Blessing",
        "topic": "User Acceptance Testing, Traceability Matrix (RTM)",
        "description": "Master UAT and traceability.",
        "story_intro": "The User's Blessing validates the solution!",
        "character": "Testing Arbiter",
        "character_quote": "UAT is the final seal of approval!",
        "icon": "check-circle",
        "color": "#1976d2",
        "missions": [
            {
                "id": 2029,
                "title": "User Acceptance Testing",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Final Validation",
                    "overview": "UAT confirms the solution meets business needs.",
                    "sections": [
                        {"heading": "UAT Process", "content": "1. Define UAT scope and criteria\n2. Create test cases from requirements\n3. Prepare test data and environment\n4. Execute tests with business users\n5. Log defects and retest\n6. Obtain sign-off"},
                        {"heading": "BA Role in UAT", "content": "Write test cases\nSupport test execution\nTrack defects\nFacilitate sign-off"}
                    ]
                },
                "story": "'UAT ensures the solution serves the realm,' Testing Arbiter explains.",
                "task": "Who executes UAT tests?",
                "starter_code": "# Executed by:\n",
                "expected_output": "business users",
                "hints": ["Business users/stakeholders"]
            },
            {
                "id": 2030,
                "title": "Requirements Traceability Matrix",
                "difficulty": "hard",
                "xp": 50,
                "lesson": {
                    "title": "Connecting Requirements to Tests",
                    "overview": "RTM ensures complete test coverage.",
                    "sections": [
                        {"heading": "RTM Contents", "content": "Requirement ID\nRequirement description\nLinked test cases\nTest status\nDefect links"},
                        {"heading": "Benefits", "content": "Ensures all requirements are tested\nIdentifies gaps in coverage\nTracks requirement changes\nProvides audit trail"}
                    ]
                },
                "story": "'The RTM connects requirements to proof,' Arbiter teaches.",
                "task": "What does RTM stand for?",
                "starter_code": "# RTM:\n",
                "expected_output": "Requirements Traceability Matrix",
                "hints": ["Requirements Traceability Matrix"]
            }
        ]
    },
    {
        "id": 11,
        "name": "The Quest Board",
        "topic": "Mastering Jira and Confluence for tracking",
        "description": "Learn essential BA tools.",
        "story_intro": "The Quest Board tracks all the kingdom's initiatives!",
        "character": "Tool Smith",
        "character_quote": "The right tools amplify your capabilities!",
        "icon": "clipboard",
        "color": "#1e88e5",
        "missions": [
            {
                "id": 2031,
                "title": "Jira for BAs",
                "difficulty": "medium",
                "xp": 45,
                "lesson": {
                    "title": "Issue Tracking",
                    "overview": "Jira tracks work items and project progress.",
                    "sections": [
                        {"heading": "Key Concepts", "content": "Projects: Container for work\nIssue Types: Story, Bug, Task, Epic\nWorkflows: Define issue lifecycle\nBoards: Visualize work (Kanban, Scrum)"},
                        {"heading": "BA Activities in Jira", "content": "Create and manage user stories\nLink requirements to tasks\nTrack defects from UAT\nReport on project progress"}
                    ]
                },
                "story": "'Jira tracks every quest,' Tool Smith explains.",
                "task": "What is a collection of related user stories called in Jira?",
                "starter_code": "# Container:\n",
                "expected_output": "Epic",
                "hints": ["Epic"]
            },
            {
                "id": 2032,
                "title": "Confluence for BAs",
                "difficulty": "medium",
                "xp": 40,
                "lesson": {
                    "title": "Collaborative Documentation",
                    "overview": "Confluence is a wiki for team documentation.",
                    "sections": [
                        {"heading": "Key Features", "content": "Spaces: Organize content by project\nPages: Individual documents\nTemplates: Pre-built structures\nIntegration: Links to Jira issues"},
                        {"heading": "BA Use Cases", "content": "Store BRD and FRD documents\nCreate meeting notes\nShare process diagrams\nMaintain project wiki"}
                    ]
                },
                "story": "'Confluence preserves the kingdom's knowledge,' Smith teaches.",
                "task": "What Atlassian tool integrates with Confluence for issue tracking?",
                "starter_code": "# Tool:\n",
                "expected_output": "Jira",
                "hints": ["Jira"]
            }
        ]
    },
    {
        "id": 12,
        "name": "The Grand Strategy Trial",
        "topic": "Final Project: Full Business Solution for a Logic Crisis",
        "description": "Apply all BA skills in a final project.",
        "story_intro": "The Grand Strategy Trial tests all your skills!",
        "character": "Grand Counselor",
        "character_quote": "You are ready to advise the kingdom!",
        "icon": "trophy",
        "color": "#2196f3",
        "missions": [
            {
                "id": 2033,
                "title": "The Logic Crisis",
                "difficulty": "hard",
                "xp": 55,
                "lesson": {
                    "title": "The Final Challenge",
                    "overview": "Solve a complete business problem.",
                    "sections": [
                        {"heading": "The Scenario", "content": "The kingdom's order processing is broken\nCustomers complain of delays\nInventory is inaccurate\nMultiple systems don't communicate"},
                        {"heading": "Your Task", "content": "Identify stakeholders\nElicit requirements\nDocument the solution\nCreate a business case"}
                    ]
                },
                "story": "'A Logic Crisis threatens the realm!' Grand Counselor announces.",
                "task": "What is the first step when facing a new business problem?",
                "starter_code": "# First step:\n",
                "expected_output": "identify stakeholders",
                "hints": ["Identify stakeholders first"]
            },
            {
                "id": 2034,
                "title": "Business Analysis Mastery",
                "difficulty": "hard",
                "xp": 75,
                "lesson": {
                    "title": "You Are the Royal Counselor",
                    "overview": "You have mastered the BA path!",
                    "sections": [
                        {"heading": "Skills Mastered", "content": "- BA role and SDLC\n- Stakeholder management\n- Elicitation techniques\n- Requirements documentation\n- Process modeling\n- Prioritization and analysis\n- Agile practices\n- Strategic analysis\n- Prototyping\n- UAT and traceability\n- BA tools"},
                        {"heading": "Next Steps", "content": "- Pursue CBAP certification\n- Explore specialized domains\n- Learn data analytics\n- Develop leadership skills"}
                    ]
                },
                "story": "'You have become a true Royal Counselor!' The Grand Counselor bows.",
                "task": "What certification validates BA expertise?",
                "starter_code": "# Certification:\n",
                "expected_output": "CBAP",
                "hints": ["CBAP - Certified Business Analysis Professional"]
            }
        ]
    }
]

ARCS_BY_LANGUAGE = {
    "python": PYTHON_ARCS,
    "javascript": JAVASCRIPT_ARCS,
    "html_css": HTML_CSS_ARCS,
    "c": C_ARCS,
    "cpp": CPP_ARCS,
    "java": JAVA_ARCS,
    "sql": SQL_ARCS,
    "dsa": DSA_ARCS,
    "react": REACT_ARCS,
    "mongodb": MONGODB_ARCS,
    "php": PHP_ARCS,
    "devops": DEVOPS_ARCS,
    "ml": ML_ARCS,
    "dl": DL_ARCS,
    "cv": CV_ARCS,
    "nlp": NLP_ARCS,
    "ai": AI_ARCS,
    "excel": EXCEL_ARCS,
    "powerbi": POWERBI_ARCS,
    "dataeng": DATAENG_ARCS,
    "ba": BA_ARCS
}

XP_REWARDS = {
    "easy": 20,
    "medium": 40,
    "hard": 80,
    "boss": 150
}

def get_languages():
    """Get all available languages."""
    return LANGUAGES

def get_arcs_for_language(language="python"):
    """Get all arcs for a specific language."""
    return ARCS_BY_LANGUAGE.get(language, PYTHON_ARCS)

def get_arc_by_id(arc_id, language="python"):
    """Get an arc by its ID for a specific language."""
    arcs = get_arcs_for_language(language)
    for arc in arcs:
        if arc["id"] == arc_id:
            return arc
    return None

def get_mission_by_id(arc_id, mission_id, language="python"):
    """Get a specific mission from an arc."""
    arc = get_arc_by_id(arc_id, language)
    if arc:
        for mission in arc["missions"]:
            if mission["id"] == mission_id:
                return mission
    return None

def get_all_arcs(language="python"):
    """Get all arcs for a language (backward compatible)."""
    return get_arcs_for_language(language)

def calculate_level(xp):
    """Calculate level from XP. Level formula: XP needed = level * 100"""
    level = 1
    xp_needed = 100
    total_xp = 0
    while total_xp + xp_needed <= xp:
        total_xp += xp_needed
        level += 1
        xp_needed = level * 100
    return level, xp - total_xp, xp_needed
