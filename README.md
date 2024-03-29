<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** raihahahan, singapore-places-names, twitter_handle, muhdraihan1140@gmail.com, Singapore Key Places Names, This repo contains the names of key places in Singapore (e.g. Bishan, Bedok, Tampines) in different data structures. You can either view the output text files, or use the command line program shown below.
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->
# Singapore Key Places Names

<!-- PROJECT LOGO -->
<br />
<p align="center">
<!--   <a href="https://github.com/raihahahan/singapore-places-names">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->
<!-- 
  <h3 align="center">Singapore Key Places Names</h3> -->

  <p align="center">
    This repo contains the names of key places in Singapore (e.g. Bishan, Bedok, Tampines) in different data structures. You can either view the <a href="https://github.com/raihahahan/singapore-places-names/tree/main/output">preset output text files</a>, or use the command line program shown below.
    <br />
<!--     <a href="https://github.com/raihahahan/README-Wiki-Test/blob/5266dedebfd1251f7069f614e8bd39a178437c77/Green%20App/Wiki.md"><strong>Wiki »</strong></a>
    <br /> -->
    <br>
    <a href="https://github.com/raihahahan/singapore-places-names/blob/main/documentation.md"><strong> Explore the docs »</strong></a>
    <br/>
    <br />
<!--     <a href="https://github.com/raihahahan/singapore-places-names">View Demo</a>  TODO-->
    ·
    <a href="https://github.com/raihahahan/singapore-places-names/issues">Report Bug</a>
    ·
    <a href="https://github.com/raihahahan/singapore-places-names/issues">Request Feature</a>
      <br/>
      <br/>
    <a href="https://github.com/raihahahan/singapore-places-names/tree/main/output">View preset output text files</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#how-it-works">How it works</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
<!--         <li><a href="#prerequisites">Prerequisites</a></li> -->
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->
### CLI program and Web Scraper
This project generates a list of key places in Singapore in different data structures - `list` and `dict`. You may either view the preset output files [here](https://github.com/raihahahan/singapore-places-names/tree/main/output) or clone this repo to use the command line program. The command line program allows you to choose your desired region (East, West, North, North East, Central) and Planning Area (i.e. places covered under Bedok, Bishan, Tampines etc.).

### Wikipedia listener (automatically push to Github)
`changes.py` is a Python script that helps to detect changes to the Wikipedia page. The `wikiChanges.txt` file in `git-helper-bot-update` branch is the most updated version of the last Wikipedia page edit data. When running the script, if there are any changes (i.e. Wikipedia page last updated value is different from what we have in `wikiChanges.txt`), then the script will update the local `wikiChanges.txt` and push the updates to `git-helper-bot-update`.

### Wikipedia listener with Crontab
You can also schedule `changes.py` to run at regular intervals with cron, which is how the branch `git-helper-bot-update` works. It uses `github.com/git-helper-bot` to push updates to the `git-helper-bot-update` branch. Read more about it [here](https://www.geeksforgeeks.org/scheduling-python-scripts-on-linux/).

### Demo

#### CLI Program
```sh
/path/to/directory/sg-places-list> python3 scripts/main.py

Type a command to choose a data structure. Invalid commands will be skipped:
0: list
1: dict

b: Go back to start
i: Show instructions again
q: Quit

$ 1

Choose the type of data you want:
0: By region only (e.g. east, west, north etc.)
1: By region and planning area (e.g. { east: { Bedok: [...] } })

b: Go back to start
i: Show instructions again
q: Quit

$ 1

Choose the region you want:
0: All
1: East
2: North
3: North East
4: Central
5: West

b: Go back to start
i: Show instructions again
q: Quit
You may combine them by listing (e.g. 1324 OR 35). If 0 is included, result will just return all items. Duplicates will be removed.

$ 1

{'east': {'Bedok': ['Bayshore', 'Bedok North', 'Bedok Reservoir', 'Bedok South', 'Frankel', 'Kaki Bukit', 'Kembangan', 'Siglap'], 'Changi': ['Changi Airport', 'Changi Point', 'Changi West'], 'Changi Bay': [], 'Pasir Ris': ['Flora Drive', 'Loyang East', 'Loyang West', 'Pasir Ris Central (Formerly called "Town" subzone.)', 'Pasir Ris Drive', 'Pasir Ris Park', 'Pasir Ris Wafer Fab Park (Formerly called "Pasir Ris West" subzone.)', 'Pasir Ris West (Formerly called "Elias" subzone.)'], 'Paya Lebar': ['Airport Road', 'Paya Lebar East', 'Paya Lebar North', 'Paya Lebar West', 'PLAB'], 'Tampines': ['Simei', 'Tampines East', 'Tampines North', 'Tampines West', 'Xilin']}}

$ q

```
#### changes.py
```sh
$ python3 scripts/scrapers/changes.py

08/30/2022, 16:09:02: A change is found:
Previous update: This page was last edited on 12 July 2022, at 12:13 (UTC).
Most recent update: This page was last edited on 29 July 2022, at 08:15 (UTC).
Text file updated successfully.
Successfully updated github repo at 08/30/2022, 16:09:05

$ python3 scripts/scrapers/changes.py
No changes detected.

```

### When is this useful?

- This is useful if you are writing a program which requires a list of key places in Singapore in string format only. Examples:
> 1. Dropdown autocomplete suggestions for a search bar component
> 2. Querying a list of places based on region (east, west etc.) and/or planning area (Bedok, Yishun etc.)
- You may use `scripts/tests.py` to play around with the provided functions. You may modify the data structures by mapping them or you may even export it as CSV, Excel, etc.
- This program only fetches the list of names in string format for each item (i.e. this is a quick and dirty way to easily get a list of key places in SG). If you need a much more detailed set of data for your use case (e.g. with coordinates, geocoding), please see Singapore's [oneMap API](https://www.onemap.gov.sg/docs/) instead.

### How it works
Webscraper Python scripts built using the [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library pull data from https://en.wikipedia.org/wiki/List_of_places_in_Singapore in HTML format. The program then cleans up and converts this data into the chosen data structures (`list`, `dictByRegion`, `dictByRegionAndPlanning`).

### Built With

* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

<!-- ### Prerequisites -->

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/raihahahan/singapore-places-names.git
   cd singapore-places-names
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
3. Start the command line program
   ```sh
   python3 scripts/main.py
   ```
4. To work with `changes.py`, you will need to upload this clone into a Github repository, or create a fork instead. Make sure that `git-helper-bot-update` branch exists. Add a `.env` file to the root of the project and add in the following data:
   ```
   githubPK=YOUR_GITHUB_ACCESS_TOKEN ## This is the Github account that will push to git-helper-bot-update branch. It can be a bot account.
   user=YOUR_GITHUB_USERNAME ## This is the Github account that will push to git-helper-bot-update branch. It can be a bot account.
   repoUser=YOUR_GITHUB_USERNAME ## This is the Github account that owns the cloned/forked repository.
   fileLocation=ABSOLUTE_PATH_TO_wikiChanges.txt
   ```
5. (optional) To schedule `changes.py` with Crontab, change the following in `changes.py`:
   ```py
   dotEnvLocation = ".env" ## CHANGE THIS TO ABSOLUTE PATH IF USING CRONTAB
   ```

<!-- USAGE EXAMPLES -->
## Usage
The CLI will show instructions on how to use the program.
   ```
   Type a command to choose a data structure. Invalid commands will be skipped:
    0: list
    1: dict

    b: Go back to start
    i: Show instructions again
    q: Quit
   ```

<!-- ROADMAP -->
## Roadmap
- [ ] Remove "(Formerly known as...)" from list items if it exists.
- [ ] Remove any square brackets from list items if it exists.

<!-- CONTRIBUTING -->
## Contributing

Contributions are **greatly appreciated**. Please read the [documentation](https://github.com/raihahahan/singapore-places-names/blob/main/documentation.md) first before starting. See the [open issues](https://github.com/raihahahan/singapore-places-names/issues) for a list of proposed features and/or known issues.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Email: mraihandev@gmail.com

<!-- Project Link: [https://github.com/raihahahan/singapore-places-names](https://github.com/raihahahan/singapore-places-names) -->


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* Template from [readMe template Github repo](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
* Data scraped from https://en.wikipedia.org/wiki/List_of_places_in_Singapore

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/raihahahan/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/raihahahan/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/raihahahan/repo.svg?style=for-the-badge
[forks-url]: https://github.com/raihahahan/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/raihahahan/repo.svg?style=for-the-badge
[stars-url]: https://github.com/raihahahan/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/raihahahan/repo.svg?style=for-the-badge
[issues-url]: https://github.com/raihahahan/repo/issues
[license-shield]: https://img.shields.io/github/license/raihahahan/repo.svg?style=for-the-badge
[license-url]: https://github.com/raihahahan/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/raihahahan
