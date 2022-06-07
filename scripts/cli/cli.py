from bs4 import BeautifulSoup
from helpers.constants import inputStr
from helpers.cliHelpers import input_1, input_2, input_3, input_4
from helpers.cliHelpers import convertNumToList

def cli(soup: BeautifulSoup):
    type = input(inputStr[0])
    while True:
        if type=="q":
            return
        if type=="i":
            print(inputStr[0])
        if type == "1" or type == "0":
            match type:
                case "0":
                    data = input(inputStr[1])
                    while True:
                        if data=="q":
                            return
                        if data=="i":
                            print(inputStr[1])
                        if data.isnumeric():
                            if "0" in data:
                                print(input_1["0"](soup))
                            elif len(data)==1:
                                if int(data) in range(6):
                                    print(input_1[data](soup))
                            else:
                                numArr=convertNumToList(data, 5)
                                finalRes=[]
                                for i in numArr:
                                    finalRes+=input_1[i](soup)
                                print(finalRes)
                        data=input()
                case "1":
                    data = input(inputStr[2])
                    while True:
                        if data=="q":
                            return
                        if data=="i":
                            print(inputStr[2])
                        if data == "0" or data=="1":
                            match data:
                                case "0":
                                    q=input(inputStr[1])
                                    while True:
                                        if q=="q":
                                            return
                                        if q=="i":
                                            print(inputStr[1])
                                        if q.isnumeric():
                                            if "0" in q:
                                                print(input_2["0"](soup))
                                            elif len(q)==1:
                                                if int(q) in range(6):
                                                    key=input_3[int(q)]
                                                    item={key: input_2[q](soup)}
                                                    print(item)
                                            else:
                                                numArr=convertNumToList(q, 5)
                                                finalRes={}
                                                for i in numArr:
                                                    finalRes[input_3[int(i)]] = input_2[i](soup)
                                                print(finalRes)
                                        q=input()
                                case "1":
                                    p=input(inputStr[1])
                                    while True:
                                        if p=="q":
                                            return
                                        if p=="i":
                                            print(inputStr[1])
                                        if p.isnumeric():
                                            if "0" in p:
                                                print(input_4["0"](soup))
                                            elif len(p)==1:
                                                if int(p) in range(6):
                                                    key=input_3[int(p)]
                                                    item={key: input_4[p](soup)}
                                                    print(item)
                                            else:
                                                numArr=convertNumToList(p, 5)
                                                finalRes={}
                                                for i in numArr:
                                                    finalRes[input_3[int(i)]] = input_4[i](soup)
                                                print(finalRes)
                                        p=input()
                        data=input()
        type=input()