import tweepy
import json
import os
from dotenv import load_dotenv
from run_prompt import execute_gemini

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    twitterClient = tweepy.Client(
        bearer_token=os.getenv('BEARER_TOKEN'),
        consumer_key=os.getenv('API_KEY'),
        consumer_secret=os.getenv('API_SECRET_KEY'),
        access_token=os.getenv('ACCESS_TOKEN'),
        access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'),
        wait_on_rate_limit=True,
    )

# Get user ID for the username "nvidia"
    user = twitterClient.get_user(username="nvidia")
    user_id = user.data.id

    tweets = twitterClient.get_users_tweets(
        user_id,
        max_results=50,
        tweet_fields=['created_at', 'text', 'public_metrics'],
    )

    # Save tweets in proper JSON format
    with open("extracted_tweets1.json", "w") as json_file:
        json.dump([tweet.data for tweet in tweets.data], json_file, indent=4) # output of phase 1 - extracted_tweets1.json
