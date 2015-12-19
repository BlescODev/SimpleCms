from flask import Flask
from flask_restful import Api, Resource
from ch.blesc.application.services.HtmlResource import HtmlResource
from ch.blesc.application.services.JavaScriptResource import JavaScriptResource
from ch.blesc.media.MediaResource import MediaResource
from ch.blesc.page.PageResource import PageResource
from ch.blesc.application.services.CssResource import CssResource


class ClientResource(Resource):
    def get(self):
        return app.send_static_file('client/html/index.html')

if __name__ == '__main__':
    print("BLESC's SimpleCms")
    app = Flask(__name__, static_folder='')
    api = Api(app)
    
    # index
    api.add_resource(ClientResource, '/')
    
    # content
    api.add_resource(PageResource, '/page/<path:route>')
    
    # media
    api.add_resource(MediaResource, '/media/<path:route>')
    
    # client
    api.add_resource(JavaScriptResource, '/js/<path:route>')
    api.add_resource(HtmlResource, '/html/<path:route>')
    api.add_resource(CssResource, '/css/<path:route>')
    
    app.run("0.0.0.0", 8080)