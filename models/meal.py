from typing import Dict

from firebase_admin import auth
from flask import request

import db


def abort_if_meal_doesnt_exist(meal_id: str):
    if db.does_resource_exist("meal", meal_id):
        abort(404, message="{} doesn't exist".format(meal_id))


class Meal:
    def __init__(self, id: str, foods: Dict, order: int) -> None:
        self.id: str = id
        self.foods: Dict = foods
        self.order: int = order

    @staticmethod
    def from_dict(data):
        return Meal(data["id"], data["foods"], data["order"])

    def to_dict(self):
        return {
            "id": self.name,
            "foods": self.foods,
            "order": self.order,
        }

    def __repr__(self):
        return f"Meal(\
                id={self.name}, \
                foods={self.foods}, \
                order={self.order}, \
            )"


class MealsView:
    def get(self, meal_id: str) -> Meal:
        abort_if_meal_doesnt_exist(meal_id)
        return Meal.from_dict(db.get("meal", meal_id))

    def post(self, meal: Dict) -> None:
        db.add("meal", meal)

    def delete(self, meal_id: str):
        abort_if_meal_doesnt_exist(meal_id)
        db.delete("meal", meal_id)
        return "", 204
