# 657. Robot Return to Origin
def judgeCircle(moves):
    if len(moves) %2 == 1:
        return False 
    lCount = rCount = uCount = dCount = 0
    for i in range(len(moves)):
        if moves[i] =='L':
            lCount += 1
        elif moves[i] == 'R':
            rCount += 1
        elif moves[i] == 'U':
            uCount += 1
        else:
            dCount += 1
    return  True if lCount == rCount and uCount == dCount else False

print(judgeCircle("UD"))


print(judgeCircle("LDRRLRUULR"))

print(judgeCircle("LL"))

