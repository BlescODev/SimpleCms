from flask_jwt import JWT

class AuthenticationService(object):
	def __init__(self, app, accountService, key):
		app.config['SECRET_KEY'] = key
		self.accountService = accountService
		JWT(app, self.authenticate, self.identity)

	def authenticate(self, name, password):
		user = self.accountService.getByName(name)
		if user.password.verify(password):
			return user
		return None

	def identity(self, payload):
		id = payload['identity']
		return self.accountService.get(id)
