class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # coins.sort(reverse=True)
        # m = {}
        # def dfs(coins,cnt):
        #     if cnt > amount:
        #         return -1
        #     if cnt 
        if not amount:
            return 0
        memo = [None for _ in range(amount+1)]
        memo[0] = 0
        for i in range(amount+1):
            if memo[i] is None:
                continue
            for j in coins:
                n = i + j 
                if n <= amount:
                    if memo[n] is None:
                        memo[n] = memo[i] + 1
                    else:
                        memo[n] = min(memo[n], memo[i] + 1)
        print(memo)
        if memo[-1] is not None:
            return memo[-1]
        return -1