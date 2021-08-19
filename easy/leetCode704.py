def search(num,arr):
    if num is None or arr is None:
        return 
    start , end = 0, len(arr)  
    while start + 1 < end:
        mid = (start + end) //2
        if arr[mid] == num :
           return mid
        elif arr[mid] > num:
            end = mid   
        else:
            start = mid  
    if arr[start] == num:
        return start
    elif arr[end] == num:
        return end
    return -1

print(search( [56,5,67,100,31],31))