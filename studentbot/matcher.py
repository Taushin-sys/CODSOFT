"""
matcher.py
-----------
This module matches user input with the most relevant intent
from the intents.json file using simple token overlap scoring.
"""

import json
import random
from studentbot.preprocess import preprocess_input

def load_intents(path="data/intents.json"):
    """
    Load the intents from a JSON file.
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["intents"]

def calculate_similarity(user_tokens, pattern_tokens):
    """
    Compare two lists of tokens and return a similarity score
    based on overlapping words.
    """
    overlap = set(user_tokens) & set(pattern_tokens)
    total = set(user_tokens) | set(pattern_tokens)
    score = len(overlap) / len(total) if total else 0
    return score

def find_best_intent(user_input, intents):
    """
    Find which intent best matches the user's input.
    """
    user_tokens = preprocess_input(user_input)
    best_score = 0
    best_tag = "fallback"

    for intent in intents:
        for pattern in intent["patterns"]:
            pattern_tokens = preprocess_input(pattern)
            score = calculate_similarity(user_tokens, pattern_tokens)
            if score > best_score:
                best_score = score
                best_tag = intent["tag"]

    return best_tag

def get_response(tag, intents):
    """
    Return a random response from the matched intent.
    """
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Hmm, I’m not sure what you mean."

# Quick test
if __name__ == "__main__":
    intents = load_intents()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Bot: Bye! Keep learning and stay curious.")
            break
        tag = find_best_intent(user_input, intents)
        response = get_response(tag, intents)
        print("Bot:", response)