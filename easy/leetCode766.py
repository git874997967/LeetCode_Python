# 766. Toeplitz Matrix
def isToeplitzMatrix(matrix):
    rows,cols = len(matrix) , len(matrix[0])
    result = True 
     
    for i in range(0,rows-1):
        for j in range(0,cols-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                result = False
                break
    print(result)
    return result
                 

def isToeplitzMatrix2(matrix):
    rows, cols = len(matrix), len(matrix[0])
    if rows == 1:
        return True 
    else:
         for i in range(rows -1):
            print(matrix[i][:-1], matrix[i+1][1:])
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False 
    return True


isToeplitzMatrix2([[1,2,3,4],
                   [5,1,2,3],
                   [9,5,1,2]])