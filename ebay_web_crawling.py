from pathlib import Path
from bs4 import BeautifulSoup
import requests
import time
from pandas import DataFrame

#===============================================================================================================
#=Variables=====================================================================================================
itemList = {
		'Item Name': [],
        'Price': []
        }
inputKey = ""
keys = []
inputEnd = False
#===============================================================================================================
#=Functions=====================================================================================================
def matchFilter(itemName):
	for key in keys:
		if( (key in name.get_text().lower())!=True ):
			return False
	return True
#===============================================================================================================

#Don't forget to add '.csv' at the end of the path
#===============================================================================================================
print("=======================================================================")
print("    This is a program for crawling items from EBay searching result    ")
print("=======================================================================\n")
url = input("Please input an URL of any page of searching result:\n")
#Example: "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone6&_sacat=0&_dmd=1&rt=nc&_prodsch=0&_ipg=200&_pgn=1"
isOnePage = True
if(url[-1].isnumeric()):
	index = url.rfind('=')
	url = url[:index+1]
	isOnePage = False

while (inputEnd==False):
	inputKey = input("\nPlease Input a key word in order to have a precised result:")
	keys.append(inputKey)
	yesOrNo = ""
	while ((yesOrNo=="Y")|(yesOrNo=="y") | (yesOrNo!="n")|(yesOrNo!="N")):
		yesOrNo = input("\nContinue ? (Y/N)")
		if((yesOrNo=='N')|(yesOrNo=='n')):
			inputEnd = True
		break
print(keys)


#=Crawling======================================================================================================
for page in range(1,1000000000):
	if(isOnePage):
		r=requests.get(url)
		c=r.content
		soup = BeautifulSoup(c, 'html.parser')
		items = soup.find_all("li",{"class":'s-item'})
		if (items!=[]):
			for item in items:
				if(item==None):
					print('It is not item')
				else:
					print('It is an item')
					# print (item)
					name = item.find("h3",{"class":'s-item__title'})
					price = item.find("div",{"class":'s-item__detail s-item__detail--primary'})
					print("Item name: ", name.get_text())
					print("Price: ", price.get_text())
					print("Page number: ", page)
					if(matchFilter(name.get_text())):
						itemList["Item Name"].append(name.get_text())
						itemList["Price"].append(price.get_text())
					else:
						print("[DROPPED]")
		else:
			print("BREAK!!!!!!!!!!!!!!!!\n\n")
			break
		print("BREAK!!!!!!!!!!!!!!!!!\n\n")
		break
	else:
		r=requests.get(url+str(page))
		c=r.content
		soup = BeautifulSoup(c, 'html.parser')
		items = soup.find_all("li",{"class":'s-item'})
		if (items!=[]):
			for item in items:
				if(item==None):
					print('It is not item')
				else:
					print('It is an item')
					# print (item)
					name = item.find("h3",{"class":'s-item__title'})
					price = item.find("div",{"class":'s-item__detail s-item__detail--primary'})
					print("Item name: ", name.get_text())
					print("Price: ", price.get_text())
					print("Page number: ", page)
					itemList["Item Name"].append(name.get_text())
					itemList["Price"].append(price.get_text())
		else:
			print("BREAK!!!!!!!!!!!!!!!!!\n\n")
			break
	time.sleep(2)

# print("List: ")
# print(itemList)
print("Exporting CSV...")
df = DataFrame(itemList, columns= ['Item Name', 'Price'])
export_csv = df.to_csv (r'D:\workplace_python\data\export_dataframe.csv', index = None, header=True)
print("Done.")
