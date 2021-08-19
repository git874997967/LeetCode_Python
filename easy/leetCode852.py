#852. Peak Index in a Mountain Array
def peakIndexInMountainArray(arr):
    start , end = 0, len(arr) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid -1 ] < arr[mid] and arr[mid + 1] < arr[mid]:
            return mid 
        elif arr[mid + 1] < arr[mid] and arr[mid - 1] > arr[mid]:
            end = mid 
        elif arr[mid -1] < arr[mid] and arr[mid + 1] > arr[mid]:
            start = mid 
     
    return start if arr[start] > arr[end] else end 


print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([0,10,5,2]))
print(peakIndexInMountainArray([3,4,5,1]))
print(peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))


    