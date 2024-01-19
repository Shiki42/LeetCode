class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        mx, my = len(board[0]), len(board)
        memo = {}
        def update(x,y):
            cnt = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if i >= 0 and i < mx and j >= 0 and j < my and (i != x or j != y):
                        if board[j][i] == 1:
                            cnt += 1
            if board[y][x] == 1 and (cnt < 2 or cnt > 3):
                memo[(y,x)] = 0
            elif board[y][x] == 0 and cnt == 3:
                memo[(y,x)] = 1
            print(y,x,cnt)

        for i in range(my):
            for j in range(mx):
                update(j,i)

        for i in memo.keys():
            board[i[0]][i[1]] = memo[i]
