from src.models.food import Food
from typing import Dict

from firebase_admin import auth
from flask import request


class Meal:
    def __init__(self, id: str, foods: Dict, order: int) -> None:
        self.id: str = id
        self.foods: Dict = foods
        self.order: int = order

    def add_food(self, food: Food, amount: float) -> None:
        if food.id not in self.foods:
            self.foods[food.id] = amount
        else:
            self.foods[food.id] += amount

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
