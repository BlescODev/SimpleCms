from settings.generalSettingsResource import GeneralSettingsResource
from accounts.accountSettingsResource import AccountSettingsResource

from .pageResource import PageResource
from .mediaResource import MediaResource

class ApiResourceService(object):
	def __init__(self, app, api, pageRepository, generalSettingsService, 
			accountService, passwordSettingsService):
		self.app = app
		self.api = api

		self.pageRepository = pageRepository
		self.generalSettingsService = generalSettingsService
		self.accountService = accountService
		self.passwordSettingsService = passwordSettingsService
		
	def start(self):
		self.api.add_resource(PageResource, '/pages/', '/pages/<path:route>',
			resource_class_kwargs={'pageRepository': self.pageRepository})

		self.api.add_resource(MediaResource, '/media/', '/media/<path:route>',
			resource_class_kwargs={'source': "../media/"})

		self.api.add_resource(GeneralSettingsResource, '/settings/general',
			resource_class_kwargs={'generalSettingsService': self.generalSettingsService})

		self.api.add_resource(AccountSettingsResource, '/settings/account',
			resource_class_kwargs={
				'accountService': self.accountService, 
				'passwordSettingsService': self.passwordSettingsService })