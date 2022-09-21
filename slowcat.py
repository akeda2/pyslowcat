import os


path = './'

#files = os.listdir(path)

for root, directories, files in os.walk(path, topdown=False):
	for name in files:
		print(os.path.join(root, name))
	for name in directories:
		print(os.path.join(root, name))


#for f in files:
#	print(f)