# 92. Reverse Linked List II
def reverseBetween(head, left, right):
    if left == right:
        return head 
    dummy = ListNode()
    dummy.next = head
    start = end = dummy 

    # find the node before left and the node on right 
    # dummy--> head --> ...--> start--> pre(left)-->.....--> end(right ) -->endNext...  
    # dummy--> head --> ...--> start--> prev -->.....--> pre -->endNext...  
    # 
    for i in range(0,left-1):
        start = start.next 
    # now start is the node before left
    for i in range(0,right):
        end = end.next   

    # pre is the head of reverse
    # endNext is the next of the end of reverse
     
    pre = start.next 
    endNext = end.next 

    end.next = None 
    #start(the node before left connect to the new head of reverse (return prev))
    start.next = self.reverseNode(pre)
    
    pre.next = endNext 
    return dummy.next 

def reverseNode(head):
    prev,cur = None,head
    while(cur!= None):
        temp = cur.next 
        cur.next = prev
        prev = cur
        cur = temp 

    return prev

