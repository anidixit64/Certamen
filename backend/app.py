from flask import Flask, jsonify, request, send_from_directory
import os
import json
import random

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Load all questions from JSON files in the data directory
questions = []
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

for filename in os.listdir(data_dir):
    if filename.endswith('.json'):
        with open(os.path.join(data_dir, filename)) as f:
            questions.extend(json.load(f))

@app.route('/api/question', methods=['GET'])
def get_random_question():
    # Select a random question
    question = random.choice(questions)
    return jsonify({"question": question['question_sanitized']})

@app.route('/')
def serve_welcome():
    # Serve the welcome page
    return send_from_directory('../frontend', 'welcome.html')

@app.route('/questions')
def serve_questions():
    # Serve the main question page when accessing /questions
    return send_from_directory('../frontend', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
