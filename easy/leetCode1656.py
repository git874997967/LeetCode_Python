#1656. Design an Ordered Stream
class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [0] * n
        self.cur = 0
    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey-1] = value 
        if self.stream[self.cur] == 0:
            return []
        else:
            result = []
            while self.cur < len(self.stream) and self.stream[self.cur] != 0:
                result.append(self.stream[self.cur])
                self.cur += 1
            return result 
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)