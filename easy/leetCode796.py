#796. Rotate String
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    
    newString = s + s 

    for i in range(len(goal)):
        if newString[i:i+len(goal)] == goal:
            return True 
    
    return False 

print(rotateString("abcde","cdeab"))


print(rotateString("abcde","abced"))