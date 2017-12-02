#! python3
'''Autom8r: filter input lines using wildcard globs

WARNING: starting implementation supports only 1 glob pattern exactly
        (some challenges require support for more patterns)
'''
import fnmatch
import sys

# Get glob pattern as argument (or fail with usage message)
try:
    pattern = sys.argv[1]
except IndexError:
    print("usage: match.py GLOB_PATTERN", file=sys.stderr)
    exit(1)

# For each line of input...
for line in sys.stdin:
    # ...strip newline...
    line = line.rstrip('\n')

    # ...and if it matches our glob pattern...
    if fnmatch.fnmatch(line, pattern):
        # ...dump it to our output.
        print(line)