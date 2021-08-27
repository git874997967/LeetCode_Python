#1176. Diet Plan Performance
def dietPlanPerformance( calories, k, lower, upper):
    result = 0
    calSum = sum(calories[0:k])
    if calSum < lower:
        result -= 1
    elif calSum > upper:
        result += 1
    for i in range(1, len(calories) - k + 1):
        calSum = calSum - calories[i-1] + calories[i + k - 1]
        if calSum > upper:
            result += 1
        elif calSum < lower:
            result -= 1

    return result 


print(dietPlanPerformance([6,5,0,0],2,1,5))
print(dietPlanPerformance([3,2],2,0,2))
print(dietPlanPerformance([1,2,3,4,5,6,5,4,3,0,2,3,2,3,5,3],3,2,6))