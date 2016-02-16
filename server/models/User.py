from werkzeug.security import safe_str_cmp
from passlib.hash import pbkdf2_sha256 as hasher

class User(object):
	def __init__(self, id, username, password):
		self.id = id
		self.name = username
		self.setPassword(password)

	def setPassword(self, password):
		self._password = hasher.encrypt(password.encode('utf-8'))

	def check_password(self, password):
		if(hasher.verify(password.encode('utf-8'), self._password)):
			return True
		return False

