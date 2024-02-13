class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 0
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                area = 1
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                area = 1                
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '1':
                    if area == 0:
                        area = 1
                    a,b,c = matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]
                    if a == '0' or b == '0' or c == '0':
                        continue
                    else:
                        matrix[i][j] = min(int(a),int(b),int(c)) + 1
                        area = max(area,matrix[i][j]**2)

        return area