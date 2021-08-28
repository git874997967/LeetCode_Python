#240. Search a 2D Matrix II
#step-wise traverse  with the same idea of question 1351
def searchMatrix( grid: List[List[int]], target: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        curRow, curCol = 0,cols -1 
        while curRow< rows and curCol >=0:
            #print(grid[curRow][curCol])
            if grid[curRow][curCol] > target:
                # add the whole row 
                curCol -= 1
            elif grid[curRow][curCol] < target:
                curRow += 1
            elif grid[curRow][curCol] == target:
                return True
        return False