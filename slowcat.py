from ast import Try
import os
import time

path = './'

#files = os.listdir(path)
try:
	for root, directories, files in os.walk(path, topdown=False):
		for name in files:
			if not name.startswith('.'):
				try:
					with open(str(os.path.join(root, name)), 'r') as f: 
						#print(f.read())
						while True:
							next_line = f.readline()
							if not next_line:
								break;
							print(next_line.strip())
							time.sleep(0.1)
						f.close()
				except:
					pass
except KeyboardInterrupt:
	pass
		#print(os.path.join(root, name))
	#for name in directories:
	#	print(os.path.join(root, name))


#for f in files:
#	print(f)