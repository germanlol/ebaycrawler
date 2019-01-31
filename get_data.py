from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_csv('./data/export_dataframe.csv') 


print(data.iloc[0][1])
