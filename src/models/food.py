class Food:
    def __init__(
        self,
        name: str,
        protein: float,
        carbs: float,
        fat: float,
        serving_size: float,
        serving_type: str,
    ) -> None:
        self.name: str = name
        self.protein: float = protein / serving_size
        self.carbs: float = carbs / serving_size
        self.fat: float = fat / serving_size
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
