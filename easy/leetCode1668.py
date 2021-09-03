#1668. Maximum Repeating Substring
def maxRepeating(sequence, word):
     
    maxTime = len(sequence) // len(word)
    while maxTime > 0:
        if sequence.count(word * maxTime) != 0:
            return maxTime
        maxTime -= 1
    return maxTime

print(maxRepeating("ababc","ab"))

print(maxRepeating("ababc","ba"))

print(maxRepeating("ababc","ac"))