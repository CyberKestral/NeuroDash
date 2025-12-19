
from textblob import TextBlob

def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"
