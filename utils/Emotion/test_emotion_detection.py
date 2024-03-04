from emotion_detection import emotion_detector
import unittest

class EmotionDetectionTest(unittest.TestCase):
    def test_joy_dominant(self):
        testCase = "I am glad this happend"
        testResult = emotion_detector(testCase)
        self.assertEqual(testResult['dominant_emotion'], 'joy')

    def test_anger_dominant(self):
        testCase = "I am really mad about this"
        testResult = emotion_detector(testCase)
        self.assertEqual(testResult['dominant_emotion'], 'anger')

    def test_disgust_dominant(self):
        testCase = "I feel disgusted just hearing about this"
        testResult = emotion_detector(testCase)
        self.assertEqual(testResult['dominant_emotion'], 'disgust')

    def test_sadness_dominant(self):
        testCase = "I am so sad about this"
        testResult = emotion_detector(testCase)
        self.assertEqual(testResult['dominant_emotion'], 'sadness')

    def test_fear_dominant(self):
        testCase = "I am really afraid that this will happen"
        testResult = emotion_detector(testCase)
        self.assertEqual(testResult['dominant_emotion'], 'fear')

unittest.main()