from flask import Flask, render_template, request, jsonify
from src.chatbot import Chatbot


app = Flask(__name__)


bot = Chatbot()

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    """
    This route is called when the user sends a message from the webpage.
    Flask receives it, passes it to the chatbot, and returns the reply.
    """
    user_message = request.form['user_message']

    bot_reply = bot.get_response(user_message)

    return jsonify({'response': bot_reply})


if __name__ == '__main__':
    app.run(debug=True)