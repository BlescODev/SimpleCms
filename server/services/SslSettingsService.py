from distutils.util import strtobool as toBool

from services.SslContextService import SslContextService

class SslSettingsService(object):
	def __init__(self, settingsService):
		self.settingsService = settingsService
		self.IS_ENABLED_SETTING = "sslIsEnabled"
		self.DEFAULT_KEY_PATH_SETTING = "sslDefaultKeyPath"
		self.KEY_PATH_SETTING = "sslKeyPath"
		self.KEY_SIZE_SETTING = "sslKeySize"

		self.DEFAULT_CERTIFICATE_PATH_SETTING = "sslDefaultCertificatePath"
		self.CERTIFICATE_PATH_SETTING = "sslCertificatePath"
		self.CERTIFICATE_SERIAL_NUMBER_SETTING = "sslCertificateSerialNumber"
		self.CERTIFICATE_LIFE_TIME_SETTING = "sslCertificateLifeTime"
		self.CERTIFICATE_HASH_ALGORITHM_SETTING = "sslCertificateHashAlgorithm"

		self.HOST_NAME_SETTING = "hostName"
		"""
		(c, st, l, o, ou, cn)
		"""

	def getIsSslEnabled(self):
		return toBool(self.settingsService.getSetting( self.IS_ENABLED_SETTING ))

	def getHostName(self):
		return self.settingsService.getSetting( self.HOST_NAME_SETTING )

	def getDefaultKeyPath(self):
		return self.settingsService.getSetting( self.DEFAULT_KEY_PATH_SETTING )

	def getKeyPath(self):
		return self.settingsService.getSetting( self.KEY_PATH_SETTING )

	def getKeySize(self):
		return int (self.settingsService.getSetting( self.KEY_SIZE_SETTING ))

	def getDefaultCertificatePath(self):
		return self.settingsService.getSetting( self.DEFAULT_CERTIFICATE_PATH_SETTING )

	def getCertificatePath(self):
		return self.settingsService.getSetting( self.CERTIFICATE_PATH_SETTING )

	def getCertificateSerialNumber(self):
		return self.settingsService.getSetting( self.CERTIFICATE_SERIAL_NUMBER_SETTING )

	def getCertificateLifeTime(self):
		return self.settingsService.getSetting( self.CERTIFICATE_LIFE_TIME_SETTING )

	def getCertificateHashAlgorithm(self):
		return self.settingsService.getSetting( self.CERTIFICATE_HASH_ALGORITHM_SETTING )

	def getCertificateSubject(self):
		hostName = self.getHostName()
		cn = SslContextService.cnFromHostName(hostName)
		return SslContextService.createCertificateSubject(
				"CH", "ZH", "ZH", "SimpleSoftware", "SimpleCms", cn)
