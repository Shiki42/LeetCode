class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k==0 or not head.next:
            return head
        ori = head
        l = 1
        while head.next:
            l += 1
            head = head.next
        tail = head
        offset = l - k % l
        if offset == l:
            return ori
        head = ori
        while offset!=1:
            head = head.next
            offset -= 1
            
        
        newHead = head.next
        head.next = None
        tail.next = ori
        return newHead