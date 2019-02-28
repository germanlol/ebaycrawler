from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
import os


print("=======================================================================")
print("                  This is a program to read CSV file                   ")
print("=======================================================================\n")

fileName = input("What do you want?  (without the extension) \n")
isExist = os.path.exists('./data/'+fileName+'.csv')

print(isExist)

if(isExist):
	data = pd.read_csv('./data/'+fileName+'.csv') 
	# print(data.iloc[0][1])
	# print(data.iloc)
	print("You'r in")
	print(data.to_string())



