#1128. Number of Equivalent Domino Pairs
def numEquivDominoPairs(dominoes):
    pairMap = {}
    for dominoe in dominoes:
        domTuple = tuple(dominoe)
        if dominoe[1] <= dominoe[0]:
            domTuple = tuple([dominoe[1],dominoe[0]])
        pairMap[domTuple] = pairMap.get(domTuple,-1) + 1
    result = 0
    for key, value in pairMap.items():
        if value > 0:
            result +=  value *(value + 1) /2
    return result


[[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]         
nums1 = [[2,1],[5,4],[3,7],[6,2],[4,4],[1,8],[9,6],[5,3],[7,4],[1,9],[1,1],[6,6],[9,6],[1,3],[9,7],[4,7],[5,1],[6,5],[1,6],[6,1],[1,8],[7,2],[2,4],[1,6],[3,1],[3,9],[3,7],[9,1],[1,9],[8,9]] # (1,2) 1 +(2,1) = 2 (3,4) 2 + (4,3) = 3  c22 + c32 = 4
nums2 = [[1,2],[1,2],[1,1],[1,2],[2,1]] # (1,2) 3 + (2,1)1 = 4   c42 = 6

print(numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]  ))
# print(numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))

print(numEquivDominoPairs(nums1))
# print(numEquivDominoPairs(nums2))