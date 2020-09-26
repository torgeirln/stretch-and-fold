from dataclasses import dataclass


@dataclass
class Overview:
    weight: float
    hydration: float
    salt: float
    levain: float # Change to the more general 'leavening agent' as to include e.g. yeast?
