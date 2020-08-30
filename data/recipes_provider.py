from data.local.included.recipes.recipe1 import Recipe1
from data.local.included.recipes.recipe2 import Recipe2
from data.local.included.recipes.recipe3 import Recipe3
from data.local.included.recipes.recipe4 import Recipe4
from data.local.included.recipes.recipe5 import Recipe5


class RecipesProvider():
    @staticmethod
    def get_included_recipes():
        return [Recipe1(), Recipe2(), Recipe3(), Recipe4(), Recipe5()]
