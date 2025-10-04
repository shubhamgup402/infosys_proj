
from flask import Flask, render_template, request, jsonify
import json
from create_tweet import create_tweet
from post_tweet import post_tweet

app = Flask(__name__)

def get_analyzed_tweets():
    with open("analyzed_tweets.json") as f:
        return json.load(f)

@app.route("/", methods=["GET", "POST"])
def chat():
    user_prompt = None
    result = None
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        analyzed_tweets = get_analyzed_tweets()
        # Pass user prompt to create_tweet
        result = create_tweet(analyzed_tweets, prompt=user_prompt, return_results=True)
    return render_template("chat.html", user_prompt=user_prompt, result=result)

@app.route("/post_tweet", methods=["POST"])
def handle_post_tweet():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No JSON data received"})
            
        tweet_text = data.get('tweet')
        if not tweet_text:
            return jsonify({"success": False, "error": "No tweet text provided"})
        
        # Clean up the tweet text
        tweet_text = tweet_text.strip()
        
        # Validate tweet length (Twitter's limit is 280 characters)
        if len(tweet_text) > 280:
            return jsonify({
                "success": False,
                "error": f"Tweet is too long ({len(tweet_text)} characters). Maximum allowed is 280 characters."
            })
        
        print(f"Attempting to post tweet: {tweet_text}")  # Debug log
        result = post_tweet(tweet_text)
        print(f"Post tweet result: {result}")  # Debug log
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in handle_post_tweet: {str(e)}")  # Debug log
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)