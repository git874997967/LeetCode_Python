def countPrefixes(words,s):
    result = 0
    for word in words:
        print(word, s[:len(word)] )
        if len(word) <= len(s) and word == s[0:len(word)]:
            result += 1
    print(result)
    return result


countPrefixes(["a","b","c","ab","bc","abc"] , "abc")