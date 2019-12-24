import pprint
from dotenv import load_dotenv
import os

from googleapiclient.discovery import build
from IPython import embed

load_dotenv()


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
      entry = {}
      entry['content'] = res['items'][0]['pagemap']['metatags'][0]['og:description']
      entry['publish_time'] = res['items'][0]['pagemap']['metatags'][0]['iso-8601-publish-date']
      final.append(entry)
    else:
      print('no news')
    offset += page_size
  print (final)

if __name__ == '__main__':
  search_bloomberg_news('tsla')


