#def addTwoNumbers(l1, l2):
def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
       dummy = ListNode(0)
       cur = dummy
       flag = 0
       while l1 and l2:
           flag, val = divmod(flag + l1.val + l2.val , 10)
           cur.next = ListNode(val)
           cur = cur.next 
           l1 = l1.next 
           l2 = l2.next 

       while l1:
             flag, val = divmod(flag + l1.val   , 10)
             cur.next = ListNode(val)
             l1 = l1.next 

        while l2:
             flag, val = divmod(flag + l2.val , 10)
             cur.next = ListNode(val)
             l2 = l2.next 
        if flag:
            cur.next = ListNode(flag)
        return dummy.next 