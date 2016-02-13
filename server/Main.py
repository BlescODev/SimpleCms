import os
from flask import Flask
from flask_restful import Api

#from persistence.SqlitePageRepository import SqlitePageRepository
from persistence.InMemoryPageRepository import InMemoryPageRepository

from services.ApiService import ApiService
from services.AuthenticationService import AuthenticationService

if __name__ == '__main__':
	print("BLESC's SimpleCms")
	app = Flask(__name__, static_folder='..')
	ApiService(app, InMemoryPageRepository())
	AuthenticationService(app)
	# SqlitePageRepository("../data/content.db")

	app.run("0.0.0.0", 8080, debug=True)
