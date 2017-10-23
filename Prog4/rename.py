# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# File: rename.py
# Author: Matthew Beals User ID: Mbeal872 Class: CPS 110
# Desc: This program renames all specified file types and
# adds the date last modified to them.
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
import os
import sys
import shutil
import datetime

if len(sys.argv) != 3:
    print('Usage: python rename.py folder-name ext1,ext2,ext3,…')
    quit()


try:
    chosenFolder = sys.argv[1]
    fileTypes = sys.argv[2].split(',')
except Exception as e:
    print('Usage: python rename.py folder-name ext1,ext2,ext3,…')
    quit()


extDic = {}
for ext in fileTypes:
    extDic[ext] = 0

def rename(folder):
    try:
        files = os.listdir(folder)
    except FileNotFoundError as e:
        print('File not found. Usage: python rename.py folder-name ext1,ext2,ext3,…')
        quit()
    for selectedFile in files:
        ext = selectedFile.split(".")[-1]
        if ext in fileTypes:
            t = os.path.getctime( folder + '/' + selectedFile)
            t = str(datetime.datetime.fromtimestamp(t).date())
            os.rename(folder + '/' + selectedFile, folder + '/' + t + str(selectedFile))
            
            extDic[ext] += 1
        
def main():
    rename(chosenFolder)
    for i in sorted(extDic):
        print(i, "- renamed", str(extDic[i]))

if __name__ =='__main__':
    main()
