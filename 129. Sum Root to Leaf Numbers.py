class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:       
        def dfs(cur,prev):          
            if not cur: return 0                
            prev=prev*10+cur.val
            if not cur.left  and not cur.right:
                return prev
            return dfs(cur.left,prev) + dfs(cur.right,prev)
            
        return dfs(root,0)
