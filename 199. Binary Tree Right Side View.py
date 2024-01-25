# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dummy = TreeNode(0)
        m = {root:dummy}
        que = [root]

        while que and (p not in m or q not in m):
            cur = que.pop()
            if cur.left: 
                m[cur.left] = cur
                que.append(cur.left)
            if cur.right: 
                m[cur.right] = cur
                que.append(cur.right)
        parents = set([p])
        while m.get(p):
            parents.add(m[p])
            p = m[p]
        while q not in parents and m.get(q):
            q = m[q]
        if  q != dummy:
            return q
        else:
            return root