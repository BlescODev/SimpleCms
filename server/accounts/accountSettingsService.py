from .user import User
from .password import Password

class AccountSettingsService(object):
	def __init__(self, settingsService, passwordSettingsService):
		self.settingsService = settingsService
		self.passwordSettingsService = passwordSettingsService

		self.ACCOUNT_NAME_SETTING = "accountName"
		self.ACCOUNT_PASSWORD_SETTING = "accountPassword"

	def getAccount(self):
		username = self.settingsService.getSetting( self.ACCOUNT_NAME_SETTING )
		password = self.settingsService.getSetting( self.ACCOUNT_PASSWORD_SETTING )
		return User(1, username, Password( password, self.passwordSettingsService ))

	def setAccount(self, account):
		self.settingsService.setSetting( self.ACCOUNT_NAME_SETTING, account.name )
		self.settingsService.setSetting( self.ACCOUNT_PASSWORD_SETTING, account.password )

