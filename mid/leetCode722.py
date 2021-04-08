# 722. Remove Comments
def removeComments( source):
      ansStr ,inBlock = '', False
      if not source :
          return ansStr
      for line in source:
          charIndex = 0
          if not inBlock:
              newLine = ''
          while charIndex < len(line):
              if line[charIndex:charIndex + 2] == '/*' and not inBlock:
                  inBlock = True
                  charIndex += 1
              elif line[charIndex:charIndex + 2] == '*/' and inBlock:
                  inBlock = False 
                  charIndex += 1
              elif line[charIndex:charIndex + 2] == '//' and not inBlock:
                  break
              elif not inBlock:
                  newLine += line[charIndex]
              charIndex += 1
          if not inBlock and newLine:
                ansStr += newLine
      print(ansStr)
      return ansStr

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source2 = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
#removeComments(source)
#removeComments(source2) # ab

def  removeComments2(source):
    inBlock , result = False,''
    lines = source.split(',')
    for line in lines:
        if not inBlock:
            newline = ''
        i = 0 
        while i < len(line):
            if line[i:i + 2] == '/*' and not inBlock:
                inBlock = True  
                i += 1
            elif line[i:i+2] == '*/' and inBlock:
                inBlock = False
                i += 1
            elif not inBlock and line[i:i + 2] == '//':
                break
            elif  not inBlock:
                newline += line[i]
            i += 1
        if newline and not inBlock:
            result += newline   
    return result
print(removeComments2('void func(int k) {// this function does nothing /*   k = k*2/4;    k = k/2;*/ }'))    
print(removeComments2('/*Test program */, int main(), { ,   // variable declaration , int a, b, c;, /* This is a test,    multiline  ,    comment for ,    testing */, a = b + c;, }'))