#1534. Count Good Triplets
def countGoodTriplets(arr, a, b, c):
    result = i = j = k = 0 
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            k = j + 1
            while k < len(arr):
                
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <= c:
                    result += 1
                k += 1
            j += 1
        i += 1
    print(result)
    return result

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
countGoodTriplets(arr,a,b,c)
arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
countGoodTriplets(arr,a,b,c)