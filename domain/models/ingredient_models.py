from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    type_: str
    amount: float


@dataclass
class LeaveningAgents:
    levain: float
    yeast: float
