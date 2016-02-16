import os
from uuid import uuid4
from flask import Flask
from flask_restful import Api

#from persistence.SqlitePageRepository import SqlitePageRepository
from persistence.InMemoryPageRepository import InMemoryPageRepository

from services.ApiService import ApiService
from services.AuthenticationService import AuthenticationService
from services.AccountService import AccountService

import sys, getopt

def main(argv):
	key = ''
	try:
		opts, args = getopt.getopt(argv,"hk:",["key="])
	except getopt.GetoptError:
		print ('main.py [--key <token key>]')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('main.py [--key <token key>]')
			sys.exit()
		elif opt in ("-k", "--key"):
			key = arg

	print("BLESC's SimpleCms")
	app = Flask(__name__, static_folder='..')
	ApiService(app, InMemoryPageRepository())

	if (key == ''):
		key = str(uuid4().hex)
	accountService = AccountService("defaultSettings","settingsPersistence")
	AuthenticationService(app, accountService, key)
	# SqlitePageRepository("../data/content.db")

	app.run("0.0.0.0", 8080, debug=True)
if __name__ == "__main__":
	main(sys.argv[1:])
