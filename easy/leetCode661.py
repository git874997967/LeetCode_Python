# 661. Image Smoother
# border detection 
import math
def imageSmoother(img):
    directs,result = [[-1,0],[1,0],[0,-1],[0,0],[0,1],[1,1],[-1,-1],[1,-1],[-1,1]], img 
    row, col = len(img), len(img[0])
    def helper(pic,r,c):
        sumNum, count = 0, 1
        for dir in directs:
            newX, newY = r + dir[0], c + dir[1] 
            if newX >= 0 and newY >= 0 and newX < row and  newY < col :
                count += 1
                sumNum += pic[newX][newY]

        return math.floor(sumNum / count )

    return result 

#print(imageSmoother([[1,1],[1,1]]))

# print(imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))


print(imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))