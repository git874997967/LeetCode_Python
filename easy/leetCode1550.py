#1550. Three Consecutive Odds
def threeConsecutiveOdds(arr):
    result = False 
    for i in range(len(arr)-2):
        if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
            return True 
    return result