from chatbot import Chatbot


def main():
        bot = Chatbot("intents.json")
        print("Study Helper Chatbot (type exit to quit)\n")

        while True:
            user_Input = input("> ")
            clean = user_Input.lower()
            if clean in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            response = bot.get_reponse(user_Input)
            print(response)

if __name__ == "__main__":
    main()