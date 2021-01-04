import db

from flask_classful import FlaskView


def abort_if_food_doesnt_exist(food_name: str):
    if db.does_resource_exist("food", food_name):
        abort(404, message="{} doesn't exist".format(food_name))


class Food:
    def __init__(
        self, name: str, protein: float, carbs: float, fat: float, serving_type: str
    ) -> None:
        self.name: str = name
        self.protein: float = protein
        self.carbs: float = carbs
        self.fat: float = fat
        self.serving_type: str = serving_type

    @staticmethod
    def from_dict(data):
        return Food(
            data["name"],
            data["protein"],
            data["carbs"],
            data["fat"],
            data["servingType"],
        )

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


class FoodView(FlaskView):
    def index(self):
        return db.get_all("food")

    def get(self, name: str):
        abort_if_food_doesnt_exist(name)
        return Food.from_dict(db.get("food", name))

    def delete(self, name: str):
        abort_if_food_doesnt_exist(name)
        db.delete("food", name)
        return "", 204

    def post(self, food: Food):
        db.add(collection="food", resource=food.to_dict())
        return 201
