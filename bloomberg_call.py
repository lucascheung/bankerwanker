import requests

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/get-cross-currencies"

querystring = {"id":"aed%2Caud%2Cbrl%2Ccad%2Cchf%2Ccnh%2Ccny%2Ccop%2Cczk%2Cdkk%2Ceur%2Cgbp%2Chkd%2Chuf%2Cidr%2Cils%2Cinr%2Cjpy%2Ckrw%2Cmxn%2Cmyr%2Cnok%2Cnzd%2Cphp%2Cpln%2Crub%2Csek%2Csgd%2Cthb%2Ctry%2Ctwd%2Cusd%2Czar"}

headers = {
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com",
    'x-rapidapi-key': "5f8c28ffe5mshfbbfda0284d77fap10a115jsn860be8760043"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
