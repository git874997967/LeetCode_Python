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
# one pass
def addDigits2(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
        if num == 0 and result > 9:
            num = result 
            result = 0
    return result 