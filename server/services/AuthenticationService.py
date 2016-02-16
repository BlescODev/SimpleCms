from werkzeug.security import safe_str_cmp
from flask_jwt import JWT

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


class AuthenticationService(object):
	def __init__(self, app, key):
		app.config['SECRET_KEY'] = key
		JWT(app, self.authenticate, self.identity)

	@staticmethod
	def authenticate(username, password):
		"""		
		user = username_table.get(username, None)
		if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
			return user
		"""
				

		if username == "simpleAdmin" and password == "tmp":
			return User(1, "simpleAdmin", "tmp")
	@staticmethod
	def identity(payload):
		"""
		user_id = payload['identity']
		return userid_table.get(user_id, None)
		"""
		return User(1, "simpleAdmin", "tmp")
