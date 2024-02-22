class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        from collections import defaultdict 
        m = defaultdict(lambda:0)
        for i,tap in enumerate(ranges):
            for j in range(i-tap,i+tap):
                m[j] = max(m[j],i+tap)

        def recur(i,m):
            if i >= n:
                return 0
            if m[i]:
                c = recur(m[i],m)
                if c == -1:
                    return -1
                return c + 1
            return -1

        return recur(0,m)