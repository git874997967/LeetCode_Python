# 70. Climbing Stairs
# memory the fib  structure to avoid the time exceed
def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0] * (n + 1)
        result[1] = 1
        result[2] = 2
        for i in range(3,n):
                result[i] = result[i-1] + result[i + 1]
        return result[n]

def climbStairs2(self,n):
        if n <= 2 :
                return n
        first = 1
        second = 2
        for i in range(3,n + 1):
                third = first + second
                first = second
                second = third
        return third
                