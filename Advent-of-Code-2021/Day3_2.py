"""Day 3: Binary Diagnostic"""

def countOxygen(oxygenValuesList, index):
    countZero = 0
    countOne = 0
    for item in oxygenValuesList:
        if item[index] == "0":
            countZero = countZero + 1
        if item[index] == "1":
            countOne = countOne + 1
    print("Oxygen - countZero:", countZero)
    print("Oxygen - countOne:", countOne)
    if countZero > countOne:
        return "0"
    else:
        return "1"

def countCo2(co2ValuesList, index):
    countZero = 0
    countOne = 0
    for item in co2ValuesList:
        if item[index] == "0":
            countZero = countZero + 1
        if item[index] == "1":
            countOne = countOne + 1
    print("CO2 - countZero:", countZero)
    print("CO2 - countOne:", countOne)
    if countZero > countOne:
        return "1"
    else:
        return "0"

def updateOxygen(oxygenValuesList, index):
    if len(oxygenValuesList) == 1:
        return oxygenValuesList
    mostPopularValue = countOxygen(oxygenValuesList, index)
    print("Oxygen - mostPopularValue is", mostPopularValue)
    newValuesList = []
    for item in oxygenValuesList:
        if item[index] == mostPopularValue:
            newValuesList.append(item)
    return newValuesList

def updateCo2(co2ValuesList, index):
    if len(co2ValuesList) == 1:
        return co2ValuesList
    leastPopularValue = countCo2(co2ValuesList, index)
    print("CO2 - leastPopularValue is", leastPopularValue)
    newValuesList = []
    for item in co2ValuesList:
        if item[index] == leastPopularValue:
            newValuesList.append(item)
    return newValuesList

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day3_input.txt")
oxygenValuesList = []
co2ValuesList = []


for line in inputFile:
    oxygenValuesList.append(line)
    co2ValuesList.append(line)
    

for i in range(12):
    oxygenValuesList = updateOxygen(oxygenValuesList, i)
    co2ValuesList = updateCo2(co2ValuesList, i)
    
        
print("oxygenValuesList:", oxygenValuesList)
print("co2ValuesList:", co2ValuesList)
print("Answer:", int(oxygenValuesList[0],base=2) * int(co2ValuesList[0],base=2))
