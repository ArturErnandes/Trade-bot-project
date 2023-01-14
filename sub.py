from bs4 import BeautifulSoup
import requests

URL = 'https://ru.tradingview.com/symbols/BTCUSD/'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
btc = soup.find_all('span', class_="tv-symbol-price-quote__value js-symbol-last")
#clear_temperature = [c.text for c in temperature]
print(btc)