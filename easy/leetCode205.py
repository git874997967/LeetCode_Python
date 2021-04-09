# 205. Isomorphic Strings
def isIsomorphic(s, t):
    if not s and not t :
        return True 
    sPattern , tPattern  = {}, {}
    for index in range(len(s)):
        if s[index] not in sPattern and t[index] not in tPattern:
            sPattern[s[index]] = [index]
            tPattern[t[index]] =  [index]
        elif s[index] in sPattern and t[index] in tPattern:
            sPos,tPos = sPattern[s[index]], tPattern[t[index]]
            if sPos != tPos:    
                return False
            else:
                sPos.append(index)
                tPos.append(index)
                sPattern[s[index]], tPattern[t[index]] = sPos, tPos
        else:
            
            return False 
    return True

def isIsomorphic2(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t :
            return True 
        sPattern = {}
        tPattern = {}
        
        for index in range(len(s)):
            if s[index] not in sPattern and t[index] not in tPattern:
                sPattern[s[index]] = t[index]
                tPattern[t[index]] = s[index]
            elif s[index] in sPattern:
                if t[index] != sPattern[s[index]]:
                    return False 
            elif t[index] in tPattern:
                if s[index] != tPattern[t[index]]:
                    return False
        return True
print(isIsomorphic("aaeaa","uuxyy"))
            
