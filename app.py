import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

import mbta_helper
from chatbot_helper import get_openai_response

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Home page with a form for MBTA search and chatbot question
    """
    return render_template("index.html")

@app.route("/nearest_mbta", methods=["POST"])
def nearest_mbta():
    """
    Handle MBTA search form submission and show nearest MBTA station
    """
    place_name = request.form.get("place_name")

    if not place_name:
        return "No place name provided.", 400

    stop_name, wheelchair_accessible = mbta_helper.find_stop_near(place_name)

    if stop_name is None:
        return "Could not find a nearby MBTA stop.", 404

    return render_template(
        "mbta_station.html",
        place_name=place_name,
        stop_name=stop_name,
        wheelchair_accessible="Yes" if wheelchair_accessible else "No",
    )

@app.route("/chat", methods=["POST"])
def chat():
    """
    Handle chatbot form submission and display response on the same page
    """
    user_question = request.form.get("user_question")

    if not user_question:
        return "No question provided.", 400

    try:
        answer = get_openai_response(user_question)

        return render_template(
            "index.html",
            chatbot_question=user_question,
            chatbot_answer=answer,
        )

    except Exception as e:
        return f"Error contacting OpenAI: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
