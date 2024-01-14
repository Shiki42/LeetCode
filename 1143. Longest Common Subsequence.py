class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        text1 = ' ' + text1
        text2 = ' ' + text2

        memo = [[0] * (len(text2)) for _ in range(len(text1))]


        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i] == text2[j]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j],memo[i][j-1])

        return memo[-1][-1]