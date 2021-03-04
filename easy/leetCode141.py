# 141. Linked List Cycle
def hasCycle( head):
    # base case  
    if head.next is None:
        return False
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
        if slow is fast:
            return True  
    return False