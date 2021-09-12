#762. Prime Number of Set Bits in Binary Representation
def countPrimeSetBits(left, right):
    result = 0
    def prime(x):
        if x == 1:
            return False 
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

    for i in range(left,right + 1):
        if prime(bin(i).count('1')):
            result += 1
    return result 