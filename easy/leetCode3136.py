def findPermutationDifference(s,t):
    print(sum(abs(t.index(i) - s.index(i)) for i in s ))

findPermutationDifference('abcde','edbac')

print('abc'.index('b'))


