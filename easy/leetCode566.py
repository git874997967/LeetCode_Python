# 566. Reshape the Matrix
def matrixReshape(mat, r, c):
    buf = []
    for row in range(len(mat)):
        for col in range(len(row)):
            buf.append(mat[row][col])
    if len(buf / r != c):
        return mat 
    result = []
    for i in range(0,len(buf), c):

        result.append(buf[i:i+c])
    return result 

mat = [[1,2],[3,4]], r = 1, c = 4

print(matrixReshape(mat,r,c))