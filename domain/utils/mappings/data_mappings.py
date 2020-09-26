from domain.models.ingredient_models import IngredientKeys
from domain.models.levain_models import LevainPctKeys
from domain.models.overview_models import OverviewKeys
from domain.models.recipe_models import RecipeKeys


def map_object_to_dict(recipe):
        recipe_dict = {}
        recipe_dict[RecipeKeys.title] = recipe.title
        recipe_dict[RecipeKeys.description] = recipe.description
        recipe_dict[RecipeKeys.image_path] = recipe.image_path
        ingredients_dict = {}
        for i, ingredient in enumerate(recipe.ingredients):
            ingredients_dict[i] = {
                IngredientKeys.name: ingredient.name,
                IngredientKeys.type_: ingredient.type,
                IngredientKeys.amount: ingredient.amount
            }
        recipe_dict[RecipeKeys.ingredients] = ingredients_dict
        if recipe.levain is not None:
            levain_dict = {}
            levain_dict[LevainPctKeys.hydration] = recipe.levain.hydration
            levain_dict[LevainPctKeys.ratio] = recipe.levain.ratio
            levain_dict[LevainPctKeys.starter_hydration] = recipe.levain.starter_hydration
            recipe_dict[RecipeKeys.levain] = levain_dict
        else:
            recipe_dict[RecipeKeys.levain] = None
        overview_dict = {}
        overview_dict[OverviewKeys.weight] = recipe.overview.weight
        overview_dict[OverviewKeys.hydration] = recipe.overview.hydration
        overview_dict[OverviewKeys.salt] = recipe.overview.salt
        overview_dict[OverviewKeys.levain] = recipe.overview.levain
        recipe_dict[RecipeKeys.overview] = overview_dict
        return recipe_dict

def map_dict_to_object(recipe_dict):
	print('map_dict_to_object not implemented')
