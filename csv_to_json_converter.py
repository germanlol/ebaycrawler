import csv  
import json  
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
import os
  
print("=======================================================================")
print("            This is a program to convert CSV file into JSON            ")
print("=======================================================================\n")


fileName = input("What do you want?  (without the extension) \n")
isExist = os.path.exists('./data/'+fileName+'.csv')

if(isExist):
	print("CSV is found.")
	# Open the CSV  
	f = open( './data/'+fileName+'.csv', 'r' )  
	# Change each fieldname to the appropriate field name.
	reader = csv.DictReader( f, fieldnames = ( "Item Name","Price" ))  
	# Parse the CSV into JSON  
	out = json.dumps( [ row for row in reader ] )  
	print ("JSON parsed!")  
	# Save the JSON  
	f = open( './data/json/'+fileName+'.json', 'w')  
	f.write(out)  
	print ("JSON saved!") 
else:
	print("CSV doesn't exist")