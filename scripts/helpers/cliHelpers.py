from bs4 import BeautifulSoup

from scrapers.scrapeList import getAllList, get_central_list, get_east_list, get_north_list, get_northEast_list, get_west_list
from scrapers.scrapeDict import getDictByPlanningArea_ALL, getDictByPlanningArea_central, getDictByRegion, getDictByPlanningArea_east, getDictByPlanningArea_north, getDictByPlanningArea_northEast, getDictByPlanningArea_west
from helpers.constants import inputStr

def convertNumToList(num:str, maxNum: int):
    if "0" in num: 
        return ["0"]
    listNum = list(num)
    for item in listNum:
        if (not item.isnumeric()) or int(item) > maxNum:
            return []
    return list(set(listNum))

input_1 = {
    # to get data as list
    "0": getAllList,
    "1": get_east_list,
    "2": get_north_list,
    "3": get_northEast_list,
    "4": get_central_list,
    "5": get_west_list
}

input_2 = {
    # to get data by region
    "0": getDictByRegion,
    "1": get_east_list,
    "2": get_north_list,
    "3": get_northEast_list,
    "4": get_central_list,
    "5": get_west_list
}

input_4 = {
    # to get data by planning area
    "0": getDictByPlanningArea_ALL,
    "1": getDictByPlanningArea_east,
    "2": getDictByPlanningArea_north,
    "3": getDictByPlanningArea_northEast,
    "4": getDictByPlanningArea_central,
    "5": getDictByPlanningArea_west
}

input_3 = ["all", "east", "north", "northEast", "central", "west"]

def listCase(soup: BeautifulSoup, cli):
    data = input(inputStr[1])
    while True:
        if data=="q":
            return
        if data=="b":
            return cli(soup)
        if data=="i":
            print(inputStr[1])
        if data.isnumeric():
            if "0" in data:
                print(input_1["0"](soup))
            elif len(data)==1:
                if int(data) in range(6):
                    print(input_1[data](soup))
            else:
                numArr=convertNumToList(data, 5)
                finalRes=[]
                for i in numArr:
                    finalRes+=input_1[i](soup)
                print(finalRes)
        data=input()

def dictCase(soup: BeautifulSoup, cli):
    data = input(inputStr[2])
    while True:
        if data=="q":
            return
        if data=="b":
            return cli(soup)
        if data=="i":
            print(inputStr[2])
        if data == "0" or data=="1":
            match data:
                case "0":
                    dictCaseByRegion(soup, cli)
                    return
                case "1":
                    dictCaseByRegionAndPlanning(soup, cli)
                    return
        data=input()

def dictCaseByRegion(soup: BeautifulSoup, cli):
    q=input(inputStr[1])
    while True:
        if q=="q":
            return
        if q=="b":
            return cli(soup)
        if q=="i":
            print(inputStr[1])
        if q.isnumeric():
            if "0" in q:
                print(input_2["0"](soup))
            elif len(q)==1:
                if int(q) in range(6):
                    key=input_3[int(q)]
                    item={key: input_2[q](soup)}
                    print(item)
            else:
                numArr=convertNumToList(q, 5)
                finalRes={}
                for i in numArr:
                    finalRes[input_3[int(i)]] = input_2[i](soup)
                print(finalRes)
        q=input()

def dictCaseByRegionAndPlanning(soup:BeautifulSoup, cli):
    p=input(inputStr[1])
    while True:
        if p=="q":
            return
        if p=="b":
            return cli(soup)
        if p=="i":
            print(inputStr[1])
        if p.isnumeric():
            if "0" in p:
                print(input_4["0"](soup))
            elif len(p)==1:
                if int(p) in range(6):
                    key=input_3[int(p)]
                    item={key: input_4[p](soup)}
                    print(item)
            else:
                numArr=convertNumToList(p, 5)
                finalRes={}
                for i in numArr:
                    finalRes[input_3[int(i)]] = input_4[i](soup)
                print(finalRes)
        p=input()