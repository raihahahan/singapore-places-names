from helpers import getWikiData
from scrapeList import getAllList
from scrapeDict import getDictByRegion

def main():
    soup=getWikiData()
    # List
    resultsList=[]
    # if soup:
    #     resultsList=getAllList(soup)
    # print(results)

    # Dict, indexed by regions
    resultsDict={}
    if soup:
        resultsDict=getDictByRegion(soup)
    print(resultsDict)

    # Dict, indexed by regions
    # Each region indexed by Planning Area
    
if __name__ == "__main__":
    main()
