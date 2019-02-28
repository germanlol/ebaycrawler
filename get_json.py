import csv  
import json  
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
import os
  
print("=======================================================================")
print("                   This is a program to read JSON file                 ")
print("=======================================================================\n")


fileName = input("What do you want?  (without the extension) \n")
isExist = os.path.exists('./data/json/'+fileName+'.json')

if(isExist):
	print("JSON is found.")
	with open('./data/json/'+fileName+'.json' , 'r') as reader:
		jf = json.loads(reader.read())
	for row in jf:
		print("Item Name:  ", row["Item Name"])
		print("Price:  ", row["Price"])
	
else:
	print("JSON doesn't exist")