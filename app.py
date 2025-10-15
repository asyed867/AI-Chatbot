from flask import Flask, render_template, request, jsonify
from src.chatbot import Chatbot

# 1️⃣ Create a Flask web app instance
app = Flask(__name__)

# 2️⃣ Create one chatbot object (so it can handle all chats)
bot = Chatbot()

# 3️⃣ Define the route for your home page
@app.route('/')
def home():
    # When someone opens the website (http://127.0.0.1:5000/)
    # Flask will look in the "templates" folder for a file called "chat.html"
    return render_template('chat.html')

# 4️⃣ Define the route that handles chat messages
@app.route('/get', methods=['POST'])
def get_bot_response():
    """
    This route is called when the user sends a message from the webpage.
    Flask receives it, passes it to the chatbot, and returns the reply.
    """
    # Get the message that was sent from the HTML input box
    user_message = request.form['user_message']

    # Pass that message to your Chatbot class (from chatbot.py)
    bot_reply = bot.get_response(user_message)

    # Send the chatbot’s reply back to the browser as JSON
    return jsonify({'response': bot_reply})

# 5️⃣ Run the Flask app
if __name__ == '__main__':
    # debug=True means Flask will auto-reload when you save changes
    app.run(debug=True)
