#1085. Sum of Digits in the Minimum Number
def sumOfDigits( nums):
    minNum , result = min(nums),0
    while minNum :
        result += minNum % 10
        minNum = minNum // 10
         

    print(abs(result%2 - 1),result)

sumOfDigits([34,23,1,24,75,33,54,8])


sumOfDigits([99,77,33,66,55])

sumOfDigits([99,99,99,99])

sumOfDigits([99,55,55,55,55,55])
