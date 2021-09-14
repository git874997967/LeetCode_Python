#1878. Get Biggest Three Rhombus Sums in a Grid
# add the line but not edge only
def getBiggestThree(grid):
    rows, cols = len(grid),len(grid[0])
    result = set()
    for i in range(rows):
        for j in range(cols):
            result.add(grid[i][j])
            length = min(i, rows - 1 - i , j , cols - 1 - j)
            for l in range(1,length + 1):
                # add the edges
                cur = 0
                cur += grid[i][j - l]
                cur += grid[i][j + l]
                cur += grid[i -l][j]
                cur += grid[i + l][j]
                ## add lines
                for k in range(1,l):
                    cur += grid[i - k][j - l + k] #
                    cur += grid[i + k][j - l + k] #
                    cur += grid[i - k][j + l - k] # 
                    cur += grid[i + k][j + l - k] #
                result.add(cur)
    result = list(result)
    result.sort(reverse= True)
    return result[:3]




print(getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]))
grid = [
[20,17,9,13,5,2,9,1,5],
[14,9,9,9,16,18,3,4,12],
[18,15,10,20,19,20,15,12,11],
[19,16,19,18,8,13,15,14,11],
[4,19,5,2,19,17,7,2,2]
]
print(getBiggestThree(grid))

print(getBiggestThree([[1,2,3],[4,5,6],[7,8,9]]))
