# 844. Backspace String Compare
def backspaceCompare(s, t):
    stack1, stack2 = [],[]
    for char in s:
        if char != '#':
            stack1.append(char)
        elif len(stack1) != 0:
            stack1.pop()
    
    for char in t:
        if char != '#':
            stack2.append(char)
        elif len(stack2) != 0:
            stack2.pop()
    print(stack1 == stack2)

    return stack1 == stack2 


backspaceCompare("ab#c","ad#c")

backspaceCompare("a##c","a##c")

backspaceCompare("ab##","ad##")

backspaceCompare("a#c","b")