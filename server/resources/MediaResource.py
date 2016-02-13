from flask_restful import Resource
from flask import send_from_directory
from flask_jwt import jwt_required

class MediaResource(Resource):     
	def get(self, route):
		return send_from_directory("../media/", route)

	@jwt_required()
	def post(self, route):
		pass
