import pandas as pd

df = pd.read_csv('concatenated.csv')

def prepareUrl(url):
    out = ''
    out = url.replace('github.com', 'raw.githubusercontent.com')
    out = out.replace('/blob', '')
    return out

df['RAW'] = df['HTML-URL'].apply(prepareUrl)

print(df['RAW'])
df.to_csv('processedURL-concat.csv')

