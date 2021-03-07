# 908. Smallest Range I
def smallestRangeI(self, A, K):
    if len(A) == 1:
        return 0
    A.sort()
    return (A[-1] - A[0]) - 2 * K