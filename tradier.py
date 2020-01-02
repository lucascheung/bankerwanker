import http.client
import os
from dotenv import load_dotenv

load_dotenv()

# Request: Market Quotes (https://sandbox.tradier.com/v1/markets/quotes?symbols=spy)

connection = http.client.HTTPSConnection('sandbox.tradier.com', 443, timeout = 30)

# Headers
API_KEY = os.getenv('TRADIER_API_KEY')

headers = {"Accept":"application/json",
           "Authorization":f"Bearer {API_KEY}"}

# Send synchronously

connection.request('GET', '/v1/markets/quotes?symbols=spy', None, headers)
try:
  response = connection.getresponse()
  content = response.read()
  print(content)
  # Success
  print('Response status ' + str(response.status))
except http.client.HTTPException as e:
  # Exception
  print('Exception during request')
