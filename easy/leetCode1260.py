#1260. Shift 2D Grid
def shiftGrid( grid, k):
    arr = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            arr.append(grid[i][j])
    newArr,k = arr + arr , k % len(arr)
    start = len(arr) - k
    end = len(grid[0])
        
    for i in range(len(grid)):
        grid[i] = newArr[start:start + end]
        start += end
    return grid