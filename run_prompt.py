# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


GEMINI_API_KEY="AIzaSyBcEei150JNnNwttiDcWiNqp7jsHVyocXA"

def execute_gemini_for_tweet_creation(prompt, model):
    client = genai.Client(api_key=GEMINI_API_KEY)

    contents = [
        types.Content(
            role="user",
            parts=[ types.Part.from_text(text=prompt) ],
        ),
    ]

    thinking_budget_ms = 512

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=thinking_budget_ms,
        ),
        response_mime_type="application/json",
        response_schema=types.Schema(
            type=types.Type.OBJECT,
            required=["tweet"],
            properties={
                "tweet": types.Schema(type=types.Type.STRING),
                
            },
        ),
    )

    try:
        result = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )
        return result.text  # should be a JSON string that matches the schema
    except genai.errors.ClientError as e:
        # show helpful debugging info
        print("GenAI ClientError:", e)
        raise
    except Exception as e:
        print("Unexpected error calling generate_content:", e)
        raise




def execute_gemini_for_tweet_compare(prompt, model):
    client = genai.Client(api_key=GEMINI_API_KEY)

    contents = [
        types.Content(
            role="user",
            parts=[ types.Part.from_text(text=prompt) ],
        ),
    ]

    thinking_budget_ms = 2000

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=thinking_budget_ms,
        ),
        response_mime_type="application/json",
        response_schema=types.Schema(
            type=types.Type.OBJECT,
            required=["prediction", "explanation"],
            properties={
                "prediction": types.Schema(type=types.Type.STRING),
                "explanation": types.Schema(type=types.Type.STRING),
            },
        ),
    )

    try:
        result = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )
        return result.text  # should be a JSON string that matches the schema
    except genai.errors.ClientError as e:
        # show helpful debugging info
        print("GenAI ClientError:", e)
        raise
    except Exception as e:
        print("Unexpected error calling generate_content:", e)
        raise



def execute_gemini(prompt):
    client = genai.Client(
        api_key=GEMINI_API_KEY,
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content( # user prompt (same as chat input)
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    tools = [
        # types.Tool(googleSearch=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["sentiment_type", "sentiment_score", "topic", "keywords", "target_audience"],
            properties={
                "sentiment_type": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=["angry", "sad", "fearful", "sarcastic", "motivational", "positive", "negative", "excited",
                          "neutral"],
                ),
                "engagement_type": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=["like", "reply", "impression", "retweet"],
                ),
                "sentiment_score": genai.types.Schema(
                    type=genai.types.Type.NUMBER,
                ),
                "topic": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "reason_for_engagement": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "engagement_score": genai.types.Schema(
                    type=genai.types.Type.NUMBER,
                ),
                "keywords": genai.types.Schema(
                    type=genai.types.Type.ARRAY,
                    items=genai.types.Schema(
                        type=genai.types.Type.STRING,
                    ),
                ),
                "target_audience": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
            },
        ),
    )

    result = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return result.text

