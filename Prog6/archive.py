import sys
import os
import time
import zipfile

try:
    zipname = time.strftime(sys.argv[1])    # treat filename as pattern for strftime (%Y, %m, %d, etc.)
except Exception as e:
    print("Usage: archive.py ZipFileName")

zipp = zipfile.ZipFile(zipname, "w", zipfile.ZIP_DEFLATED)

for line in sys.stdin:
    line = line.rstrip('\n')
    zipp.write(line)

zipp.close()