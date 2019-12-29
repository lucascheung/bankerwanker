import pandas as pd
from IPython import embed

from historical_data import get_historical_data
from searchapi import sentiment_analysis, search_bloomberg_news


if __name__ == '__main__':
  news_df = search_bloomberg_news('tsla')
  historical_df = get_historical_data('TSLA')

  news_match_data_df = pd.merge(news_df, historical_df, how='inner', left_on='s_publish_time', right_index=True)
  news_match_data_df['same_day_accuracy'] = news_match_data_df['sentiment'] * news_match_data_df['same_day_percentage_change']
  news_match_data_df['1_day_accuracy'] = news_match_data_df['sentiment'] * news_match_data_df['1_day_percentage_change']
  news_match_data_df.to_csv('news_match_data.csv')

  data_match_news_df = pd.merge(news_df, historical_df, how='outer', left_on='s_publish_time', right_index=True)
  data_match_news_df['same_day_accuracy'] = data_match_news_df['sentiment'] * data_match_news_df['same_day_percentage_change']
  data_match_news_df['1_day_accuracy'] = data_match_news_df['sentiment'] * data_match_news_df['1_day_percentage_change']
  data_match_news_df.to_csv('data_match_news_df.csv')


  print(news_df)
  print(historical_df)
  print(news_match_data_df)
