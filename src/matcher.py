"""
matcher.py
------------
Handles user intent matching based on token overlap scoring.
This helps the chatbot identify the closest intent for a given user input.
"""

from src.utils import normalize_text


def tokenize(text):
    """Convert text into normalized tokens (words)."""
    return normalize_text(text).split()


def token_overlap_score(text_a, text_b):
    """
    Calculate similarity between two texts using token overlap.
    Returns a float between 0.0 and 1.0.
    """
    tokens_a = set(tokenize(text_a))
    tokens_b = set(tokenize(text_b))
    if not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_b)


def get_best_intent(user_input, intents, threshold=0.4):
    """
    Find the intent that best matches the user's input.

    Args:
        user_input (str): The user's message.
        intents (dict): Loaded intents file with tags and patterns.
        threshold (float): Minimum similarity to consider a match.

    Returns:
        tuple: (best_tag, best_score)
    """
    best_tag = None
    best_score = 0.0

    for intent in intents.get("intents", []):
        for pattern in intent.get("patterns", []):
            score = token_overlap_score(user_input, pattern)
            if score > best_score:
                best_score = score
                best_tag = intent["tag"]

    return (best_tag, best_score) if best_score >= threshold else (None, best_score)
