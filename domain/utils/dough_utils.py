import numpy as np

from domain.models.ingredient_models import Ingredient
from domain.models.levain_models import LevainWeight
from domain.types.ingredient_types import IngredientTypes, LevainTypes


# def bakerspcts2weights(recipe, total_dough_weight):
#     if (recipe.leavening_agents.levain is not None) and (recipe.leavening_agents.yeast is not None):
#         return 0
#     elif recipe.leavening_agents.levain is not None:
#         return bakerspcts2weights_levain(total_dough_weight, recipe.overview, recipe.ingredients, recipe.levain)
#     elif recipe.leavening_agents.yeast is not None:
#         return 2
#     else:
#         raise RuntimeError('No or unknown leavening agent!')

def bakerspcts2weights(total_dough_weight, overview, ingredients, levain, leavening_agents):
    """ Solves Ax=b for x, yielding the ingredients weights in grams. 
        x-vector:
        [tot_flour, tot_liquid, tot_salt, tot_other, tot_yeast, \
        tot_levain, levain_flour, levain_liquid, levain_starter, starter_flour, starter_liquid].T
    """
    ingredients_pct = remove_ingredients_wo_type(ingredients)
    # flour_ingrs, liquid_ingrs, salt_ingrs, other_ingrs, levain_ingrs = group_ingredients(ingredients_pct)
    # n_flour, n_liquid, n_salt, n_other, n_levain, n_yeast = get_ingredient_counts(ingredients_pct)
    print_ingr_counts(ingredients_pct)
    # Total pct of 'other' ingredients
    # tot_other_pct = sum([other.amount/100 for other in other_ingrs])
    tot_other_pct = get_total_of_other(ingredients_pct)
    print(f'tot_other_pct = {tot_other_pct}')
    print(f'levain = {levain}')
    if levain is None:
        # Create b vector
        b = np.hstack((
            total_dough_weight, 0, 0, 0, 0
        )).reshape(-1,1)
        # print(f'b vector = {b}')
        # Create A matrix
        A = create_A_matrix_wo_levain(overview, leavening_agents, tot_other_pct)
    else: # Sourdough recipe
        b = np.hstack((
            total_dough_weight, 0, 0, 0, 0, np.zeros(6)
        )).reshape(-1,1)
        A = create_A_matrix_with_levain(overview, leavening_agents, levain, tot_other_pct)

    # Solve for x
    x = np.linalg.inv(A) @ b
    print(x)
    # Find weights of individual ingredients
    ingredients_weights = []
    # other_ind = 0
    for ingredient in ingredients_pct:
        if ingredient.type_ == IngredientTypes.flour:
            new_ingredient = Ingredient(
                ingredient.name, 
                ingredient.type_,
                ingredient.amount/100 * x[0,0]
            )
        elif ingredient.type_ == IngredientTypes.liquid:
            new_ingredient = Ingredient(
                ingredient.name, 
                ingredient.type_,
                ingredient.amount/100 * x[1,0]
            )
        elif ingredient.type_ == IngredientTypes.salt:
            new_ingredient = Ingredient(
                ingredient.name, 
                ingredient.type_,
                ingredient.amount/100 * x[2,0]
            )
        elif ingredient.type_ == IngredientTypes.other:
            new_ingredient = Ingredient(
                ingredient.name, 
                ingredient.type_,
                (ingredient.amount/100)/tot_other_pct * x[3,0]
            )
            # other_ind += 1
        elif ingredient.type_ == IngredientTypes.yeast:
            new_ingredient = Ingredient(
                ingredient.name, 
                ingredient.type_,
                x[4,0]
            )
        elif ingredient.type_ == IngredientTypes.levain:
            new_ingredient = Ingredient(
                ingredient.name, 
                ingredient.type_,
                x[5,0]
            )
        ingredients_weights.append(new_ingredient)
    if levain is not None:
        levain_weights = LevainWeight(
            total=x[5,0], 
            flour=x[6,0], 
            liquid=x[7,0], 
            starter=x[8,0]
        )
    else:
        levain_weights = None
    return ingredients_weights, levain_weights

def create_A_matrix_wo_levain(overview, leavening_agents, tot_other_pct):
    hyd_pct, salt_pct = overview.hydration/100, overview.salt/100
    yeast_pct = leavening_agents.yeast/100
    print(f'yeast_pct = {yeast_pct}')
    # Total dough weight
    row_tot = np.hstack((
        1, 1, 1, 1, 1
    ))
    # Total hydration
    row_hydration = np.hstack((
        -hyd_pct, 1, 0, 0, 0
    ))
    # Total amount of salt
    row_salt = np.hstack((
        -salt_pct, 0, 1, 0, 0
    ))
    # Other ingredients
    row_other = np.hstack((
        -tot_other_pct, 0, 0, 1, 0
    ))
    # Yeast
    row_yeast = np.hstack((
        -yeast_pct, 0, 0, 0, 1
    ))
    A = np.vstack((
        row_tot, row_hydration, row_salt, row_other, row_yeast
    ))
    return A

def create_A_matrix_with_levain(overview, leavening_agents, levain, tot_other_pct):
    # hyd_pct, salt_pct, levain_pct = get_desired_result_pcts(overview)
    hyd_pct, salt_pct = overview.hydration/100, overview.salt/100
    levain_pct, yeast_pct = leavening_agents.levain/100, leavening_agents.yeast/100
    print(f'levain_pct = {levain_pct}')
    print(f'yeast_pct = {yeast_pct}')
    levain_hyd, levain_ratio, levain_starter_hyd = get_levain_pcts(levain)
    print(f'levain_hyd = {levain_hyd}')
    print(f'levain_ratio = {levain_ratio}')
    print(f'levain_starter_hyd = {levain_starter_hyd}')
    # Total dough weight
    row_tot = np.hstack((
        1, 1, 1, 1, 1, \
        1, 0, 0, 0, 0, 0
    ))
    # Total hydration
    row_hydration = np.hstack((
        -hyd_pct, 1, 0, 0, 0, \
        0, -hyd_pct, 1, 0, -hyd_pct, 1
    ))
    # Total amount of salt
    row_salt = np.hstack((
        -salt_pct, 0, 1, 0, 0, \
        0, -salt_pct, 0, 0, -salt_pct, 0
    ))
    # Other ingredients
    row_other = np.hstack((
        -tot_other_pct, 0, 0, 1, 0, \
        0, -tot_other_pct, 0, 0, -tot_other_pct, 0
    ))
    # Yeast
    row_yeast = np.hstack((
        -yeast_pct, 0, 0, 0, 1, \
        0, -yeast_pct, 0, 0, -yeast_pct, 0
    ))
    # Levain rows
    # - Total levain
    row_total_levain = np.hstack((
        -levain_pct, 0, 0, 0, 0, \
        1, -levain_pct, 0, 0, -levain_pct, 0 
    ))
    # - Flour
    row_levain_flour = np.hstack((
        0, 0, 0, 0, 0, \
        -(1-levain_ratio), 1, 1, 0, 0, 0 
    ))
    # - Liquid
    row_levain_liquid = np.hstack((
        0, 0, 0, 0, 0, \
        0, -levain_hyd, 1, 0, -levain_hyd, 1
    ))
    # - Starter
    row_levain_starter = np.hstack((
        0, 0, 0, 0, 0, \
        -levain_ratio, 0, 0, 1, 0, 0 
    ))
    # - Starter, flour
    row_starter_flour = np.hstack((
        0, 0, 0, 0, 0, \
        0, 0, 0, -1/(1+levain_starter_hyd), 1, 0 
    ))
    # - Starter, liquid
    row_starter_liquid = np.hstack((
        0, 0, 0, 0, 0, \
        0, 0, 0, -1/(1+1/(levain_starter_hyd)), 0, 1 
    ))

    A = np.vstack((
        row_tot, row_hydration, row_salt, row_other, row_yeast, \
        row_total_levain, row_levain_flour, row_levain_liquid, \
        row_levain_starter, row_starter_flour, row_starter_liquid
    ))
    return A

def remove_ingredients_wo_type(ingredients):
    ingredients_w_type = []
    for ingredient in ingredients:
        if ingredient.type_ in IngredientTypes.all_types:
            ingredients_w_type.append(ingredient)
    return ingredients_w_type

def get_levain_pcts(levain):
    if levain is not None:
        return levain.hydration/100, levain.ratio/100, levain.starter_hydration/100
    else:
        return 0, 0, 0

def get_total_of_other(ingredients):
    other_ingrs = []
    for ingredient in ingredients:
        if ingredient.type_ == IngredientTypes.other:
            other_ingrs.append(ingredient)
    return sum([other.amount/100 for other in other_ingrs])


def get_ingredient_counts(ingredients_pct):
    n_yeast = 0
    for ingr in ingredients_pct:
        if ingr.type_ == IngredientTypes.yeast:
            n_yeast += 1

    n_levain = 0
    for ingr in ingredients_pct:
        if ingr.type_ == IngredientTypes.levain:
            n_levain += 1
    
    n_flour = 0
    for ingr in ingredients_pct:
        if ingr.type_ == IngredientTypes.flour:
            n_flour += 1
    
    n_liquid = 0
    for ingr in ingredients_pct:
        if ingr.type_ == IngredientTypes.liquid:
            n_liquid += 1

    n_salt = 0
    for ingr in ingredients_pct:
        if ingr.type_ == IngredientTypes.salt:
            n_salt += 1
    
    n_other = 0
    for ingr in ingredients_pct:
        if ingr.type_ == IngredientTypes.other:
            n_other += 1

    return n_flour, n_liquid, n_salt, n_other, n_levain, n_yeast

def print_ingr_counts(ingredients):
    n_flour, n_liquid, n_salt, n_other, n_levain, n_yeast = get_ingredient_counts(ingredients)
    print(f'n_flour: {n_flour}')
    print(f'n_liquid: {n_liquid}')
    print(f'n_salt: {n_salt}')
    print(f'n_other: {n_other}')
    print(f'n_levain: {n_levain}')
    print(f'n_yeast: {n_yeast}')


# def get_desired_result_pcts(overview):
#     return overview.hydration/100, overview.salt/100, overview.levain/100
    
# def group_ingredients(ingredients_pct):
#     flour_ingrs = []
#     for ingr in ingredients_pct:
#         if ingr.type_ == IngredientTypes.flour:
#             flour_ingrs.append(ingr)
    
#     liquid_ingrs = []
#     for ingr in ingredients_pct:
#         if ingr.type_ == IngredientTypes.liquid:
#             liquid_ingrs.append(ingr)

#     salt_ingrs = []
#     for ingr in ingredients_pct:
#         if ingr.type_ == IngredientTypes.salt:
#             salt_ingrs.append(ingr)
    
#     other_ingrs = []
#     for ingr in ingredients_pct:
#         if ingr.type_ == IngredientTypes.other:
#             other_ingrs.append(ingr)

#     levain_ingrs = []
#     for ingr in ingredients_pct:
#         if ingr.type_ == IngredientTypes.levain:
#             levain_ingrs.append(ingr)
    
#     yeast_ingrs = []
#     for ingr in ingredients_pct:
#         if ingr.type_ == IngredientTypes.yeast:
#             yeast_ingrs.append(ingr)

#     return flour_ingrs, liquid_ingrs, salt_ingrs, other_ingrs, levain_ingrs