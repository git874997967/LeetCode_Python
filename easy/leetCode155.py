# 155. Min Stack
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.min = x
            #stack.append(x)
            self.stack.push(x - self.min )
        else:
            self.stack.push(x - self.min)  # push diff part positive number
            if x <= self.min:
                 # x = 1 self.min = 3 push -2 
                self.min = x   # update self.min
    def pop(self):
        """
        :rtype: None
        """
        topVal = self.stack.pop()
        if topVal >= 0:
            self.min = self.min - topVal  # update the self.min val 
        # stack.pop()
    def top(self):
        """
        :rtype: int
        """
        topVal = self.stack[-1]
        if topVal >= 0:
            return topVal + self.min
        # return self.min - topVal
        return self.min
    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()