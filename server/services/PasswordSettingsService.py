from policies.PasswordPolicy import PasswordPolicy
from policies.SecurityPolicy import SecurityPolicy

from distutils.util import strtobool as toBool

class PasswordSettingsService(object):
	def __init__(self, settingsService):
		self.settingsService = settingsService
		self.saltSizeSetting = "passwordSecuritySaltSize"
		self.roundsSetting = "passwordSecurityRounds"
		self.minLengthSetting = "passwordMinLength"
		self.needsLowercaseSetting = "passwordNeedsLowercase"
		self.needsUppercaseSetting = "passwordNeedsUppercase"
		self.needsNumbersSetting = "passwordNeedsNumbers"
		self.needsSpecialSetting = "passwordNeedsSepcial"


	def getPasswordPolicy(self):
		return PasswordPolicy ( self.getMinLength(), self.getNeedsLowercase(),
				self.getNeedsUppsercase(), self.getNeedsNumbers(), self.getNeedsSpecial() )

	def getSecurityPolicy(self):
		return SecurityPolicy( self.getRounds(), self.getSaltSize() )

	def getSaltSize(self):
		return int(self.settingsService.getSetting( self.saltSizeSetting ))

	def getRounds(self):
		return int(self.settingsService.getSetting( self.roundsSetting ))

	def getMinLength(self):
		return int(self.settingsService.getSetting( self.minLengthSetting ))

	def setMinLength(self, value):
		self.settingsService.setSetting( self.minLengthSetting, value )

	def getNeedsLowercase(self):		
		return toBool(self.settingsService.getSetting ( self.needsLowercaseSetting ))

	def setNeedsLowercase(self, value):
		self.settingsService.getSetting ( self.needsLowercaseSetting, value )

	def getNeedsUppsercase(self):
		return toBool(self.settingsService.getSetting ( self.needsUppercaseSetting ))

	def setNeedsUppercase(self, value):
		self.settingsService.setSetting ( self.needsUppercaseSetting, value )

	def getNeedsNumbers(self):
		return toBool(self.settingsService.getSetting( self.needsNumbersSetting ))

	def setNeedsNumbers(self, value):
		self.settingsService.setSetting( self.needsNumbersSetting , value)

	def getNeedsSpecial(self):
		return toBool(self.settingsService.getSetting ( self.needsSpecialSetting))

	def setNeedsSpecial(self, value):
		self.settingsService.setSetting ( self.needsSpecialSetting, value )
