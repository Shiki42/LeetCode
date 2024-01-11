class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = head
        while head and head.next:
            cur = head
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            head.next = cur.next
            head = head.next
        return res