import glob
import os.path as path

with open(path.expanduser('~/.nanorc'), 'w') as f:
	for file in glob.glob('nanorc/*.nanorc'):
		print(path.abspath(file))
		f.write('include "'+path.abspath(file)+'"\n')
