# 682. Baseball Game
def calPoints(ops):
    result,stk = 0, []
    for item in ops:
        if item.isnumeric() or item.strip("-").isnumeric():
            print(int(item))
            stk.append(int(item))
        if item == 'C':
            stk.pop()
        if item == 'D':
            prev = stk.pop()
            stk.append(prev)
            stk.append(prev * 2)
        if item == '+':
            second = stk.pop()
            first = stk.pop()
            stk.append(first)
            stk.append(second)
            stk.append(second + first)
 
    return sum([key for key in stk])

# print(calPoints(["5","2","C","D","+"]))

print(calPoints(["5","-2","4","C","D","9","+","+"]))

# print(calPoints(["1"]))

