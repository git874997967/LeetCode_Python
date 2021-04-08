# 204. Count Primes
def countPrimes(n):
    if n < 3 :
        return 0
    primes = [True] * n
    primes[0] = primes[1] = True
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)
countPrimes(10)