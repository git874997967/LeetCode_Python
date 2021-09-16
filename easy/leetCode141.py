# 141. Linked List Cycle
def hasCycle( head):
    # base case  
    if  not head.next:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow is fast:
            return True  
    return False