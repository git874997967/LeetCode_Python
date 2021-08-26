#1122. Relative Sort Array
from typing import DefaultDict


def relativeSortArray(arr1, arr2):
    result, rest = [],[]
    orderMap = {}
    restMap = {}
    for num in arr1:
        if num in arr2:
            orderMap[num] = orderMap.get(num,0) + 1
        else:
            restMap[num] = restMap.get(num,0) + 1
     
    for k in arr2:
        times = orderMap[k]
        while times:
            result.append(k)
            times -= 1

    for k,v in restMap.items():
        times = v
        while times:
            rest.append(k)
            times -= 1     
    result += sorted(rest)
     
    return result

arr1 =[2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]

print(relativeSortArray(arr1,arr2))
    