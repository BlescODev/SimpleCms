from models.User import User
from models.Password import Password

class AccountSettingsService(object):
	def __init__(self, settingsService, passwordSettingsService):
		self.settingsService = settingsService
		self.passwordSettingsService = passwordSettingsService

	def getDefaultAccount(self):
		username = self.settingsService.getSetting( "defaultUserName" )
		password = self.settingsService.getSetting( "defaultUserPassword" )
		return User(1, username, Password( password, self.passwordSettingsService ))
