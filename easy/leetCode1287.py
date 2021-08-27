# 1287. Element Appearing More Than 25% In Sorted Array
# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.
# [1,2,2,6,6,6,6,7,10]  ans = 6
def findSpecialInteger(arr):
    length = len(arr)
    times = length//4 + 1
    for i in range(length - times + 1):
        if arr[i] == arr[i + times - 1]:
            print(arr[i])
    return 0
arr = [1,2,2,6,6,6,7,10]
arr2 = [1,2,2,3]
findSpecialInteger(arr)
findSpecialInteger(arr2)
