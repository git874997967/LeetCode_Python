# 682. Baseball Game
def calPoints(ops):
    
    result,stk = 0, []
    
    for item in ops:

        if item == 'C':
        
            stk.pop()
        
        elif item == 'D':
        
            prev = stk.pop()
            stk.append(prev)
            stk.append(prev * 2)
        
        elif item == '+':
        
            second = stk.pop()
            first = stk.pop()
            stk.append(first)
            stk.append(second)
            stk.append(second + first)
        
        else: 
        
            print(int(item))
            stk.append(int(item))
 
    return sum([key for key in stk])

# print(calPoints(["5","2","C","D","+"]))

print(calPoints(["5","-2","4","C","D","9","+","+"]))

# print(calPoints(["1"]))

