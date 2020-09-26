from data.repository import Repository
from domain.constants.paths import included_recipes_path, new_recipes_path
from domain.use_cases.compute_recipe_weights_use_case import ComputeRecipeWeightsUseCase
from domain.use_cases.get_recipes_use_case import GetRecipesUseCase
from domain.use_cases.save_recipe_use_case import SaveRecipeUseCase


class ViewModel():
    def __init__(self):
        self.repository = Repository(
            new_recipes_path,
            included_recipes_path
        )

    def get_recipes(self, callback):
        recipes = GetRecipesUseCase(self.repository).execute()
        callback(recipes)

    def compute_recipe_weights(self, callback, *args):
        ingredient_weights, levain_weights = ComputeRecipeWeightsUseCase().execute(*args)
        callback(ingredient_weights, levain_weights)
        
    def save_recipe(self, callback, recipe):
        save_recipe_response = SaveRecipeUseCase(self.repository).execute(recipe)
        callback(save_recipe_response)
