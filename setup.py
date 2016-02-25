import pip

def install(package):
    pip.main(['install', package])

modules = {
	"flask_restful",
	"flask_jwt",
	"passlib",
	"pyOpenSSL"
}

for module in modules:
	install(module)

