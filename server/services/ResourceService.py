from flask_restful import Api

from resources.PageResource import PageResource
from resources.MediaResource import MediaResource

from resources.ClientResource import ClientResource
from resources.HtmlResource import HtmlResource
from resources.JavaScriptResource import JavaScriptResource
from resources.CssResource import CssResource

class ResourceService(object):
	def __init__(self, app, pageRepository, api_only = False):
		self.app = app
		self.api = Api(app)

		self.__init_api(pageRepository)

		if not api_only:
			self.__init_webpage()

	def __init_api(self, pageRepository):
		self.api.add_resource(PageResource, '/pages/', '/pages/<path:route>',
			resource_class_kwargs={'pageRepository': pageRepository})
		self.api.add_resource(MediaResource, '/media/', '/media/<path:route>')
	
	def __init_webpage(self):
		self.api.add_resource(ClientResource, '/',
			resource_class_kwargs={'app': self.app})
		self.api.add_resource(JavaScriptResource, '/js/<path:route>')
		self.api.add_resource(HtmlResource, '/html/<path:route>')
		self.api.add_resource(CssResource, '/css/<path:route>')
