# 293. Flip Game
def generatePossibleNextMoves( currentState):
    if len(currentState) <= 1:
        return []
    result = []
    for index in range(len(currentState)-1):
        if currentState[index:index + 2] == '++':
            revertStr  =  '--'
        else: continue 
        newStr = currentState[:index ] + revertStr + currentState[index +2:]
        result.append(newStr)
    return result
 