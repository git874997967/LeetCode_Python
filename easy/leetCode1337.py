#1337. The K Weakest Rows in a Matrix
def kWeakestRows(mat, k):
    rowMap = {}
    result = []
    for index  in range(len(mat)):
        row = mat[index]
        count = row.count(1) 
        soliderCount = count
        rowMap[index] = soliderCount
    sortedMap = sorted(rowMap.items(),key = lambda x:(x[1],x[0]))
    for i in range(k):
        pair = sortedMap[i]
        
        result.append(pair[0])
    print(result)
    return result

mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
kWeakestRows(mat,k)
mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
k = 2
kWeakestRows(mat,k)