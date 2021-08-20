#896. Monotonic Array
def isMonotonic(nums):
    increase = decrease = False 
    
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            increase = True 
        elif nums[i] < nums[i - 1]:
            decrease = True 

        if increase and decrease :
         return False
    return True 

print(isMonotonic([1,2,2,3])) # True


print(isMonotonic([6,5,4,4])) # True 


print(isMonotonic([1,3,2])) # False 


print(isMonotonic([1,1,1]))  # True 

