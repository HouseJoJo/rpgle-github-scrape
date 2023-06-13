import requests
import os
from dotenv import load_dotenv
import pandas as pd

#------Program 1 requests and creates .csv from Github API Code Search request-----
#----Default search find ALL RPGLE Code-----

load_dotenv() #LOADS GITHUB TOKEN FOR API CODE SEARCH ACCESS
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

base_url = 'https://api.github.com/search/code'
search_query = 'language:python'
sort_by = 'stars'
request_url = f'{base_url}?q={search_query}&sort={sort_by}'

headers = { #PREPARE API HEADERS
    'Accept': 'application/vnd.github.text-match+json',
    'Authorization': f'token '+AUTH_TOKEN,
    'X-GitHub-Api-Version': '2022-11-28'
    }

totalCount = 0 #counter variable for total API request count
pageCount = 5 #CHANGE pageCount for endpoint
index1 = 0 #CHANGE INDEX1 FOR PAGE START
totalList = []

for index1 in range(index1, pageCount): #Iterate through API Page requests
    link = f'https://api.github.com/search/code?q=language:rpgle&page='+str(index1)
    print('Making request for page ' + str(index1))
    #print(link)
    response = requests.get(link,headers=headers)
    #print(response.status_code)
    #print('PAGENUMBER =>' + str(index1))
    if response.status_code != 200: #Request not fulfilled (Most likely an error)
        json_data = response.json()
        print(json_data)
        break 

    if response.status_code == 200:
        json_data = response.json()
        json_items = json_data['items']
        #print(json_data['total_count'])
        index = 0
        for index in range(30): #Default search returns 30 results per page
            totalCount+=1
            #print(str(totalCount) + ' -> ' + str(index)) #print to view page/item iterations
            tempJsonItem = json_items[index]
            tempList = [tempJsonItem['name'], tempJsonItem['html_url'], tempJsonItem['url'],
                        (tempJsonItem['repository'])['name'], (tempJsonItem['repository'])['description'],
                        totalCount, index1, index
                        ] #Gather all table items
            #print((tempJsonItem['name']))
            totalList.append(tempList)

#Make data table with column headers
df = pd.DataFrame(totalList, columns=['NAME', 'HTML-URL', 'REPO-URL', 'REPO-NAME',
                                      'REPO-DESCRIPTION', 'ENTRY-NUMBER', 'PAGE-NUMBER',
                                      'RELATIVE-ENTRY-NUMBER'])
df.to_csv('./file-history/data1.csv') #Export to .csv file in file-history folder
print('Export complete')