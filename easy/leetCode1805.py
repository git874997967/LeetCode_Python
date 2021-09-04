#1805. Number of Different Integers in a String
def numDifferentIntegers(word):
    result = set()
    i = 0 
    while i < len(word):
        if word[i].isalpha():
            i += 1
        else:
            j = i
            num = ""
            while  j < len(word) and word[j].isdigit():
                num += word[j]
                j += 1
            result.add(int(num))
            i = j 
    return len(result)



numDifferentIntegers("a123bc34d8ef34")

numDifferentIntegers("a1b001c0001")



