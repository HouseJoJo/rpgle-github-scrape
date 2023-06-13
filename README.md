# RPGLE Github Scraping

RPGLE Github Scraping is a Python-based program that leverages Github's Code Search REST API to gather data from 1000 RPGLE repositories. The data is then processed using BeautifulSoup to extract the source code, which is compiled into a .csv file using Pandas.
This repo is part of the data aggregation intended to train a small scale coding LLM for RPGLE.

## main.py

Main program that calls Github API with a Code Search query and exports a .csv of relevant data to /file-history folder

## combine.py

Short code to combine multiple .csv files of same headings into one .csv named 'concatenated.csv'
