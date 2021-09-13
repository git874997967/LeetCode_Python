#362. Design Hit Counter
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        message = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if len(self.message) == 300:
            self.message.pop(0)
        
        self.message.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while len(self.message) > 0 and timestamp  - self.message[0] >= 300:
            self.message.pop(0)
        return len(self.message)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)