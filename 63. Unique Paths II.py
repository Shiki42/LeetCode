class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        memo = [[0 for _ in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        memo[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                up = memo[i-1][j] if i!=0 else 0
                left =  memo[i][j-1] if j!=0 else 0
                memo[i][j] = memo[i][j] + up + left if not obstacleGrid[i][j] else 0

        return memo[-1][-1] if not obstacleGrid[0][0] else 0 
