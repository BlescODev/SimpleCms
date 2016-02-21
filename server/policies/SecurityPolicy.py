class SecurityPolicy(object):
	def __init__(self, rounds, saltSize):
		self.rounds = rounds
		self.saltSize = saltSize

		self.validationTests = dict()

		self.validationTests[self.roundsTest] = \
				"the password wasn't generated with enougth rounds."
		self.validationTests[self.saltSizeTest] = \
				"the passwords salt isn't long enougth."

	def isAllowed(self, password):
		for test in self.validationTests.keys():
			if not test(password):
				return False
		return True

	def validate(self, password):
		errors = list()
		for test in self.validationTests.keys():
			if not test(password):
				errors.append(self.validationTests[test])
		return errors

	def roundsTest(self, password):
		return password.rounds >= self.rounds

	def saltSizeTest(self, password):
		return password.saltSize >= self.saltSize
