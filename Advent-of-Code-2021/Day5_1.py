"""Day 5: Hydrothermal Venture"""

def getPositions(line):
    # line has format: 941,230 -> 322,849
    start = line.split()[0]
    end = line.split()[2]
    startX, startY = start.split(",")
    endX, endY = end.split(",")
    return ([int(startX),int(startY)], [int(endX),int(endY)])

def updateVentArray(startPos, endPos, ventArray):
    # check for horizontal line
    if startPos[1] == endPos[1]:
        # go from left to right
        rangeStart = min(startPos[0],endPos[0])
        rangeEnd = max(startPos[0],endPos[0]) + 1
        for i in range(rangeStart,rangeEnd):
            ventArray[i][startPos[1]] = ventArray[i][startPos[1]] + 1
        return
    # check for vertical line
    if startPos[0] == endPos[0]:
        # go from top to bottom
        rangeStart = min(startPos[1],endPos[1])
        rangeEnd = max(startPos[1],endPos[1]) + 1
        for j in range(rangeStart,rangeEnd):
            ventArray[startPos[0]][j] = ventArray[startPos[0]][j] + 1
        return
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
