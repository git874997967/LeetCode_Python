# 1200. Minimum Absolute Difference
# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

def minimumAbsDifference(arr):
    result = []
    arr.sort()
    # Intervals.sort(key = lambda x:x[0])
    minDistance =  float('inf')
    print(arr)
    dict = {}
    for i in range(len(arr) - 1):
        distance = arr[i+ 1] - arr[i]
        minDistance = min(minDistance,distance)
        if distance not in dict:
            dict[distance] = []
        dict[distance].append([arr[i], arr[i + 1]])
    return dict[minDistance]

arr = [3,8,-10,23,19,-4,-14,27]
arr2 = [1,3,6,10,15]
print(minimumAbsDifference(arr))
print(minimumAbsDifference(arr2))



def minimumAbsDifference2(self, arr):
"""
:type arr: List[int]
:rtype: List[List[int]]
"""
    arr.sort()
    minDif = float("inf")

    for i in range(1, len(arr)):
        prev = arr[i-1]
        curr = arr[i]
        dif = abs(curr-prev)

        if dif<minDif:
            res = [[prev, curr]]
            minDif = dif
        elif dif==minDif:
            res.append([prev, curr])

    return res