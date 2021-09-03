#1614. Maximum Nesting Depth of the Parentheses
 def maxDepth(s):
     result = 0
     level = 0
     for char in s:
         if char == '(':
             level += 1
             result = max(level,result)
         elif char == ')':
             level -= 1
     return result   