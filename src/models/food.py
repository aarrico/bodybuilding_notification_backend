class Food:
    def __init__(
        self,
        id: str,
        protein: float,
        carbs: float,
        fat: float,
        serving_size: float,
        serving_type: str,
    ) -> None:
        self.id: str = id
        self.protein: float = protein / serving_size
        self.carbs: float = carbs / serving_size
        self.fat: float = fat / serving_size
        self.serving_type: str = serving_type

    @staticmethod
    def from_dict(data):
        return Food(
            data["id"],
            data["protein"],
            data["carbs"],
            data["fat"],
            data["servingType"],
        )

    def to_dict(self):
        return {
            "id": self.id,
            "protein": self.protein,
            "carbs": self.carbs,
            "fat": self.fat,
            "servingType": self.serving_type,
        }

    def __repr__(self):
        return f"Food(\
                id={self.id}, \
                protein={self.protein}, \
                carbs={self.carbs}, \
                fat={self.fat}, \
                servingType={self.serving_type}\
            )"
