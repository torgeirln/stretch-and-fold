from domain.models.ingredient_models import SimpleIngredient
from domain.types.ingredient_types import IngredientTypes
from domain.types.recipe_types import RecipeTypes


recipe1 = {
    'recipe_type': RecipeTypes.ingredients_based,
    'title': 'Sourdough bread v.1',
    'description': 'This is a basic sourdough recipe! Its description covers several lines!',
    'rel_image_path': 'data/local/included/images/sourdough_bread.jpg',
    'ingredients': [
        SimpleIngredient(
            name='Vetemjöl special',
            type_of_ingredient=IngredientTypes.flour,
            amount=569
        ),
        SimpleIngredient(
            name='Grahamsmjöl',
            type_of_ingredient=IngredientTypes.flour,
            amount=244
        ),
        SimpleIngredient(
            name='Vatten',
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
    ],
    'levain': {
        'Hydration': 175,
        'Starter': 50,
        'Finmalt rågmjöl': 54,
        'Vatten': 94
    }
}
