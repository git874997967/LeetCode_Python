#1790. Check if One String Swap Can Make Strings Equal
def areAlmostEqual(s1, s2):
    set1,set2 = set(),set()
    diffInd = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            set1.add(s1[i])
            set2.add(s2[i])
            diffInd.append(i)
    if len(diffInd) % 2 == 1 or set1 != set2:
        return False 
    return True 
