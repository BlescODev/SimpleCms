from flask_restful import Resource

class InMemoryPageRepository(Resource):
	def __init__(self):
		self.pages = {
			"navigation" : open("../data/navigation.json", 'r').read(),
			"index" : open("../data/index.json", 'r').read()}

	def get(self, route):
		try:
			return self.pages[route]
		except KeyError:
			return None

	def addOrUpdate(self, route, page):
		self.pages[route] = page

	def remove(self, route):
		del self.pages[route]
