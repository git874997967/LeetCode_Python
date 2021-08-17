# 716. Max Stack mid 
# one stack for actuall number one for all max in history 
# use extra temp stack to handle the popMax 
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
       self.stack = []
       self.max_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        if self.max_stack:
            return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        temp = []
        while self.stack[-1] != self.max_stack[-1]:
           temp.append(self.pop())
            
        out = self.pop()
        self.max_stack.pop()

        while temp:
            self.push(temp[-1])
        return out 

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()