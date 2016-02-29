from os import listdir
from os.path import isfile, join, isdir

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
