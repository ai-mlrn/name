from flask import Flask, jsonify, request, send_file

app = Flask(__name__)


# 1. Serve the HTML file when you visit the main URL
@app.route("/")
def home():
    return send_file("index.html")


# 2. Create a backend endpoint that receives and returns JSON data
@app.route("/greet", methods=["POST"])
def greet():
    data = request.get_json()  # Get data sent from HTML
    user_name = data.get("name", "Stranger")
    return jsonify({"message": f"Hello, {user_name}! From Python."})


if __name__ == "__main__":
    app.run(debug=True)
