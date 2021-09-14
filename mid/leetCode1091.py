#1091. Shortest Path in Binary Matrix
def shortestPathBinaryMatrix(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
        n,result = len(grid), 1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0 :
            return -1
        nodeList = [(0,0)]

        while nodeList:
            for _ in range(len(nodeList)):
                x, y = nodeList.pop(0)
                if x == y == n - 1:
                    return result 
                for dir in dirs :
                    newX, newY = x + dir[0], y + dir[1]
                    if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 0:
                        nodeList.append((newX,newY))
                        grid[newX][newY] = 1

            result += 1
        return - 1