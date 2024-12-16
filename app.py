from flask import Flask, render_template, request, jsonify
from chatbot import get_intent, responses  # Make sure this imports your logic correctly

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input")  # Get user input from JSON
    intent = get_intent(user_input)  # Get the intent using your existing logic

    # Handle the response
    if intent in responses:
        response = responses[intent]
    else:
        response = "I'm sorry, I didn't understand that."
    
    # Return the response as JSON
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
