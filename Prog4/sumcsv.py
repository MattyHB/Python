# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# File: sumcsv.py
# Author: Matthew Beals User ID: Mbeal872 Class: CPS 110
# Desc: This program makes a filter type option for CSV files.
# It will take two columns and display them.
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
import sys
import csv
    
csvFile = open(sys.argv[1])
#csvFile.readline() #First line gone... maybe turn into variable?
csvread = csv.reader(csvFile)

fileDic = {}

column1 = sys.argv[2]

for item in fileDic:
    if column1 in fileDic:
        fileDic[column1] = fileDic[column1] + float()






oldProg = '''filename = sys.argv[1]
column1 = sys.argv[2]
column2 = sys.argv[3]

def relevantFunctionName(filename, column1, column2):
    lineNum = 1
    csvFile = open(filename)
    read = csv.reader(csvFile)
    print(read)
    
    index1 = read[0][column1]
    index2 = read[0][column2]

    for line in read:
        
        print(line[index1], line[index2])
        lineNum += 1

if len(sys.argv) != 4:
    print("Usage: python sumcsv.py csv-filename item-column count-column")
    sys.exit(1)



try:
    with open(filename) as readfile:
        relevantFunctionName(filename, column1, column1)
except FileNotFoundError as e:
    print("File not found!")'''