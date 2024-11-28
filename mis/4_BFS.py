def getFood(grid):
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    result, n = 0, len(grid)
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                nodelist = [(i,j)]
                
    while nodelist:
         for _ in range(len(nodelist)):
             x,y = nodelist.pop(0)
             for dir in dirs:
                 newX, newY = x + dir[0], y + dir[1]
                 if 0 <= newX < n and 0 <= newY < n:
                     if grid[newX][newY] == '#':
                         print('get food')
                         return result
                     if grid[newX][newY] == 'O':
                         grid[newX][newY] = 'X' 
                         nodelist.append((newX,newY))

         result += 1
    return result                  

getFood([["X","X","X","X","X","X","X","X"],
        ["X","*","O","X","O","#","O","X"],
        ["X","O","O","X","O","O","X","X"],
        ["X","O","O","O","O","#","O","X"],
        ["X","X","X","X","X","X","X","X"]])