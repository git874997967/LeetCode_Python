# 566. Reshape the Matrix
def matrixReshape(mat, r, c):
    buf = []
    for row in range(len(mat)):
        for col in range(len(row)):
            buf.append(mat[row][col])
    result = []
    for i in range(r):
        row = buf[i:i + c]    
        result.append(row)

    return result 

mat = [[1,2],[3,4]], r = 1, c = 4

print(matrixReshape(mat,r,c))