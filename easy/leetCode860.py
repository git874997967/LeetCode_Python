# 860. Lemonade Change
def lemonadeChange( bills):
    changeMap = {}
    for bill in bills:
        if bill == 5:
             changeMap[5] = changeMap.get(5,0) + 1
        elif bill == 10:
            change = changeMap.get(5,0)
            if change == 0 :
                return False 
            changeMap[5] = change - 1
            changeMap[10] = changeMap.get(10,0) + 1
        elif bill == 20:
             change10 = changeMap.get(10,0)
             change5 = changeMap.get(5,0)
             if change10 > 0 and change5 > 0:
                 changeMap[10] = change10 - 1
                 changeMap[5] = change5 - 1
             elif change5 > 2:
                changeMap[5] = change5 - 3
             else:
                 return False

    return True




bills1 = [5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,
         5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20]
bills2  = [5,5,5,10,20]
bills3 = [5,5,10,10,20]
print(lemonadeChange(bills1))
print(lemonadeChange(bills2))
print(lemonadeChange(bills3))