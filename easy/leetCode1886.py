#1886. Determine Whether Matrix Can Be Obtained By Rotation
def findRotation(mat, target):
    if mat == target:
        return True
    D90 ,D180,D270 = [],[],[]
    newMat = mat[::-1]
    for col in zip(*newMat):
        D90.append(list(col))
    if D90 == target :return True 
    newMat = D90[::-1]
    for col in zip(*newMat):
        D180.append(list(col))
    if D180 == target: return True 
    newMat = D180[::-1]
    for col in zip(*newMat):
        D270.append(list(col))
    if D270 == target : return True 

    return False
##matrix rotation
def findRotation2(mat,target):
    for _ in range(4):
        if mat == target:
            return True
        else:
            mat = [list(x) for x in zip(*mat)[::-1]]
    return False

mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]
findRotation(mat,target=target)
mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
findRotation(mat,target=target)