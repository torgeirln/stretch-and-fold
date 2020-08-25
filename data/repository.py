from data.local.recipes.recipes_provider import RecipesProvider


class Repository():
    def get_recipes(self):
        print('Fetching recipes')
        return RecipesProvider.get_included_recipes()

