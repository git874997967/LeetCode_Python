#937. Reorder Data in Log Files
# 1 the default split() is " "
# lambda sort will take return value as sort logic 
def reorderLogFiles(logs):
     lLog , dLog =[], []
     for log in logs:
        if log.split()[1].isalpha():
            lLog.append(log)
        else:
            dLog.append(log)
     print(lLog, "----",dLog ,sep= "\t")
     def sort(log):
         allParts = log.split()
         key ,body = allParts[0],allParts[1:]
         return (body,key )

     lLog.sort(key = sort)
     #print(lLog + dLog )
     return lLog + dLog 


logs1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


reorderLogFiles(logs1)

reorderLogFiles(logs2)