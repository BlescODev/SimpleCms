from flask_restful import Resource
from flask.globals import request
from flask_jwt import jwt_required
import json

class PageResource(Resource):
	def __init__(self, pageRepository):
		self.pageRepository = pageRepository

	def get(self, route=''):
		if route.endswith(".scms"):
			return self.__getScms(route)
		return self.__getTree(route)

	@jwt_required()
	def put(self, route=''):
		page = request.get_json(force=True)['page']
		self.pageRepository.add(page)

	@jwt_required()
	def post(self, route):		
		page = request.get_json(force=True)['page']
		self.pageRepository.update(page)

	@jwt_required()
	def delete(self, route):
		self.pageRepository.removeByRoute(route)

	def __getScms(self, route):
		page = self.pageRepository.getByRoute(route)
		if not page:
			return {}, 404
		return page

	def __getTree(self, route):
		tree = self.pageRepository.getTree(route)
		if not len(tree):
			return {}, 404
		return json.loads(json.dumps(tree))

