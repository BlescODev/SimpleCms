from filesystem.FileSystemService import FileSystemService
from flask_restful import Resource
from flask.globals import request
from flask_jwt import jwt_required
import json

class MediaResource(Resource):
	def __init__(self, source):
		self.source = source

	def get(self, route=''):
		if '.' in route:
			return self.__getFile(route)
		try:		
			return self.__getTree(route)
		except FileNotFoundError:
			return {"error": "404 - File not found"}, 404

	@jwt_required()
	def put(self, route):
		file = request.files['file']
		route += file.filename
		try:
			self.__saveFile(route, file)
		except NotFound:
			return {"error": "invalide route"}, 400
		return json.dumps({'filename':route})


	@jwt_required()
	def post(self, route):
		file = request.files['file']
		try:
			self.__deleteFile(route)
			self.__saveFile(route, file)
		except NotFound:
			return {"error": "invalide route"}, 400
		return json.dumps({'filename':route})

	@jwt_required()
	def delete(self, route):
		self.__deleteFile(route)

	def __getTree(self, route):
		tree = FileSystemService.getFiles(self.source+route, self.source+route)
		return json.loads(json.dumps(tree))

	def __getFile(self, route):
		return FileSystemService.getFile(self.source, route)

	def __saveFile(self, route, file):
		FileSystemService.saveFile(self.source, route, file)

	def __deleteFile(self, route):
		FileSystemService.deleteFile(self.source, route)
