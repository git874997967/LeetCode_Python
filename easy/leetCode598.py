# 598. Range Addition II
def maxCount(m, n, ops):
    minRow, minCol = m,n
    for op in ops:
        minRow, minCol = min(minRow, op[0]) , min(minCol,op[1])
    return minRow * minCol
