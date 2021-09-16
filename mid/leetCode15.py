# 15 3sum
# for each num in arr play the 2 sum  
 
def threeSum(arr):
    arr.sort()
    result = []
    n = len(arr)
    for i in range(n):
        left , right = i + 1, n - 1
        # all others larger than 0 and no matched condition anymore 
        if arr[i] > 0 :
          break 
        # we need to find the last th for the repeat num
        if i >= 1 and arr[i] == arr[i - 1]:
            continue
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total > 0 :
                right -= 1
            elif total < 0:
                left += 1
            else:
                # as left - i + 1 and right = n - i   means i is the smallest one  
                result.append([arr[i],arr[left],arr[right]])
                while left != right and arr[left] == arr[left + 1] : left += 1
                while left != right and arr[right] == arr[right - 1]: right -= 1
                left += 1
                right -= 1
    print(result)
    return result



threeSum([-1,0,1,2,-1,-4])

threeSum([0,0,0,0])
