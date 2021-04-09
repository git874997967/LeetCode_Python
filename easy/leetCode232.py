# 232. Implement Queue using Stacks
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1, self.stack2 = [],[]
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        result = self.stack1.pop()
        while len(self.stack2) >= 1:
            self.stack1.append(self.stack2.pop())
        return result

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack1[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return True if len(self.stack1) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()