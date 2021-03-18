class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        def findIndex(arr, word):
            try:
                num = arr.index(word)
                return num 
            except ValueError:
                return -1
        if len(sentence1) != len(sentence2):
            return False
        if len(similarPairs ) == 0 and sentence1 == sentence2:
            return True
        for i in range(len(sentence1)):
            s1 , s2 = sentence1[i],sentence2[i]
            if s1 != s2:
                if findIndex(similarPairs,[s1,s2]) == -1 and findIndex(similarPairs,[s2,s1]) == -1:
                    
                    return False      
        return True
        
            