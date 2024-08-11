from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint

# Set the minimum number of tweets to retrieve
MINIMUM_TWEETS = 10

# Define the search query for tweets from Elon Musk between January 1, 2018, and January 1, 2020
QUERY = '(from:elonmusk) lang:en until:2020-01-01 since:2018-01-01'

def get_tweets(tweets):
    if tweets is None:
        # If no tweets have been fetched yet, initiate the first search
        print(f'{datetime.now()} - Getting tweets...')
        tweets = client.search_tweet(QUERY, product='Top')
    else:
        # If tweets have been fetched, wait for a random time between 5 and 10 seconds before fetching more
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds ...')
        time.sleep(wait_time)
        tweets = tweets.next()  # Fetch the next set of tweets

    return tweets

# Load login credentials from the config file
config = ConfigParser()
config.read('config.ini')
username = config['X']['username']
email = config['X']['email']
password = config['X']['password']

# Create a CSV file to store the tweets and write the header row
with open('tweets.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tweet_count', 'Username', 'Text', 'Created At', 'Retweets', 'Likes'])

# Authenticate to X.com using cookies (instead of logging in with username, email, and password)
client = Client(language='en-US')
# client.login(auth_info_1=username, auth_info_2=email, password=password)  # Optional login using credentials
# client.save_cookies('cookies.json')  # Optional: Save cookies for future sessions

try:
    client.load_cookies('cookies.json')
except FileNotFoundError:
    print("Cookies file not found. Logging in with credentials instead.")
    client.login(auth_info_1=username, auth_info_2=email, password=password)
    client.save_cookies('cookies.json')  # Save cookies for future use


tweet_count = 0  # Initialize the tweet count
tweets = None  # Initialize the tweets object to None

# Loop until the minimum number of tweets has been fetched
while tweet_count < MINIMUM_TWEETS:

    try:
        # Attempt to get tweets (or the next batch of tweets)
        tweets = get_tweets(tweets)
    except TooManyRequests as e:
        # If the rate limit is reached, calculate the wait time and pause until it resets
        rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
        print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
        wait_time = rate_limit_reset - datetime.now()
        time.sleep(wait_time.total_seconds())
        continue

    # If no more tweets are found, exit the loop
    if not tweets:
        print(f'{datetime.now()} - No more tweets found')
        break

    # Process each tweet in the batch
    for tweet in tweets:
        tweet_count += 1  # Increment the tweet count
        # Prepare the data for the CSV file
        tweet_data = [tweet_count, tweet.user.name, tweet.text, tweet.created_at, tweet.retweet_count, tweet.favorite_count]
        
        # Append the tweet data to the CSV file
        with open('tweets.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(tweet_data)

    print(f'{datetime.now()} - Got {tweet_count} tweets')  # Log the progress

print(f'{datetime.now()} - Done! Got {tweet_count} tweets found')  # Final log statement when done
