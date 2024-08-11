TweetFetcher is a Python script designed to retrieve tweets from X (formerly Twitter) and save them into a CSV file.
Utilizing the twikit library, this tool efficiently fetches tweets, handles rate limits, and manages authentication using cookies.

Features
Fetch tweets from specific users based on a defined query.
Save tweet data, including username, tweet text, creation date, retweets, and likes, to a CSV file.
Manage rate limits and handle missing cookies by logging in with credentials and saving new cookies.
Prerequisites
Python 3.7 or later
twikit library

Install the required Python packages:
pip install twikit
Configuration
Create a config.ini file in the project directory with your X (formerly Twitter) login credentials:
ini
[X]
username = your_username
email = your_email
password = your_password
Run the script to fetch tweets and save them to tweets.csv:

to run the code.
python main.py
