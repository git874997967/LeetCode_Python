#933. Number of Recent Calls
# slide window
class RecentCounter(object):

    def __init__(self):
        self.window = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.window.append(t)
        while self.window[0] < t - 3000:
            self.window.popleft()
        return len(self.window)