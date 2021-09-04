#1758. Minimum Changes To Make Alternating Binary String
def minOperations(s):
     oddOdd , oddEven = 0 , 0
     for index in range(len(s)):
         if index % 2 == 0 and s[index] == '0':
             oddEven += 1
         elif index % 2 == 0 and s[index] == '1':
             oddOdd += 1
         if index % 2 == 1 and s[index] == '0':
                oddOdd += 1
         elif index % 2 == 1 and s[index] == '1':
             oddEven += 1
     return min(oddEven,oddOdd)



print(  minOperations("0100"))
print(  minOperations("10"))
print(  minOperations("1111"))
print(  minOperations("11111"))
print(  minOperations("10000"))