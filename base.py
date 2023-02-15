
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

#CLEANING HOMEPAGE AND GETTING TEAM LINK DATA
process = str(raw)

process = process.replace("</a></li>", "")
process = process.replace("<li class=\"product-category product\">", "")
process = process.replace("><img", "")
process = process.replace("\'", "")
process = process.replace("\"", "")
process = process.replace("href=", "")

process = process.split(" ")

process = set([x for x in process if "https://altjerseys.com/team/" in x])

# print(process)

#GETTING THE TEAM DATA

v = "https://altjerseys.com/team/flyers/"

def teamStore(link):
    data = requests.get(link)
    html = BeautifulSoup(data.text, 'html.parser')
    raw = html.find(attrs={'class':'content-full'})

    enter = str(raw)

    enter = enter.replace("</a></li>", "")
    enter = enter.replace("<li class=\"product-category product\">", "")
    enter = enter.replace("><img", "")
    enter = enter.replace("\'", "")
    enter = enter.replace("\"", "")
    enter = enter.replace("href=", "")

    enter = enter.split(" ")

    return set([x for x in enter if "https://altjerseys.com/product/" in x])

def itemPage(link):
    data = requests.get(link)

    html = BeautifulSoup(data.text, 'html.parser')

    return(not "Out of stock" in str(html.find('div', attrs={'class':'summary'})))


z = teamStore(v)
for x in z:
    print(itemPage(x))
