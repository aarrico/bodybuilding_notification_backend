from src.models.food import Food
import math


def test_new_food():
    """
    GIVEN a Food model
    WHEN a new food is created
    THEN check the name, protein, carbs, fat, serving_type fields are defined correctly
    """
    food = Food(
        name="chicken",
        protein=53.4,
        carbs=0,
        fat=6.2,
        serving_size=172,
        serving_type="gram",
    )
    assert math.isclose(food.protein, 0.3104651162790698)
    assert math.isclose(food.carbs, 0)
    assert math.isclose(food.fat, 0.036046511627907)
    assert food.serving_type == "gram"
    assert food.name == "chicken"
