#! python3
'''Autom8r: list filenames from 1+ directories'''
import os
import sys

# Which directories to list?
if len(sys.argv) > 1:
    dirs = sys.argv[1:]
else:
    dirs = ['.']    # default to just the current working directory

# For each selected directory...
for path in dirs:
    # ... for each name in that directory...
    for name in os.listdir(path):
        # ... figure out if it's a file...
        fname = os.path.join(path, name)
        if os.path.isfile(fname):
            # ...and if it is, print the absolute path to that file to stdout
            print(os.path.abspath(fname))