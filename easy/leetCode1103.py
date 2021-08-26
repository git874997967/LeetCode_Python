#1103. Distribute Candies to People
def distributeCandies( candies, num_people):
    candyArr  = []
    result = [0] * num_people
    start , index  = 0
    while candies > 0:
        if candies >= start + 1:
            candyArr.append(start)
        else:
            candyArr.append(candies)
        candies -= start
        start += 1
    candyLength = num_people - (len(candyArr) % num_people) 
    while candyLength > 0 :
        candyArr.append(0)
        candyLength -= 1
    
    while index < len(candyArr):
        currentRound = candyArr[index:index+ num_people]
        for i in range(num_people):
            result[i] += currentRound[i]
        index += num_people
    return result 


def distributeCandies2(candies,n):
    res = [0] * n
    i = 0 
    while candies > 0:
        res[i % n] += min(candies,i+ 1)
        candies -= i + 1
        i += 1
    print(res)



distributeCandies2(11,3)
distributeCandies2(30,4)
distributeCandies2(7,4)