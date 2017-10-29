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
    try:
        jsonpoint = requests.get(sys.argv[1])
    except Exception as e:
        print("The URL you submitted is unavalible.")
        print('Usage: python json2excel.py filename-or-url spreadsheet-filename')
        sys.exit(1)
    jsonpoint = jsonpoint.json

try:
    pandas.read_json(jsonpoint)
except Exception as e:
    print("The URL you submitted is unavalible.")
    print('Usage: python json2excel.py filename-or-url spreadsheet-filename')

pandas.read_json(jsonpoint).to_excel(xceldoc)
