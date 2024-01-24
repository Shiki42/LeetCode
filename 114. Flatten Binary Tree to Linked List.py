# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        l = []
        def dfs(root):
            if not root:
                return
            l.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        for i in range(len(l)-1):
            l[i].left = None
            l[i].right = l[i+1]
