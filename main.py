import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

base_url = 'https://api.github.com/search/code'
search_query = 'language:python'
sort_by = 'stars'
request_url = f'{base_url}?q={search_query}&sort={sort_by}'
query = 'language: rpgle'
params = {
    'q': query,
    'sort': 'stars'
}

headers = {
    'Accept': 'application/vnd.github.text-match+json',
    'Authorization': f'token '+AUTH_TOKEN,
    'X-GitHub-Api-Version': '2022-11-28'
    }

#response = requests.get(request_url, params=params, headers=headers)
totalCount = 0
pageCount = 50
index1 = 36
totalList = []

for index1 in range(index1, pageCount):
    link = f'https://api.github.com/search/code?q=language:rpgle&page='+str(index1)
    print(link)
    response = requests.get(link,headers=headers)
    print(response.status_code)
    print('PAGENUMBER =>' + str(index1))
    if response.status_code != 200:
        json_data = response.json()
        print(json_data)
        break 

    if response.status_code == 200:
        json_data = response.json()
        json_items = json_data['items']
        print(json_data['total_count'])
        index = 0
        for index in range(30):
            totalCount+=1
            print(str(totalCount) + ' -> ' + str(index))
            tempJsonItem = json_items[index]
            tempList = [tempJsonItem['name'], tempJsonItem['html_url'], tempJsonItem['url'],
                        (tempJsonItem['repository'])['name'], (tempJsonItem['repository'])['description'],
                        totalCount, index1, index
                        ]
            print((tempJsonItem['name']))
            totalList.append(tempList)


df = pd.DataFrame(totalList, columns=['NAME', 'HTML-URL', 'REPO-URL', 'REPO-NAME',
                                      'REPO-DESCRIPTION', 'ENTRY-NUMBER', 'PAGE-NUMBER',
                                      'RELATIVE-ENTRY-NUMBER'])
df.to_csv('data.csv')