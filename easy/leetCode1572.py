#1572. Matrix Diagonal Sum
def diagonalSum(mat):
   
    size = len(mat[0])
    result = 0 
    for i in range(size):
        
        result += mat[i][i]
        result += mat[i][len(mat) - i-1]
    
    return result - mat[(size + 1) //2 -1 ][(size + 1)//2 -1] if size % 2 == 1 else result 


print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))


print(diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]))