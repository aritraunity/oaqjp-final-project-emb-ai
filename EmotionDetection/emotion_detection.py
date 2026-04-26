import requests
import json

# Function to call the BERT Sentiment Analyzer
def emotion_detector(text_to_analyze):
    """
    The function will use the url to call the api of watson sentiment analyzer
    and return the analysed emotional aspects of the text.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document":{
            "text": text_to_analyze
        }
    }
    result = requests.post(url, json=payload, headers=header)
    if result.status_code == 200:
        result_json = json.loads(result.text)
        anger = result_json['emotionPredictions'][0]['emotion']['anger']
        disgust = result_json['emotionPredictions'][0]['emotion']['disgust']
        fear = result_json['emotionPredictions'][0]['emotion']['fear']
        joy = result_json['emotionPredictions'][0]['emotion']['joy']
        sadness = result_json['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = ''
        max = 0
        for emotion in result_json['emotionPredictions'][0]['emotion'].items():
            if emotion[1] > max:
                max = emotion[1]
                dominant_emotion = emotion[0]
        return {
            "anger":anger,
            "disgust":disgust,
            "fear":fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion":dominant_emotion
        }
    elif status_code == 400:
        return {
            "anger":None,
            "disgust":None,
            "fear":None,
            "joy": None,
            "sadness": None,
            "dominant_emotion":None
        }

    
