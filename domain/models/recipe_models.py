from dataclasses import dataclass
from typing import List

from domain.models.dough_size_models import DoughSize
from domain.models.ingredient_models import Ingredient, LeaveningAgents
from domain.models.levain_models import LevainPct
from domain.models.overview_models import Overview


@dataclass
class Recipe:
    """ Model for saved recipe. Has an id. """
    __id__: int
    title: str
    category: str
    description: str
    image_path: str
    is_sourdough: bool
    ingredients: List[Ingredient]
    levain: LevainPct
    overview: Overview
    dough_size: DoughSize
    leavening_agents: LeaveningAgents

    def __post_init__(self):
        """ Used to map inner data classes from dicts to a 
            dataclass instance when loading a saved recipe. """
        if self.ingredients and isinstance(self.ingredients[0], dict):
            self.ingredients = [Ingredient(**ingredient) for ingredient in self.ingredients]
        if isinstance(self.levain, dict):
            self.levain = LevainPct(**self.levain)
        if isinstance(self.overview, dict):
            self.overview = Overview(**self.overview)
        if isinstance(self.dough_size, dict):
            self.dough_size = DoughSize(**self.dough_size)
        if isinstance(self.leavening_agents, dict):
            self.leavening_agents = LeaveningAgents(**self.leavening_agents)


@dataclass
class NewRecipe:
    """ Model for new recipes. Has no id. """
    title: str
    category: str
    description: str
    image_path: str
    is_sourdough: bool
    ingredients: List[Ingredient]
    levain: LevainPct
    overview: Overview
    dough_size: DoughSize
    leavening_agents: LeaveningAgents
