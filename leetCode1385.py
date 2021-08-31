#1385. Find the Distance Value Between Two Arrays
import bisect 
# diff between arr1[i] and all val in arr2  diff > 2
def findTheDistanceValue(arr1, arr2, d):
    arr2.sort()
    minVal ,maxVal= arr2[0] - d, arr2[-1] + d
    result = len(arr1)
    for num in arr1:
        if num in range(minVal,maxVal):
            result -= 1
    print(result)

def findTheDistanceValue2(arr1, arr2, d):
    arr2.sort()
    distance = 0
    for num1 in arr1:
        index = bisect.bisect_left(arr2, num1)
        if index == 0:
            if abs(arr2[0] - num1) > d:
                distance += 1
        elif index == len(arr2):
            if abs(arr2[-1] - num1) > d:
                distance += 1
        else:
            if abs(arr2[index] - num1) > d and abs(arr2[index - 1] - num1) > d:
                distance += 1
    return distance 

 
findTheDistanceValue2([-3,2,-5,7,1],[4],84)