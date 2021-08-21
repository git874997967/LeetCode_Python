#944. Delete Columns to Make Sorted
def minDeletionSize2( strs):
    delete = len(strs[0])
    for i in range(len(strs[0])):
        result = []
        for j in range(len(strs)):
             result.append(strs[j][i])  
        inscO = sorted(result)
        if inscO == result:
            delete -= 1
    return delete

def minDeletionSize( strs):
     res = 0
     for c in zip(*strs):
         if list(c) != sorted(c):
             res += 1
     return res

 



minDeletionSize(["abd","bbc","cbb","dba"])

minDeletionSize(["a","b"])


minDeletionSize(["zyx","wvu","tsr"])
 