# 720. Longest Word in Dictionary (mid) (Tire) 
def longestWord( words):
    words.sort()
    wordSet, result = set(['']),""
    for word in words:
        print(word,word[:-1])
        if word[:-1] in wordSet:
            wordSet.add(word)
            if len(word) > len(result):
                result = word
    return result

print(longestWord(["w","wo","wor","worl","world"]))

print(longestWord(["a","banana","app","appl","ap","apply","apple"]))