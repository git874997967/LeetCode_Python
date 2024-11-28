def stableMountains(height, threshold):
     result = []
     for idx in range(1,len(height)):
         if height[idx-1] > threshold:
             result.append(idx)
             
             
     print(result)
    
stableMountains([1,2,3,4,5],2)

stableMountains([10,1,10,1,10],3)

stableMountains([10,1,10,1,10],10)
         