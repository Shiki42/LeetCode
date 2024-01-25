# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root]
        while q:
            next_q = []
            cnt = 0
            for i in q:
                cnt += i.val
                if i.left: next_q.append(i.left)
                if i.right: next_q.append(i.right)
            res.append(cnt/len(q))
            q = next_q
        return res        