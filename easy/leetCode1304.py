#1304. Find N Unique Integers Sum up to Zero
def sumZero(n):
    print(n)
    result = []
    result.append(0) if n % 2 ==1 else None
    n = int(n/2)
    for i in range(1,n+1):
        result.append(i)
        result.append(-i)
    
    return result

print(sumZero(5))
print(sumZero(6))

print(sumZero(1))
print(sumZero(3))

     