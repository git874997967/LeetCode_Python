#1086. High Five
import collections
def highFive( items):
    scoreMap = collections.defaultdict(list)
    resultArr = []
    for id,score in items:
        scoreMap[id].append(score)
    for id, scores in scoreMap.items():
       sorted(scores, reverse= True)
       resultArr.append([id,sum(scores[:5])//5])
    print(sorted(resultArr))
    return sorted(resultArr)


items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
#items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
#Output: [[1,87],[2,88]]
items = [[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]
highFive(items)

