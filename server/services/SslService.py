from os.path import isfile
import ssl
import random

from services.SslContextService import SslContextService

class SslService(object):
	def __init__(self, sslSettingsService):
		self.sslSettingsService = sslSettingsService

	def getSslContext(self):
		if self.sslSettingsService.getIsSslEnabled():
			dataDir = "../data/"
			keyFile = dataDir + self.sslSettingsService.getKeyPath()
			certificateFile = dataDir + self.sslSettingsService.getCertificatePath()

			if not isfile(keyFile):
				keyFile = dataDir + self.sslSettingsService.getDefaultKeyPath()
				if not isfile(keyFile):
					keySize = self.sslSettingsService.getKeySize()
					key = SslContextService.generateKey( keySize )
					print (key)
					SslContextService.writeKeyToFile( key, keyFile )

			if not isfile(certificateFile):
				certificateFile = dataDir + self.sslSettingsService.getDefaultCertificatePath()
				if not isfile(certificateFile):
					key = SslContextService.readKeyFromFile( keyFile )
					serialNumber =  random.randint(0, 1000000)
					runTime = self.sslSettingsService.getCertificateLifeTime()
					subject = self.sslSettingsService.getCertificateSubject()
					hashAlgorithm = self.sslSettingsService.getCertificateHashAlgorithm()
					certificate = SslContextService.generateCertificate( 
							key, serialNumber, runTime, subject, hashAlgorithm )
					SslContextService.writeCertificateToFile( certificate, certificateFile )

			#protocol = self.sslSettingsService.getProtocol()
			context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
			context.load_cert_chain(certificateFile, keyFile)

			return context
		return None
