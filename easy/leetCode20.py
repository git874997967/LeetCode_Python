#20. Valid Parentheses
def isValid(s):
    # base case
    if len(s) == 0 or len(s) % 2 == 1:
        return False
    stack = []
    for i in range(len(s)):
        if s[i] =='(' or s[i] =='[' or s[i] =='{':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0 or s.pop() != '(':
                return False
        elif s[i] == ']':
            if len(stack) == 0 or s.pop() != '[':
                return False
        elif s[i] =='}':
            if len(stack) == 0 or s.pop() != '{':
                return False
    if len(stack) == 0:
        return True
    return False
            
    