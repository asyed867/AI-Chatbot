import re, json
def load_intents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # collapse extra spaces
    return text