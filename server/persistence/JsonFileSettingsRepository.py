import json

class JsonFileSettingsRepository(object):
	def __init__ (self, settingsFilePath):
		self.settingsFilePath = settingsFilePath

	def getSetting(self, key):
		with open(self.settingsFilePath) as settingsFile:
			settingsJson = json.load(settingsFile)
			return settingsJson[key]

	def setSetting(self, key, value):
		pass
