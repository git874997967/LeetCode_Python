#1051. Height Checker
def heightChecker(heights):
    sortedHeight ,count = sorted(heights), 0
    for i in range(len(sortedHeight)):
        if sortedHeight[i] != heights[i]:
            count += 1
    return count 

print(heightChecker([1,1,4,2,1,3]))


print(heightChecker([5,1,2,4,3]))


print(heightChecker([1,2,3,4,5]))
print(heightChecker([5,1,2,3,4]))