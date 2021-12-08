"""Day 3: Binary Diagnostic"""

def updateBits(line, numberOfBitsSet, numberOfBitsUnset):
    for i in range(12):
        if line[i] == "0":
            numberOfBitsUnset[i] = numberOfBitsUnset[i] + 1
        if line[i] == "1":
            numberOfBitsSet[i] = numberOfBitsSet[i] + 1
            
    return


inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day3_input.txt")
numberOfBitsSet = [0,0,0,0,0,0,0,0,0,0,0,0]
numberOfBitsUnset = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in inputFile:
    updateBits(line, numberOfBitsSet, numberOfBitsUnset)
    
print(numberOfBitsSet)
print(numberOfBitsUnset)
    
gamma = 0
epsilon = 0
for i in range(12):
    bitValue = pow(2, 11-i)
    if numberOfBitsSet[i] > numberOfBitsUnset[i]:
        gamma = gamma + bitValue
    else:
        epsilon = epsilon + bitValue
    
        
    print(gamma)
    print(epsilon)
print(gamma * epsilon)
