# 422. Valid Word Square
def validWordSquare(words):
     n = len(words)
     for i in range(n):
         row = words[i]
         if len(row) > len(words):
             return False
         row = words[i]
         for j in range( len(row)):
             if len(words[j]) <= i or words[j][i] != row[j]:
                 return False 
     return True
print(validWordSquare(["abcd","bnrt","crmy","dtye"]))


print(validWordSquare( ["abcd","bnrt","crm","dt"]))

print(validWordSquare(["ball","area","read","lady"]))


print(validWordSquare(["ball","asee","let","lep"]))