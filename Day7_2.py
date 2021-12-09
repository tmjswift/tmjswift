"""Day 7: The Treachery of Whales"""

def getIntList(inputText):
    listText = inputText.split(",")
    intList = []
    for item in listText:
        intList.append(int(item))
    return intList

def createFuelCostTable(maxMove):
    table = {}
    cost = 0
    for i in range(0, maxMove+1):
        cost = cost + i
        table[i] = cost
    return table

def calculateFuel(intList, position, fuelCostTable):
    fuelTotal = 0
    for item in intList:
        distance = abs(item - position)
        fuelTotal = fuelTotal + fuelCostTable[distance]
    return fuelTotal



inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day7_input.txt")
fileText = inputFile.readline()
crabList = getIntList(fileText)
#crabList = getIntList("16,1,2,0,4,2,7,1,2,14")
fuelCostTable = createFuelCostTable(2000)

lowestFuelCost = calculateFuel(crabList, 0, fuelCostTable)
for i in range(1, 2000):
    fuelCost = calculateFuel(crabList, i, fuelCostTable)
    if fuelCost < lowestFuelCost:
        lowestFuelCost = fuelCost
        print("position:", i)
        print("fuelTotal:", lowestFuelCost)
