#1184. Distance Between Bus Stops
def distanceBetweenBusStops2( distance, start, destination):
    newDistance = distance * 2
    if start < destination:
        return min(sum(newDistance[start:destination]), sum(newDistance[destination:start + len(distance)]))
    elif start > destination:
        return min(sum(newDistance[start:destination+len(distance)]),sum(newDistance[destination:start]))
    else:
        return 0

def distanceBetweenBusStops(distance,start, destination):
    sumDist = sum(distance)
    a = sum(distance[min(start,destination):max(start,destination)])
    return min(a, sumDist - a)

# [7, 10, 1, 12, 11, 14, 5, 0, 0, 5, 14, 11, 12, 1, 10, 7]
distance = [7,10,1,12,11,14,5,0]
start = 7
end = 2
print(distanceBetweenBusStops(distance, start, end ))
distance = [1,2,3,4]
start = 0
end = 1

print(distanceBetweenBusStops(distance, start, end ))
distance = [1,2,3,4]
start = 0
end = 2
print(distanceBetweenBusStops(distance, start, end ))

distance = [1,2,3,4]
start = 0
end = 3

print(distanceBetweenBusStops(distance, start, end ))

distance = [14,13,4,7,10,17,8,3,2,13]
start  = 2
end = 9
print(distanceBetweenBusStops(distance, start, end ))