# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# File: sumcsv2.py
# Author: Matthew Beals User ID: Mbeal872 Class: CPS 110
# Desc: This program continues the sumcsv.py file
#this program also handles .xlsx file formats and can read and write
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
import sys
import csv
import openpyxl

if len(sys.argv) != 4:
    print("Usage: python sumcsv.py csv-filename item-column count-column")
    sys.exit(1)

csvFile = open(sys.argv[1])
csvread = csv.reader(csvFile)
column1 = sys.argv[2]
column2 = sys.argv[3]
headers = next(csvread)
col1index = 0
col2index = 0

try:
    col1index = headers.index(column1)
except ValueError as e:
    print("You supplied an Item Name that does not exit in this file.")
    print()
    print("Usage: python sumcsv.py csv-filename item-column count-column")
    print()
    sys.exit(1)
try:
    col2index = headers.index(column2)
except ValueError as e:
    print('You supplied a count column that does not exist in this file.')
    print()
    print("Usage: python sumcsv.py csv-filename item-column count-column")
    print()
    sys.exit(1)

fileDic = {}

for line in csvread:
    item = line[col1index]
    count = line[col2index]
    try:
        count = int(count)
    except ValueError as e:
        continue
    if item in fileDic:
        fileDic[item] = fileDic[item] + int(count)
    else:
        fileDic[item] = int(count)

print(column1 + ',' + column2)

for i in sorted(fileDic):
    print(i +','+ str(fileDic[i]))