#1688. Count of Matches in Tournament
def numberOfMatches(n):
    result = 0
    while n > 1:
        match = n // 2 if n % 2 == 0 else (n - 1) // 2
        n = n // 2 if n % 2 == 0 else (n-1)//2 + 1
        
        
        result += match 
    print(result)

numberOfMatches(7)

numberOfMatches(14)