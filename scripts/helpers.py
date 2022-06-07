import string
import requests 
from bs4 import BeautifulSoup

def getWikiData():
    try:
        wikiURL = "https://en.wikipedia.org/wiki/List_of_places_in_Singapore"
        response=requests.get(wikiURL)
        if (response.status_code != 200):
            print("[Error] Web scraping is not allowing in this URL: ", wikiURL)
            return []
        
        return BeautifulSoup(response.text, "html.parser")
    
    except: 
        print("An exception occurred")
        return []

def removeBracket(text: string):
    planningArea=text
    indexBracket = planningArea.find("[")
    endOfPlanningArea = planningArea.find("\n")
    if indexBracket != -1:
        planningArea = text[0:indexBracket]
    textList = planningArea + "\n" + text[endOfPlanningArea: len(text)]
    return textList.split("\n")

def cleanList(list: list):
    return filter(lambda i: i.strip() != "" and i != "]", list)