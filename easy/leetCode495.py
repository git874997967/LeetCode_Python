# 495. Teemo Attacking 
def findPoisonedDuration( timeSeries, duration):
    result = 0
    for i in range(1,len(timeSeries)):
        if timeSeries[i] - timeSeries[i -1] > duration:
            result += duration
        else:
            result += timeSeries[i] - timeSeries[i-1]
    return result + duration

print(findPoisonedDuration([1,4],2))


print(findPoisonedDuration([1,2],2))


