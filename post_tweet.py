import tweepy
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

def authenticate_twitter():
    """Authenticate with Twitter using OAuth 1.0a User Context"""
    # Load credentials with correct variable names
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET_KEY')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    
    if not all([api_key, api_secret, access_token, access_token_secret]):
        raise ValueError("Missing required Twitter credentials in .env file")
    
    # Create client with OAuth 1.0a User Context (for posting tweets)
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True
    )
    return client

def post_tweet(text):
    """
    Post a tweet to Twitter
    Args:
        text (str): The text content of the tweet
    Returns:
        dict: Response from Twitter API containing tweet details
    """
    try:
        # Check for placeholder content
        placeholder_patterns = [
            '[Customer Name]', '[Customer Name/Industry]', '[Customer Name/Company]',
            '[Link to Case Study]', '[Industry]', '[Company]'
        ]
        
        for pattern in placeholder_patterns:
            if pattern in text:
                return {
                    "success": False,
                    "error": f"Tweet contains placeholder text: {pattern}. Please replace with actual content."
                }

        # Authenticate with Twitter
        client = authenticate_twitter()
        
        # Post the tweet
        response = client.create_tweet(text=text)
        
        if response and response.data:
            tweet_id = response.data['id']
            tweet_url = f"https://twitter.com/i/web/status/{tweet_id}"
            print(f"Tweet posted successfully! URL: {tweet_url}")
            return {
                "success": True, 
                "tweet_id": tweet_id,
                "tweet_url": tweet_url
            }
        else:
            error_msg = "Failed to post tweet - No response data"
            print(error_msg)
            return {"success": False, "error": error_msg}
            
    except Exception as e:
        print(f"Error posting tweet: {str(e)}")
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    # Example usage
    test_tweet = "This is a test tweet from my Python application!! "
    result = post_tweet(test_tweet)
    print(result)