import pandas as pd
from bs4 import BeautifulSoup
import requests
import sys
import time
import lxml

df = pd.read_csv('processedURL-concat.csv')

urlList = df['RAW']

def fetchCode(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()
        
print('start')
df['CODE'] = urlList.apply(fetchCode) #1108 Entries will take ~220 Seconds to fetch all data

df.to_csv('finalTable.csv')