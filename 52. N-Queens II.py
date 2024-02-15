class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(queens,xysums,xydiffs):
            cnt = 0
            y = len(queens)
            if y == n:
                return 1
            for x in range(n):
                if x not in queens and x+y not in xysums and x-y not in xydiffs:
                    cnt += backtrack(queens | { x }, xysums | {x + y}, xydiffs | {x - y})
            return cnt
        return backtrack(set(),set(),set())