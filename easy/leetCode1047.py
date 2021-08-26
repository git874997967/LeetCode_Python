#1047. Remove All Adjacent Duplicates In String
def removeDuplicates(s):
    charStack = []
    for char in s:
         if len(charStack) != 0 and  charStack[-1] == char:
             charStack.pop()
         else:
              charStack.append(char)  
        
    print(charStack)



removeDuplicates("abbaca")

removeDuplicates("a")

