
from flask import Flask, render_template, request
import json
from create_tweet import create_tweet

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

if __name__ == "__main__":
    app.run(debug=True)