def differenceOfSums(n,m):
    return sum(i if i % m != 0 else -i for i in range(0,n + 1))