from werkzeug.security import safe_str_cmp

from models.User import User

class AccountService(object):
	def __init__(self, accountSettingsService):
		self.users = list()
		self.add(accountSettingsService.getDefaultAccount())

	def get(self, id):
		for user in self.users:
			if user.id == id:
				return user
		return None

	def getByName(self, name):		
		for user in self.users:
			if user.name == name:
				return user
		return None

	def add(self, user):
		self.users.append(user)

	def remove(self, id):
		for user in self.users:
			if user.id == id:
				self.users.remove(user)
				return

	def update(self, user):
		pass
