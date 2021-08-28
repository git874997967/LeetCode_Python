#1351. Count Negative Numbers in a Sorted Matrix

# the matrix is step-liked
# ++++++
# ++++--
# ++++--
# +++---
# +-----
# +-----
def countNegatives(self, grid):
    # start from bottom left corner
    m , n = len(grid) ,len(grid[0])
    r,c ,result = m - 1, 0 , 0 
    while r >= 0 and c < n :
        if grid[r][c] < 0:
            r -= 1
            result += n- c 
        else:
            c += 1
    return result
