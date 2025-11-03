from flask import Flask, render_template, request
import sys
import os

# Añadir la ruta raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from EmotionDetection.emotion_detection import emotion_detector

"""
Flask web application for emotion detection.
This module provides a web interface for analyzing emotions in text.
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    "Emotion Detector",
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

@app.route('/emotionDetector')
def emo_dect():
    """
    Analyze emotions in the provided text.
    
    Returns:
        str: Formatted emotion analysis results or error message
    """
    text_to_detc = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_detc)

    dominant_emotion = emotion_result.get('dominant_emotion', 'unknown')

    emotion_scores = {k: v for k, v in emotion_result.items() if k != 'dominant_emotion'}

    emotion_parts = [f"'{emo}': {score:.4f}" for emo, score in emotion_scores.items()]

    response = (
    f"For the given statement, the system response is "
    + ", ".join(emotion_parts)
    + f". The dominant emotion is {dominant_emotion}."
    )

    return response


@app.route('/')
def index():
    """
    Main route that serves the index.html page
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
