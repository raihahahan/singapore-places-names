import requests 
from bs4 import BeautifulSoup

def getWikiData():
    try:
        wikiURL = "https://en.wikipedia.org/wiki/List_of_places_in_Singapore"
        response=requests.get(wikiURL)
        if (response.status_code != 200):
            print("[Error] Web scraping is not allowed in this URL: ", wikiURL)
            return None
        
        return BeautifulSoup(response.text, "html.parser")
    
    except: 
        print("An exception occurred")
        return None