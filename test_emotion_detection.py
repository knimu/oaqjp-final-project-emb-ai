"""Unit tests for the emotion detection application."""

import unittest
from unittest.mock import patch, Mock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test emotion detector behavior."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_success_response(self, mock_post):
        """Test a successful response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.1,
                    "disgust": 0.1,
                    "fear": 0.1,
                    "joy": 0.6,
                    "sadness": 0.1
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am happy")

        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        """Test handling of a bad request."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()