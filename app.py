from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# Load dataset
with open('dataset.json') as file:
    data = json.load(file)

# Extract data from dataset
intents = data['intents']

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    response = get_chatbot_response(user_message)
    return jsonify({'bot_response': response})

# Chatbot logic
def get_chatbot_response(user_message):
    user_message = user_message.lower()

    # Check for matching patterns
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in user_message:
                return random.choice(intent['responses'])

    return "I'm sorry, I don't understand that question."

if __name__ == '__main__':
    app.run(debug=True)
