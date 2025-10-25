"""
bot_core.py
-----------
Robust chatbot wrapper for the Student Helper Bot.
Improved error handling and case-insensitive name extraction.
"""

import os
import re
from typing import Dict, Any
from studentbot.matcher import load_intents, find_best_intent, get_response

DEFAULT_INTENTS_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'intents.json')

class StudentBot:
    def __init__(self, intents_path: str = None):
        self.intents_path = intents_path or DEFAULT_INTENTS_PATH
        # ensure self.intents always exists even if loading fails
        try:
            self.intents = load_intents(self.intents_path)
        except Exception as e:
            # If loading fails, set an empty list and print a friendly warning
            print(f"[Warning] Could not load intents from {self.intents_path}: {e}")
            self.intents = []

        # Small session store for the running session
        self.session: Dict[str, Any] = {
            "user_name": None,
            "last_topic": None,
            "reminders": []
        }

    def _handle_reminder_intent(self, user_text: str) -> str:
        reminder_text = user_text.strip()
        self.session["reminders"].append(reminder_text)
        return f"Okay — I noted this for the session: \"{reminder_text}\". (I will remember it until you close this chat.)"

    def _extract_name(self, user_text: str) -> str | None:
        """
        Try a few patterns to extract a first name robustly and case-insensitively.
        Examples it handles: "My name is Tosh", "my name's Tosh", "I am called Tosh", "I am Tosh"
        Returns the first token it finds as a name (capitalized) or None.
        """
        text = user_text.strip()
        # common patterns (case-insensitive)
        patterns = [
            r"my name is\s+([A-Za-z'-]+)",
            r"my name's\s+([A-Za-z'-]+)",
            r"i am called\s+([A-Za-z'-]+)",
            r"i am\s+([A-Za-z'-]+)"
        ]
        for pat in patterns:
            m = re.search(pat, text, flags=re.IGNORECASE)
            if m:
                name = m.group(1)
                return name.capitalize()
        return None

    def respond(self, user_text: str) -> str:
        """
        Primary method: takes user text and returns the bot response string.
        Defensive and robust: will not crash on unexpected inputs.
        """
        if not user_text or not isinstance(user_text, str):
            return "I didn't catch that — could you type it again?"

        lower = user_text.lower()

        # 1) Name extraction
        name = self._extract_name(user_text)
        if name:
            self.session["user_name"] = name
            return f"Nice to meet you, {self.session['user_name']}! How can I help today?"

        # 2) Reminder handling
        if "remind me" in lower or "reminder" in lower or "set a reminder" in lower:
            return self._handle_reminder_intent(user_text)

        # 3) Intent matching (safe: use fallback if intents list is empty)
        if not self.intents:
            # fallback behavior if intents were not loaded
            return "Sorry, I can't access my knowledge base right now. Try again later."

        tag = find_best_intent(user_text, self.intents)
        response = get_response(tag, self.intents)

        # record last topic for simple personalization
        if tag in ("study_tips", "math_help", "motivation"):
            self.session["last_topic"] = tag

        # personalize if name known and not fallback
        if self.session.get("user_name") and tag != "fallback":
            response = f"{self.session['user_name']}, {response}"

        return response

    def get_session_summary(self) -> Dict[str, Any]:
        """Return a small summary of session info for debugging/display."""
        return {
            "user_name": self.session.get("user_name"),
            "last_topic": self.session.get("last_topic"),
            "reminders_count": len(self.session.get("reminders", [])),
            "reminders": self.session.get("reminders", [])
        }