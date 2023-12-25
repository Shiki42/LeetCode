class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtracking(cur,left,right):
            if left == n and right == n:
                res.append(''.join(cur))
            else:
                if left != n:
                   cur.append('(')
                   backtracking(cur,left+1,right)
                   cur.pop()
                if right != n and right < left:
                   cur.append(')')
                   backtracking(cur,left, right+1)
                   cur.pop()
            
        backtracking([],0,0)

        return res
