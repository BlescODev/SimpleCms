from flask_restful import Resource
from flask.globals import request
import json

class PageResource(Resource):
    
    def __init__(self, pageRepository):
        self.pageRepository = pageRepository
        
    def get(self, route):
        return self.toJson( self.pageRepository.get(route) )
    
    def post(self, route):
        content = request.form['page']
        self.pageRepository.addOrUpdate(route, content)

    def delete(self, route):
        self.pageRepository.remove(route)
        
    def toJson(self, page):
        return json.loads(page)
