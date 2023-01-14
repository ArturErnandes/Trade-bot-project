from bs4 import BeautifulSoup
import requests

URL = 'https://yandex.com.am/weather/'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
temperature = soup.find_all('div', class_="temp fact__temp fact__temp_size_s")
clear_temperature = [c.text for c in temperature]
print( clear_temperature)