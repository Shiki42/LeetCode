# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        s = []
        heapq.heapify(s)
        def dfs(cur,s):            
            if not cur:
                return
            heapq.heappush(s,cur.val)
            dfs(cur.left,s)
            dfs(cur.right,s)
        dfs(root,s)
        diff = 10**5
        prev = heapq.heappop(s)
        for i in range(len(s)):
            cur = heapq.heappop(s)
            diff = min(diff,cur-prev)
            prev = cur

        return diff