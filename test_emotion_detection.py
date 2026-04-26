import unittest
from EmotionDetection.emotion_detection import emotion_detector

#Unit Test Class to contain test cases for emotion_detector
class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector(self):
        """
        Perform test cases against given statements below,
        the BERT analyzer shall return the dominant emotion as 
        returned from the emotion_detector shall match against the following:
        I am glad this happened	- joy
        I am really mad about this - anger
        I feel disgusted just hearing about this - disgust
        I am so sad about this - sadness
        I am really afraid that this will happen - fear
        """
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")

unittest.main()