class Food:
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
                protein={self.country}, \
                carbs={self.population}, \
                fat={self.capital}, \
                servingType={self.regions}\
            )"