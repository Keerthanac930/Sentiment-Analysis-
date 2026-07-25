import unittest

from src.absa.analyzer import AspectSentimentAnalyzer


class AspectSentimentAnalyzerTest(unittest.TestCase):
    def test_detects_positive_food_sentiment(self):
        analyzer = AspectSentimentAnalyzer()

        results = analyzer.analyze("The food was delicious and the service was friendly.")

        sentiments = {result["aspect"]: result["sentiment"] for result in results}
        self.assertEqual(sentiments["food"], "positive")
        self.assertEqual(sentiments["service"], "positive")

    def test_detects_negative_delivery_sentiment(self):
        analyzer = AspectSentimentAnalyzer()

        results = analyzer.analyze("The delivery was late and slow.")

        sentiments = {result["aspect"]: result["sentiment"] for result in results}
        self.assertEqual(sentiments["delivery"], "negative")

    def test_returns_empty_when_no_aspect_is_found(self):
        analyzer = AspectSentimentAnalyzer()

        self.assertEqual(analyzer.analyze("This sentence has no configured category."), [])


if __name__ == "__main__":
    unittest.main()
