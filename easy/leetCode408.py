# 408. Valid Word Abbreviation

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)

def validWordAbbreviation( word, abbr):
   wPointer = aPointer = 0
   while wPointer < len(word) and aPointer < len(abbr):
       if abbr[aPointer].isalpha():
           if word[wPointer] != abbr[aPointer]:
               return False 
           wPointer += 1
           aPointer += 1
       else:
            if abbr[aPointer] == '0':
                return False 
            temp = 0
            while aPointer <len(abbr) and abbr[aPointer].isdigit():
                temp = temp * 10 + int(abbr[aPointer])
                aPointer += 1
            wPointer += temp 
   return word[wPointer] == abbr[aPointer] 
 


 