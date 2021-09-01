#1474. Delete N Nodes After M Nodes of a Linked List
def deleteNodes(head, m, n):
        t = ListNode(0, head)
        keep = m - 1
        delete = n
        while head.next:
            while head.next and keep > 0:
                head = head.next
                keep -= 1
            temp = head
            while head.next and delete > 0 and temp.next:
                temp = temp.next
                delete -= 1
            keep = m
            delete = n
            head.next = temp.next
        return t.next
