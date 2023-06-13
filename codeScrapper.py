import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.read_csv('./file-history/concatenated.csv')

def prepareUrl(url): #reformats HTML-URL to redirect to raw code for scraping
    out = ''
    out = url.replace('github.com', 'raw.githubusercontent.com')
    out = out.replace('/blob', '')
    return out

df['RAW'] = df['HTML-URL'].apply(prepareUrl)

urlList = df['RAW']
print('URL editing complete')

def fetchCode(url): #Calls BeautifulSoup to grab code from altered URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()
        
print('start')
df['CODE'] = urlList.apply(fetchCode) 
#1108 Entries will take ~220 Seconds to fetch all data (WILL VARY ON CONNECTION SPEED)

df.to_csv('./file-history/finalTable.csv')
print('finalTable.csv created')