import pandas as pd
import os

# Program takes ALL .csv files in /file-history folder and combines into one .csv
# 'concatenated.csv' for processing

files = os.listdir('./file-history')
datafiles = []
for file in files:
    datafiles.append(pd.read_csv('./file-history/' + file))


concat = pd.concat(datafiles)
concat.to_csv('./file-history/concatenated.csv')