import os
import time
import sys
import shutil

try:
    chosenFolder = sys.argv[1]
    fileType = sys.argv[2]
except FileNotFoundError as e:
    print('Usage: python rename.py folder-name ext1,ext2,ext3,…')


def rename(folder, type: str):
    for  i in fileType:
        fileType.split(',')

    if fileType in :
        os.rename()

def main():
    rename():


if __name__ =='__main__':
    main()
