# 953. Verifying an Alien Dictionary
import unittest
class Solution(object):
    def isAlienSorted(self, words, order):
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

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

