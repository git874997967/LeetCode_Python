# 346. Moving Average from Data Stream
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum , self.count ,self.limit= 0.0 , 0, size
        self.arr = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.count += 1
        self.arr.append(val)
        self.sum += val
        if self.count <= self.limit:

            return float(self.sum / self.count)
        else:
            self.sum -= self.arr[0]
            self.arr.pop(0)
            return float(self.sum /self.limit)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)