from models import Food
import os

from flask import Flask, request

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)


# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(
    cred,
    {
        "projectId": "bodybuilding-notification-app",
    },
)

db = firestore.client()


@app.route("/")
def index():

    return ""


@app.route("/food", methods=["GET", "POST"])
def food():
    if request.method == "POST":
        food = Food(request.json)
        doc_ref = db.collection(u"foods").document(food.name).set(food.to_dict())

    food_json = request.json
    return food_json


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
