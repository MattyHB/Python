import os
import sys
import pandas

name = sys.argv[1]
xcell = sys.argv[2]

pandas.read_json(name).to_excel(xcell)