from src.absa.lexicon import ASPECT_KEYWORDS, NEGATIVE_WORDS, POSITIVE_WORDS
from src.absa.preprocessing import tokenize


class AspectSentimentAnalyzer:
    """Rule-based baseline analyzer for aspect-level sentiment."""

    def __init__(self, aspects=None, positive_words=None, negative_words=None):
        self.aspects = aspects or ASPECT_KEYWORDS
        self.positive_words = positive_words or POSITIVE_WORDS
        self.negative_words = negative_words or NEGATIVE_WORDS

    def analyze(self, review):
        tokens = tokenize(review)
        token_set = set(tokens)

        results = []
        for aspect, keywords in self.aspects.items():
            matched_keywords = sorted(token_set.intersection(keywords))
            if not matched_keywords:
                continue

            sentiment, score = self._classify_aspect_sentiment(tokens, keywords)
            results.append(
                {
                    "aspect": aspect,
                    "matched_keywords": ", ".join(matched_keywords),
                    "sentiment": sentiment,
                    "score": score,
                }
            )

        return results

    def analyze_dataframe(self, dataframe, text_column="review"):
        import pandas as pd

        rows = []

        for index, review in dataframe[text_column].items():
            analysis = self.analyze(review)
            if not analysis:
                rows.append(
                    {
                        "row_id": index,
                        "review": review,
                        "aspect": "not_detected",
                        "matched_keywords": "",
                        "sentiment": "neutral",
                        "score": 0,
                    }
                )
                continue

            for result in analysis:
                rows.append({"row_id": index, "review": review, **result})

        return pd.DataFrame(rows)

    def analyze_records(self, records, text_column="review"):
        rows = []

        for index, record in enumerate(records):
            review = record.get(text_column, "")
            analysis = self.analyze(review)
            if not analysis:
                rows.append(
                    {
                        "row_id": index,
                        "review": review,
                        "aspect": "not_detected",
                        "matched_keywords": "",
                        "sentiment": "neutral",
                        "score": 0,
                    }
                )
                continue

            for result in analysis:
                rows.append({"row_id": index, "review": review, **result})

        return rows

    def _classify_aspect_sentiment(self, tokens, keywords, window_size=2):
        aspect_positions = [index for index, token in enumerate(tokens) if token in keywords]
        sentiment_tokens = []

        for position in aspect_positions:
            start = max(0, position - window_size)
            end = min(len(tokens), position + window_size + 1)
            sentiment_tokens.extend(tokens[start:end])

        return self._classify_sentiment(sentiment_tokens)

    def _classify_sentiment(self, tokens):
        positive_count = sum(1 for token in tokens if token in self.positive_words)
        negative_count = sum(1 for token in tokens if token in self.negative_words)
        score = positive_count - negative_count

        if score > 0:
            return "positive", score
        if score < 0:
            return "negative", score
        return "neutral", score
