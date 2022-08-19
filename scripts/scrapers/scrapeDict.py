import string
from bs4 import BeautifulSoup, ResultSet
from .scrapeList import get_central_list, get_east_list, get_north_list, get_northEast_list, get_west_list
from helpers.helpers import cleanList, removeBracket, cleanItem
from helpers.constants import regionID

def getDictByRegion(soup: BeautifulSoup):
    central = get_central_list(soup)
    east = get_east_list(soup)
    north = get_north_list(soup)
    northEast = get_northEast_list(soup)
    west = get_west_list(soup)

    return {
        "east": east,
        "west": west,
        "north": north,
        "central": central,
        "northEast": northEast
    }

# def getDictByPlanningArea_central(soup:BeautifulSoup):
#     finalResults = {}
    
#     def get_central():
#         centralResults = {}
#         sizeList=[]
#         tmpItemList=[]
#         central_table = soup.find("table", {"class": "wikitable"})
#         a: ResultSet = central_table.find_all("td")
#         for tag in a:         
#             if "rowspan" in tag.attrs:
#                 size = int(tag.attrs["rowspan"])
#                 item = tag.findChild().text
#                 sizeList.append({ "name": item, "size": size })
#                 centralResults[item] = []
#         i = 0
#         tmpItemListIndex=0
#         for tag in a:
#             if "rowspan" not in tag.attrs:
#                 if tag.text.strip() != "":
#                     tmpItemList.append(tag.text[:-1])

#         for obj in sizeList:
#             currSize=sizeList[i]["size"]
#             for j in range(tmpItemListIndex, currSize + tmpItemListIndex):
#                 centralResults[sizeList[i]["name"]].append(cleanItem(tmpItemList[j]))
#             tmpItemListIndex += currSize
#             i += 1
#         return centralResults

#     if soup:
#         central = get_central()
#         finalResults = central

#         return finalResults
#     else:
#         return {}

def getDictByPlanningArea(soup: BeautifulSoup, id: string):
    finalResults = {}
    def getDict_helper():
        results={}
        sizeList=[]
        tmpItemList=[]
        table_header = soup.find("span", { "class": "mw-headline", "id": id})
        for sibling in table_header.parent.next_siblings:
            if (sibling.name == "table"):
                list_table = sibling
                a: ResultSet = list_table.find_all("td")
                for tag in a:         
                    if "rowspan" in tag.attrs:
                        size = int(tag.attrs["rowspan"])
                        item = tag.findChild().text
                        sizeList.append({ "name": item, "size": size })
                        results[item] = []
                i = 0
                tmpItemListIndex=0
                for tag in a:
                    if "rowspan" not in tag.attrs:
                        if tag.text.strip() != "":
                            tmpItemList.append(tag.text[:-1])

                for obj in sizeList:
                    currSize=sizeList[i]["size"]
                    for j in range(tmpItemListIndex, currSize + tmpItemListIndex):
                        results[sizeList[i]["name"]].append(cleanItem(tmpItemList[j]))
                    tmpItemListIndex += currSize
                    i += 1
                return results
    
    if soup:
        central = getDict_helper()
        finalResults = central
        return finalResults
    else:
        return {}

# def getDictByPlanningArea_others(soup: BeautifulSoup, id: string):
#     finalResults = {}
    
#     def get_list():
#         results = {}
#         listArr = soup.find("span", {"class": "mw-headline", "id": id})
#         for sibling in listArr.parent.next_siblings:
#             if sibling.name == "ul":
#                 for item in sibling: 
#                     text=item.text
#                     if text.strip() != "":
#                         textList = removeBracket(text)
#                         cleanerList=[]
#                         for txt in textList:
#                             cleanerList.append(cleanItem(txt))
#                         firstItem = cleanerList.pop(0)
#                         otherItems = list(cleanList(cleanerList))
#                         results[firstItem] = otherItems 
#                 break
#         return results

#     if soup:
#         finalResults = get_list()
#         return finalResults
#     else:
#         return []

def getDictByPlanningArea_east(soup: BeautifulSoup):
    return getDictByPlanningArea(soup, regionID["east"])

def getDictByPlanningArea_north(soup: BeautifulSoup):
    return getDictByPlanningArea(soup, regionID["north"])

def getDictByPlanningArea_northEast(soup: BeautifulSoup):
    return getDictByPlanningArea(soup, regionID["northEast"])

def getDictByPlanningArea_west(soup: BeautifulSoup):
    return getDictByPlanningArea(soup, regionID["west"])

def getDictByPlanningArea_central(soup: BeautifulSoup):
    return getDictByPlanningArea(soup, regionID["central"])


def getDictByPlanningArea_ALL(soup: BeautifulSoup):
    central = getDictByPlanningArea_central(soup)
    east = getDictByPlanningArea_east(soup)
    north = getDictByPlanningArea_north(soup)
    northEast = getDictByPlanningArea_northEast(soup)
    west = getDictByPlanningArea_west(soup)

    return {
        "east": east,
        "west": west,
        "north": north,
        "central": central,
        "northEast": northEast
    }