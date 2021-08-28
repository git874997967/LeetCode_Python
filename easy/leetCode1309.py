#1309. Decrypt String from Alphabet to Integer Mapping
def freqAlphabets(s):
    charMap ,result = {},""
    for i in range(97,123):
        if i - 96 < 10:
            charMap[chr(i)] = str(i-96)
        else:
            charMap[chr(i)] = str(i - 96) + '#'

    index = len(s) - 1
    while index >= 0:
        if s[index] == '#':
            val = s[index-2:index + 1]
            index -= 3
        else:
            val = s[index]
            index -= 1
        for k,v  in charMap.items():
            if val == v:
                result += k
    return result[::-1]
freqAlphabets("10#11#12")


freqAlphabets("1326#")


freqAlphabets("25#")

freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")