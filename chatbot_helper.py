import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_openai_response(user_prompt):
    """
    Connects to OpenAI API and returns a response based on user prompt.
    """
    client = OpenAI()

    system_prompt = (
        "You are a friendly Boston tourist guide, specifically aiding in MBTA station location. "
        "Answer questions about famous places, activities, history, food, and travel tips in Boston."
    )

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return completion.choices[0].message.content
