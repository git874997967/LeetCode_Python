#941. Valid Mountain Array

#only inscrease happend in the firs part 
def validMountainArray( arr):
  i = 0 
  n = len(arr)
  # check the insc part first 
  while i < n - 1 and arr[i] < arr[i + 1]:
      i += 1
  # check if we meet the end
  if i == 0 or i == n - 1:
      return False 
  while i < n - 1 and arr[i] > arr[i + 1]:
      i += 1
  return i == n - 1
  # check the desc part second 
  # check if we meet the dest last
def validMountainArray2( arr):
     i,n = 0, len(arr)
     while i + 1 < n and arr[i] < arr[i+1]:
         i += 1
     if i == 0 or i == n - 1:
        return False 
     while i + 1 < n and arr[i] > arr[i +1]:
        i += 1
     return i == n -1


print(validMountainArray([0,3,2,1]))
print(validMountainArray([2,1,0,2,1,0]))
print(validMountainArray([2,1,1,0]))
print(validMountainArray([2,1,0,-1]))
print(validMountainArray([1,2,3,2,1]))
print(validMountainArray([3,5,5]))
