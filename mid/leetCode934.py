#934. Shortest Bridge BFS + DFS
def shortestBridge(grid):
        result,n = 0, len(grid)
        dirs = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]
        landList = []
        def dfs(i,j):
            for dir in dirs:
                newX, newY = i + dir[0], j + dir[1]
                if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 1:
                    grid[newX][newY]  = 2
                    landList.append((newX,newY))
                    dfs(newX,newY)

        def findIsland():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] :
                       return dfs(i,j)
                
        findIsland()
                    
                        
        while landList:
            for _ in range(len(landList)):
                x, y = landList.pop(0)
                for dir in dirs:
                    newX , newY = x + dir[0], y + dir[1]
                    if 0 <= newX < n  and 0 <= newY < n and grid[newX][newY] != 2:
                        if grid[newX][newY] == 0:
                            grid[newX][newY ] = 2
                            landList.append((newX,newY))
                        elif grid[newX][newY] == 1:
                            print(result)
                            return result
            result += 1
        return result

grid = [[0,1],[1,0]]
shortestBridge(grid)