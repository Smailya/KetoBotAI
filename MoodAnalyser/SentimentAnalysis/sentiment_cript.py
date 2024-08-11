from textblob import TextBlob  # Importing TextBlob for sentiment analysis
from dataclasses import dataclass  # Importing dataclass to create simple data structures

@dataclass
class Mood:
    emoji: str  # Represents the emoji corresponding to the sentiment
    sentiment: float  # Holds the sentiment polarity score

def get_mood(input_text: str, *, threshold: float) -> Mood:
    # Analyze the sentiment polarity of the input text using TextBlob
    sentiment: float = TextBlob(input_text).sentiment.polarity

    # Define thresholds for positive (friendly) and negative (hostile) sentiment
    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold  # Using negative threshold for proper comparison

    # Determine the mood based on the sentiment score
    if sentiment > friendly_threshold:
        return Mood('😄', sentiment)  # Positive sentiment, return a happy emoji
    elif sentiment < hostile_threshold:
        return Mood('😠', sentiment)  # Negative sentiment, return an angry emoji
    else:
        return Mood('😐', sentiment)  # Neutral sentiment, return a neutral emoji

# Main execution block
if __name__ == '__main__':
    while True:
        text: str = input('Text: ')  # Prompt the user for text input
        mood: Mood = get_mood(text, threshold=0.3)  # Get the mood based on the input text
        print(f'{mood.emoji} ({mood.sentiment})')  # Print the resulting emoji and sentiment score
