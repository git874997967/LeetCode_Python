#1078. Occurrences After Bigram
def findOcurrences(text, first, second):
    textArr, resultArr = text.split(), []
    for i in range(0, len(textArr)-2):
         
        if textArr[i] == first and textArr[i+1] == second:
            #print(wordArr)
            resultArr.append(textArr[i+2])
    print(resultArr)

findOcurrences("alice is a good girl she is a good student","a","good")

findOcurrences("we will we will rock you ","we","will")