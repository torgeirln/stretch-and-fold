from domain.utils.dough_utils import bakerspcts2weights


class ComputeRecipeWeightsUseCase():
	def execute(self, total_dough_weight, desired_result, ingredients_pct, levain):
		return bakerspcts2weights(total_dough_weight, desired_result, ingredients_pct, levain)
