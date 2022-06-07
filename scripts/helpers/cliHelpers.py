import string

from numpy import number
from scrapers.scrapeList import getAllList, get_central_list, get_east_list, get_north_list, get_northEast_list, get_west_list
from scrapers.scrapeDict import getDictByPlanningArea_ALL, getDictByPlanningArea_central, getDictByRegion, getDictByRegion_east, getDictByRegion_north, getDictByRegion_northEast, getDictByRegion_west

def convertNumToList(num:string, maxNum: number):
    if "0" in num: 
        return ["0"]
    listNum = list(num)
    for item in listNum:
        if (not item.isnumeric()) or int(item) > maxNum:
            return []
    return listNum

input_1 = {
    "0": getAllList,
    "1": get_east_list,
    "2": get_north_list,
    "3": get_northEast_list,
    "4": get_central_list,
    "5": get_west_list
}

input_2 = {
    "0": getDictByRegion,
    "1": get_east_list,
    "2": get_north_list,
    "3": get_northEast_list,
    "4": get_central_list,
    "5": get_west_list
}

input_4 = {
    "0": getDictByPlanningArea_ALL,
    "1": getDictByRegion_east,
    "2": getDictByRegion_north,
    "3": getDictByRegion_northEast,
    "4": getDictByPlanningArea_central,
    "5": getDictByRegion_west
}

input_3 = ["all", "east", "north", "northEast", "central", "west"]