# 509. Fibonacci Number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
 
def fib2(n):
    if n == 0:
        return 0
    curr, prev = 1,0
    for i in range(1,n):
        # take care the assign order
        prev , cur = cur,prev + cur 
    return cur 
