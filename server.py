"""
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""
#Import Flask and Dependencies
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the Flask App
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    """
    This code recieves the text from HTML interface and
    runs the emotion detection over emotion_detector() function.
    The output returned shows the label and its emotional scores.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result['anger'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']
    out = f"For the given statement, the system response is 'anger':{anger},\
    'disgust':{disgust}, 'fear':{fear}, 'joy':{joy} and 'sadness':{sadness}.\
    The dominant emotion is {dominant_emotion}"
    return out
@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application page over
    the Flask channel.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
