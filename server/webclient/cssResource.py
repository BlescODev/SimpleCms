from flask_restful import Resource
from flask import send_from_directory

class CssResource(Resource):      
	def __init__(self, designService):
		self.designService = designService

	def get(self, route):
		if route == "style.css":		
			return self.designService.getActiveCss()
		return send_from_directory("../design/css/", route)
