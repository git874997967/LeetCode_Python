#1065. Index Pairs of a String
def indexPairs(text, words):
    words.sort(key = lambda x:(len(x)))
    resultArr = []
    for word in words:
        length = len(word)
        for i in range(0,len(text)- length+1):
            
            if text[i:i+length] == word:
                print(text[i:i+length])
                resultArr.append([i,i+length-1])
    print(resultArr) 
    return sorted(resultArr)



indexPairs("thestoryofleetcodeandme",["story","fleet","leetcode","me"])

indexPairs("ababa",["aba","ab"])