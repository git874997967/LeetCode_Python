#1652. Defuse the Bomb
def decrypt(code, k):
    result = []
    if k == 0:
        return [0] * len(code)
    elif k > 0:
        newCode  = code * 2 
        for i in range(len(code)):
            result.append(sum(newCode[i+1:i+1+k]))    
    else:
        newCode  = code * 2
        for i in range(len(code),len(newCode),1):
            result.append(sum(newCode[i+k:i]))

    print(result)

decrypt([5,7,1,4],3)

decrypt([5,7,1,4],0)

decrypt([2,4,9,3],-2)
  