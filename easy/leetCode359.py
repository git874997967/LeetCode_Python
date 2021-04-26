# # 359. Logger Rate Limiter
# ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]
# [[],[0,"A"],[0,"B"],[0,"C"],  [0,"A"],[0,"B"],[0,"C"], [11,"A"],[11,"B"],[11,"C"],[11,"A"]]
# [null,true,true,true, false,false,false, true,true,true,false]
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message  not in self.dict or timestamp - self.dict[message] >= 10:
            self.dict[message] = timestamp  
            return True
        return False  
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)