import os
import sys
from operator import itemgetter

try:
    sortType = sys.argv[1]
except Exception as e:
    print('Usage: sortby.py SortByType')
    print("Acceptable types: 'name' 'size' mtime' 'atime'")
    exit(1)

fileList = []

for line in sys.stdin:
    line = line.rstrip('\n')
    fileList.append((line, os.path.getsize(line), os.path.getmtime(line), os.path.getatime(line)))

# Now that I know how to access each value, I need to know how to compare them and return the 
# name based on the sorting 
sortable = []
testList =[]

for (name, size, mtime, atime) in fileList:
    i = 0

    if sortType == 'name':
        sortable.append(name)
        sortable[i][1]

    if sortType == 'size':
        sortable = sorted(fileList, key=itemgetter(1), reverse = True)
        sortable = [x[0] for x in sortable]

    if sortType == 'mtime':
        sortable = sorted(fileList, key=itemgetter(2), reverse = True)
        sortable = [x[0] for x in sortable]
        
    if sortType == 'atime':
        sortable = sorted(fileList, key=itemgetter(3), reverse = True)
        sortable = [x[0] for x in sortable]
        
    i += 1

stringList = '\n'.join(sortable)

print(stringList)