def removeBracket(text: str):
    planningArea=text
    indexBracket = planningArea.find("[")
    endOfPlanningArea = planningArea.find("\n")
    if indexBracket != -1:
        planningArea = text[0:indexBracket]
    textList = planningArea + "\n" + text[endOfPlanningArea: len(text)]
    return textList.split("\n")

def cleanList(list: list):
    return filter(lambda i: i.strip() != "" and i != "]", list)

def cleanItem(item: str):
    if "(Formerly" in item:
        indexToRemove_0 = item.index("(Formerly")
        return item[0:indexToRemove_0-1]

    elif "(Also" in item:
        indexToRemove_1 = item.index("(Also")
        return item[0:indexToRemove_1-1]

    elif "(Not" in item:
        indexToRemove_2 = item.index("(Not")
        return item[0:indexToRemove_2-1]
        
    elif "[" in item:
        indexToRemove = item.index("[")
        return item[0:indexToRemove]
        
    else:
        return item

