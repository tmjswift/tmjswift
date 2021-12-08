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
depthMeasurements = []
previousAverageDepth = None
currentAverageDepth = None


for line in inputFile:
    depthMeasurements.append(int(line))
    
for i in range(1, len(depthMeasurements)-1):
    previousAverageDepth = currentAverageDepth
    currentAverageDepth = (depthMeasurements[i-1] + depthMeasurements[i] + depthMeasurements[i+1]) / 3
    if checkDepthIncreased(currentAverageDepth, previousAverageDepth):
        depthIncreaseCount = depthIncreaseCount + 1

print(depthIncreaseCount)
