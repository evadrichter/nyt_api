from pynytimes import NYTAPI

apikey = "{yourAPIKey}"
nytapi = pynytimes.NYTAPI(apikey, parse_dates=True)

# importing datetime to be able to specify te publication date
import datetime

# searching for specific articles
articles = nytapi.article_search(
    query = "Climate Change",
    options = {
        "sort": "newest",
        "sources": [
            "New York Times"
        ],
        "news_desk": [
            "OpEd"
        ],
      dates = {
        "begin": datetime.datetime(2020, 1, 1),
        "end": datetime.datetime(2020, 12, 31)
    },
    },
)

# for each of the articles in the list, get the information that is stored in a nested dictionary:
headline = map(lambda x: x["headline"]["main"], articles)
author = map(lambda x: x["headline"]["kicker"], articles)
leadparagraph = map(lambda x: x["lead_paragraph"], articles)
pubdate = map(lambda x: x["pub_date"], articles)

# since keywords are a branch down in the nested dictionary, we need to add an additional for loop to collect all keywords:
keywords = map(lambda x:list(i["value"] for i in x["keywords"]), articles)

# transforming the data into a pandas dataframe:
import pandas as pd
data={'headline': list(headline), 'author': list(author), 'leadparagraph':list(leadparagraph),
     'publication date': list(pubdate), "keywords": list(keywords)}
df = pd.DataFrame(data)

# exporting the data to csv:
df.to_csv('NYT_data.csv')
# exporting the data to excel:
df.to_excel('NYT_data.xslx')
