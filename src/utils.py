import re
import json


class Utils:
    """Utility functions for text normalization and loading chatbot intents."""

    @staticmethod
    def load_intents(file_path):
        """
        Load intents from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing intents.

        Returns:
            dict: Parsed JSON data with intent tags, patterns, and responses.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def normalize_text(text):
        """
        Normalize user input by lowercasing and removing punctuation.

        Args:
            text (str): Input text to normalize.

        Returns:
            str: Cleaned text without punctuation and extra spaces.
        """
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\s+', ' ', text)     # Collapse multiple spaces
        return text
