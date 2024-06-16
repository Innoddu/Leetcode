def reverseList( head):
        prev, curr = None, head
        temp = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        return prev
