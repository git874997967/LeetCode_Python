#1064. Fixed Point
def fixedPoint(arr):
# binary search 
    start, end = 0 , len(arr) - 1
    while start + 1 < end:
        mid = (start + end) / 2
        if arr[mid] <= mid:

            


