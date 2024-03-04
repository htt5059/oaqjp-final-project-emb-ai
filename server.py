"""
This module initiates web server on localhost:5000
"""
from flask import Flask, request, render_template
from utils.Emotion.emotion_detection import emotion_detector

app = Flask("Emotion Prediction")

@app.route("/emotionDetector")
def emotion_predictor():
    """
    This function returns analysis result
    Output:
        string: analysis result
    """
    text = request.args.get("textToAnalyze")
    res = emotion_detector(text)
    if res['dominant_emotion'] is None:
        return "Invalid Input"

    return f"""
    For the given statement, the system response is \'anger\': {res['anger']}, \'disgust\': {res['disgust']}, \'fear\': {res['fear']}, \'joy\': {res['joy']}, and \'sadness\': {res['sadness']}.
    The dominant emotion is <b>{res['dominant_emotion']}</b>
    """

@app.route("/")
def index():
    """
    This function returns front end design of the home page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
