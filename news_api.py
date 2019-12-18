import requests
import csv
import json
import pandas as pd

from newsapi import NewsApiClient


def sentiment_analysis(text):
    url = "https://text-sentiment.p.rapidapi.com/analyze"

    payload = text
    headers = {
        'x-rapidapi-host': "text-sentiment.p.rapidapi.com",
        'x-rapidapi-key': "5f8c28ffe5mshfbbfda0284d77fap10a115jsn860be8760043",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)


    print(response.text)
    return response.text


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
news_df['sentiment'] = news_df['description'].apply(lambda x: sentiment_analysis(x))

news_df.to_csv('news_data.csv')

