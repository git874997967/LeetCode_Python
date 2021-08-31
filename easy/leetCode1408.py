#1408. String Matching in an Array
def stringMatching(words):
     words.sort(key = lambda x:len(x))
     result = []
     for i in range(len(words)):
         for j in range(i+1 ,len(words)):
           
              firstStr,secStr = words[i], words[j]
              firstLen , secLen = len(firstStr), len(secStr)
              if firstStr == secStr:
                result.append(firstStr)
              else:
                  index = 0 
                  while index in range(secLen - firstLen + 1):
                    
                      if secStr[index:index + firstLen] == firstStr:
                          result.append(firstStr)
                          break
                      index += 1
     print(set(result))

stringMatching(["mass","as","hero","superhero"])
stringMatching(["leetcode","et","code"])
stringMatching(["blue","green","bu"])