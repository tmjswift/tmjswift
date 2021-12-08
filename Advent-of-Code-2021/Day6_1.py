"""Day 6: Lanternfish"""

def getFish(fishText):
    fishListText = fishText.split(",")
    fishList = []
    for item in fishListText:
        fishList.append(int(item))
    return fishList
    

def updateFishList(fishList):
    spawnCount = 0
    for i in range(len(fishList)):
        # check if ready to spawn
        if fishList[i] == 0:
            spawnCount = spawnCount + 1
            fishList[i] = 6
        else:
            fishList[i] = fishList[i] - 1
    for i in range(spawnCount):
        fishList.append(8)
    return

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day6_input.txt")
fileText = inputFile.readline()
fishList = getFish(fileText)
for i in range(80):
    updateFishList(fishList)
#    print(fishList)

print("Number of fish:", len(fishList))
