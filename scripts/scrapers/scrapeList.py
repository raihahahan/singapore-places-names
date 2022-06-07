import sys
sys.path.append("..") # Adds higher directory to python modules path.
import string
from bs4 import BeautifulSoup
from helpers.helpers import removeBracket, cleanList
from helpers.constants import regionID

def getAllList(soup: BeautifulSoup):
    result = []
    central = get_central_list(soup)
    east = get_east_list(soup)
    north = get_north_list(soup)
    northEast = get_northEast_list(soup)
    west = get_west_list(soup)
    result = central + east + north + northEast + west
    return result

def get_central_list(soup):
    finalResults = []
    
    def get_central():
        centralResults = []
        central_table = soup.find("table", {"class": "wikitable"})
        a = central_table.find_all("a")
        for tag in a:         
            if "title" in tag.attrs:
                centralResults.append(tag.text)
        return centralResults

    if soup:
        central = get_central()
        finalResults += central

        return finalResults
    else:
        return []

def getFromList(id: string, soup: BeautifulSoup):
    finalResults = []
    
    def get_list():
        results = []
        listArr = soup.find("span", {"class": "mw-headline", "id": id})
        for sibling in listArr.parent.next_siblings:
            if sibling.name == "ul":
                for item in sibling: 
                    text=item.text
                    if text.strip() != "":
                        textList = removeBracket(text)
                        results += textList
                break
        results = cleanList(results)

        return results

    if soup:
        res = get_list()
        finalResults += res
        return finalResults
    else:
        return []

def get_east_list(soup: BeautifulSoup):
    return getFromList(regionID["east"], soup)

def get_north_list(soup: BeautifulSoup):
    return getFromList(regionID["north"], soup)

def get_northEast_list(soup: BeautifulSoup):
    return getFromList(regionID["northEast"], soup)

def get_west_list(soup: BeautifulSoup):
    return getFromList(regionID["west"], soup)
