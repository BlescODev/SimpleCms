from webclient.clientResource import ClientResource
from webclient.htmlResource import HtmlResource
from webclient.javaScriptResource import JavaScriptResource
from webclient.cssResource import CssResource	

class WebClientResourceService(object):
	def __init__(self, app, api, designService):
		self.app = app
		self.api = api
		self.designService = designService
		
	def start(self):
		self.api.add_resource(ClientResource, '/',
			resource_class_kwargs={'app': self.app})
		self.api.add_resource(JavaScriptResource, '/js/<path:route>')
		self.api.add_resource(HtmlResource, '/html/<path:route>')
		self.api.add_resource(CssResource, '/css/<path:route>',
			resource_class_kwargs={'designService': self.designService})