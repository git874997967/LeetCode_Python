#1933. Check if String Is Decomposable Into Value-Equal Substrings
def isDecomposable(s):
     i,n ,two = 0,len(s),False
     if n % 3 != 2: return False
     while i < n:
         if i < n - 2 and s[i] == s[i+1] == s[i+2]:
             i+= 3
         elif s[i] == s[i+1] and not two:
             two = True
             i += 2
         else:
             return False 

     return True
isDecomposable("0000")
isDecomposable("000111000")
# isDecomposable("00011111222")
# isDecomposable("011100022233")