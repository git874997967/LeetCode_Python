def islandPerimeter(grid):
    if grid is None or len(grid) == 0:
        return 0
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    rows,cols, result  = len(grid), len(grid[0]), 0
    def helper(grid,row,col):
        edge = 0
        for dir in dirs:
            newX , nexY = row + dir[0],col + dir[1]
            if 0 <= newX < rows and 0 <= newY < newY or grid[newX][newY] == 0:
                edge += 1
        return edge
                
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                result += helper(grid,row,col)
                
                
    return result 
  
