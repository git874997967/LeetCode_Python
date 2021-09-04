#1816. Truncate Sentence
def truncateSentence(s, k):
    sArr = s.split(" ")
    
    return " ".join(sArr)  if len(sArr) <= k else " ".join(sArr[:k])