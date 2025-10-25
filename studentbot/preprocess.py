"""
preprocess.py
-------------
This module prepares the user’s input text for processing by the chatbot.
It cleans, tokenizes, and lemmatizes the text to make pattern matching easier.
"""

import nltk
import string
from nltk.stem import WordNetLemmatizer

# Make sure necessary NLTK resources are available
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)
# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Convert text to lowercase and remove punctuation.
    Example: "Hello!!! How's it going?" -> "hello hows it going"
    """
    text = text.lower()  # make lowercase
    text = "".join([ch for ch in text if ch not in string.punctuation])
    return text

def tokenize(text):
    """
    Split text into a list of individual words.
    Example: "i love studying" -> ["i", "love", "studying"]
    """
    return nltk.word_tokenize(text)

def lemmatize_words(words):
    """
    Lemmatize each word to its root form.
    Example: ["studying", "books"] -> ["study", "book"]
    """
    return [lemmatizer.lemmatize(word) for word in words]

def preprocess_input(text):
    """
    Clean, tokenize, and lemmatize user input in one go.
    Example: "I'm studying hard!!!" -> ["im", "study", "hard"]
    """
    clean = clean_text(text)
    tokens = tokenize(clean)
    lemmas = lemmatize_words(tokens)
    return lemmas

# Run this section only if file is executed directly (for quick testing)
if __name__ == "__main__":
    sample = "Hey!! Can you remind me about my homework?"
    print("Original:", sample)
    print("Processed:", preprocess_input(sample))