from textblob import TextBlob

def sentiment_agent(text, personality):
    polarity = TextBlob(text).sentiment.polarity

    base = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

    if personality == "Energetic":
        return f"{base}! ⚡ Energy detected"
    elif personality == "Analytical":
        return f"{base}. Sentiment score processed logically."
    else:
        return f"{base}. Calm emotional state detected."

def insight_agent(text):
    length = len(text.split())
    return f"Text contains {length} words. Suitable for deeper analysis."
