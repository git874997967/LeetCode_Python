#883. Projection Area of 3D Shapes(mid)
def projectionArea(self, grid):
    ans = 0
    for i in range(len(grid)):
        bestRow = bestCol = 0
        for j in range(len(grid)):
            if grid[i][j] :
                ans += 1
            bestRow = max(bestRow,grid[i][j])
            bestCol = max(bestCol,grid[j][i])
        ans += bestRow + bestCol
    return ans 