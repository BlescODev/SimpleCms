from OpenSSL import crypto

class SslContextService(object):
	@staticmethod
	def generateKey(keySize):
		key = crypto.PKey()
		key.generate_key(crypto.TYPE_RSA, keySize)
		return key

	@staticmethod
	def generateCertificate(key, serialNumber, runTime, subject, hashAlgorithm):
		certificate = crypto.X509()
		certificate.set_serial_number(serialNumber)
		certificate.gmtime_adj_notBefore(0)
		certificate.gmtime_adj_notAfter(runTime)
		certificate.set_subject(subject)
		certificate.set_issuer(subject)
		certificate.set_pubkey(key)
		certificate.sign(key, hashAlgorithm)
		return certificate

	@staticmethod
	def createCertificateSubject(c, st, l, o, ou, cn):
		subject = crypto.X509Req().get_subject()
		subject.C = c
		subject.ST = st
		subject.L = l
		subject.O = o
		subject.OU = ou
		subject.CN = cn
		return subject

	@staticmethod
	def cnFromHostName(host):
		return '*.%s/CN=%s' % (host, host)

	@staticmethod
	def writeKeyToFile( key, keyPath ):
		with open(keyPath, 'wb') as keyFile:
			keyFile.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

	@staticmethod
	def readKeyFromFile( keyPath ):
		with open(keyPath, 'rb') as keyFile:
			return crypto.load_privatekey(crypto.FILETYPE_PEM, keyFile.read())
		
	@staticmethod
	def writeCertificateToFile( certificate, certificatePath ):
		with open(certificatePath, 'wb') as certificateFile:
			certificateFile.write(crypto.dump_certificate(crypto.FILETYPE_PEM, certificate))

