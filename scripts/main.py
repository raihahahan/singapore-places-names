from scrapers.mainWikiScrape import getWikiData
from helpers.constants import inputStr
from helpers.cliHelpers import input_1, input_2, input_3, input_4
from cli.cli import cli
from scripts.helpers.cliHelpers import convertNumToList

def main():
    soup=getWikiData()
    cli(soup)
    
if __name__ == "__main__":
    main()
