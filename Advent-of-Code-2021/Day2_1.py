"""Day 2: Dive!"""

def getNewPosition(currentHorizontalPosition, currentDepth, movement):
    movementDirection, movementDistance = movement.split(' ')
    if movementDirection == "forward":
        newHorizontalPosition = currentHorizontalPosition + int(movementDistance)
        newDepth = currentDepth
        
    if movementDirection == "down":
        newHorizontalPosition = currentHorizontalPosition
        newDepth = currentDepth + int(movementDistance)
        
    if movementDirection == "up":
        newHorizontalPosition = currentHorizontalPosition
        newDepth = currentDepth - int(movementDistance)
        if newDepth < 0:
            newDepth = 0
    
    return (newHorizontalPosition, newDepth)
        

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day2_input.txt")
horizontalPosition = 0
depth = 0

for line in inputFile:
    horizontalPosition, depth = getNewPosition(horizontalPosition, depth, line)
    

print(horizontalPosition)
print(depth)
print(horizontalPosition * depth)
