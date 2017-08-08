#!../flasky2/bin/python
import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = '../flasky2/bin/pybabel'
os.system(pybabel + ' compile -d app/translations')