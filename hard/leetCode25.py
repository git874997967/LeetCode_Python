# 25. Reverse Nodes in k-Group
def reverseKGroup(head, k):
    # append the new head to the list  because the head will be changed 
    # but no matter how the list changed  the dummy.next is the first element  
    dummy = ListNode()
    # pass the head to dummy.next  then the head become the first node to be reverted
    dummy.next = head 
    head = dummy 
    while( head is not None):
        head = reversed(head,k)
    return dummy.next 

##  head --> n1 --> n2 --> n3 --> n4 -->...--> nk --> nk + 1 -->....
## head --> nk --> nk-1 -->... > n3-->n2-->n1-->nk+1-->nk+2-->...
def reversed(head,k):
    # get next start  
    kStart = head.next 
    # 
    kEnd = head 
    for i in range(0,k):
        kEnd = kEnd.next 
        if(kEnd is None):
            return 
    kNextStart ,prev, curt = kEnd.next , None, kStart
    while (curt != kNextStart):
        temp = curt.next 
        curt.next = prev 
        prev = curt
        curt = temp 
    
    ## concate them back 

    head.next = kEnd
    kStart.next = kNextStart
    return kStart 