# Documentation

## Quick start
   ```sh
   git clone https://github.com/raihahahan/singapore-places-names.git
   cd singapore-places-names
   pip install -r requirements.txt
   python scripts/main.py
   ```

## Folder structure
The project has the following folder structure:
```
sg-places-list/
    output/
        dict/
        list/
    scripts/
        cli/
        helpers/
        scrapers/
        main.py
```
- `output/`: preset text output files containing results from the CLI program. This is useful as a quick reference to copy text from.
- `scripts/`: All the Python scripts for this project.
- `scripts/cli/`: Python script for the CLI.
- `scripts/scrapers/`: Python scripts for the webscraper. Files in this folder contain the main code for webscraping. Some of the program logic are abstracted into helper functions in `helpers/helpers.py`. These helpers usually handle the logic behind cleaning the data and to structure them as lists/dict.
- `scripts/helpers`: helper functions

## Files
- `main.py`: The file that will be run in the command line. No changes required in this file as everything is abstracted into the `cli(soup: BeautifulSoup)` function.
- `cli/cli.py`: Contains the interface for the command line. Modify this file only if there are any changes to the flow of the CLI program. Else, other CLI logic are abstracted into helper functions found in `helpers/cliHelpers`. Constants such as printed texts are found in `helpers/constants.py`
- `scrapers/mainWikiScrape.py`: The script to fetch data from the Wikipedia site. The `getWikiData()` function in this script returns a BeautifulSoup object (i.e `return BeautifulSoup(response.text, "html.parser")`) 
- `scrapers/scrapeDict.py`: Converts the BeautifulSoup object into a dict structure.
- `scrapers/scrapeList.py`: Converts the BeautifulSoup object into a list structure.
- `helpers/`: Folder containing all the helper functions.

## How the program works
- `getWikiData()` in `scrapers/mainWikiScrape.py` returns a BeautifulSoup object. This is the only script which fetches data from the Wikipedia site.
- Functions in `scrapeDict.py` and `scrapeList.py` take in the BeautifulSoup object as an argument and return the data in the desired data structure. These conversions are aided with helpers from `helpers/`.
- `cli.py` controls the user interface of the command line program. It contains the `cli` function which takes in the BeautifulSoup object as an argument and pass this down to the respective functions created in `scrapers/`.
- `main.py` calls `soup=getWikiData()` and passes `soup` as an argument to `cli(soup)`. This ensures that `getWikiData()` is only called once.

## Contributing
See the current issues [here](https://github.com/raihahahan/singapore-places-names/issues). 

## Function reference
|      Name     |  Description   |
| -------------  |----------------|
| `getWikiData()` | Fetches data from the https://en.wikipedia.org/wiki/List_of_places_in_Singapore#cite_note-8. If no error, returns a `BeautifulSoup` object. Else, returns `None`.|
| `getDictByRegion(soup: BeautifulSoup)`   |Takes in a `BeautifulSoup` object as argument. Returns a `dict` containing all the key places in Singapore, with "east", "northEast", "central", "west", "north" as the keys, and a list of all the places in that region as the values.| 
| `getDictByPlanningArea_all(soup: BeautifulSoup)` |Takes in a `BeautifulSoup` object as argument. Returns a `dict` containing all the key places in Singapore, with "east", "northEast", "central", "west", "north" as the keys. Each value is a `dict` keyed by the Planning Areas of that region, and each value is the list of places in that Planning Area.|
| `getAllList(soup: BeautifulSoup)`  |Takes in a `BeautifulSoup` object as argument. Returns a `list` containing all the places in Singapore (which were fetched from the site)|

The scraper functions above each contains their respective helper functions to get the `list`/`dict` by region. See examples below.

## Examples
```py
soup = getWikiData()

all_list = getAllList(soup)
east_list = get_east_list(soup)
west_list = get_west_list(soup)

all_byRegion_dict = getDictByRegion(soup)
east_byRegion_dict = getDictByRegion_east(soup)
west_byRegion_dict = getDictByRegion_west(soup)

all_byPlanningAreaAndRegion_dict = getDictByPlanningArea_all(soup)
east_byPlanningAreaAndRegion_dict = getDictByPlanningArea_east(soup)
west_byPlanningAreaAndRegion_dict = getDictByPlanningArea_west(soup)

```
