# 160. Intersection of Two Linked Lists
def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    nodeInB = set()
    while headA is not None:
        nodeInB.add(headA)
        headA = headA.next
    while headB is not None:
        if headB in nodeInB:
            return headB
        headB = headB.next
    return None
    
    # nodeInB = set()
    # while headA is not None:
    #     nodeInB.add(headA)
    #     headA = headA.next  
    # while headB is not None:
    #     if headB in nodeInB:
    #         return headB
    #     headB = headB.next 
    # return None