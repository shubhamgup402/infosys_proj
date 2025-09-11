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
    prompt = "Create the tweet for the new NVIDIA H200 Tensor Core GPU designed for accelerating generative AI workloads."
    engagement_type = "like"

    top_5_tweets = top_5_selection(analysed_tweets, engagement_type)

    print(f"Top 5 tweets for engagement type '{engagement_type}':")
    for i, tweet_data in enumerate(top_5_tweets):
        print(f"  {i+1}: {tweet_data}")

    system_prompt = f""" 
    
    You are tasked with creating a high-engagement marketing tweet for {prompt}.  

    Follow these steps:  
    1. Analyze the following example tweets ({top_5_tweets}) from similar companies with very high user engagement.  
    2. Identify the engagement drivers (tone, structure, keywords, emotional appeal, audience targeting).  
    3. Generate a new tweet that leverages these proven strategies while staying authentic to {prompt}.  
    4. Provide a direct comparison between the new tweet and one example tweet, highlighting similarities and differences.  
    5. Predict how the new tweet will perform relative to the examples.  
    6. Explain in detail why this tweet is likely to succeed (or fail) based on sentiment, clarity, and alignment with engagement patterns.  

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

