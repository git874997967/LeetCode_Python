#1598. Crawler Log Folder
def minOperations(logs):
    step =  0
    for log in logs:
         if log == '../':
            if step != 0:
                step -= 1
         elif log != './':
             step += 1
             
    print(step) 


minOperations(["d1/","d2/","../","d21/","./"]) # 2 

minOperations(["d1/","d2/","./","d3/","../","d31/"]) # 3

minOperations(["d1/","../","../","../"]) # 0