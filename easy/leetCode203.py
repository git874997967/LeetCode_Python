# 203. Remove Linked List Elements
def removeElements_ite(self, head, val):
     prev = None 
     cur = head  
     prev.next = head
     while cur:
         if cur.val == val:
             prev.next = cur.next 
         else:
             prev = cur 
         cur = cur.next 
     return head
def removeElements_rec(head,val):
    def rec(node,val):
        if node:
            if node.val == val:
                return rec(node.next,val)
            else:
                node.next = rec(node.next,val)
            return node
    return rec(head,val)