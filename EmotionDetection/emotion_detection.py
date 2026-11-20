"""Emotion detection module using the Watson NLP service."""

import requests


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores and dominant emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson_runtime/run"
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            url, headers=headers, json=payload, timeout=15
        )

        if response.status_code == 400:
            return None

        response.raise_for_status()

        emotions = response.json()["emotionPredictions"][0]["emotion"]
        dominant = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant,
        }

    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return None
