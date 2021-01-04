from typing import Dict

from flask_restful import Resource, abort


def abort_if_food_doesnt_exist(food_name: str):
    if db.does_resource_exist("food", food_name):
        abort(404, message="{} doesn't exist".format(food_name))


class Food(Resource):
    def __init__(self, data: Dict) -> None:
        self.name: str = data["name"]
        self.protein: float = data["protein"]
        self.carbs: float = data["carbs"]
        self.fat: float = data["fat"]
        self.serving_type: str = data["servingType"]

    @staticmethod
    def from_dict(source):
        return Food(source)

    def to_dict(self):
        return {
            "name": self.name,
            "protein": self.protein,
            "carbs": self.carbs,
            "fat": self.fat,
            "servingType": self.serving_type,
        }

    def __repr__(self):
        return f"Food(\
                name={self.name}, \
                protein={self.protein}, \
                carbs={self.carbs}, \
                fat={self.fat}, \
                servingType={self.serving_type}\
            )"

    def get(self, food_name: str):
        abort_if_food_doesnt_exist(food_name)
        return Food(db.get("food", food_name))

    def delete(self, food_name: str):
        abort_if_food_doesnt_exist(food_name)
        db.delete("food", food_name)
        return "", 204

    def put(self, food_name: str):
        args = parser.parse_args()
        food = {"food": args["food"]}
        db.put("food", food_name)
        return food, 201
