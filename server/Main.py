import os
from uuid import uuid4
from flask import Flask
from flask_restful import Api

#from persistence.SqlitePageRepository import SqlitePageRepository
from persistence.InMemoryPageRepository import InMemoryPageRepository
from persistence.InMemorySettingsRepository import InMemorySettingsRepository
from persistence.JsonFileSettingsRepository import JsonFileSettingsRepository

from services.ResourceService import ResourceService
from services.AuthenticationService import AuthenticationService
from services.AccountService import AccountService
from services.AccountSettingsService import AccountSettingsService
from services.SettingsService import SettingsService
from services.PasswordSettingsService import PasswordSettingsService
from services.SslSettingsService import SslSettingsService
from services.SslService import SslService

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
	if (key == ''):
		key = str(uuid4().hex)

	print("BLESC's SimpleCms")
	app = Flask(__name__, static_folder='..')

	defaultSettingsRepository = JsonFileSettingsRepository("defaultSettings.json")
	settingsRepository = InMemorySettingsRepository()
	pageRepository = InMemoryPageRepository()# SqlitePageRepository("../data/content.db")	

	settingsService = SettingsService(defaultSettingsRepository, settingsRepository)
	passwordSettingsService = PasswordSettingsService(settingsService)
	accountSettingsService = AccountSettingsService(settingsService, passwordSettingsService)
	sslSettingsService = SslSettingsService(settingsService)

	accountService = AccountService(accountSettingsService)
	sslService = SslService(sslSettingsService)	

	AuthenticationService(app, accountService, key)	
	ResourceService(app, pageRepository) 
	app.run("0.0.0.0", 8080, debug=True, ssl_context=sslService.getSslContext())

if __name__ == "__main__":
	main(sys.argv[1:])
