class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balanceMap = collections.defaultdict(int)
        for a, b, amount in transactions:
            balanceMap[a] += amount
            balanceMap[b] -= amount

        balanceList = [amount for amount in balanceMap.values() if amount]
        n = len(balanceList)

        def dfs(cur):
            while cur < n and not balanceList[cur]:
                cur += 1
            if cur == n:
                return 0

            cost = float('inf')

            for nxt in range(cur + 1, n):
                if balanceList[nxt] * balanceList[cur] < 0:
                    balanceList[nxt] += balanceList[cur]
                    cost = min(cost, 1 + dfs(cur + 1))
                    balanceList[nxt] -= balanceList[cur]
            
            return cost

        return dfs(0)
