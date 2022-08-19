regionID = {
    "east": "East_Region",
    "north": "North_Region",
    "northEast": "North-East_Region",
    "west": "West_Region",
    "central": "Central_Region"
}

inputStr = [
"Type a command to choose a data structure. Invalid commands will be skipped:\n0: list\n1: dict\n\nb: Go back to start\ni: Show instructions again\nq: Quit\n",
"Choose the region you want:\n0: All\n1: East\n2: North\n3: North East\n4: Central\n5: West\n\nb: Go back to start\ni: Show instructions again\nq: Quit\nYou may combine them by listing (e.g. 1324 OR 35). If 0 is included, result will just return all items. Duplicates will be removed.\n",
"Choose the type of data you want:\n0: By region only (e.g. east, west, north etc.)\n1: By region and planning area (e.g. { east: { Bedok: [...] } })\n\nb: Go back to start\ni: Show instructions again\nq: Quit\n"
]

invalid_command = "Error. Invalid command."
 