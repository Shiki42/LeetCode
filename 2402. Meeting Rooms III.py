class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0 for _ in range(n)]
        res = [0 for _ in range(n)]
        meetings.sort(key=lambda x:x[0])
        while meetings:
            nxt = meetings.pop(0)
            earlist = [None,float('inf')]
            for i in range(n):
                if rooms[i] < earlist[1]:
                    earlist = [i,rooms[i]]
                if rooms[i] <= nxt[0]:
                    rooms[i] = nxt[1]
                    res[i] += 1
                    break
            if earlist[1] > nxt[0]:
                rooms[earlist[0]] += nxt[1] - nxt[0]
                res[earlist[0]] += 1
        
        return res.index(max(res))
