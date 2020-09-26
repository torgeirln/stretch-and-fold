from dataclasses import dataclass


@dataclass
class LevainPct: 
    hydration: float
    ratio: float
    starter_hydration: float


@dataclass
class LevainWeight: 
    total: float
    flour: float
    liquid: float
    starter: float

