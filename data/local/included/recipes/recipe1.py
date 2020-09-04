from domain.models.ingredient_models import IngredientModel, LevainWeightModel, DesiredResultModel
from domain.types.ingredient_types import IngredientTypes
from domain.constants.paths import rel_image_path


class Recipe1():
    title = 'Sourdough bread v.1'
    description = 'This sourdough bread recipe gives you a delicious bread. \
    The amount of whole grain wheat flour is quite high, which results in a bread with a lot of tang!'
    rel_image_path = rel_image_path
    ingredients = [
        IngredientModel(
            name='Vetemjöl special med fullkorn',
            type_=IngredientTypes.flour,
            amount=80
        ),
        IngredientModel(
            name='Grahamsmjöl',
            type_=IngredientTypes.flour,
            amount=20
        ),
        IngredientModel(
            name='Vann',
            type_=IngredientTypes.liquid,
            amount=100
        ),
        IngredientModel(
            name='Levain',
            type_=IngredientTypes.levain,
            amount=22
        ),
        IngredientModel(
            name='Salt',
            type_=IngredientTypes.salt,
            amount=100
        )
    ]
    desired_result = DesiredResultModel(
        weight=800, 
        hydration=80, 
        salt=2.3, 
        levain=22
    )
    # percentages = {
    #     'Hydration': 80,
    #     'Flour2': 30,
    #     'Salt': 2.3,
    #     'Levain': 22 
    # }
    # levain = {
    #     'Starter': 50,
    #     'Finmalt rågmjöl': 54,
    #     'Vatten': 94
    # }
    # starter_hydration = 175
    levain = LevainWeightModel(
        total=97,
        flour=26,
        liquid=46,
        starter=24
    )
