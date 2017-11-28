#! python3
'''Autom8r: log all inputs to a log file (possibly stderr) before echoing them to stdout'''
import sys
import time

try:
    logname = time.strftime(sys.argv[1])    # treat filename as pattern for strftime (%Y, %m, %d, etc.)
    logfile = open(logname, "a")            # open file for appending (not over-writing)
except IndexError:
    logfile = sys.stderr

# For each line of input...
for line in sys.stdin:
    # ...strip newline...
    line = line.rstrip('\n')

    # ...and print them to BOTH stdout AND our logfile
    print(line)
    print(line, file=logfile)

# For legibility, print a divider bar of '-'s to stderr here (if we are logging to stderr)
if logfile is sys.stderr:
    print('-'*60, file=logfile)
else:
    logfile.close()