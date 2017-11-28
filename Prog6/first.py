# Output only the first lines of input, supplied by the user.
import os
import sys

try:
    num = sys.argv[1]
    num = int(num)
except IndexError:
    print('Usage: first.py # of lines')
    exit(1)

i = 0
while i < num:
    line = sys.stdin.readline()
    line = line.rstrip('\n')
    print(line)
    i += 1