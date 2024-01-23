"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        q = [root]
        while q:
            l = len(q)
            for i in range(l):
                cur = q.pop(0)
                if i != l - 1:
                    cur.next = q[0]
                else:
                    cur.next = None
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root