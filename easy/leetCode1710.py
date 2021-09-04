#1710. Maximum Units on a Truck
def maximumUnits(boxTypes, truckSize):
    sortedBox = sorted(boxTypes,key = lambda x:(x[1],x[0]),reverse = True )
    result = 0
    while truckSize > 0 and len(sortedBox) > 0:
        
        boxType =sortedBox.pop(0)
        if boxType[0] <= truckSize:
            
            result += boxType[0] * boxType[1]
            truckSize -= boxType[0]
        else:
            amount = truckSize  
            result += amount * boxType[1]
            truckSize -= amount
    return result 
             
   

maximumUnits([[1,3],[2,2],[3,1]],4)

maximumUnits([[5,10],[2,5],[4,7],[3,9]],10)
[[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
35
maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]],35)
