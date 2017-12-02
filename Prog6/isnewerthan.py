import sys
import os

try:
    checkDir = sys.argv[1]
except Exception as e:
    print('Usage: isnewerthan.py C:/destination ')
    exit(1)

for checkFile in os.listdir(checkDir):
    path = (checkDir + '\\' + checkFile)
    for line in sys.stdin:
        line = line.rstrip('\n')
        if os.path.getmtime(line) > os.path.getmtime(path):
            print(line)