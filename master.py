# import pprint
# from dotenv import load_dotenv
# import csv
# import json
# import os
import pandas as pd
# import requests
# import urllib.parse
# from newsapi import NewsApiClient
# from googleapiclient.discovery import build
from IPython import embed

from historical_data import get_historical_data
from searchapi import sentiment_analysis, search_bloomberg_news


# load_dotenv()

if __name__ == '__main__':
  news_df = search_bloomberg_news('tsla')
  historical_df = get_historical_data('TSLA')
  final_df = pd.merge(news_df, historical_df, how='inner', left_on='publish_time', right_index=True)
  embed()
  final_df['accurate'] = final_df['sentiment'] * final_df['percentage_change']

  final_df.to_csv('final.csv')



  print(news_df)
  print(historical_df)
  print(final_df)
