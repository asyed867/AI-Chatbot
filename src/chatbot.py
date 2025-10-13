import random
from utils import Utils
from matcher import Matcher

class Chatbot:
    def __init__ (self,intents_path = "data/intents.json", threshold=0.4):
        self.intents= Utils.load_intents(intents_path)
        self.threshold = threshold
        


    def get_response(self, user_input):
        clean = Utils.normalize_text(user_input)
        tag, score = Matcher.get_best_intent(clean,self.intents)
        if tag and score >=self.threshold:
            for intent in self.intents["intents"]:
                if intent["tag"] == tag:
                    return random.choice(intent["responses"])
        return "I'm sorry, I didn't understand that. Can you please rephrase?"
    
    def chat(self):
        print("Chatbot is running. Type 'quit' to exit.")
        while True:
            user_text = input("> ")
            if user_text.lower() in ["quit", "exit"]:
                print("👋 Bye!")
                break
            print(self.get_response(user_text))
           



if __name__ == "__main__":
    bot = Chatbot()
    bot.chat()
   