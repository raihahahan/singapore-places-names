from bs4 import BeautifulSoup
from helpers.constants import inputStr
from helpers.cliHelpers import dictCase, listCase

def cli(soup: BeautifulSoup):
    type = input(inputStr[0])
    while True:
        if type=="q":
            return
        if type=="b":
            return cli(soup)
        if type=="i":
            print(inputStr[0])
        if type == "1" or type == "0":
            match type:
                case "0":
                    listCase(soup, cli)
                    return
                case "1":
                    dictCase(soup, cli)
                    return
        type=input()

