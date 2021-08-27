#1175. Prime Arrangements
def getPrime(n):
    primeNum = 0
    for num in range(1, n + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primeNum += 1
    return primeNum

print(getPrime(5))