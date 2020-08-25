from domain.models.ingredient_models import SimpleIngredient
from domain.types.ingredient_types import IngredientTypes


class Recipe1():
    description = 'This is a basic sourdough recipe!'
    ingredients = [
        SimpleIngredient(
            name='Vetemjöl special',
            type_of_ingredient=IngredientTypes.flour,
            amount=90
        ),
        SimpleIngredient(
            name='Grahamsmjöl',
            type_of_ingredient=IngredientTypes.flour,
            amount=20
        ),
        SimpleIngredient(
            name='Vatten',
            type_of_ingredient=IngredientTypes.liquid,
            amount=80
        ),
        SimpleIngredient(
            name='Levain',
            type_of_ingredient=IngredientTypes.levain,
            amount=20
        ),
        SimpleIngredient(
            name='Salt',
            type_of_ingredient=IngredientTypes.salt,
            amount=2
        )
    ]
