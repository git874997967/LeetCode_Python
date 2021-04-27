# 392. Is Subsequence
from collections import defaultdict
import bisect
# use two pointer to iterate two strings 
# find the match char one by one in t string 
# if the s to end then means find all in s 
def isSubsequence(s, t):
     leftBound , rightBound = len(s),len(t)
     pLeft = pRight = 0
     while pLeft < leftBound and pRight < rightBound:
         if s[pLeft] == t[pRight]:
             pLeft += 1 
         pRight += 1 
     return pLeft == leftBound

# s = abc t = xx a xx b xx c

# round 1 : -> 
#            abc
#           -> 
#           xxaxxbxxc
# round 2
#            ->
#           xxaxxbxxc
# follow up question 
def isSubsequence2(s,t):
    letter_dice_table = defaultdict(list)
    for index,letter in enumerate(t):
        letter_dice_table[letter].append(index)
    print(letter_dice_table)
    curr_match_index = -1
    for letter in s:
        # the letter in source not in target table 
        if letter not in letter_dice_table:
            return False 
        indices_list = letter_dice_table[letter]
        match_Index = bisect.bisect_right(indices_list, curr_match_index)
        print(letter,indices_list,curr_match_index,match_Index)
        if match_Index != len(indices_list):
            curr_match_index = indices_list[match_Index]
            print(letter,indices_list,curr_match_index,match_Index)
        else: 
            return False
    return True
     
        
 
print(isSubsequence2(  "abc",   "abbadc"))
 