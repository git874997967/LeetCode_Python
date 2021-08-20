#892. Surface Area of 3D Shapes
# edge detection
def surfaceArea(grid):
    directions = [[-1,0],[0,-1],[0,1],[1,0]]
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0 :
                result += 2 ## top and bottom area inclued
            for dir in directions:
                newX, newY = i + dir[0], j + dir[1]
                if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]):
                    result += grid[i][j]       ## paint the edge  
                elif grid[i][j] > grid[newX][newY]: 
                    result += (grid[i][j] - grid[newX][newY])  ## paint the diff part beteen two grids
    print(result)
    return result
def surfaceArea2(grid):
    m, n = len(grid), len(grid[0])
    area = 2 * m * n
    
    for i in range(m):
        area += grid[i][0] + grid[i][n-1]
        area -= 2 * grid[i].count(0)
        for j in range(n-1):
            
            area += abs(grid[i][j+1] - grid[i][j])
            
            
    for j in range(n):
        area += grid[0][j] + grid[m-1][j]
        for i in range(m-1):
            area += abs(grid[i+1][j] - grid[i][j])
            
    return area

grid1 =  [[2]]
grid2 = [[1,2],[3,4]]
grid3 = [[1,0],[0,2]]
grid4 = [[1,1,1],[1,0,1],[1,1,1]]
grid5 = [[2,2,2],[2,1,2],[2,2,2]]
surfaceArea(grid1)
surfaceArea(grid2)
surfaceArea(grid3)
surfaceArea(grid4)
surfaceArea(grid5)
