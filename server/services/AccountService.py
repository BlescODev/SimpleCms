from werkzeug.security import safe_str_cmp

from models.User import User

class AccountService(object):
	def __init__(self, accountSettingsService):
		self.users = list()
		self.add(accountSettingsService.getDefaultAccount())

	def getByName(self, name):		
		for user in self.users:
			if user.name == name:
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
