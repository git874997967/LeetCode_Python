#1544. Make The String Great
def makeGood(s):
    result = [s[0]]
    i = 0
    for index in range(1,len(s)):
          
         if len(result) != 0 and abs(ord(result[-1]) - ord(s[index])) == 32:
              
             result.pop()
         else:
              
             result.append(s[index])
             
    print(result)
    return str(result)

makeGood("abBAcC")
makeGood("abBbBbBAcC")
makeGood("leEeetcode")

makeGood("s")