#744. Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, target):
    for char in letters:
        if ord(char) - ord(target) > 0:
            return char 
    return letters[0]


print(nextGreatestLetter(["c","f","j"],"a" ))



print(nextGreatestLetter(["c","f","j"],"c" ))



print(nextGreatestLetter(["c","f","j"],"d" ))

print(nextGreatestLetter(["c","f","j"],"g" ))

print(nextGreatestLetter(["c","f","j"],"j" ))


print(nextGreatestLetter(["a","b","d"],"z"))