#1779. Find Nearest Point That Has the Same X or Y Coordinate\
def nearestValidPoint(x, y, points):
    minDistance,result = float('inf'),0
    for i in range(len(points)):
        point = points[i]
        if point[0] == x and point[1] == y:
            return i
        elif point[0] == x or point[1] == y:
            dis = abs(point[0]- x) + abs(point[1]- y)
            if dis < minDistance:
                minDistance = dis
                result = i 
    return -1 if minDistance == float('inf') else result 