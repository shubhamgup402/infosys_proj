#create_tweet.py
import json
import pandas as pd
from run_prompt import execute_gemini_for_tweet_creation

from google import genai
from google.genai import types
import os

# --- Utility to select top tweets ---
def top_5_selection(analysed_tweets, engagement_type: str):
    df = pd.DataFrame(analysed_tweets)
    filtered_df = df[df['engagement_type'] == engagement_type]
    return filtered_df.nlargest(5, columns=['engagement_score']).to_dict(orient="records")

# --- Main function ---
def create_tweet(analysed_tweets):
    prompt = "Create the tweet for new iPhone 17 Pro"
    engagement_type = "like"

    top_5_tweets = top_5_selection(analysed_tweets, engagement_type)

    print(f"Top 5 tweets for engagement type '{engagement_type}':")
    for i, tweet_data in enumerate(top_5_tweets):
        print(f"  {i+1}: {tweet_data}")

    system_prompt = f""" 
    
    Create the tweet compare it with the example tweets
    and predict and explain why and how this tweet will
    perform well comparing to the given examples. {prompt}
    
    Here are some example tweets and their sentiment analysis with very
    high user engagements of other similar companies. Example Tweets: {top_5_tweets}

    """

    out = execute_gemini_for_tweet_creation(system_prompt)

    out_dict = json.loads(out)
    tweet_a = out_dict.get("tweet_a", "")
    tweet_b = out_dict.get("tweet_b", "")
    tweet_a_and_b = out_dict.get("tweet_a_and_b", "")
    prediction = out_dict.get("prediction", "")
    explanation = out_dict.get("explanation", "")

    print(f"\nGenerated Tweet: {tweet_a} \n")
    print(f"Example Tweet: {tweet_b} \n")
    print(f"Tweet A vs Tweet B: {tweet_a_and_b} \n")
    print(f"Prediction: {prediction} \n")
    print(f"Explanation: {explanation} \n")

# --- Run the pipeline ---
if __name__ == "__main__":
    with open("analyzed_tweets.json") as f:
        data = json.load(f)
        print(f"Tweets loaded: {len(data)}")
        create_tweet(data)

