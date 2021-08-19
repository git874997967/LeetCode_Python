#876. Middle of the Linked List
def middleNode(head):
    fast = slow = head 
    
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next 
    return slow 