class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not len(s3) == len(s1) + len(s2):
            return False
        memo = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        i,j,k = 0, 0, 0
        memo[0][0] = True
        for i in range(1,len(s1)+1):
            memo[i][0] = s1[i-1] == s3[i-1] and memo[i-1][0]
        for i in range(1,len(s2)+1):
            memo[0][i] = s2[i-1] == s3[i-1] and memo[0][i-1]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                memo[i][j] = memo[i-1][j] and s1[i-1] == s3[i + j - 1] or memo[i][j-1] and s2[j-1] == s3[i + j - 1]

        return memo[-1][-1]
