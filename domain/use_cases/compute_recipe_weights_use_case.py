from domain.utils.dough_utils import bakerspcts2weights


class ComputeRecipeWeightsUseCase():
	def execute(self, *args):
		return bakerspcts2weights(*args)
