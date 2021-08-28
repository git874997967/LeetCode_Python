#1299. Replace Elements with Greatest Element on Right Side
def replaceElements(arr):
   arr.append(-1) 
   curMax = float('-inf')
   for i in range(len(arr)-1,-1,-1):
       curMax = max(arr[i],curMax)
       arr[i] = curMax
     
   print(arr[1:])

        
replaceElements([17,18,5,4,6,1])

replaceElements([17])