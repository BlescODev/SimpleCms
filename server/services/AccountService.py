from werkzeug.security import safe_str_cmp

from models.User import User

class AccountService(object):
	def __init__(self, accountSettingsService):
		self.accounts = list()
		self.accountSettingsService = accountSettingsService
		self.add(self.accountSettingsService.getAccount())

	def get(self, id):
		for account in self.accounts:
			if account.id == id:
				return account
		return None

	def getByName(self, name):		
		for account in self.accounts:
			if account.name == name:
				return account
		return None

	def add(self, account):
		self.accounts.append(account)

	def remove(self, id):
		for account in self.accounts:
			if account.id == id:
				self.accounts.remove(account)
				return

	def update(self, account):
		self.accountSettingsService.setAccount(account)
