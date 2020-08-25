from data.local.recipes.included.recipe1 import Recipe1
from data.local.recipes.included.recipe2 import Recipe2


class RecipesProvider():
    @staticmethod
    def get_included_recipes():
        return [Recipe1(), Recipe2()]
