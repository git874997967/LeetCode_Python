#1021. Remove Outermost Parentheses
def removeOuterParentheses(s):
      result , opened = [], 0 
      for c in s:
          if c == '(' and opened > 0: result.append(c)
          if c == ')' and opened > 1: result.append(c)
          opened += 1 if c == '(' else -1



      return ''.join(result)
        
print(removeOuterParentheses("()()"))


#print(removeOuterParentheses("(()())(())(()(()))"))

print(removeOuterParentheses("(()())"))

print(removeOuterParentheses("(()())(())"))