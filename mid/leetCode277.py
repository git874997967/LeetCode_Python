# 277. Find the Celebrity
class solution():
    
    numOfPeople = 0
    def findCelebrity(self, n):
        numOfPeople = n
        celeCandidate = 0
        for i in range(n):
            
            if knows(celeCandidate,i):
                celeCandidate = i
        if isCelebrarity(celeCandidate):
            return celeCandidate
        return -1

    def isCelebrarity(i):
        # all others must know i  
        for j in range(numOfPeople):
            # skip himself
            if i == j :
                continue
            # i 不够高冷  认识了别人 或者 i 不够出名  有人不认识
            if knows(i,j) or not knows(j,i):
                return False
        return True
    
