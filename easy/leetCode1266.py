#1266. Minimum Time Visiting All Points
def minTimeToVisitAllPoints(points):
    step = 0
    for i in range(len(points)-1):
        current,dest = points[i],points[i+1]
        while current[0] < dest[0] and current[1] < dest[1]:
            current[0] += 1
            current[1] += 1
            step += 1
        while current[0] > dest[0] and current[1] > dest[1]:
            current[0] -= 1
            current[1] -= 1
            step += 1
        while current[0] < dest[0] and current[1] > dest[1]:
            current[0] += 1
            current[1] -= 1
            step += 1
        while current[0] > dest[0] and current[1] < dest[1]:
            current[0] -= 1
            current[1] += 1
            step += 1
        while current[0] < dest[0]:
            current[0] += 1
            step += 1
        while current[0] > dest[0]:
            current[0] -= 1
            step += 1
        while current[1] < dest[1]:
            current[1] += 1
            step += 1
        while current[1] > dest[1]:
            current[1] -= 1
            step += 1
    return step

def minTimeToVisitAllPoints2(points):
    count, size = 0,len(points)
    for index in range(size-1):
        x_diff = points[index][0] - points[index+1][0]
        y_diff = points[index][1] - points[index + 1][1]
        count += max(abs(x_diff),abs(y_diff))
# minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
# minTimeToVisitAllPoints([[3,2],[-2,2]])
minTimeToVisitAllPoints([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])

