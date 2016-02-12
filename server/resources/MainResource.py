from flask_restful import Resource
from flask import send_from_directory

class MainResource(Resource):
	def __init__(self, app):
		self.app = app

	def get(self):
		return self.app.send_static_file('client/html/index.html')
