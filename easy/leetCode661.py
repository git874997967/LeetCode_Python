import math
class Solution(object):
    dirs = [[-1,0],[1,0],[0,-1],[0,0],[0,1],[1,1],[-1,-1],[1,-1],[-1,1]]
    rows , cols  = 0, 0
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.rows , self.cols = len(img), len(img[0])
        result = [[0] * self.cols for i in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):    
                result[row][col] = self.helper(img, row, col)
                
        return result
            
    def helper(self, pic, row,col):
        count, numSum = 0, 0
        for dir in self.dirs:
            newX, newY = row + dir[0] , col + dir[1]
            if newX >= 0 and newY >= 0 and newX < self.rows and newY < self.cols:
                numSum += pic[newX][newY]
                count += 1
         
        return numSum // count