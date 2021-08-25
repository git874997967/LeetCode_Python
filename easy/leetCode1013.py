#1013. Partition Array Into Three Parts With Equal Sum
def canThreePartsEqualSum(arr):
    # the 3 sum must be 3 divided
    if sum(arr) % 3  != 0:
        return False
    
    totalSum, start , end = sum(arr), 0 , len(arr) - 1
    sum1,sum2,sum3 = 0, 0 , 0
    while start < len(arr):
        sum1 += arr[start]
        start += 1
        if sum1 == totalSum / 3:
            break
    while end > 0:
        sum3 += arr[end]
        end -= 1
        if sum3 == totalSum/3:
             break
    print(sum1,sum3, sum(arr[start:end+1]), start, end)
    return sum(arr[start:end+1]) == sum1 and start <= end 

def canThreePartsEqualSum2(arr):
    total = sum(arr)
    if total %3 != 0:
        return False 
    count , target , cuSum = 0,total //3, 0
    for num in arr:
        cuSum += num 
        if cuSum == target:
            count += 1
            cuSum = 0 
    return count >= 3

print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))

print(canThreePartsEqualSum([3,2,1,3]))

print(canThreePartsEqualSum([3,3,1,2]))


print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))

print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))