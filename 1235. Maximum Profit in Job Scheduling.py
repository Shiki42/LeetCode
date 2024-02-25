class Solution:
    def findMaxProfit(self, i, jobs, startTime, dp, n):
        if i == n:
            return 0
        if dp[i] != -1:
            return dp[i]

        index = bisect.bisect_left(startTime,jobs[i][1])

        pick = jobs[i][2] + self.findMaxProfit(index, jobs, startTime, dp, n)
        nonpick = self.findMaxProfit(i + 1, jobs, startTime, dp, n)
        dp[i] = max(pick,nonpick)
        return dp[i]
        
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        dp = [-1 for _ in range(n)]

        jobs.sort(key=lambda x:x[0])
        startTime.sort()

        return self.findMaxProfit(0, jobs, startTime, dp, n)