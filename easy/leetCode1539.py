#1539. Kth Missing Positive Number
def findKthPositive( arr, k):
    result = 0
    for num in range(1,arr[-1]):
        if num not in arr:
            result += 1
        if result == k:
            print(num)
            return num
    return arr[-1] + k
    

def findKthPositive2(arr,k):
    start,end = 0 , len(arr) - 1
    while start + 1 < end:
        mid = (start + end) / 2 
        # 前 mid 个数字 是否有gap
        gap = arr[mid] - (mid +1)
        if gap < k:
            start = mid 
        else:
            end = mid  
    # the number is beyond the  arr[-1]
    if arr[end] - (end + 1) < k:
        return arr[end] + k - (arr[end] - (end + 1))
    if arr[start] - (start + 1) < k:
        return arr[start] + k - (arr[start] - (start + 1))
    return k 


findKthPositive([2,3,4,7,11], 5) 
    
findKthPositive([1,2,3,4], 2) 
    