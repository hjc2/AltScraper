
import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://altjerseys.com/product/turbulence-neckie/"
# url = "https://altjerseys.com/product/2f2f-reversible/"

data = requests.get(url)

html = BeautifulSoup(data.text, 'html.parser')

raw = html.find('div', attrs={'class':'summary'})

process = str(raw)

# print(process.find("Out of stock"))

print(process)

print("Out of stock" in process)
