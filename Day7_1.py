"""Day 7: The Treachery of Whales"""

def getIntList(inputText):
    listText = inputText.split(",")
    intList = []
    for item in listText:
        intList.append(int(item))
    return intList
    
def calculateFuel(intList):
    intList.sort()
    #print(intList)
    medianIndex = len(intList) // 2
    print(intList[medianIndex])
    fuelTotal = 0
    for item in intList:
        fuel = abs(item - intList[medianIndex])
        fuelTotal = fuelTotal + fuel
    print(fuelTotal)
    return



inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day7_input.txt")
fileText = inputFile.readline()
crabList = getIntList(fileText)

calculateFuel(crabList)


