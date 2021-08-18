# 824. Goat Latin
def toGoatLatin(sentence):
    result = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    words = sentence.split(" ")
    for index, word in enumerate(words):
        newWord = ""
        if word[0] in vowels:
            newWord = word 
        else:
            newWord = word[1:] + word[0]
        
        newWord += "ma" + "a" *(index + 1)
        result.append(newWord)
    print(" ".join(result))
    return result

toGoatLatin("I speak Goat Latain")