#1486. XOR Operation in an Array
def xorOperation(n, start):
    result = start
    for ind in range(1,n):
        
        num = start + 2 * ind 
        #print(num)
        result ^= num  

    print(result)

xorOperation(5,0)

xorOperation(4,3)


xorOperation(1,7)