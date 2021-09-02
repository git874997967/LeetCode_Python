#1496. Path Crossing
def isPathCrossing(path):
    pointSet = [(0,0)]
    
    for dir in path:
        curPoint = pointSet[-1]
        if dir == 'N':
            curPoint = (curPoint[0],curPoint[1]+1)
        elif dir == 'S':
           curPoint = (curPoint[0],curPoint[1]-1)
        elif dir == 'E':
            curPoint = (curPoint[0]+1,curPoint[1])
        elif dir == 'W':
            curPoint = (curPoint[0]-1,curPoint[1])
        if curPoint in pointSet:
            return True 
        else:
            pointSet.append(curPoint)
     
    return False 

print(isPathCrossing("NS"))
print(isPathCrossing("NES"))
print(isPathCrossing("NESWW"))