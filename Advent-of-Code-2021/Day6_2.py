"""Day 6: Lanternfish"""

def getFish(fishText):
    fishListText = fishText.split(",")
    fishList = [0,0,0,0,0,0,0,0,0]
    # Count how many fish there are for each timer value
    for item in fishListText:
        fishDay = int(item)
        fishList[fishDay] = fishList[fishDay] + 1
    return fishList
    

def updateFishList(fishList):
    # store number of fish on timer 0, they will spawn new fish
    spawnCount = fishList[0]
    for i in range(len(fishList)-1):
        # shuffle values along to reduce all timers by 1
        fishList[i] = fishList[i+1]
    # fish that were on timer 0 move to timer 6 and spawn new fish on timer 8
    fishList[6] = fishList[6] + spawnCount
    fishList[8] = spawnCount
    return

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day6_input.txt")
fileText = inputFile.readline()
fishList = getFish(fileText)

for i in range(256):
    updateFishList(fishList)
print(fishList)

sumFish = 0
for item in fishList:
    sumFish = sumFish + item
print("Number of fish:", sumFish)
