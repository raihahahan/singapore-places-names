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
- `scripts/`: the Python scripts for the CLI program.
- `scripts/cli/`: Python script for the CLI.
- `scripts/scrapers/scrapeDict.py`: Python scripts for the webscraper. Files in this folder contain the main code for webscraping. Some of the program logic are abstracted into helper functions in `helpers/helpers.py`. These helpers usually handle the logic behind cleaning the data and to structure them as lists/dict.
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
