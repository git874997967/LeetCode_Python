#914. X of a Kind in a Deck of Cards
def hasGroupsSizeX( deck):
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b, a % b)
    if len(deck) == 1:
        return False 
    cardMap = {}
    for card in deck:
        cardMap[card] = cardMap.get(card, 0) + 1
    if len(cardMap) == 1:
        return True 
    numSet = list(set([v for v in cardMap.values()]))

    x = numSet[0]
    for i in range(1,len(numSet)):
        print(x,numSet[i])
        x = gcd(x,numSet[i])
        if x == 1:
            return False 
    return True 

print(hasGroupsSizeX([1,2,3,3,2,1]))