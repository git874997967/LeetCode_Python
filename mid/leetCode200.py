#200. Number of Islands edge detection
def numIslands(grid):
    dirs = [[-1,0],[1,0],[0,1],[0,-1]]
    result = 0
    def borderTest(i,j,grid):
        for dir in dirs:
            newX , newY = i + dir[0], j + dir[1]
            if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
                if grid[newX][newY] == "1":
                    borderTest(newX,newY,grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
              grid[i][j] = "0"
              borderTest(i,j,grid)
              result += 1
    print(result)
    print(grid)
    return result
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
numIslands(grid= grid)