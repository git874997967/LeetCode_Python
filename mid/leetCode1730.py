#1730. Shortest Path to Get Food
def getFood(grid):
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    result , n = 0 , len(grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                nodeList = [(i,j)]

    while nodeList:
        for _ in range(len(nodeList)):
            x, y = nodeList.pop(0)
             
            for dir in dirs:
                newX , newY = x + dir[0], y + dir[1]

                if 0 <= newX < n and 0 <= newY < n :
                    if grid[newX][newY] == '#':
                        print("find food will return")
                        return result
                    if grid[newX][newY] == 'O':
                        grid[newX][newY] = 'X'
                        nodeList.append((newX,newY))
                    
        result += 1
    print(grid)
    return - 1


getFood([["X","X","X","X","X","X","X","X"],
        ["X","*","O","X","O","#","O","X"],
        ["X","O","O","X","O","O","X","X"],
        ["X","O","O","O","O","#","O","X"],
        ["X","X","X","X","X","X","X","X"]])


        # ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
        # ['X', '*', 'X', 'X', 'X', '#', 'O', 'X'], 
        # ['X', 'X', 'X', 'X', 'X', 'O', 'X', 'X'], 
        # ['X', 'X', 'X', 'X', 'X', '#', 'O', 'X'], 
        # ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']