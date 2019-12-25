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
  # tsla_data is a pandas dataframe, tsla_meta_data is a dict
  tsla_data, tsla_meta_data = ts.get_daily(symbol=stock, outputsize='full')
  # tsla_data, tsla_meta_data = ts.get_intraday(symbol='TSLA',interval='60min', outputsize='full')

  # tsla_sma is a dict, tsla_meta_sma also a dict
  # tsla_sma, tsla_meta_sma = ti.get_sma(symbol='TSLA')

  tsla_data['day_change'] = tsla_data['4. close'] - tsla_data['1. open']
  tsla_data['percentage_change'] = tsla_data['day_change'] / tsla_data['1. open']


  # print (tsla_data)
  return tsla_data
  # print(tsla_meta_data)


if __name__ == '__main__':
  get_historical_data('TSLA')
