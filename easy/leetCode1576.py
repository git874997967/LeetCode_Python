#1576. Replace All ?'s to Avoid Consecutive Repeating Characters
def modifyString(s):
    if len(s) == 1:
        if s == '?':
            return 'a'
        else:
            return s
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            for c in "abc":
                if i == 0 and s[i + 1] != c:
                    s[i] = c
                    break
                if i == len(s) - 1 and s[i-1] != c:
                    s[i] = c
                    break
                if i > 0 and i < len(s) - 1 and s[i - 1] != c and s[i + 1] != c:
                    s[i] = c
                    break
    return ''.join(s)
     

modifyString('a?b')
# modifyString('ubv?w')
# modifyString('j?qg??b')
# modifyString('??ywipkj?')
# modifyString('??????????')