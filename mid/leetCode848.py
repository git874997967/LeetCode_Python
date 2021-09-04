#848. Shifting Letters
def shiftingLetters(s, shifts):
    result = [chr(97 + (ord(s[-1]) + shifts[-1] - 97) % 26)]
    #print(ord(s[-1]), ord(s[-1]) + shifts[-1],chr(97+ (ord(s[-1]) + shifts[-1]) % 97))
    for i in range(len(shifts)-2,-1,-1):
        shifts[i] += shifts[i+1]
        result.insert(0,chr(97 + (ord(s[i]) + shifts[i] -97) % 26 ))

    print(shifts)
    print("".join(result))

def shiftingLetters2(s,shifts):
        lenShifts = len(shifts)
        lenS = len(s)
        cumulative = 0
        letterToIdx = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,
                    'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19,
                    'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
        alphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                       'q','r','s','t','u','v','w','x','y','z']
        s = list(s)
        # Assumption: We do not have to worry about int overflow
        for i in range(-1, -lenShifts-1, -1):
          
            shifts[i] += cumulative
            cumulative = shifts[i]
            s[i] = alphabetList[(letterToIdx[s[i]]+shifts[i])%26]
#         
            
        return "".join(s)

shiftingLetters("abc",[3,5,9])    
shiftingLetters("ruu",[26,9,17])
shiftingLetters("z",[52])         

