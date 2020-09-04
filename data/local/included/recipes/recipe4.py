from domain.models.ingredient_models import IngredientModel, LevainWeightModel
from domain.types.ingredient_types import IngredientTypes


class Recipe4():
    title = 'Sourdough bread v.1'
    description = 'This is another basic sourdough recipe!'
    rel_image_path = 'data/local/included/images/sourdough_bread.jpg'
    ingredients = [
        IngredientModel(
            name='Vetemjöl special med fullkorn',
            type_=IngredientTypes.flour,
            amount=90
        ),
        IngredientModel(
            name='Grahamsmjöl',
            type_=IngredientTypes.flour,
            amount=20
        ),
        IngredientModel(
            name='Vatten',
            type_=IngredientTypes.liquid,
            amount=80
        ),
        IngredientModel(
            name='Levain',
            type_=IngredientTypes.levain,
            amount=20
        ),
        IngredientModel(
            name='Salt',
            type_=IngredientTypes.salt,
            amount=2
        )
    ]
    levain = LevainWeightModel(
        total=97,
        flour=26,
        liquid=46,
        starter=24
    )
