#17. Letter Combinations of a Phone Number
def letterCombinations(digits):
    charMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    res = []
    if not digits: return res

    def backTracking(index,block):

        if index == len(digits):
            return res.append(block)

        digit = int(digits[index])
        letters = charMap[digit]
        
        for i in range(len(letters)):
            block += letters[i]
            backTracking(index + 1, block)
            block = block[:-1]

    backTracking(0,"")
    print(res)
    return res

def letterCombinations2(digits):
    result = []
    charMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    if not digits: return result 

    def backTrack(index,s):

        if index == len(digits):
            
            return result.append(s)

        digit = int(digits[index])
        letters = charMap[digit]

        for i in range(len(letters)):

            s += letters[i]
            backTrack(index + 1,s)
            s = s[:-1]


    backTrack(0,"")
    print(result)
    return result 

letterCombinations2("23") 