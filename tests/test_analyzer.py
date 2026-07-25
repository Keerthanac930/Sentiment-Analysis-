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

    def test_detects_positive_driver_schedule_sentiment(self):
        analyzer = AspectSentimentAnalyzer()

        results = analyzer.analyze("The driver arrived ten minutes ahead of schedule.")

        sentiments = {result["aspect"]: result["sentiment"] for result in results}
        self.assertEqual(sentiments["delivery"], "positive")

    def test_returns_overall_sentiment_when_no_aspect_is_found(self):
        analyzer = AspectSentimentAnalyzer()

        results = analyzer.analyze("I hate this useless experience.")

        self.assertEqual(results[0]["aspect"], "overall")
        self.assertEqual(results[0]["sentiment"], "negative")

    def test_returns_overall_neutral_when_no_sentiment_words_are_found(self):
        analyzer = AspectSentimentAnalyzer()

        results = analyzer.analyze("The item is on the table.")

        self.assertEqual(results[0]["aspect"], "overall")
        self.assertEqual(results[0]["sentiment"], "neutral")


if __name__ == "__main__":
    unittest.main()
