import pprint
from dotenv import load_dotenv
import csv
import json
import os
import pandas as pd
import requests
import urllib.parse
from newsapi import NewsApiClient

from googleapiclient.discovery import build
from IPython import embed
from historical_data import get_historical_data

load_dotenv()

def sentiment_analysis(text):
    url = "https://text-sentiment.p.rapidapi.com/analyze"
    formatted = text.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    formatted = urllib.parse.quote(formatted)
    payload = f"text={formatted}"
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


def search_bloomberg_news(query):
  key = os.getenv("GOOGLE_CSE_API_KEY")
  service = build("customsearch", "v1",
            developerKey=key)

  page_size = 10
  offset = 1
  more_pages = True
  final = []
  while more_pages and offset < 100:
    res = service.cse().list(
        q=query,
        cx='002823925215809699006:zouiii0rfzq',
        num=10,
        start=offset
      ).execute()
    if 'items' in res:
      # pprint.pprint(res)
      for article in res['items']:
        entry = {}
        entry['content'] = article['pagemap']['metatags'][0]['og:description']
        entry['publish_time'] = article['pagemap']['metatags'][0]['iso-8601-publish-date']
        final.append(entry)
    else:
      print('no news')
    offset += page_size
  news_df = pd.DataFrame.from_dict(final)
  news_df['s_publish_time'] = news_df['publish_time'].apply(lambda x: x[:10])
  news_df['s_publish_time'] = pd.to_datetime(news_df['s_publish_time'], utc=True)

  # news_df['publish_time'] = pd.to_datetime(news_df['publish_time'])

  # Apply sentiment score
  news_df['sentiment'] = news_df['content'].apply(lambda x: sentiment_analysis(x))

  news_df.to_csv('bloomberg_news.csv')
  # print (news_df)
  return news_df

if __name__ == '__main__':
  news_df = search_bloomberg_news('tsla')
  print(news_df)



