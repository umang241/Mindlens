from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "🧠 Mindlens AI API is live!"

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    question = data.get("question", "")

    # Use Groq or OpenAI compatible API (free-tier logic)
    response = f"AI Thought Process: Analyzing '{question}' deeply... here's a simple answer."

    return jsonify({
        "question": question,
        "answer": response
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
