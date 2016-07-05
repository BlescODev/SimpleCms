from flask_restful import Resource
from flask.globals import request
from flask_jwt import jwt_required, current_identity
import json

class AccountSettingsResource(Resource):
	def __init__(self, accountService, passwordSettingsService):
		self.passwordSettingsService = passwordSettingsService
		self.accountService = accountService

	@jwt_required()
	def get(self):
		print(current_identity.name)
		return json.loads('{"name": "'+ current_identity.name +'"}')

	@jwt_required()
	def post(self):
		settings = request.get_json(force=True)
		oldPassword = settings["oldPassword"]
		newPassword = settings["newPassword"]
		if current_identity.password.verify(oldPassword):
			current_identity.name = settings["name"]
			errors = self.passwordSettingsService.getPasswordPolicy().validate(newPassword)
			if len(errors) > 0:
				return errors, 403
			current_identity.password = Password( newPassword, self.passwordSettingsService )
			self.accountService.update(current_identity)
		else:
			return {"message": "password could not be verified"}, 401
