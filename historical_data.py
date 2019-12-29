from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from dotenv import load_dotenv
import os
from IPython import embed

load_dotenv()


def get_historical_data(stock):
  # Your key here
  key = os.getenv("ALPHA_VANTAGE_API_KEY")
  # Chose your output format, or default to JSON (python dict)
  ts = TimeSeries(key, output_format='pandas')
  ti = TechIndicators(key)

  # Get the data, returns a tuple
  # stock_data is a pandas dataframe, stock_meta_data is a dict
  stock_data, stock_meta_data = ts.get_daily(symbol=stock, outputsize='full')
  # stock_data, stock_meta_data = ts.get_intraday(symbol='TSLA',interval='60min', outputsize='full')

  # stock_sma is a dict, stock_meta_sma also a dict
  # stock_sma, stock_meta_sma = ti.get_sma(symbol='TSLA')

  stock_data['same_day_change'] = stock_data['4. close'] - stock_data['1. open']
  stock_data['same_day_percentage_change'] = stock_data['same_day_change'] / stock_data['1. open']

  stock_data['1_day_change'] = stock_data['4. close'].diff()
  stock_data['1_day_percentage_change'] = stock_data['4. close'].pct_change()

  # embed()


  stock_data.index = stock_data.index.astype('datetime64[ns, UTC]')
  # stock_data = stock_data.shift(1)

  # embed()

  print (stock_data)
  return stock_data
  # print(stock_meta_data)


if __name__ == '__main__':
  get_historical_data('TSLA')
