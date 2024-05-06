import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
k=1
crypto = []
price=[]
capital=[]
perday=[]
url = 'https://finance.yahoo.com/crypto/'
for page in range(1,5):
    u=f'{url}?count={page*25}&offset=0'
    response = requests.get(u)
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        c = soup.find('div', {'id': 'scr-res-table'})
        b = c.find('table', {'class': 'W(100%)'})
        s = b.find('tbody')
        for row in s.find_all('tr'):
            crypto_cell = row.find('td', {'aria-label': 'Name'})
            crypto_name = crypto_cell.text.strip()
            crypto.append(crypto_name)
            price_cell = row.find('td', {'aria-label': 'Price (Intraday)'})
            fin_streamer1 = price_cell.find('fin-streamer', {'data-test': 'colorChange'})
            price.append(fin_streamer1.get('value'))
            market_cell = row.find('td', {'aria-label': 'Market Cap'})
            fin_streamer2 = market_cell.find('fin-streamer', {'data-test': 'colorChange'})
            capital.append(fin_streamer2.get('value'))
            per=row.find('td',{'aria-label':'Total Volume All Currencies (24Hr)'})
            perday.append(per.text.strip())
    else:
        print("Failed to retrieve the web page.")
        k=0
if k:
    df=pd.DataFrame({'crypto_currency_name':crypto,
                     'price(intrady)':price,
                     'market capital':capital,
                     'capital_per_day':perday})
    print(df)