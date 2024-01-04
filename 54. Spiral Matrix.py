class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      
        x,y,dx,dy,mx,my = 0,0,1,0, len(matrix[0]),len(matrix)
        res = []
        for i in range(mx*my):
            res.append(matrix[y][x])
            matrix[y][x]=101
            if (x+dx)==mx or (y-dy)==my or (x+dx)<0 or (y-dy)<0 or matrix[y-dy][x+dx]==101:
                dx, dy = dy, -dx
            x += dx
            y -= dy
        return res