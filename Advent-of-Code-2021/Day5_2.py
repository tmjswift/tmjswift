"""Day 5: Hydrothermal Venture"""

def getPositions(line):
    # line has format: 941,230 -> 322,849
    start = line.split()[0]
    end = line.split()[2]
    startX = int(start.split(",")[0])
    startY = int(start.split(",")[1])
    endX = int(end.split(",")[0])
    endY = int(end.split(",")[1])
    # arrange coordinates so we always go from left to right
    if startX > endX:
        # switch
        return ([endX,endY], [startX,startY])
    else:
        # as normal
        return ([startX,startY], [endX,endY])
    

def updateVentArray(startPos, endPos, ventArray):
    # check for vertical line
    if startPos[0] == endPos[0]:
        # go from top to bottom
        rangeStart = min(startPos[1],endPos[1])
        rangeEnd = max(startPos[1],endPos[1]) + 1
        for j in range(rangeStart,rangeEnd):
            ventArray[startPos[0]][j] = ventArray[startPos[0]][j] + 1
        return
    # horizontal and diagonal lines
    if startPos[1] == endPos[1]:
        # horizontal (right)
        verticalDirection = 0
    if startPos[1] < endPos[1]:
        # down and right
        verticalDirection = 1
    if startPos[1] > endPos[1]:
        # up and right
        verticalDirection = -1 
    for i in range(endPos[0] - startPos[0] + 1):
        ventArray[i+startPos[0]][startPos[1]+i*verticalDirection] = ventArray[i+startPos[0]][startPos[1]+i*verticalDirection] + 1
    return
    

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day5_input.txt")

rows = 1000
columns = 1000
ventArray = [[0 for i in range(columns)] for j in range(rows)]

for line in inputFile:
    startPos, endPos = getPositions(line)
    updateVentArray(startPos, endPos, ventArray)

# for j in range(rows):
#     outputLine = ""
#     for i in range(columns):
#         outputLine = outputLine + " " + str(ventArray[i][j])
#     print(outputLine)

ventCount = 0
for j in range(columns):
     for i in range(rows):
         if ventArray[i][j] > 1:
             ventCount = ventCount + 1
print("Number of dangerous vents:", ventCount)
