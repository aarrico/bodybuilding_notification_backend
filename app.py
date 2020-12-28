import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():

    return ""


@app.route("/food", methods=["GET", "POST"])
def food():
    if request.method == "POST":
        # eventually get/store to firestore
        pass

    food_json = request.json
    return food_json


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
