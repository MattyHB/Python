#Rewrite filenames passed to input so as to refer to a different base directory.

import sys
import os

try:
    newdir = sys.argv[1]

# Find the correct error to use.
except Exception as e:
    print('Usage: rebase.py c:\some\path')
    exit(1)

###NOT COMPLETE!!

