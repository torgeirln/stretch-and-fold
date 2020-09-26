from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    type_: str
    amount: float
