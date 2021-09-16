## 141. Linked List Cycle
def detectCycle(head):
    slow = fast = head 
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next 
        if fast == slow:
            break
     
    if fast == slow:
        while fast != head:
            fast = fast.next 
            head = head.next 
        return head
    return None 


    slow = head
    fast = head
    if not head:
        return None
    if not head.next:
        return None
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            break
    if fast == slow:
        while fast != head:
            fast = fast.next
            head = head.next
        return head
    else:
        return None