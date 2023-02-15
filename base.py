
import requests
from bs4 import BeautifulSoup


homeURL = "https://altjerseys.com/shop/"

def homePage(link):
    data = requests.get(link)
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

    return set([x for x in process if "https://altjerseys.com/team/" in x])

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

    return(set([x for x in enter if "https://altjerseys.com/product/" in x and "sun-hoodie" in x]))


def itemPage(link):
    data = requests.get(link)

    html = BeautifulSoup(data.text, 'html.parser')
    
    return(not "Out of stock" in str(html.find('div', attrs={'class':'summary'})))


for x in homePage(homeURL):
    for y in teamStore(x):
        print(str(itemPage(y)) + ": " + y)