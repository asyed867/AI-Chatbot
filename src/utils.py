import re, json

class Utils:
    @staticmethod
    def load_intents(file_path):
        """Load intents from a JSON file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    @staticmethod
    def normalize_text(text):
        """Lowercase and remove punctuation from text."""
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\s+', ' ', text)  # collapse extra spaces
        return text