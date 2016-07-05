from flask import render_template, Response
import json

class DesignService(object):
	def __init__(self, designSettingsService):
		self.designSettingsService = designSettingsService

	def getActiveCss(self):
		designPath = self.designSettingsService.getDesignPath()
		pattern = self.getActivePattern()
		css = render_template(designPath, style=pattern)
		return  Response(css, mimetype='text/css')

	def getActivePattern(self):
		patternPath = "../" + self.designSettingsService.getPatternPath()
		return json.load(open(patternPath))
