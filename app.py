from flask import Flask, render_template, request, jsonify
from emotion import detect_emotion
from agents import sentiment_agent, insight_agent

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json["text"]
    personality = request.json["personality"]

    emotion = detect_emotion(text)
    sentiment = sentiment_agent(text, personality)
    insight = insight_agent(text)

    return jsonify({
        "emotion": emotion,
        "sentiment": sentiment,
        "insight": insight
    })

if __name__ == "__main__":
    app.run(debug=True)
