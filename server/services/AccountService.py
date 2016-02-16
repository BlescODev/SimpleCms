from werkzeug.security import safe_str_cmp

from models.User import User

class AccountService(object):
	def __init__(self, defaultConfigRepository, configRepository):
		self.defaultConfigRepository = defaultConfigRepository 
		self.configRepository = configRepository
		self.users = {User(1, "simpleAdmin", "ThisIsAnInsecurePassword;ItMustBeReplaced")}

	def getByName(self, name):		
		for user in self.users:
			if(safe_str_cmp(user.name.encode('utf-8'), name.encode('utf-8')) ):
				return user
		return None

	def add(self, user):
		self.users.append(user)

	def remove(self, user_id):
		for user in self.users:
			if(user.id == user_id ):
				self.users.remove(user)
				return

	def update(self, user):
		pass

	def getPasswordPolicy(self):
		"""
		We want our CMS to be as customizable as possible.
		We want our CMS to be as secure as possible.
		"""

