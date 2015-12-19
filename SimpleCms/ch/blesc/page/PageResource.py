from flask_restful import Resource
from ch.blesc.page.PageRepository import PageRepository
from flask.globals import request
import json

class PageResource(Resource):
    
    def __init__(self):
        self.pageRepository = PageRepository()
        
    def get(self, route):
        return self.toJson( self.pageRepository.get(route) )
    
    def post(self, route):
        content = request.form['page']
        self.pageRepository.addOrUpdate(route, content)

    def delete(self, route):
        self.pageRepository.remove(route)
        
    def toJson(self, page):
        return json.loads(page)