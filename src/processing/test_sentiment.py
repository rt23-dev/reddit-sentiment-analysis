from src.processing.sentiment_analysis import vader_sentiment

sample_text = "This stock is doing great!"
print(vader_sentiment(sample_text))