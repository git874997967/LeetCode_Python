#3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring2(s):
    # use the queue to save length only but not the actual string 
    dq, result = [],0
    for char in s:
        while char in dq:
            dq.pop(0)
        dq.append(char)
        result = max(result, len(dq))

    return result 

def lengthOfLongestSubstring(s):
    result = start = 0
    charMap = {}
    for i, v in enumerate(s):
        if v in charMap:
            # update the new start
            start = max(start, charMap[v] + 1)

        result = max(result, i - start + 1)
        charMap[v] = i
    print(result)
    return result
 
        

lengthOfLongestSubstring("abcabcbb")

lengthOfLongestSubstring("bbbbb")

lengthOfLongestSubstring("pwwkew")

lengthOfLongestSubstring("")