from dataclasses import dataclass
from typing import List

from domain.models.ingredient_models import Ingredient
from domain.models.levain_models import LevainPct
from domain.models.overview_models import Overview


@dataclass
class Recipe:
    """ Model for saved recipe. Has an id. """
    __id__: int
    title: str
    description: str
    image_path: str
    is_sourdough: bool
    ingredients: List[Ingredient]
    levain: LevainPct
    overview: Overview

    def __post_init__(self):
        """ Used to map inner data classes from dicts to a 
            dataclass instance when loading a saved recipe. """
        if self.ingredients and isinstance(self.ingredients[0], dict):
            self.ingredients = [Ingredient(**ingredient) for ingredient in self.ingredients]
        if isinstance(self.levain, dict):
            self.levain = LevainPct(**self.levain)
        if isinstance(self.overview, dict):
            self.overview = Overview(**self.overview)


@dataclass
class NewRecipe:
    """ Model for new recipes. Has no id. """
    title: str
    description: str
    image_path: str
    is_sourdough: bool
    ingredients: List[Ingredient]
    levain: LevainPct
    overview: Overview
