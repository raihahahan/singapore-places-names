from helpers import getWikiData
from scrapeList import getAllList

def main():
    # List
    results=[]
    soup=getWikiData()
    if soup:
        results+=getAllList(soup)
    print(results)

    # Dict, indexed by regions

    # Dict, indexed by regions
    # Each region indexed by Planning Area
    
if __name__ == "__main__":
    main()
