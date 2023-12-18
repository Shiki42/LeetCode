def solveNQueens(n):
    result = []

    def backtracking(queens, xy_diff, xy_sums):
        p = len(queens)
        if p == n:
            result.append(queens)
            return
        for q in range(n):
            if q not in queens and p - q not in xy_diff and p + q not in xy_sums:
                backtracking(queens + [q], xy_diff | {p - q}, xy_sums | {p + q})

    backtracking([], set(), set())
    return [['.' * i + 'Q' + '.' * (n - i - 1) for i in queen] for queen in result]