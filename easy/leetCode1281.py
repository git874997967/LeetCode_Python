#1281. Subtract the Product and Sum of Digits of an Integer
def subtractProductAndSum(n):
    prod , sum = 1 , 0 
    while n:
        mode = n % 10
        prod *= mode 
        sum += mode 
        n = n // 10
    
    return prod - sum

subtractProductAndSum(234)


subtractProductAndSum(4421)


subtractProductAndSum(77621)