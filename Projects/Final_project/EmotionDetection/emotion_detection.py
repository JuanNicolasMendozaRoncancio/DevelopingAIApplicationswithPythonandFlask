import requests  

token = "hf_xxxYourHuggingFaceTokenxxx"
url = "https://router.huggingface.co/hf-inference/models/j-hartmann/emotion-english-distilroberta-base"
headers = {"Authorization": f"Bearer {token}"}

def emotion_detector(text):
    payload = {"inputs": text}
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    response = {}
    values = []
    for dic in result[0]:
        response[dic['label']] = dic['score']
        values.append(dic['score'])
    response['dominant_emotion'] = result[0][values.index(max(values))]['label']
    return response
