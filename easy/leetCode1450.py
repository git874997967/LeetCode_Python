#1450. Number of Students Doing Homework at a Given Time
def busyStudent( startTime, endTime, queryTime):
    result = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime or queryTime <= endTime[i]:
            result += 1
    print(result)
