from flask_restful import Resource
from flask.globals import request
from flask_jwt import jwt_required
import json

class AuthenticationResource(Resource):
	def post(self):
		pass
