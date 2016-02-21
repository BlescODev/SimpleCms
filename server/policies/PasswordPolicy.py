import re
import string

class PasswordPolicy(object):
	def __init__(self, minLength, needsLowercase, needsUppsercase, needsNumbers, needsSpecial):
		self.minLength = minLength
		self.needsLowercase = needsLowercase
		self.needsUppercase = needsUppsercase
		self.needsNumbers = needsNumbers
		self.needsSpecial = needsSpecial

		self.validationTests = dict()

		self.validationTests[self.minLengthTest] = \
				"the password must contain at least "+ str(self.minLength) +" characters."
		self.validationTests[self.lowercaseTest] = \
				"the password must contain at least one lowercase character."
		self.validationTests[self.uppsercaseTest] = \
				"the password must contain at least one uppercase character."
		self.validationTests[self.numbersTest] = \
				"the password must contain at least one numeric character."
		self.validationTests[self.specialTest] = \
				"the password must contain at least one special character("+ string.punctuation +")."

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

	def minLengthTest(self, password):
		return len(password) >= self.minLength

	def lowercaseTest(self, password):
		return not self.needsLowercase or len(re.findall('[a-z]', password)) > 0

	def uppsercaseTest(self, password):
		return not self.needsUppercase or len(re.findall('[a-z]', password)) > 0

	def numbersTest(self, password):
		return not self.needsNumbers or len(re.findall('[0-9]', password)) > 0

	def specialTest(self, password):
		return not self.needsSpecial or len(re.findall('['+ string.punctuation +']', password)) > 0
