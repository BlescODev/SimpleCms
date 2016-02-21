class InMemorySettingsRepository(object):
	def __init__(self):
		self.settings = dict()

	def getSetting(self, key):
		try:
			return self.settings[key]
		except KeyError:
			return None

	def setSetting(self, key, value):
		self.settings[key] = value
