from DocumentSimilarity import DocumentSimilarity as docSim
from flask import Flask, redirect, url_for, render_template, request, jsonify
import math

app = Flask(__name__)


result = -1
text_one = ""
text_two = ""
docSim_Obj = docSim()


@app.route("/", methods=["POST", "GET", "DELETE"])
def homepage():
    """Handles requests to get text inputs from webpage and
    calculates similarity score and appropriately redirects user"""
    if request.method == "POST":
        text_one = request.form["text_one"]
        text_two = request.form["text_two"]
        print("T1: ", text_one, " T2: ", text_two)

        result = docSim_Obj.similarity_score(text_one, text_two)
        return render_template(
            "output.html", result=result, text_one=text_one, text_two=text_two
        )
    else:
        return render_template("index.html")


@app.route("/api/similarity", methods=["POST"])
def similarity_api():
    """Provides an API endpoint to get text inputs from a json body
    and returns similarity score in JSON fromat"""
    if request.method == "POST":

        data = request.get_json()

        text_one = data["text_one"]
        text_two = data["text_two"]

        result = docSim_Obj.similarity_score(text_one, text_two)

        return jsonify({"similarity_score": result})


if __name__ == "__main__":
    app.run(debug=True)