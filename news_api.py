import requests
import urllib.parse
import csv
import json
import pandas as pd
import re
from dotenv import load_dotenv
import os

from newsapi import NewsApiClient

load_dotenv()

def sentiment_analysis(text):
    url = "https://text-sentiment.p.rapidapi.com/analyze"
    formatted = text.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    formatted = urllib.parse.quote(formatted)
    payload = f"text={formatted}"
    print (payload)
    headers = {
        'x-rapidapi-host': "text-sentiment.p.rapidapi.com",
        'x-rapidapi-key': os.getenv("RAPID_API_KEY"),
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    score = 0
    score += response.json()['pos']
    score -= response.json()['neg']
    return score




# Init
newsapi = NewsApiClient(api_key='4ff2056a11a24d6fb2cca23f2f37b6c5')

all_articles = newsapi.get_everything(q='tsla',
                                    #   sources='bbc-news,the-verge',
                                    #   domains='bbc.co.uk,techcrunch.com',
                                      from_param='2019-12-01',
                                      to='2019-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page_size=100,
                                      page=1)       


news_df = pd.DataFrame.from_dict(all_articles['articles'])

news_df = news_df[['source','author','title','publishedAt']]
news_df['source'] = news_df['source'].apply(lambda x: x['name'])
news_df['sentiment'] = news_df['title'].apply(lambda x: sentiment_analysis(x))

news_df.to_csv('news_data.csv')

