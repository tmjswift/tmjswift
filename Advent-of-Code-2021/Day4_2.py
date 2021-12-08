"""Day 4: Giant Squid"""

def getBingoNumbers(bingoNumbersLine):
    bingoNumbersText = bingoNumbersLine.split(",")
    bingoNumbers = []
    for item in bingoNumbersText:
        bingoNumbers.append(int(item))
    #print("Bingo Numbers:", bingoNumbers)
    return bingoNumbers

def getBingoCard(bingoCardLines):
    bingoCardLinesText = bingoCardLines.split()
    bingoCard = []
    for item in bingoCardLinesText:
        bingoCard.append(int(item))
    #print("bingoCard:", bingoCard)
    return bingoCard

def checkBingoLine(bingoLine, bingoNumbers):
    for item in bingoLine:
        if item not in bingoNumbers:
            return False
    # All numbers in line have been called
    print("Bingo!:", bingoLine)
    return True

def checkBingoCard(bingoCard, bingoNumbers):
    # check rows
    if checkBingoLine([bingoCard[0], 
                       bingoCard[1], 
                       bingoCard[2], 
                       bingoCard[3], 
                       bingoCard[4]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[5], 
                       bingoCard[6], 
                       bingoCard[7], 
                       bingoCard[8], 
                       bingoCard[9]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[10], 
                       bingoCard[11], 
                       bingoCard[12], 
                       bingoCard[13], 
                       bingoCard[14]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[15], 
                       bingoCard[16], 
                       bingoCard[17], 
                       bingoCard[18], 
                       bingoCard[19]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[20], 
                       bingoCard[21], 
                       bingoCard[22], 
                       bingoCard[23], 
                       bingoCard[24]],
                      bingoNumbers):
        return True
    # check columns
    if checkBingoLine([bingoCard[0], 
                       bingoCard[5], 
                       bingoCard[10], 
                       bingoCard[15], 
                       bingoCard[20]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[1], 
                       bingoCard[6], 
                       bingoCard[11], 
                       bingoCard[16], 
                       bingoCard[21]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[2], 
                       bingoCard[7], 
                       bingoCard[12], 
                       bingoCard[17], 
                       bingoCard[22]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[3], 
                       bingoCard[8], 
                       bingoCard[13], 
                       bingoCard[18], 
                       bingoCard[23]],
                      bingoNumbers):
        return True
    if checkBingoLine([bingoCard[4], 
                       bingoCard[9], 
                       bingoCard[14], 
                       bingoCard[19], 
                       bingoCard[24]],
                      bingoNumbers):
        return True
    # no lines complete
    return False
    
def checkForBingo(bingoCards, bingoNumbers):
    sumUncheckedNumbers = 0
    currentNumber = 5
    while currentNumber < len(bingoNumbers) and len(bingoCards) > 1:
        print("------------------------------------------------")
        print("Called numbers are:", bingoNumbers[:currentNumber])
        for card in bingoCards:
            if checkBingoCard(card, bingoNumbers[:currentNumber]):
                bingoCards.remove(card)
        currentNumber = currentNumber + 1
        print("Cards remaining:", len(bingoCards))
    
    # one card remaining - calculate its score
    while currentNumber < len(bingoNumbers):
        if checkBingoCard(bingoCards[0], bingoNumbers[:currentNumber]):
            print("Last number:", bingoNumbers[currentNumber-1])
            print("Unchecked numbers:")
            for number in bingoCards[0]:
                if number not in bingoNumbers[:currentNumber]:
                    print(number)
                    sumUncheckedNumbers = sumUncheckedNumbers + number
        return (sumUncheckedNumbers * bingoNumbers[currentNumber-1])
        currentNumber = currentNumber + 1
    return None

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2021\\input\\Day4_input.txt")
inputLines = inputFile.readlines()

bingoNumbers = getBingoNumbers(inputLines[0])

bingoCards = []
lineNumber = 2

while lineNumber < (len(inputLines)-4):
    bingoCards.append(getBingoCard(inputLines[lineNumber] + 
                                   inputLines[lineNumber+1] +
                                   inputLines[lineNumber+2] +
                                   inputLines[lineNumber+3] +
                                   inputLines[lineNumber+4]))
    lineNumber = lineNumber + 6
    
score = checkForBingo(bingoCards, bingoNumbers)
print("Score:", score)
