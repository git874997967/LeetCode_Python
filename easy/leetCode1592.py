#1592. Rearrange Spaces Between Words
def reorderSpaces(text):
    textArr,wordArr = text.split(" "),[]
    spaceCount, wordCount = 0,0
    result = []
    for tex in textArr:
        if tex != '':
            wordCount += 1
            wordArr.append(tex)
    spaceCount = len(textArr) - 1
    if len(wordArr) == 1:
        return wordArr[0] + spaceCount * ' '
    betteenSpaceCount = spaceCount // (wordCount - 1)
    remind = spaceCount % (wordCount - 1)   
    spaceStr = " " * betteenSpaceCount
    result = spaceStr.join(wordArr) + " " * remind
    
    print(result)

reorderSpaces("  this   is  a sentence ")
reorderSpaces(" practice   makes   perfect")
reorderSpaces("hello   world")
reorderSpaces("  walks  udp package   into  bar a")
reorderSpaces("a")
reorderSpaces(" hello")