# 277. Find the Celebrity
def findCelebrity(n):
    celeCandidate = 0 
    for i in range(1,n):
        if knows(celeCandidate, i):
            celeCandidate = i  
    for i in range(n):
        if i == celeCandidate:
            continue
        elif not knows(i,celeCandidate) or knows(celeCandidate,i):
            return -1 
        
    return celeCandidate
        

 