from ast import Try
import os


path = './'

#files = os.listdir(path)

for root, directories, files in os.walk(path, topdown=False):
	for name in files:
		if not name.startswith('.'):
			try:
				with open(str(os.path.join(root, name)), 'r') as f: 
					print(f.read())
			except:
				pass
		#print(os.path.join(root, name))
	#for name in directories:
	#	print(os.path.join(root, name))


#for f in files:
#	print(f)