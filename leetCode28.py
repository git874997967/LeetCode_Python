# implement-strstr
 def strStr(self, haystack, needle):
     if (haystack == "" and needle == ""):
         return 0
     i = 0
     while i < len(haystack):
         window = haystack[i,i+len(needle)]
         if window == needle:
             return i
         i += 1
    return -1
def strStr2(self,haystack,needle):
    if needle == "":
        return 0
    n_length = len(needle)
    h_length = len(haystack)
    if n_length > h_length:
        return -1
     for i in range(h_length):
         if (haystack[i] == needle[0]) and ( h_length - i >= n_length):
            flag = 0
            for j in range( 1,n_length):
                if needle[j] != haystack[i + j]:
                    flag = 1 
                    break
            if flag == 1 :
                continue
            else:
                return i
        return -1