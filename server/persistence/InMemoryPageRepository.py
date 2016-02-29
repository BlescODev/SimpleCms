from flask_restful import Resource

class InMemoryPageRepository(Resource):
	def __init__(self):
		self.pages = {
			"navigation.scms" : open("../data/navigation.json", 'r').read(),
			"index.scms" : open("../data/index.json", 'r').read()}

	def get(self, route):
		try:
			return self.pages[route]
		except KeyError:
			return None

	def getTree(self, route):
		tree = list()
		for page in self.pages:
			if page.startswith(route):
				tree.append(page)
		return tree

	def addOrUpdate(self, route, page):
		self.pages[route] = page

	def remove(self, route):
		del self.pages[route]
