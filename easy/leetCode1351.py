#1351. Count Negative Numbers in a Sorted Matrix

# the matrix is step-liked   矩阵扫描  从一个角落开始 按行/列 进行扫描
# ++++++
# ++++--
# ++++--
# +++---
# +-----
# +-----
def countNegatives(self, grid):
    # start from bottom left corner 
    # add by row by row based
     rows, cols = len(grid), len(grid[0])
     curRow,curCol, result = rows - 1, 0, 0
     while curRow >= 0 and curCol < cols:  # we need to reach the righest col 
         if grid[curRow][curCol] < 0:
             curRow -= 1 # move up
             result += cols - curCol  # add up the cols 
         elif grid[curRow][curCol] >=0:
             # move to the right by one more col 
             curCol += 1
     return result

def countNegatives2(grid):
    # start from top right corner
    # add by col based 
    rows, cols = len(grid), len(grid[0])
    curRow, curCol, result = 0,cols -1,0
    while curRow< rows and curCol >=0:
        if grid[curRow][curCol] <0:
            # add the whole row 
            result += rows- curRow
            curCol -= 1
        else:
            curRow += 1

