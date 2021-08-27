#1290. Convert Binary Number in a Linked List to Integer
def getDecimalValue(numStr):
   
    cur = head
    result = 0 
    while cur != None:
        if cur.val == 1:
            result = result * 2 + 1
        elif cur.val == 0:
            result = result * 2
            
        cur = cur.next 
        
    return result
getDecimalValue("101")
getDecimalValue("11")
getDecimalValue("100100111000000")
            