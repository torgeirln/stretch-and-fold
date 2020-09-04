

class DesiredResultModel():
    def __init__(self, weight, hydration, salt, levain):
        self.weight = weight
        self.hydration = hydration
        self.salt = salt
        self.levain = levain


class IngredientModel():
    """ Used for ingredients with an amount given as either weight or percentage. """
    def __init__(self, name, type_, amount):
        self.name = name
        self.type = type_
        self.amount = amount


class LevainPctModel():
    def __init__(self, hydration, ratio, starter_hydration):
        self.hydration = hydration
        self.ratio = ratio
        self.starter_hydration = starter_hydration


class LevainWeightModel():
    def __init__(self, total, flour, liquid, starter):
        self.total = total
        self.flour = flour
        self.liquid = liquid
        self.starter = starter

