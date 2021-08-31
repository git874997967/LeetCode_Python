# 1380. Lucky Numbers in a Matrix
def luckyNumbers (matrix):
    minRows, maxCol = [],[]
    for row in range(len(matrix)):
        minRows.append(min(matrix[row]))
    for col in zip(*matrix):
        maxCol.append(max(col))

    for i in range(min(len(minRows),min(maxCol))):
        if minRows[i] in maxCol:
            print(minRows[i])
            return minRows[i]
        
    return []





matrix = [[3,7,8],[9,11,13],[15,16,17]]
luckyNumbers(matrix)