#1018. Binary Prefix Divisible By 5
def prefixesDivBy5(nums):
      resultArr,result =[], 0
      numStr = ''
      
      for i in range(len(nums)-1):
          numStr += str(nums[i])
      
          result += int(numStr[i])
          result *= 2
          resultArr.append(True) if result % 5 ==0 else resultArr.append(False)
      numStr += str(nums[-1])
      result += int(numStr[-1])
      resultArr.append(True) if result % 5 ==0 else resultArr.append(False)
      print(resultArr)
#ef perfixDivBy52(nums):
    
prefixesDivBy5([0,1,1])
prefixesDivBy5([1,1,1])


