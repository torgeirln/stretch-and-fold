from domain.models.response_models import SaveRecipeResponse, ResponseStates


class SaveRecipeUseCase():
	def __init__(self, repository):
		self.repository = repository
	
	def execute(self, recipe):
		try:
			self.repository.save_recipe(recipe)
			return SaveRecipeResponse(ResponseStates.successful)
		except Exception as e:
			return SaveRecipeResponse(
				ResponseStates.error, 
				e
			)
	