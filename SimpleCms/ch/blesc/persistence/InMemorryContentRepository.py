from flask_restful import Resource

class InMemorryContentRepository(Resource):
    
    def __init__(self):
        self.pages = {
                "navigation" : open("media/page/navigation.json", 'r').read(),
                "home" : open("media/page/home.json", 'r').read()}
    
    def get(self, route):
        return self.pages[route]
    
    def addOrUpdate(self, route, page):
        self.pages[route] = page
    
    def remove(self, route):
        del self.pages[route]
