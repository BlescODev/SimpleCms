from os.path import isfile
import ssl
import random

class SslService(object):
	def __init__(self, sslSettingsService):
		self.sslSettingsService = sslSettingsService
		self.dataDir = "../data/"

	def getSslContext(self):
		if self.sslSettingsService.getIsSslEnabled():
			keyFile = self.dataDir + self.sslSettingsService.getKeyPath()
			certificateFile = self.dataDir + self.sslSettingsService.getCertificatePath()

			if not isfile(keyFile):
				keyFile = self.dataDir + self.sslSettingsService.getDefaultKeyPath()
				if not isfile(keyFile):
					self.createKey(keyFile)

			if not isfile(certificateFile):
				certificateFile = self.dataDir + self.sslSettingsService.getDefaultCertificatePath()
				if not isfile(certificateFile):
					self.createCertificate(certificateFile, keyFile=keyFile)
			
			#protocol = self.sslSettingsService.getProtocol()
			context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
			context.load_cert_chain(certificateFile, keyFile)

			return context
		return None

	def createKey(self, keyFile):
		keySize = self.sslSettingsService.getKeySize()
		key = SslContextService.generateKey( keySize )
		SslContextService.writeKeyToFile( key, keyFile )
		certificateFile = self.dataDir + self.sslSettingsService.getDefaultCertificatePath()
		certificate = self.createCertificate(certificateFile, key=key)
		return certificate, key

	def createCertificate(self, certificateFile, key=None, keyFile=None):
		if not key:		
			key = SslContextService.readKeyFromFile( keyFile )
		serialNumber =  random.randint(0, 1000000)
		runTime = self.sslSettingsService.getCertificateLifeTime()
		subject = self.sslSettingsService.getCertificateSubject()
		hashAlgorithm = self.sslSettingsService.getCertificateHashAlgorithm()
		certificate = SslContextService.generateCertificate( 
				key, serialNumber, runTime, subject, hashAlgorithm )
		SslContextService.writeCertificateToFile( certificate, certificateFile )
		return certificate

