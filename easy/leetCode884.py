#884. Uncommon Words from Two Sentences
def uncommonFromSentences(s1, s2):
    combine = (s1 +" "+s2).split(" ")
    wordMap = {}
    
    for word in combine:
        wordMap[word] = wordMap.get(word,0) + 1
    return [k for k in wordMap.keys() if wordMap.get(k) == 1 ]
    
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1,s2))

