import os

import openai
from flask import Flask, redirect, render_template, request, url_for
#from modeltest import form

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(question),
            max_tokens=256,
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text.strip().split("\n")
))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(question):
    return """give the correct translation of a japanese kanji if wrong. if correct say correct.

    Question: 人 person
    Answer: Correct

    Question: 女 man
    Answer: Incorrect. Correct answer is woman

    Question: 日は大きいです The sun is big
    Answer: Correct

    Question: What is the kanji for "eye"?  What is the tanslation of "I eat sushi" in japanese? 私はすしを食べる
    Answer: Incorrect. Correct answer is 目


Question: {}
Answer:""".format(
        question.capitalize()
    )




# @app.route("/form")
# def forms():
#     return redirect(form())

