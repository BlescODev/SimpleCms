from distutils.util import strtobool as toBool

class DesignSettingsService(object):
	def __init__(self, settingsService):
		self.settingsService = settingsService
		self.DESIGN_PATH = "designCssDesignPath"
		self.PATTERN_PATH = "designCssPatternPath"
		
	def getDesignPath(self):
		return self.settingsService.getSetting( self.DESIGN_PATH )

	def setDesignPath(self, path):
		self.settingsService.setSetting( self.DESIGN_PATH, path )

	def getPatternPath(self):
		return self.settingsService.getSetting( self.PATTERN_PATH )

	def setPatternPath(self, path):
		self.settingsService.setSetting( self.PATTERN_PATH, path )
