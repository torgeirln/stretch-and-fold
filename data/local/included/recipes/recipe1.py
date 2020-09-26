# from domain.models.ingredient_models import Ingredient, LevainWeightModel, DesiredResultModel
from domain.models.ingredient_models import Ingredient
from domain.models.levain_models import LevainPct
from domain.models.overview_models import Overview
from domain.types.ingredient_types import IngredientTypes
from domain.constants.paths import rel_image_path


class Recipe1():
    title = 'Sourdough bread v.1'
    description = 'This sourdough bread recipe gives you a delicious bread. \
    The amount of whole grain wheat flour is quite high, which results in a bread with a lot of tang!'
    image_path = rel_image_path
    is_sourdough = True
    ingredients = [
        Ingredient(
            name='Vetemjöl special med fullkorn',
            type_=IngredientTypes.flour,
            amount=80
        ),
        Ingredient(
            name='Grahamsmjöl',
            type_=IngredientTypes.flour,
            amount=20
        ),
        Ingredient(
            name='Vann',
            type_=IngredientTypes.liquid,
            amount=100
        ),
        Ingredient(
            name='Levain',
            type_=IngredientTypes.levain,
            amount=22
        ),
        Ingredient(
            name='Salt',
            type_=IngredientTypes.salt,
            amount=100
        )
    ]
    overview = Overview(
        weight=800, 
        hydration=80, 
        salt=2.3, 
        levain=22
    )
    levain = LevainPct(
        hydration=175,
        ratio=25,
        starter_hydration=175
    )
