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

def get_list(soup: BeautifulSoup, id: str):
    finalResults = []
    def get_list_helper():
        listResults = []
        table_header = soup.find("span", { "class": "mw-headline", "id": id})
        for sibling in table_header.parent.next_siblings:
            if sibling.name == "table":
                list_table = sibling
                a = list_table.find_all("a")
                for tag in a:         
                    if "title" in tag.attrs:
                        listResults.append(tag.text)
                return listResults

    if soup:
        list = get_list_helper()
        finalResults += list

        return finalResults
    else:
        return []
    
def get_east_list(soup: BeautifulSoup):
    return get_list(soup, regionID["east"])

def get_north_list(soup: BeautifulSoup):
    return get_list(soup, regionID["north"])

def get_northEast_list(soup: BeautifulSoup):
    return get_list(soup, regionID["northEast"])

def get_west_list(soup: BeautifulSoup):
    return get_list(soup, regionID["west"])

def get_central_list(soup: BeautifulSoup):
    return get_list(soup, regionID["central"])
