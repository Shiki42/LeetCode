# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root,depth):
            if not root:
                return depth
            else:
                left = dfs(root.left,depth+1)
                right = dfs(root.right,depth+1)
                if left == -1 or right == -1 or abs(left-right) > 1:
                    return -1
                return max(left,right)

        return dfs(root,0) != -1