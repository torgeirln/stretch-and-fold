from data.repository import Repository
from domain.use_cases.get_recipes_use_case import GetRecipesUseCase

class ViewModel():
    def __init__(self):
        self.repository = Repository()

    def get_recipes(self, callback):
        recipes = GetRecipesUseCase(self.repository).execute()
        callback(recipes)
