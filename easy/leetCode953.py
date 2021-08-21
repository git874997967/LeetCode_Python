# 953. Verifying an Alien Dictionary
import unittest
class Solution(object):
    def isAlienSorted(self, words, order):
        orderMap = {c:i for i, c in enumerate(order)}
        # compare the i and i + 1 in words
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j > len(words[i + 1]):
                    return False 
                if words[i][j] != words[i + 1][j]:
                    if orderMap[words[i][j]] > orderMap[words[i+1][j]]:
                        return False 
                    else:
                        break
        return True 
         

class UnitTest(unittest.TestCase):
   
    def test(self):
        words ,order = ["apap","app"],  "abcdefghijklmnopqrstuvwxyz"
        
        s = Solution()
        result = s.isAlienSorted(words,order)
         
        self.assertEqual(result,True)
       
    def test1(self):
        
       
        words1 , order1 = ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
       
        s = Solution()
        result1 = s.isAlienSorted(words1,order1)
      
       
        self.assertEqual(result1,True)
        
    def test2(self):
        
       
        words2, order2 = ["word","world","row"], "worldabcefghijkmnpqstuvxyz"
        s = Solution()
        result2 = s.isAlienSorted(words2,order2)
        
        self.assertEqual(result2,False)
 


        
if __name__ == '__main__':
    unittest.main()    

