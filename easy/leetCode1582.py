#1582. Special Positions in a Binary Matrix (dimension projection)
def numSpecial(mat):
    rowSum, colSum = [], []
    result  = 0
    for i in range(len(mat)):
        rowSum.append(sum(mat[i]))
    for col in zip(*mat):
        colSum.append(sum(col))

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and rowSum[i] + colSum[j] == 2:
                result += 1
    
    return result 
    


print(numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]))
