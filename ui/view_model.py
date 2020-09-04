from data.repository import Repository
from domain.use_cases.get_recipes_use_case import GetRecipesUseCase
from domain.use_cases.compute_recipe_weights_use_case import ComputeRecipeWeightsUseCase


class ViewModel():
    def __init__(self):
        self.repository = Repository()

    def get_recipes(self, callback):
        recipes = GetRecipesUseCase(self.repository).execute()
        callback(recipes)

    def compute_recipe_weights(self, callback, *args):
        ingredient_weights, levain_weights = ComputeRecipeWeightsUseCase().execute(*args)
        callback(ingredient_weights, levain_weights)
        