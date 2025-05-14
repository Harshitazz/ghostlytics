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
- Install dependencies using:

#!/bin/bash

# ---------------------------------------
# 📦 1. CLONE THE REPO (if not done yet)
# ---------------------------------------
git clone https://github.com/your-username/ghostlytics.git
cd modeswitch

# ---------------------------------------
# 🐍 2. CREATE & ACTIVATE VIRTUAL ENV
# ---------------------------------------
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# ---------------------------------------
# 📥 3. INSTALL DEPENDENCIES
# ---------------------------------------
pip install -r requirements.txt

# ⚙️ 4. Create a `.env` file in the root directory (if needed)
touch .env
# Add your environment variables like API keys or secrets:
# GROQ_API_KEY=your-secret-key

# ---------------------------------------
# 🚀 5. RUN THE APP
# ---------------------------------------
python modeswitch.py

# You'll be prompted to:
# - Select your mode: [gaming, work, study]
# - Choose your mood: [happy, stressed, tired, energetic]
# - Time is auto-detected unless passed with --time

# ---------------------------------------
# ⚙️ OPTIONAL: RUN WITH ARGUMENTS
# ---------------------------------------
python modeswitch.py --mode work --mood tired --time evening

# ---------------------------------------
# 📜 SHOW SESSION HISTORY
# ---------------------------------------
python modeswitch.py --history

# ---------------------------------------
# 🔚 DEACTIVATE VIRTUAL ENV WHEN DONE
# ---------------------------------------
deactivate

