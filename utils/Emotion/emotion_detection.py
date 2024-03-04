import requests, json

def emotion_detector(text_to_analyze):
    """
    This sends text to Watson NLP to detect customer's emotion
    Inputs:
        string: text_to_analyze
    Outputs:
        dict: emotion_complex
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    INPUT = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }
    res = requests.post(URL, headers = HEADERS, json = INPUT)
    if res.status_code == 200:
        res = json.loads(res.text)["emotionPredictions"][0]["emotion"]
        dominant_emotion = ""
        maxPoint = 0
        for key in res:
            dominant_emotion = key if maxPoint < res[key] else dominant_emotion
            maxPoint = max(maxPoint, res[key])
        res["dominant_emotion"] = dominant_emotion
        return res
    else:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
