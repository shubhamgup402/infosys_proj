#create_tweet.py
import json
from time import sleep
import pandas as pd
from run_prompt import execute_gemini_for_tweet_creation, execute_gemini_for_tweet_compare

# --- Utility to select top tweets ---
def top_5_selection(analysed_tweets, engagement_type: str):
    df = pd.DataFrame(analysed_tweets)
    filtered_df = df[df['engagement_type'] == engagement_type]
    return filtered_df.nlargest(5, columns=['engagement_score']).to_dict(orient="records")

# --- Validation function ---
def validate_tweet(tweet):
    """
    Validates a tweet and truncates it if necessary
    Returns: (valid_tweet, is_valid)
    """
    if not tweet:
        return "", False
        
    # Remove extra whitespace
    tweet = ' '.join(tweet.split())
    
    # Check for placeholder text
    placeholders = ['[', ']', '[Company]', '[Link]', '[Name]', '[Customer']
    if any(p in tweet for p in placeholders):
        return tweet, False
        
    # Truncate if too long
    if len(tweet) > 280:
        # Try to truncate at a word boundary
        tweet = tweet[:277] + "..."
        
    return tweet, len(tweet) <= 280

# --- Main function ---
def create_tweet(analysed_tweets, prompt=None, return_results=False):
    if prompt is None:
        prompt = "Create the tweet for the new NVIDIA H200 Tensor Core GPU designed for accelerating generative AI workloads."
    engagement_type = "like"

    top_5_tweets = top_5_selection(analysed_tweets, engagement_type)

    system_prompt = f"""
    You are tasked with creating a high-engagement marketing tweet for {prompt}.

    CRITICAL REQUIREMENTS:
    - Tweet MUST be under 250 characters (strict limit, including spaces and punctuation)
    - NO placeholder text like [Company Name] or [Link]
    - Use real, specific content only
    - Include relevant hashtags but limit them to 2-3 most impactful ones
    - If mentioning URLs, include a real link only if it’s essential. Otherwise, omit it completely.


    Follow these steps:
    1. Analyze the following example tweets ({top_5_tweets}) from similar companies with very high user engagement.
    2. Generate a new tweet that leverages these proven strategies while staying authentic to {prompt}.
    3. Before finalizing, count the exact number of characters and ensure it's under 250.
    4. Provide a direct comparison between the new tweet and one example tweet.
    5. Predict how the new tweet will perform relative to the examples.
    6. Explain in detail why this tweet is likely to succeed (or fail).
    7. Identify the engagement drivers.
    """

    # --- Generate tweet with model A ---
    out_a = execute_gemini_for_tweet_creation(prompt=system_prompt, model="gemini-2.5-flash-lite")
    try:
        out_dict_a = json.loads(out_a)
    except Exception:
        print("Failed parsing JSON from model A. Raw response:\n", out_a)
        raise

    tweet_a = out_dict_a.get("tweet", "")
    tweet_a, is_valid_a = validate_tweet(tweet_a)
    
    # If tweet is invalid, try one more time
    if not is_valid_a:
        sleep(5)
        out_a = execute_gemini_for_tweet_creation(prompt=system_prompt, model="gemini-2.5-flash-lite")
        try:
            out_dict_a = json.loads(out_a)
            tweet_a = out_dict_a.get("tweet", "")
            tweet_a, is_valid_a = validate_tweet(tweet_a)
        except Exception:
            print("Failed second attempt for model A")

    sleep(5)

    # --- Generate tweet with model B ---
    out_b = execute_gemini_for_tweet_creation(prompt=system_prompt, model="gemini-2.5-flash-lite")
    try:
        out_dict_b = json.loads(out_b)
    except Exception:
        print("Failed parsing JSON from model B. Raw response:\n", out_b)
        raise

    sleep(5)
    tweet_b = out_dict_b.get("tweet", "")
    tweet_b, is_valid_b = validate_tweet(tweet_b)
    
    # If tweet is invalid, try one more time
    if not is_valid_b:
        sleep(5)
        out_b = execute_gemini_for_tweet_creation(prompt=system_prompt, model="gemini-2.5-flash-lite")
        try:
            out_dict_b = json.loads(out_b)
            tweet_b = out_dict_b.get("tweet", "")
            tweet_b, is_valid_b = validate_tweet(tweet_b)
        except Exception:
            print("Failed second attempt for model B")
    
    sleep(5)

    # --- Comparison prompt ---
    compare_prompt = f"""
    You are tasked with comparing two marketing tweets generated for {prompt}.
    Example tweets from similar companies: {top_5_tweets}

    Tweet A: {tweet_a}
    Tweet B: {tweet_b}

    
    Carefully analyze Tweet A and Tweet B in terms of clarity, readability, emotional appeal, tone, authenticity to {prompt}, 
    and their use of engagement drivers such as hooks, questions, hashtags, emojis, and urgency. 
    Evaluate which tweet is more likely to achieve higher virality potential (likes, shares, comments), 
    clearly outlining the strengths and weaknesses of each. 
    Then provide a final judgment on which tweet is more effective overall, explain why it would likely outperform the other, 
    and propose a refined version that combines the strongest aspects of both for maximum engagement.
    """

    compare_out = execute_gemini_for_tweet_compare(prompt=compare_prompt, model="gemini-2.5-flash-lite")

    sleep(5)
    # Parse comparison output
    try:
        compare_dict = json.loads(compare_out)
    except Exception:
        print("Failed parsing comparison JSON. Raw response:\n", compare_out)
        raise

    tweet_a_vs_tweet_b = compare_dict.get("tweet_a_vs_tweet_b", "")
    prediction = compare_dict.get("prediction", "")
    sleep(5)
    explanation = compare_dict.get("explanation", "")

    # --- Print outputs ---
    if return_results:
        return {
            "tweet_a": tweet_a,
            "tweet_b": tweet_b,
            "tweet_a_vs_tweet_b": tweet_a_vs_tweet_b,
            "prediction": prediction,
            "explanation": explanation,
        }
    else:
        print(f"\nGenerated Tweet (model A): {tweet_a}\n")
        print(f"Generated Tweet (model B): {tweet_b}\n")
        print("=== Comparison Result ===")
        print("=== Tweet A vs Tweet B ===")
        print(tweet_a_vs_tweet_b)
        print(f"Prediction: {prediction}\n")
        print("=== Explanation ===")
        print(explanation)


# --- Run the pipeline ---
if __name__ == "__main__":
    with open("analyzed_tweets.json") as f:
        data = json.load(f)
        print(f"Tweets loaded: {len(data)}")
        create_tweet(data)
