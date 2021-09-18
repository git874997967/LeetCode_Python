def maxDistToClosest(seats):
     emptySeates = [0,0]
     result = 1
     N = len(seats)
     seats += [1]
     i = 0
     while i <= N:
        es = i
        zLength = 0  
        while es <= N and seats[es] == 0 and seats[es + 1] == 0:
           es += 1
           zLength += 1
        emptySeates[0] , emptySeates[1] = i , es 

        if emptySeates[0] == 0 or emptySeates[1] == N -1:
            distance = (1 + emptySeates[1] - emptySeates[0])
        else:
            distance = (2 + emptySeates[1] - emptySeates[0])// 2
            
        result = max(result,distance)
         
        i = es 
        i += 1
      
     return result 



print(maxDistToClosest([1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0]))

print(maxDistToClosest([0,0,0,0,1,0,0,0]))
print(maxDistToClosest([1,0,0,0,1,0,1]))

print(maxDistToClosest([1,0,0,0,0,0,1]))

print(maxDistToClosest([1,0,0,0,1,0,0]))
print(maxDistToClosest([1,0,0,0,0,0,0]))

print(maxDistToClosest([0,0,0,0,1,0,0]))


