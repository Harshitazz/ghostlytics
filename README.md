# 🎮 ModeSwitch - AI Productivity Assistant

ModeSwitch is a command-line productivity assistant that uses your **mode**, **mood**, and **time of day** to suggest personalized actions to boost your focus and energy.

## 🚀 Features

- Suggests personalized productivity actions based on:
  - Your current **mode** (e.g., work, study, gaming)
  - Your **mood** (happy, stressed, tired, energetic)
  - The **time of day** (auto-detected or user-provided)
- CLI interaction with auto-prompting if arguments aren't passed
- Lets you select the top suggestion interactively
- Maintains a history of recent sessions and suggestions

## 📦 Requirements

- Python 3.7+
- Dependencies (installed via requirements.txt):
  - langchain-groq
  - langchain
  - questionary
  - python-dotenv
  - colorama

## 🚀 Quick Start

```bash
# 📦 1. CLONE THE REPO
git clone https://github.com/your-username/modeswitch.git
cd modeswitch

# 🐍 2. CREATE & ACTIVATE VIRTUAL ENV
python3 -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

# 📥 3. INSTALL DEPENDENCIES
pip install -r requirements.txt

# ⚙️ 4. Create a `.env` file in the root directory
touch .env
# Add your API key: GROQ_API_KEY=your-secret-key

# 🚀 5. RUN THE APP
python modeswitch.py
# You'll be prompted to:
# - Select your mode: [gaming, work, study]
# - Choose your mood: [happy, stressed, tired, energetic]
# - Time is auto-detected unless passed with --time

# ⚙️ OPTIONAL: RUN WITH ARGUMENTS
python modeswitch.py --mode work --mood tired --time evening

# 📜 SHOW SESSION HISTORY
python modeswitch.py --history

# 🔚 DEACTIVATE VIRTUAL ENV WHEN DONE
deactivate
```

## 🛠️ Project Structure

```
modeswitch/
├── __init__.py
├── main.py              # Main CLI entry point
├── config.py            # Configuration and settings
├── models/
│   ├── __init__.py
│   ├── user_session.py  # User session data models
│   └── suggestions.py   # Suggestion models
├── services/
│   ├── __init__.py
│   ├── llm_service.py   # LLM integration
│   ├── suggestion_service.py  # Suggestion generation logic
│   └── history_service.py     # Session history management
├── utils/
│   ├── __init__.py
│   └── cli_utils.py     # CLI formatting utilities
└── data/
    └── session_history.json  # Persistent storage for session history
```

## 📋 Command Line Arguments

ModeSwitch supports the following command line arguments:

```
--mode [gaming|work|study]    Set your current activity mode
--mood [happy|stressed|tired|energetic]  Set your current mood state
--time [morning|afternoon|evening|night] Override the auto-detected time
--history                     Display your recent suggestion history
--help                        Show this help message
```

## 📈 Session History

ModeSwitch automatically saves your session data, including the suggestions you received and which one you selected. View your history with:

```bash
python modeswitch.py --history
```

## 🔄 API Usage

ModeSwitch uses the Groq API for generating personalized suggestions. Make sure to set your API key in the `.env` file.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[MIT License](LICENSE)
