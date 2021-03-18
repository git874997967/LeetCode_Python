# 722. Remove Comments
def removeComments( source):
    ans, in_block = [],False
    for line in source:
            i = 0
            if not in_block:
                newline = []
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    newline.append(line[i])
                i += 1
            if newline and not in_block:
                ans.append("".join(newline))
    print(ans)
    return ans

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
print(removeComments2('/*Test program */, int main(), { ,   // variable declaration , int a, b, c;, /* This is a test,    multiline  ,    comment for ,    testing */, a = b + c;, }'))