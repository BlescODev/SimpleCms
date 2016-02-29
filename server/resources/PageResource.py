from flask_restful import Resource
from flask.globals import request
from flask_jwt import jwt_required
import json

class PageResource(Resource):

	def __init__(self, pageRepository):
		self.pageRepository = pageRepository

	def get(self, route=''):
		# validate route
		if route.endswith(".scms"):
			return self.getScms(route)
		return self.getTree(route)

	def getScms(self, route):
		page = self.pageRepository.get(route)
		if not page:
			return {}, 404
		return json.loads(page)

	def getTree(self, route):
		tree = self.pageRepository.getTree(route)
		if not len(tree):
			return {}, 404
		return json.loads(json.dumps(tree))


	@jwt_required()
	def post(self, route):
		# validate route
		content = request.form['page']
		# validate content

		self.pageRepository.addOrUpdate(route, content)

	@jwt_required()
	def delete(self, route):
		# validate route

		self.pageRepository.remove(route)
