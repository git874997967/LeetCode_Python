#1243. Array Transformation
def transformArray(arr):
    count = 0
    while count != len(arr)-2:
        count = 0
        addArr,minArr = [],[]
        for i in range(1,len(arr)-1):
            if arr[i-1] > arr[i] and  arr[i] < arr[i + 1]:
                addArr.append(i)
            elif arr[i] > arr[i-1] and arr[i] > arr[i + 1]:
                minArr.append(i)
            else:
                count += 1
        for i in addArr:
            arr[i] += 1
        for i in minArr:
            arr[i] -= 1
       

    print(arr)

transformArray([6,2,3,4]) 
transformArray([1,6,3,4,3,5]) 

transformArray([2,1,2,1,1,2,2,1]) #[2,2,1,1,1,2,2,1]
 