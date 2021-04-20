# 258. Add Digits
 def addDigits(num):
      if num < 10:
          return num 
      result = 0
      while num >= 10:
          result += num % 10
          num = num // 10
      result += num 
      while result >= 10:
          result = result % 10 + result // 10
          if result < 10:
              return result 
      return result
     