Student Helper Chatbot

Internship – CodSoft (AI Domain)

Overview

The Student Helper Chatbot is a simple yet intelligent rule-based conversational agent that provides study tips, motivation, and reminders to students.
It demonstrates text preprocessing, intent classification, and contextual conversation logic — built entirely from scratch using Python and NLTK.

⸻

Tech Stack
	•	Language: Python 3
	•	Libraries: NLTK · Regex · Flask (optional web demo)
	•	IDE: Visual Studio Code
	•	Version Control: Git & GitHub

⸻

Project Structure
    CODSOFT/
└── Task1_Chatbot/
    ├── data/
    │   └── intents.json
    ├── studentbot/
    │   ├── _init_.py
    │   ├── preprocess.py
    │   ├── matcher.py
    │   └── bot_core.py
    ├── demo_cli.py
    ├── app.py            # optional Flask demo
    ├── requirements.txt
    └── README.md

⸻  

Setup Instructions

1. Clone the Repository
git clone https://github.com/Taushin-sys/CodSoft.git
cd CodSoft/Task1_Chatbot

2. Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# or source venv/bin/activate on Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Download Required NLTK Resources
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('punkt_tab')
>>> nltk.download('wordnet')
>>> exit()

_______

Run the Chatbot ( CLI Mode )
python demo_cli.py

Example conversation:
You: My name is Tosh
Bot: Nice to meet you, Tosh! How can I help today?

You: study tips
Bot: Tosh, Try the Pomodoro technique — 25 minutes of focus followed by a 5-minute break.

You: remind me to submit assignment
Bot: Okay — I noted this for the session: "remind me to submit assignment" …

You: session
Bot (session): {'user_name': 'Tosh', 'last_topic': 'study_tips', 'reminders_count': 1}

You: quit
Bot: Take care! Good luck with your studies.

Run the Optional Flask Web Demo
python app.py

Key Features
	•	Intent-based responses using JSON intents.
	•	Text cleaning & lemmatization via NLTK.
	•	Lightweight session memory for names and reminders.
	•	Extendable design: add more intents easily.
	•	Web demo (optional) with Flask.

⸻

Originality Statement

All code and responses were written by me (Toshin Syed) for the CodSoft AI Internship Task 1.
No code was copied from public repositories. The chatbot’s intents, logic, and wording are uniquely created.

⸻

How to Contribute / Fork
	1.	Fork this repo.
	2.	Create a branch for enhancements (git checkout -b feature-name).
	3.	Submit a pull request with your changes.

⸻

Author

Taushin Sayed
B.E. in Artificial Intelligence & Data Science
CodSoft AI Intern | October 2025 Batch

License

This project is open-sourced for learning purposes under the MIT License.