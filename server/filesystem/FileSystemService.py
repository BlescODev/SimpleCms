from os import listdir
from os.path import isfile, join, isdir
from flask import send_from_directory, safe_join

class FileSystemService(object):
	@staticmethod
	def getFiles(root, hide='', R=True):
		print(root)
		files = [ join(root,file)[len(hide):] for file in listdir(root) if isfile(join(root,file))]
		dirs = [ dir for dir in listdir(root) if isdir(join(root,dir))]
		if R:
			for dir in dirs:
				files_in_dir = FileSystemService.getFiles(join(root,dir))
				if files_in_dir:
					for file in files_in_dir:
						files.append(file[len(hide):])
		return files

	@staticmethod
	def getFile(root, location):
		return send_from_directory(root, location)
	
	@staticmethod
	def saveFile(root, location, file):
		file.save(saveJoin(root, location))

	@staticmethod
	def deleteFile(root,locattion):
		 os.remove(saveJoin(root, location))

	@staticmethod
	def saveJoin(root, location):
		return save_join(root, location)
