from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

def vader_sentiment(text):
    """Analyze sentiment using VADER"""
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

