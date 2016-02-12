from flask_restful import Resource
from flask import send_from_directory

class CssResource(Resource):      
    def get(self, route):
        return send_from_directory("../design/css/", route)
