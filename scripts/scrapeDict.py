from bs4 import BeautifulSoup

from scrapeList import get_central_list, get_east_list, get_north_list, get_northEast_list, get_west_list

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
