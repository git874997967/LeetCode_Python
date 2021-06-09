# 422. Valid Word Square
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        rows = len(words)
        for row in range(rows):
            word = words[row]
            if len(word) > rows:
                return False
            for col in range(len(word)):
                if  len(words[col]) <= row or words[row][col] != words[col][row]:
                    return False
        return True

    def validWordSquare2(self,words):
        for i, row in enumerate(words):
            col = ''.join(row[i] for row in words if i < len(words))
            if len(col) != len(row) or col != row:
                return False
        return True
