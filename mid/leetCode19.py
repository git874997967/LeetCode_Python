#19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    
    #p1 ,p2 = head, head 
    p1, p2 = dummy,dummy
    while n :
        p1 = p1.next 
        n -= 1
    
    p1 = p1.next

    while p1:
        p1 = p1.next 
        p2 = p2.next 

    behind = p2.next.next 
    p2.next = None 
    p2.next = behind 

    return dummy.next 