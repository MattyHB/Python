import sys

def searchfile(readfile, word2find):
    lineNum = 1
    for line in readfile:
        if word2find in line:
            print("Found in line", lineNum)
        lineNum += 1
# ------------ main script -----------------

if len(sys.argv) != 3:
    print("Usage: findword.py filename word")
    sys.exit(1)

filename = sys.argv[1]
word = sys.argv[2]

if filename == '-':
    searchfile(sys.stdin, word)
else:
    try:
        with open(filename) as readfile:
            searchfile(readfile, word)
    except FileNotFoundError as e:
        print("File not found!")