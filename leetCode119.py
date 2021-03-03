# Pascal's Triangle II
def getRow(self, rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    prev = [1,1]
    for i in range(rowIndex + 1):
        cur = [0] * (i + 1)
        cur[0],cur[-1] = 1,1
        for j in range(1,i):
            cur[j] =  prev[j-1] + prev[j]
        prev = cur    
    return cur
