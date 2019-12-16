import requests
import csv
import json
import pandas as pd

from newsapi import NewsApiClient

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

news_df = news_df[['source','author','title','description','publishedAt']]
news_df['source'] = news_df['source'].apply(lambda x: x['name'])

news_df.to_csv('news_data.csv')