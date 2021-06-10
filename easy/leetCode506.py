# 506. Relative Ranks
def findRelativeRanks(score):
    rank, scoreOrg = {},score.copy()
    score.sort(reverse = True )
     
    for i in range(len(score)):
        rank[score[i]] = i
    for i in range(len(score)):
        print(scoreOrg[i])
        scoreOrg[i] = rank.get(scoreOrg[i]) + 1
        if scoreOrg[i] == 1:
            scoreOrg[i] = 'Gold Medal'
        if scoreOrg[i] == 2:
            scoreOrg[i] = 'Silver Medal'
        if scoreOrg[i] == 3:
            scoreOrg[i] = 'Bronze Medal'
        else:
            scoreOrg[i] = str(scoreOrg[i])
    return scoreOrg

def findRelativeRanks2(score):
    sorted_score = sorted(score, reverse = True)
    rank = {}
    for i in range(len(sorted_score)):
        if i == 0:
            rank[sorted_score[i]] = "Gold Medal"
        
        elif i == 1:
            rank[sorted_score[i]] = "Silver Medal"
        
        elif i == 2:
            rank[sorted_score[i]] = "Bronze Medal"
        else:
            rank[sorted_score[i]] = str( i + 1)
    return [rank[points] for points in score]

print(findRelativeRanks2([10,3,8,9,4]))
        

