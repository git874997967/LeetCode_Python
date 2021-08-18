# 748. Shortest Completing Word
def shortestCompletingWord(licensePlate, words):
     plate = [s.lower() for s in licensePlate if s.isalpha()]
     for word in sorted(words, key = len):
         temp = plate.copy()
         for c in word:
             if c in temp:
                 del temp[temp.index(c)]
         if len(temp) == 0:
            return word

print(shortestCompletingWord("1s3 PSt" ,["step","steps","stripe","stepple"]))



 