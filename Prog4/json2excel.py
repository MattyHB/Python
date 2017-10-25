import sys
import os
import pandas as pd
import openpyxl
import xlsxwriter
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

pd.read_json(jsonpoint).to_excel(xceldoc)


#https://www.dallasopendata.com/resource/are8-xahz.json