"""Day 1: Sonar Sweep"""

def checkDepthIncreased(currentDepth, previousDepth):
    if currentDepth == None or previousDepth == None:
        return False
    if currentDepth > previousDepth:
        return True
    # default case
    return False

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day1_input.txt")
depthIncreaseCount = 0
previousDepth = None
currentDepth = None


for line in inputFile:
    previousDepth = currentDepth
    currentDepth = int(line)
    if checkDepthIncreased(currentDepth, previousDepth):
        depthIncreaseCount = depthIncreaseCount + 1

print(depthIncreaseCount)
