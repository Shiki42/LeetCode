# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def recur(cur):
            if not cur.left and not cur.right:
                return {1:1}
            if cur.left:
                left = recur(cur.left)
            if cur.right:
                right = recur(cur.right)
            if cur.left and cur.right:
                for i in range(1,distance):
                    for j in range(1,distance - i + 1):
                        if i in left and j in right:
                            self.ans += left[i] * right[j]
            d = collections.defaultdict(lambda: 0)
            if cur.left:
                for i in left.keys():
                    d[i+1] += left[i]
            if cur.right:
                for i in right.keys():
                    d[i+1] += right[i]
            return d

        recur(root)
        return self.ans