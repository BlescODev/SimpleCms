from flask_restful import Api

from resources.PageResource import PageResource
from resources.MediaResource import MediaResource
from resources.GeneralSettingsResource import GeneralSettingsResource
from resources.AccountSettingsResource import AccountSettingsResource

from resources.ClientResource import ClientResource
from resources.HtmlResource import HtmlResource
from resources.JavaScriptResource import JavaScriptResource
from resources.CssResource import CssResource

class ResourceService(object):
	def __init__(self, app, pageRepository, designService, generalSettingsService, 
			accountService, passwordSettingsService, api_only = False):
		self.app = app
		self.api = Api(app)

		self.__init_api(pageRepository, generalSettingsService, accountService, passwordSettingsService)

		if not api_only:
			self.__init_client(designService)

	def __init_api(self, pageRepository, generalSettingsService, accountService, passwordSettingsService):
		self.api.add_resource(PageResource, '/pages/', '/pages/<path:route>',
			resource_class_kwargs={'pageRepository': pageRepository})

		self.api.add_resource(MediaResource, '/media/', '/media/<path:route>',
			resource_class_kwargs={'source': "../media/"})

		self.api.add_resource(GeneralSettingsResource, '/settings/general',
			resource_class_kwargs={'generalSettingsService': generalSettingsService})

		self.api.add_resource(AccountSettingsResource, '/settings/account',
			resource_class_kwargs={
				'accountService': accountService, 
				'passwordSettingsService': passwordSettingsService })
	
	def __init_client(self, designService):
		self.api.add_resource(ClientResource, '/',
			resource_class_kwargs={'app': self.app})
		self.api.add_resource(JavaScriptResource, '/js/<path:route>')
		self.api.add_resource(HtmlResource, '/html/<path:route>')
		self.api.add_resource(CssResource, '/css/<path:route>',
			resource_class_kwargs={'designService': designService})
