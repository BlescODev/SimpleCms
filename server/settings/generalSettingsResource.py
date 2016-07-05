from flask_restful import Resource
from flask.globals import request
from flask_jwt import jwt_required
import json

class GeneralSettingsResource(Resource):
	def __init__(self, generalSettingsService):
		self.generalSettingsService = generalSettingsService

	@jwt_required()
	def get(self):
		return json.loads(json.dumps(self.generalSettingsService.get()))

	@jwt_required()
	def post(self):
		settings = request.get_json(force=True)
		self.generalSettingsService.set(settings)
