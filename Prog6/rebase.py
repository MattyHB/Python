#Rewrite filenames passed to input so as to refer to a different 
# base directory.
import sys
import os

try:
    newdir = sys.argv[1]
except Exception as e:
    print('Usage: rebase.py C:\some\path')
    exit(1)

for line in sys.stdin:
    line = line.rstrip('\n')
    if '\\' in line:
        os.path.basename(line)
        print(newdir+ '\\' +line)
    if '\\' not in line:
        os.path.join(newdir, line)
        print(newdir +'\\' + line)