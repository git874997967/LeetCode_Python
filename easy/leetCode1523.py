#1523. Count Odd Numbers in an Interval Range
def countOdds(low, high):
    diff = high - low 
    result = 0
    if low % 2 == 0 and high % 2 == 0:
        return diff // 2 
    elif low % 2 == 1 and high % 2 == 1:
        return diff // 2 + 1
     
    else:
        return (diff + 1) /2 
     