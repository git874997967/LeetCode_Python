#925. Long Pressed Name


def isLongPressedName2( name, typed):
    if typed == name :
        return True
    if len(typed ) < len(name) :
        return False 
    np = tp = 0
    while np < len(name) and tp < len(typed)  :
        
        if name[np] != typed[tp] :
            return False 
        nCount = tCount = 0
        while  np < len(name) - 1 and name[np] == name[np + 1]:
            np += 1
            nCount += 1
        while  tp < len(typed) - 1 and typed[tp] == typed[tp + 1]:
            tp += 1
            tCount += 1
        if tCount < nCount:
            return False 
        np += 1
        tp += 1
     
    return True  if np == len(name) and tp == len(typed) else False



def isLongPressedName(name,typed):
    ln , lt = len(name),len(typed)
    np, tp = 0 , 0 
    while tp < lt:
        # move the same length as the char in name typed move as well
        if np < ln and name[np] == typed[tp]:
            np += 1
            tp += 1
        # move the typed pointer only if the the current = previous
        elif tp > 0 and typed[tp] == typed[tp - 1]:
            tp += 1
        else:
            return False 
    # pointer in name move to the end
    return np == ln 


print(isLongPressedName("alex","alleex"))



print(isLongPressedName("aleexx","aaaalleexxxxx"))

print(isLongPressedName("saeed","ssaaedd"))

print(isLongPressedName("abcdefg","abcdefg"))


print(isLongPressedName("leelee","llllleeleee"))

print(isLongPressedName("a","ab"))
print(isLongPressedName("a","bc"))