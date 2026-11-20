"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the application home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze submitted text and return emotion results."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Emotion service unavailable. Please try again."

    dominant = result["dominant_emotion"]

    return (
        f"For the given text, the dominant emotion is {dominant}. "
        f"anger: {result['anger']}, disgust: {result['disgust']}, "
        f"fear: {result['fear']}, joy: {result['joy']}, "
        f"sadness: {result['sadness']}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
