# 859. Buddy Strings
def buddyStrings(s, goal):
    # check length
    if len(s) != len(goal):
        return False 
    # if string are equal then check if some chars repeat twice 
    elif s == goal:
        countArr = [0] * 26
        for char in s:
            countArr[ord(char) - ord('a')] += 1
        for num in countArr:
            if num >= 2:
                return True 
        return False    
    # not equal  then just check one char swap 
    else:
        countArr = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                countArr.append(i)
        if len(countArr) == 2:
            if s[countArr[0]] == goal[countArr[1]] and s[countArr[1]] == goal[countArr[0]]:
                return True 
        return False 


print(buddyStrings("aa","aa")) # True 

print(buddyStrings("ab","ba")) # True 

print(buddyStrings("ab","ab")) # False 

print(buddyStrings("abcd","abcd")) # False 

print(buddyStrings("abab","abab")) # True 





