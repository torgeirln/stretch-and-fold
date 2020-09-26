import time

from data.repository import Repository
from domain.models.ingredient_models import Ingredient
from domain.models.levain_models import LevainPct
from domain.models.overview_models import Overview
from domain.models.recipe_models import NewRecipe
from domain.types.ingredient_types import IngredientTypes

out_path = 'tests/__out__/save_recipe'

test_recipe_object_ingredients = [
	Ingredient(name='Ingredient 1', type_='Type 1', amount=80),
	Ingredient(name='Ingredient 2', type_='Type 2', amount=20),
	Ingredient(name='Ingredient 3', type_='Type 3', amount=100),
	Ingredient(name='Ingredient 4', type_='Type 4', amount=100)
]
test_recipe_object_levain = LevainPct(
	hydration=80, ratio=20, starter_hydration=175
)
test_recipe_object_overview = Overview(
	weight=700, hydration=80, salt=2.3, levain=20
)
test_recipe_object_1 = NewRecipe(
	title = 'test_recipe_object Title',
	description = 'test_recipe_object description',
	image_path = 'test_recipe_object image_path',
	is_sourdough=True,
	ingredients=test_recipe_object_ingredients,
	levain=test_recipe_object_levain,
	overview=test_recipe_object_overview
)
test_recipe_object_2 = NewRecipe(
	title = 'test_recipe_object_2 Title',
	description = 'test_recipe_object_2 description',
	image_path = 'test_recipe_object_2 image_path',
	is_sourdough=True,
	ingredients=test_recipe_object_ingredients,
	levain=None,
	overview=test_recipe_object_overview
)

new_recipes_path = f'{out_path}/new_recipes'
included_recipes_path = ''
repository = Repository(new_recipes_path, included_recipes_path)

def get_new_recipe_id_test_1():
	test1_path = f'{out_path}/get_id/test1'
	recipe_id = repository.get_new_recipe_id(test1_path)
	assert recipe_id == 0, 'An empty recipe folder should yield a recipe_id = 0'

def get_new_recipe_id_test_2():
	test2_path = f'{out_path}/get_id/test2'
	recipe_id = repository.get_new_recipe_id(test2_path)
	assert recipe_id == 2, 'A recipe folder with 2 recipes should yield a new recipe_id = 2'

def map_object_to_dict_test_1():
	recipe_dict = repository.map_recipe_to_dict(test_recipe_object_1, 0)
	assert recipe_dict['title'] == test_recipe_object_1.title, 'Wrong recipe title'
	assert recipe_dict['description'] == test_recipe_object_1.description, 'Wrong recipe description'
	assert len(recipe_dict['ingredients']) == len(test_recipe_object_ingredients), 'Number of ingredients do not match'
	assert recipe_dict['levain']['hydration'] == test_recipe_object_1.levain.hydration, 'Wrong levain hydration'
	assert recipe_dict['overview']['hydration'] == test_recipe_object_1.overview.hydration, 'Wrong overview hydration'
	
def map_object_to_dict_test_2():
	recipe_dict = repository.map_recipe_to_dict(test_recipe_object_2, 0)
	assert recipe_dict['title'] == test_recipe_object_2.title, 'Wrong recipe title'
	assert recipe_dict['description'] == test_recipe_object_2.description, 'Wrong recipe description'
	assert len(recipe_dict['ingredients']) == len(test_recipe_object_ingredients), 'Number of ingredients do not match'
	assert recipe_dict['levain'] == test_recipe_object_2.levain, 'Levain should be None'
	assert recipe_dict['overview']['hydration'] == test_recipe_object_2.overview.hydration, 'Wrong overview hydration'
		
def run_tests():
	print('- Running save_recipe_tests')
	tests = [get_new_recipe_id_test_1, get_new_recipe_id_test_2, map_object_to_dict_test_1, map_object_to_dict_test_2]

	for test in tests:
		try:
			test()
			print(f'-- {test.__name__} PASSED!')
		except Exception as e:
			print(f'-- {test.__name__} FAILED! {e}')

if __name__ == "__main__":
	run_tests()
