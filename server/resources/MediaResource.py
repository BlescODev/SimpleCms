from services.FileSystemService import FileSystemService
from flask_restful import Resource
from flask import send_from_directory
from flask_jwt import jwt_required
import json

class MediaResource(Resource):
	def __init__(self):
		self.source = "../media/"

	def get(self, route=''):
		if '.' in route:
			return send_from_directory(self.source, route)		
		try:		
			return json.loads(json.dumps(self.getTree(route)))
		except FileNotFoundError:
			return {"error": "404 - File not found"}, 404

	def getTree(self, route):
		return FileSystemService.getFiles(self.source+route, self.source+route)
		

	@jwt_required()
	def post(self, route):
		pass
