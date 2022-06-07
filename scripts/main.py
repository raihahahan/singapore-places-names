from scrapers.mainWikiScrape import getWikiData
from cli.cli import cli

def main():
    soup=getWikiData()
    cli(soup)
    
if __name__ == "__main__":
    main()
