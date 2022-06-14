import pandas as pd
from scrapers.scrapeList import getAllList
from scrapers.mainWikiScrape import getWikiData
from scrapers.scrapeDict import getDictByPlanningArea_ALL

soup = getWikiData()
planningAreaData = getDictByPlanningArea_ALL(soup)

# data.to_csv("output/output_data.csv")