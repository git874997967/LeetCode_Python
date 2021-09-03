#1588. Sum of All Odd Length Subarrays
def sumOddLengthSubarrays(arr):
    lenArr,result = len(arr),0
    for i in range(lenArr+1):
        if i % 2 == 1:
            for j in range(0,lenArr-i+1):
                result += sum(arr[j:j+ i])
    print(result)

sumOddLengthSubarrays([1,4,2,5,3])
sumOddLengthSubarrays([10,11,12])
sumOddLengthSubarrays([1,2])
