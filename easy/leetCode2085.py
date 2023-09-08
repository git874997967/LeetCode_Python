def countWords( words1, words2):
    count_map1,count_map2 = {},{}
    result = []
    for word in words1:
        count_map1[word] =count_map1.get(word,0) + 1 
    for word in words2:
        count_map2[word] = count_map2.get(word,0) + 1
        
    for k ,v in count_map1.items():
        if v == 1 and count_map2.get(k,0) == 1:
            result.append(k)
    return result
    
    
words1 = ['leetcode','is','amazing','as','is']
words2 = ['amazing','leetcode','is']
print(countWords(words1,words2))