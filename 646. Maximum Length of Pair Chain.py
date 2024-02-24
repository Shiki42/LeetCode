class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        i, res, end = 1, 1, pairs[0][1]
        while i != len(pairs):
            if pairs[i][0] > end:
                end = pairs[i][1]
                res += 1
            i += 1
        return res