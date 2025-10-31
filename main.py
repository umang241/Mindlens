from flask import Flask, request, jsonify

app = Flask(__name__)

# This will store all chat memory in Python (for now)
memory = []

@app.route("/", methods=["GET"])
def home():
    return "🧠 Mindlens Memory API is Live — it can remember what you say!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Save what user said
    memory.append(user_message)

    # Create a reply that shows memory
    reply = f"I remember {len(memory)} things so far. You said: '{user_message}'"

    return jsonify({
        "reply": reply,
        "memory": memory  # show everything remembered
    })

if __name__ == "__main__":
    app.run()
