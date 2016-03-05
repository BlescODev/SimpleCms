from flask_restful import Resource
from uuid import uuid4 as uuid
import json

class InMemoryPageRepository(Resource):
	def __init__(self):
		self.pages = list()
		self.add(json.load(open("../data/navigation.json", 'r')))
		self.add(json.load(open("../data/simpleCmsHome.json", 'r')))

	def add(self, page):
		page['id'] = str(uuid())
		self.pages.append(page)

	def get(self, id):
		for page in self.pages:
			if page['id'] == id:
				return page
		return None

	def getByRoute(self, route):
		for page in self.pages:
			if page['route'] == route:
				return page
		return None

	def update(self, page):
		self.remove(page['id'])
		self.pages.append(page)

	def remove(self, id):
		for page in self.pages:
			if page['id'] == id:
				self.pages.remove(page)
				return

	def removeByRoute(self, route):
		for page in self.pages:
			if page['route'] == route:
				self.pages.remove(page)
				return

	def getTree(self, route):
		tree = list()
		for page in self.pages:
			page_route = page['route']
			if page_route.startswith(route):
				tree.append(page_route[len(route):])
		return tree
