# 15 3sum
def threeSum(nums):
      nums.sort()
      result = []
      def twoSum(nums,i,result):
          start , end = i + 1, len(nums) - 1
          while start < end:
              numSum = nums[start] + nums[i] + nums[end]
              if numSum > 0:
                  end -= 1
              elif numSum < 0:
                  start += 1
              else:
                  result.append([nums[start],nums[i],nums[end]])
                  start += 1
                  end -= 1
                  # start == start -1 corresponding to i != i - 1 start will pass all the duplidate i  
                  # i points to the start of duplidate and end  will point to the end 
                  # take example of  0 -1(i) -1 -1(start)  
                  while start < end and  nums[start] == nums[start - 1]:
                      start += 1


      for i in range(len(nums)):
          if nums[i] > 0 :
              break
          if i == 0 or nums[i] != nums[i-1]:
              # i is the min num in the tuple  start will be i + 1 till end and i always point to the first num  in duplicate set 
              print("passing num ",nums[i:])
              twoSum(nums,i,result)

      print( result )


threeSum([-1,0,1,2,-1,-4])

threeSum([0,0,0,0])
