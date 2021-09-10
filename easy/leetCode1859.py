#1859. Sorting the Sentence
def sortSentence(s):
    wordArr = s.split(' ')
    posArr ,newWordArr ,result = [],[],''
     
    for word in wordArr:
        num = 0
        for i in range(len(word)-1,-1,-1):
            if word[i].isdigit():
                num += int(word[i])
                num *= 10
        num //= 10
        posArr.append(num)
    for i in range(len(posArr)):
        if i < 10:
            newWordArr.append([wordArr[i][:-1],posArr[i]])
        elif i < 100:
             newWordArr.append([wordArr[i][:-2],posArr[i]])
        else:
             newWordArr.append([wordArr[i][:-3],posArr[i]])
    newWordArr.sort(key = lambda x: x[1])
    
    print(' '.join(newWord[0] for newWord in newWordArr))


sortSentence("is2 sentence4 This1 a3")
sortSentence("Myself2 Me1 I4 and3")


    