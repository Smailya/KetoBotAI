# TweetFetcher - Automated Tweet Collection Tool

## Overview

**TweetFetcher** is a Python script that automates the collection and storage of tweets from X (formerly Twitter). Using the powerful **twikit** library, it efficiently fetches tweets based on specified queries, manages authentication via cookies, and handles API rate limits with robust error handling. The collected tweet data is saved into a structured CSV file for easy analysis.

## Features

- Fetch tweets from specific users or based on custom queries
- Save tweet details including:
  - Username  
  - Tweet text  
  - Creation date  
  - Retweets count  
  - Likes count  
- Manage rate limits gracefully to avoid interruptions  
- Authenticate sessions using cookie-based login  
- Automatically handle missing or expired cookies by logging in with credentials and saving new cookies  

## Why This Matters

This project is highly relevant for full-stack engineers working on:

- Real-time data pipelines  
- Social media integration  
- Content scraping and aggregation tools  

Through this project, I gained valuable experience in:

- Authenticating sessions with cookies  
- Managing large-scale data ingestion workflows  
- Handling API usage limits effectively  

These skills enable companies to automate social media data collection, support social listening strategies, and generate actionable insights from vast volumes of user-generated content.

## Getting Started

### Prerequisites

- Python 3.7 or later  
- `twikit` library  

### Installation

Install the required package using pip:

pip install twikit

text

### Configuration

Create a `config.ini` file in the project root directory with your X (formerly Twitter) login credentials:

[X]
username = your_username
email = your_email
password = your_password

text

### Usage

Run the script to start fetching tweets and saving them to `tweets.csv`:

python main.py

text

## Output

The script generates a CSV file named `tweets.csv` containing the fetched tweet data with columns such as username, tweet text, creation date, retweets, and likes.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---
Developed by Ismail Cisse
Automating social media data collection with Python and twikit for smarter insights.
