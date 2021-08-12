def search(num,arr):
    if num is None or arr is None:
        return 
    start , end = 0, len(arr) - 1
    while start + 1 < end:
        mid = (start + end) //2
        if arr[mid] == num :
           return mid
        elif arr[mid] > num:
            end = mid - 1 
        else:
            start = mid + 1
    if arr[start] == num:
        return start
    elif arr[end] == num:
        return end
    return -1