from flask_restful import Resource
from flask.globals import request
from flask_jwt import jwt_required
import json

class PageResource(Resource):
    
    def __init__(self, pageRepository):
        self.pageRepository = pageRepository

    def get(self, route):
        page = self.pageRepository.get(route)
        if not page:
            return {}, 404
        return self.toJson( page )

    @jwt_required()
    def post(self, route):
        content = request.form['page']
        self.pageRepository.addOrUpdate(route, content)

    @jwt_required()
    def delete(self, route):
        self.pageRepository.remove(route)
        
    def toJson(self, page):
        return json.loads(page)
