

class ResponseStates():
	successful = 'successful'
	error = 'error'


class SaveRecipeResponse():
	def __init__(self, state, message=None):
		self.state = state
		self.message = message
	