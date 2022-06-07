from mainWikiScrape import getWikiData
from scrapeList import getAllList
from scrapeDict import getDictByRegion, getDictByPlanningArea_ALL

def main():
    soup=getWikiData()
    # List
    resultsList=[]
    # if soup:
    #     resultsList=getAllList(soup)
    # print(resultsList)

    # Dict, indexed by regions
    resultsDict={}
    # if soup:
    #     resultsDict=getDictByRegion(soup)
    # print(resultsDict)

    # Dict, indexed by regions
    # Each region indexed by Planning Area
    if soup:
        resultsAllDict=getDictByPlanningArea_ALL(soup)
        print(resultsAllDict)
    
if __name__ == "__main__":
    main()
