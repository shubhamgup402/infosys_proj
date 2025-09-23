import tweepy
import json
from run_prompt import execute_gemini

API_KEY = "C7CZj6iQXjx9lGHfHSn25mrNf"
API_SECRET_KEY = "06y7dFUKXMh4Z19fS1tEHKa5yHcfeTO10z7M0DSa9SVA57WE0G"
ACCESS_TOKEN = "1957425206898946049-u2hbfZ2sC9jgujYUd3AAEFl44hU2lU"
ACCESS_TOKEN_SECRET = "WTmW4yhmw9LY4hFwrgP8w8h34jSoHX2aoV3VIHbZlg6NQ"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAM6M3gEAAAAAZeI5fZTmGbBvJUJN%2B42nOCD6tb4%3DQ7zRxdupelS480DMrXdnk8qVYDkbKdRULx2xjMKMAoy8rjdjYd"

if __name__ == "__main__":
    twitterClient = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET_KEY,
        access_token=ACCESS_TOKEN,
        wait_on_rate_limit=True,
    )


    user = twitterClient.get_user(username="nvidia")
    user_id = user.data.id

    tweets = twitterClient.get_users_tweets(
        user_id,
        max_results=50,
        tweet_fields=['created_at', 'text', 'public_metrics'],
    )

    # Save tweets in proper JSON format
    with open("extracted_tweets1.json", "w") as json_file:
        json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
