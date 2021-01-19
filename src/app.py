import json
import os

from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError

import db
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_user():
    id_token = request.headers["Authorization"]
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token["uid"]
    except ExpiredIdTokenError:
        return jsonify({"error": "ID Token expired."})


@app.route("/food", defaults={"name": None}, methods=["POST"])
@app.route("/food/<name>", methods=["GET"])
def food(name: str):
    uid = get_user()

    if request.method == "GET":
        return jsonify(db.get(collection="food", resource_id=name)), 200

    if db.add(collection="food", resource=request.json):
        return {"success": True}, 201
    else:
        return {"success": False}, 500


@app.errorhandler(ExpiredIdTokenError)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
