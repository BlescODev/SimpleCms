from flask_restful import Resource
from flask import send_from_directory

class HtmlResource(Resource):  
    def get(self, route):
        return send_from_directory("client/html/", route)