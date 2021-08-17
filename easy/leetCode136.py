# 136. Single Number
def singleNumber(  nums):
    result = 0
    for  i in range(len(nums)):
        result = result ^ nums[i]

    return result

arr = [2,2,1]
res =  singleNumber(arr)

def singleChar(str):
     result = ""
     if str is None:
         return result 
     charMap = {}
     for char in str:
         if charMap.get(char,0) == 0:
             charMap[char] = 1
         else:
            charMap[char]  += 1
     for k,v in charMap.items():
        if charMap[k] == 1:
            result = k
            break
     return result

str = "abcdeefgaabefcdbcdef"
print(singleChar(str)
)