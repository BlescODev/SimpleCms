
class SettingsService(object):
	def __init__ (self, defaultSettingsRepository, settingsRepository):
		self.defaultSettingsRepository = defaultSettingsRepository
		self.settingsRepository = settingsRepository

	def getSetting(self, key):
		setting = self.settingsRepository.getSetting(key)
		if not setting:
			return self.defaultSettingsRepository.getSetting(key)
		return setting

	def setSetting(self, key, value):
		self.settingsRepository.setSetting(key, value)
