#2062. Count Vowel Substrings of a String
def countVowelSubstrings(word):
    result,last_not_vowel = 0, -1
    vowel_list =  ['a','e','i','o','u']
    last_seen_vowels = {v:-2 for v in vowel_list}
    for i , x in enumerate(word):
        if x  in vowel_list:
            last_seen_vowels[x] = i
            result += max(min(last_seen_vowels.values()) - last_not_vowel,0)
        else:
            last_not_vowel = i
    return result