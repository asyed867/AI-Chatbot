from .utils import Utils
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Matcher:
    """Handles user intent matching using TF-IDF vectorization and cosine similarity."""

    @staticmethod
    def tokenize(text):
        """
        Normalize and split text into tokens (words).

        Args:
            text (str): The text to tokenize.

        Returns:
            list: A list of normalized word tokens.
        """
        return Utils.normalize_text(text).split()

    @staticmethod
    def get_best_intent(user_input, intents, threshold=0.4):
        """
        Identify the intent that best matches the user's input.

        Uses TF-IDF vectorization and cosine similarity to compare the user's input
        against all intent patterns.

        Args:
            user_input (str): The user's message.
            intents (dict): A dictionary containing intent tags, patterns, and responses.
            threshold (float): Minimum similarity score to consider a valid match.

        Returns:
            tuple: (best_tag, best_score)
                - best_tag (str or None): The tag of the best-matching intent.
                - best_score (float): The similarity score of the match.
        """
        patterns = []
        tags = []

        # Collect patterns and corresponding tags
        for intent in intents.get("intents", []):
            for pattern in intent.get("patterns", []):
                patterns.append(Utils.normalize_text(pattern))
                tags.append(intent["tag"])

        # Handle empty or missing patterns
        if not patterns:
            return None, 0.0

        # Vectorize the patterns and user input
        vectorizer = TfidfVectorizer()
        pattern_vectors = vectorizer.fit_transform(patterns)
        user_vector = vectorizer.transform([Utils.normalize_text(user_input)])

        # Calculate cosine similarity between user input and patterns
        similarities = cosine_similarity(user_vector, pattern_vectors).flatten()

        # Find best match
        best_index = similarities.argmax()
        best_score = similarities[best_index]
        best_tag = tags[best_index]

        return best_tag, best_score
