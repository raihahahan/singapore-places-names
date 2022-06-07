import string

def removeBracket(text: string):
    planningArea=text
    indexBracket = planningArea.find("[")
    endOfPlanningArea = planningArea.find("\n")
    if indexBracket != -1:
        planningArea = text[0:indexBracket]
    textList = planningArea + "\n" + text[endOfPlanningArea: len(text)]
    return textList.split("\n")

def cleanList(list: list):
    return filter(lambda i: i.strip() != "" and i != "]", list)