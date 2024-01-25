# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        def iterate(root):
            if not root:
                return []
            else:
                return iterate(root.left) + [root.val] + iterate(root.right)
        self.iter = iterate(root)
        self.point = 0

    def next(self) -> int:
        cur = self.iter[self.point]
        self.point += 1
        return cur

    def hasNext(self) -> bool:
        return self.point != len(self.iter)