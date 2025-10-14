"""
matcher.py
------------
Handles user intent matching based on token overlap scoring.
This helps the chatbot identify the closest intent for a given user input.
"""
from utils import Utils
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Matcher:
    @staticmethod
    def tokenize(text):
        """Convert text into normalized tokens (words)."""
        return Utils.normalize_text(text).split()


    

    @staticmethod
    def get_best_intent(user_input, intents, threshold=0.4):
        """
        Find the intent that best matches the user's input using TF-IDF and cosine similarity.

        Args:
        user_input (str): The user's message.
        intents (dict): Loaded intents file with tags and patterns.
        threshold (float): Minimum similarity to consider a match.

        Returns:
        tuple: (best_tag, best_score)

        """
        patterns = []
        tags = []

        for intent in intents.get("intents", []):
            for pattern in intent.get("patterns", []):
                patterns.append(Utils.normalize_text(pattern))
                tags.append(intent["tag"])
        
        if not patterns:
            return (None, 0.0)
           
        
        vectorizer = TfidfVectorizer()
        pattern_vectores = vectorizer.fit_transform(patterns)
        user_vector = vectorizer.transform([Utils.normalize_text(user_input)])
        similarities = cosine_similarity(user_vector, pattern_vectores).flatten()
       
        best_index = similarities.argmax()
        best_score = similarities[best_index]
        best_tag = tags[best_index]
        
        
        

        return best_tag, best_score
