from flask_restful import Resource

class InMemoryContentRepository(Resource):
    
    def __init__(self):
        self.pages = {
                "navigation" : open("data/navigation.json", 'r').read(),
                "index" : open("data/index.json", 'r').read()}
    
    def get(self, route):
        return self.pages[route]
    
    def addOrUpdate(self, route, page):
        self.pages[route] = page
    
    def remove(self, route):
        del self.pages[route]
