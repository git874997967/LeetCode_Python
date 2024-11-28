def largestLocal(grid):
    n = len(grid)
    max_grid = [[0] * (n-2) for _ in range(n-2)]
    
    for i in range(n-2):
        for j in range(n-2):
            max_grid[i][j] = findMax(grid,i,j)
    return max_grid

def findMax(grid,x,y):
    max_ele = 0
    for i in range(x , x + 3):
        for j in range(y, y + 3):
            max_ele = max(max_ele, grid[i][j])
            
    return max_ele