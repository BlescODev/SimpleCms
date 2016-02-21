from passlib.hash import pbkdf2_sha256 as hasher

class Password(object):
	def __init__(self, password, passwordSettingsService):
		self.passwordSettingsService = passwordSettingsService
		self._setPassword(password)

	def _setPassword(self, password):
		passwordPolicy = self.passwordSettingsService.getPasswordPolicy()
		
		if not passwordPolicy.isAllowed(password):
			raise ValueError("password did not match policy", password)

		self.rounds = self.passwordSettingsService.getRounds()
		self.saltSize = self.passwordSettingsService.getSaltSize()		
		
		self._hash = hasher.encrypt(password.encode('utf-8'), rounds=self.rounds, salt_size=self.saltSize)
		

	def verify(self, password):
		return hasher.verify(password.encode('utf-8'), self._hash)
