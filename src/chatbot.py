import random
import os
from utils import Utils
from matcher import Matcher
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


class Chatbot:
    def __init__ (self,intents_path = "data/intents.json", threshold=0.4):
        self.intents= Utils.load_intents(intents_path)
        self.threshold = threshold
        self.oclient = OpenAI(api_key= os.environ.get("OPENAI_API_KEY"))
        

    def callOpenAI(self, user_input):
       

        messages = [
            {"role": "system", "content": f"You are a helpful assistant. "},
            {"role": "user", "content": user_input}
        ]

        response = self.oclient.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=500
        )   

        return response.choices[0].message.content

    
    def get_response(self, user_input):
        clean = Utils.normalize_text(user_input)
        tag, score = Matcher.get_best_intent(clean,self.intents)

        if tag and score >=self.threshold:
            for intent in self.intents["intents"]:
                if intent["tag"] == tag:
                    return random.choice(intent["responses"])
        return self.callOpenAI(user_input)  
    
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
   