import json
import os

from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError

import db
from flask import Flask, request, jsonify

from src.models.food import Food

app = Flask(__name__)


def get_user():
    id_token = request.headers["Authorization"]
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token["uid"]
    except ExpiredIdTokenError:
        return jsonify({"error": "ID Token expired."})


@app.route("/foods", methods=["POST"])
def add_food():
    data = request.json
    food = Food(data["id"], data["protein"], data["carbs"], data["fat"], data["servingSize"], data["servingType"])
    if db.add(collection="foods", resource=food.to_dict()):
        return {"success": True}, 201
    else:
        return {"success": False}, 500


@app.route("/foods", methods=["GET"])
def food(name: str):
    #uid = get_user()
    name = request.args.get('name')
    if name:
        food = db.get(collection="foods", resource_id=name)
        if food:
            return jsonify(food), 200
        return jsonify({"error:", f"{name} not found in database"}), 404
    else:
        return jsonify(db.get_all("foods")), 200


@app.errorhandler(ExpiredIdTokenError)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.id,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
