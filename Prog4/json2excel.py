# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# File: json2excel.py
# Author: Matthew Beals User ID: Mbeal872 Class: CPS 110
# Desc: This program takes a .json file or json URL and converts it
# into a working Excel file (.xlsx) format.
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−

import sys
import os
import pandas
import requests

if len(sys.argv) != 3:
    print('Usage: python json2excel.py filename-or-url spreadsheet-filename')
    sys.exit(1)

jsonpoint = sys.argv[1]
xceldoc = sys.argv[2]

if jsonpoint[:3] == "http":
    print(jsonpoint[:3])
    jsonpoint = requests.get(sys.argv[1])
    jsonpoint = jsonpoint.json

pandas.read_json(jsonpoint).to_excel(xceldoc)
