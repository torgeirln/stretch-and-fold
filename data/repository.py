from dataclasses import asdict
import json
import os

from domain.models.recipe_models import Recipe


class Repository():
    def __init__(self, new_recipes_path, included_recipes_path):
        self.new_recipes_path = new_recipes_path
        self.included_path = included_recipes_path

    def get_recipes(self):
        print('Fetching recipes')
        all_recipes = []
        all_recipes.extend(self.get_included_recipes())
        all_recipes.extend(self.get_added_recipes())
        return all_recipes

    def get_included_recipes(self):
        included_recipes = []
        for (dirpath, dirnames, filenames) in os.walk(self.included_path):
            for filename in filenames:
                with open(f'{self.included_path}/{filename}', 'r') as recipe:
                    included_recipes.append(
                        Recipe(**json.load(recipe))
                    )
        return included_recipes

    def get_added_recipes(self):
        added_recipes = []
        for (dirpath, dirnames, filenames) in os.walk(self.new_recipes_path):
            for filename in filenames:
                with open(f'{self.new_recipes_path}/{filename}', 'r') as recipe:
                    added_recipes.append(
                        Recipe(**json.load(recipe))
                    )
        return added_recipes

    def save_recipe(self, new_recipe):
        print('Saving recipe')
        # Get ID for new recipe 
        recipe_id = self.get_new_recipe_id(self.new_recipes_path)
        # Convert recipe to dict
        recipe_dict = self.map_recipe_to_dict(new_recipe, recipe_id)
        # Save dict as JSON
        self._save_recipe_dict(recipe_dict, recipe_id)

    def get_new_recipe_id(self, path):
        new_id = 0
        for (_, _, filenames) in os.walk(path):
            if filenames:
                current_ids = [int(filename.split('.json')[0]) for filename in filenames]
                new_id = max(current_ids) + 1
        return new_id
    
    def _save_recipe_dict(self, recipe_dict, recipe_id):
        if not os.path.exists(self.new_recipes_path):
            os.mkdir(self.new_recipes_path)
        with open(f'{self.new_recipes_path}/{recipe_id}.json', 'w') as outfile:
    	    json.dump(recipe_dict, outfile)

    def map_recipe_to_dict(self, new_recipe, recipe_id):
        return asdict(Recipe(recipe_id, **asdict(new_recipe)))
