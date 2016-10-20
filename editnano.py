import glob
import os.path

for file in glob.glob('nanorc/*.nanorc'):
	print('include "'+os.path.abspath(file)+'"\n')
