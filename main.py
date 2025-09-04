# import tweepy
# import json
# from run_prompt import execute_gemini

# # 🔑 New Twitter API credentials
# API_KEY = "lp1rNFo74HYvgo3WQrYWauDxg"
# API_SECRET_KEY = "n2JOkCHKW702KZHbrNbK06RQ3iv8nbtj7f25OZjJHOR7l8Sw8u"
# ACCESS_TOKEN = "1692596758893727744-PLGEqaLev9iJ62tXwFtktLR4SkkayE"
# ACCESS_TOKEN_SECRET = "bnBhHjKaYRu1ZSIhP1wrlcAU5wi6CekmM4NbWno8oo9B1"
# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABQ13wEAAAAAY2NHTfeKpB3lturUerwQw8HN3iQ%3DbRjLtfuV30f7VEmebP4nAhpFg4J75IOtnF7WxFQVvMypRXuRYh"

# if __name__ == "__main__":
#     twitterClient = tweepy.Client(
#         bearer_token=BEARER_TOKEN,
#         access_token_secret=ACCESS_TOKEN_SECRET,
#         consumer_key=API_KEY,
#         consumer_secret=API_SECRET_KEY,
#         access_token=ACCESS_TOKEN,
#         wait_on_rate_limit=True,
#     )

#     # Example user
#     user = twitterClient.get_user(username="nvidia")
#     user_id = user.data.id

#     # Fetch tweets with required fields
#     tweets = twitterClient.get_users_tweets(
#         user_id,
#         max_results=50,
#         tweet_fields=['created_at', 'text', 'public_metrics'],
#     )

#     # Save tweets to JSON (exact format as screenshot)
#     with open("myextracted_tweets.json", "w") as json_file:
#         json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)



import pandas as pd
import json

from run_prompt import execute_gemini_for_tweet_creation

def top_5_tweet(analysed_tweets, engagement_type: str):
    df = pd.DataFrame(analysed_tweets)
    filtered_df = df[df['engagement_type'] == engagement_type]
    e1 = filtered_df.nlargest(5, columns=['engagement_score']).to_dict(orient="records")
    return e1

# --- Run the pipeline ---
if __name__ == "__main__":
    with open("analyzed_tweets.json") as f:
        data = json.load(f)
        print(f"Tweets loaded: {len(data)}")

    top_tweets = top_5_tweet(data, "like")
    print("Top 5 tweets by likes:")
    print(json.dumps(top_tweets, indent=2))
