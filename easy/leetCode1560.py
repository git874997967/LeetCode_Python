#1560. Most Visited Sector in a Circular Track
def mostVisited(n, rounds):
    score = [0] * (n + 1)
    result = []
    for round in range(1,len(rounds)):
        start, end = rounds[round-1], rounds[round]
        if start < end :
            for i in range(start+1,end+1):
                score[i] += 1
        else:
            for i in range(start+1,n+ 1):
                score[i] += 1
            for i in range(1,end+1):
                score[i] += 1
    score[rounds[0]] += 1
    for i in range(1,len(score)):
        if score[i] == max(score):
            result.append(i)

    return result


mostVisited(4,[1,3,1,2])
mostVisited(2, [2,1,2,1,2,1,2,1,2])
mostVisited(7,[1,3,5,7])
 
   