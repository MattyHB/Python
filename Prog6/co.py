#Copy all named input files into a user selected destination directory (including the file metadata, if possible).
import sys
import shutil

try:
    outdir = sys.argv[1]
except Exception as e:
    print('Usage: co.py some/path')
    exit(1)

input = sys.stdin

for line in input:
    line = line.rstrip('\n')
    shutil.copy2(line, outdir)
    print(shutil.copy2(line, outdir))