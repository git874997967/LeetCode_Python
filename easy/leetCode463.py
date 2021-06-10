# 463. Island Perimeter

def islandPerimeter(grid):
  if grid is None or len(grid) == 0:
      return 0
  rows , cols = len(grid), len(grid[0])
  result = 0
  dirs = [[1,0],[-1,0],[0,1],[0,-1]]
  def helper(grid, row, col):
      
      edge = 0
      for dir in dirs:
          newX = row + dir[0]
          newY = col + dir[1]
          if newX < 0 or newX >= rows or newY < 0 or newY >= cols or grid[newX][newY] == 0:
              edge += 1
      return edge 

  for row in range(rows):
      for col in range(cols):
          if grid[row][col] == 1:
              result += helper(grid, row,col)
  return result 



grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

 
print(islandPerimeter(grid))
