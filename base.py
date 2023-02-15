
import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://altjerseys.com/shop/"
# url = "https://cs.trinity.edu/~hcolema1/"

data = requests.get(url)

# print(data.headers)

# print(data.text)

html = BeautifulSoup(data.text, 'html.parser')

raw = html.find('div', attrs={'class':'content-full'})

process = str(raw)

process = process.replace("</a></li>", "")
process = process.replace("<li class=\"product-category product\">", "")
process = process.replace("><img", "")
process = process.replace("\'", "")
process = process.replace("\"", "")
process = process.replace("href=", "")

process = process.split(" ")

# process = [x for x in process if "team" in x]
process = [x for x in process if "https://altjerseys.com/team/" in x]

print(process)

print(len(process))

# print(articles)
#

# <a href="https://altjerseys.com/team/zoodisc/">

# process = [x for x in process if x.startswith("https://altjerseys.com/team/")]
