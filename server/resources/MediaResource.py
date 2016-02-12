from flask_restful import Resource
from flask import send_from_directory

class MediaResource(Resource):     
    def get(self, route):
        return send_from_directory("../media/", route)
    
    def post(self, route):
        pass
