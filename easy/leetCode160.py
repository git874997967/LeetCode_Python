# 160. Intersection of Two Linked Lists
def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    a1 a2 c1 c2( b1 b2 b3 *c1 c2)
    b1 b2 b3 c1 c2(a1 a2 *c1 c2)
    """
     
    p1,p2 = headA,headB
    while p1 != p2:
        if not p1:
            p1 = headB
        else:
            p1 = p1.next 

        if not p2:
            p2 = headA
        else:
            p2 = p2.next 
    return p1
    