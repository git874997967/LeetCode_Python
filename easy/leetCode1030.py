#1030. Matrix Cells in Distance Order
from collections import deque
def allCellsDistOrder( rows, cols, rCenter, cCenter):
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    visited = [[0] * cols for _ in range(rows)]
    center = (rCenter,cCenter)
    queue = deque()
    queue.append(center)
    result = []
    while queue:
        for i in range(len(queue)):
            cell = queue.popleft()
            x,y = cell[0],cell[1]
            if visited[x][y]:
                continue
            visited[x][y] = 1
            result.append([x,y])
            for dir in dirs:
                newX, newY = x + dir[0], y + dir[1]
                if 0 <= newX < rows and 0 <= newY < cols:
                    queue.append([newX,newY])
    print(result)
    return result 
     


allCellsDistOrder(1,2,0,0)

allCellsDistOrder(2,2,0,1)

allCellsDistOrder(2,3,1,2)

# [[0,2],[0,1],[1,2],[0,0],[1,1],[2,2],[1,0],[2,1],[2,0]]
# [[0, 2], [1, 2], [0, 1], [1, 1], [0, 0], [1, 0]]

allCellsDistOrder(3,3,0,2)
