#1768. Merge Strings Alternately
def mergeAlternately(word1, word2):
    i,j,result = 0, 0,""
    while i < len(word1) and j < len(word2):
        result += word1[i] + word2[j]
        i += 1
        j += 1

    while i < len(word1):
        result += word1[i]
        i += 1
    while j < len(word2):
        result += word2[j]
        j += 1
    print(result)
        