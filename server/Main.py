import os
import sys, getopt
from uuid import uuid4

from flask import Flask
from flask_restful import Api

from api import *
from webclient import *
from settings import *
from filesystem import *
from accounts import *

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
	import jinja2
	loader = jinja2.FileSystemLoader("..")
	app.jinja_loader = loader

	defaultSettingsRepository = JsonFileSettingsRepository("defaultSettings.json")
	settingsRepository = InMemorySettingsRepository()
	pageRepository = InMemoryPageRepository() # SqlitePageRepository("../data/content.db")	

	settingsService = SettingsService(defaultSettingsRepository, settingsRepository)
	passwordSettingsService = PasswordSettingsService(settingsService)
	accountSettingsService = AccountSettingsService(settingsService, passwordSettingsService)
	sslSettingsService = SslSettingsService(settingsService)
	designSettingsService = DesignSettingsService(settingsService)
	generalSettingsService = GeneralSettingsService(settingsService)

	accountService = AccountService(accountSettingsService)
	sslService = SslService(sslSettingsService)
	designService = DesignService(designSettingsService)

	AuthenticationService(app, accountService, key)	
	
	api = Api(app)
	
	ApiResourceService(app, api, pageRepository, 
		generalSettingsService, accountService, passwordSettingsService).start()
	
	WebClientResourceService(app, api, designService).start()
	
	app.run(generalSettingsService.getHostName(), 
			generalSettingsService.getPort(), 
			debug=True, 
			ssl_context=sslService.getSslContext())

if __name__ == "__main__":
	main(sys.argv[1:])
