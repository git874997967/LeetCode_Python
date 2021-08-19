# 867. Transpose Matrix
def transpose(matrix):
    rows, cols, result = len(matrix), len(matrix[0]),[]
    for i in range(cols):
        arr = []
        for j in range(rows):
            arr.append(matrix[j][i])
        result.append(arr)
    print(result)
    return result

matrix1 = [[1,2,3],[4,5,6]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix1)
transpose(matrix2)

