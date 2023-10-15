from textblob import TextBlob as tb


class Sentiment:
    @staticmethod
    def analyze(input_text: str) -> dict:
        sentiment = tb(input_text).sentiment
        return {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity,
        }
