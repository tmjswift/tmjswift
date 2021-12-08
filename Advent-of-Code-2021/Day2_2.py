"""Day 2: Dive!"""

def getNewPosition(currentHorizontalPosition, currentDepth, currentAim, movement):
    movementDirection, movementDistance = movement.split(' ')
    if movementDirection == "forward":
        newAim = currentAim
        newHorizontalPosition = currentHorizontalPosition + int(movementDistance)
        newDepth = currentDepth + (aim * int(movementDistance))
        if newDepth < 0:
            newDepth = 0
        
    if movementDirection == "down":
        newHorizontalPosition = currentHorizontalPosition
        newDepth = currentDepth
        newAim = currentAim + int(movementDistance)
        
    if movementDirection == "up":
        newHorizontalPosition = currentHorizontalPosition
        newDepth = currentDepth
        newAim = currentAim - int(movementDistance)
    
    return (newHorizontalPosition, newDepth, newAim)
        

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day2_input.txt")
horizontalPosition = 0
depth = 0
aim = 0

for line in inputFile:
    horizontalPosition, depth, aim = getNewPosition(horizontalPosition, depth, aim, line)
    

print(horizontalPosition)
print(depth)
print(horizontalPosition * depth)
