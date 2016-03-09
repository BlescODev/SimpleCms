class GeneralSettingsService(object):
	def __init__(self, settingsService):
		self.settingsService = settingsService
		self.HOST_NAME_SETTING = "hostName"
		self.PORT_SETTING = "port"
		self.START_PAGE_SETTING = "startPage"
	
	def get(self):
		generalSettings = dict()
		generalSettings[self.HOST_NAME_SETTING] = self.getHostName()
		generalSettings[self.PORT_SETTING] = self.getPort()
		generalSettings[self.START_PAGE_SETTING] = self.getStartPage()
		return generalSettings

	def set(self, generalSettings):
		self.setHostName(generalSettings[self.HOST_NAME_SETTING])
		self.setPort(generalSettings[self.PORT_SETTING])
		self.setStartPage(generalSettings[self.START_PAGE_SETTING])

	def getHostName(self):
		return self.settingsService.getSetting( self.HOST_NAME_SETTING )

	def setHostName(self, hostName):
		self.settingsService.setSetting( self.HOST_NAME_SETTING, hostName )

	def getPort(self):
		return int(self.settingsService.getSetting( self.PORT_SETTING ))

	def setPort(self, port):
		self.settingsService.setSetting( self.PORT_SETTING, str(port) )

	def getStartPage(self):
		return self.settingsService.getSetting( self.START_PAGE_SETTING )

	def setStartPage(self, startPage):
		self.settingsService.setSetting( self.START_PAGE_SETTING, startPage )
