#167. Two Sum II - Input array is sorted
 def twoSum(numbers, target):
      start , end = 0, len(numbers) - 1
      while start < end:
          if numbers[start] + numbers[end] < target:
              start += 1
          elif numbers[start] + numbers[end] > target:
              end -= 1
          else:
              return [start + 1, end + 1]

              
