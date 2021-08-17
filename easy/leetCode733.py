# 733. Flood Fill  
def floodFill(image, sr, sc, newColor):
     dirs = [[0,1],[0,-1],[1,0], [1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]
     if newColor == image[sr][sc]:
         return image 
     oldColor = image[sr][sc]
     def helper(image, sr,sc,oldColor,newColor):
         image[sr][sc] = newColor
         for dir in dirs:
             newX = dir[0] + sr
             newY = dir[1] + sc 
             if newX >=0 and newX < len(image) and newY >= 0 and newY < len(image[0]):
                 if image[newX][newY] == oldColor:
                     helper(image,newX,newY,oldColor,newColor)
     
     helper(image,sr,sc,oldColor,newColor)
     return image 
 
    

 