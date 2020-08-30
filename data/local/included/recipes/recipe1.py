from domain.models.ingredient_models import SimpleIngredient
from domain.types.ingredient_types import IngredientTypes


class Recipe1():
    title = 'Sourdough bread v.1'
    description = 'This sourdough bread recipe gives you two delicious breads. \
    The amount of whole grain wheat flour is quite high, which results in a bread with a lot of tang!'
    rel_image_path = 'data/local/included/images/sourdough_bread.jpg'
    ingredients = [
        SimpleIngredient(
            name='Vetemjöl special med fullkorn',
            type_of_ingredient=IngredientTypes.flour,
            amount=569
        ),
        SimpleIngredient(
            name='Grahamsmjöl',
            type_of_ingredient=IngredientTypes.flour,
            amount=244
        ),
        SimpleIngredient(
            name='Vann',
            type_of_ingredient=IngredientTypes.liquid,
            amount=589
        ),
        SimpleIngredient(
            name='Levain',
            type_of_ingredient=IngredientTypes.levain,
            amount=179
        ),
        SimpleIngredient(
            name='Salt',
            type_of_ingredient=IngredientTypes.salt,
            amount=19
        )
    ]
    percentages = {
        'Hydration': 80,
        'Flour2': 30,
        'Salt': 2.3,
        'Levain': 22 
    }
    levain = {
        'Starter': 50,
        'Finmalt rågmjöl': 54,
        'Vatten': 94
    }
    starter_hydration = 175
