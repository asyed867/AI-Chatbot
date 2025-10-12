import random
from utils import load__intents, normalize_text
from matcher import get_best_intent

class Chatbot:
    def _init_ (self,intents_path = "data/intents.json", threshold=0.4):
        self.intents= load__intents(intents_path)
        self.threshold = threshold
        print("Chatbot initalized successfully!")


    def get_reponse(self, user_input):
        clean = normalize_text(user_input)
        tag, score = get_best_intent(clean, self.intents)
        if tag and score >=self.threshold:
            for intent in self.intents["intents"]:
                if intent["tag"] == tag:
                    return random.choice(intent["responses"])
        return "I'm sorry, I didn't understand that. Can you please rephrase?"
    
    
   