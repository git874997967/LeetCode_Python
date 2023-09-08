#2068. Check Whether Two Strings are Almost Equivalent
def checkAlmostEquivalent( word1, word2):
    count_map = {}
    for char in word1:
        count_map[char] = count_map.get(char,0) + 1
        
    for char in word2:
        count_map[char] = count_map.get(char,0) - 1 
       
    for v in count_map.values():
        if abs(v) > 3:
            return False
    print(count_map)
    return True

word1 = "abcdeef"
word2 = "abaaacc"
word1 = "dfgcbehcifihghedhffbggdcebbbghigfhddhiigcgfeiih"
word2 = "cdcgbeeceifbgchhfiffhifghiebfchbcbfhggchfbbhddb"
print(checkAlmostEquivalent(word1,word2))
