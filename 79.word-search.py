class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board

        for i in range(len(board)):
          for j in range(len(board[0])):
            if self.dfs((i,j), word):
              return True
        return False

    def dfs(self, s, word):
          if not word:
            return True
          if s[0] == len(self.board) or s[0] < 0 or s[1] == len(self.board[0]) or s[1] < 0 or self.board[s[0]][s[1]] != word[0]:
            return False          
          self.board[s[0]][s[1]] = '#'         
          for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            n = (s[0]+d[0],s[1]+d[1])            
            if self.dfs(n, word[1:]):
              return True
            
          self.board[s[0]][s[1]] = word[0]
          
          return False