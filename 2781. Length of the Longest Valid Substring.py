class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        forbidden_set = set(forbidden)
        res = 0
        # memo = [-1 for _ in range(n)]
        # memo[0] = 1
        memo = 1 if word[0] not in forbidden_set else 0
        for i in range(1, n):
            cur = word[i-memo:i+1]
            k = memo
            for j in range(k):
                if cur[k-j-1:k+1] in forbidden_set:
                    res = max(memo,res)
                    memo = j-1
            if k == memo:
                memo += 1
        return max(memo,res)