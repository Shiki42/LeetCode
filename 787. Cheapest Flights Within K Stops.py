class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        fMap = {}
        for i in flights:
            if i[0] not in fMap:
                fMap[i[0]] = [(i[1],i[2])]
            else:
                fMap[i[0]].append((i[1],i[2]))

        dMap = {src:0}
        q = [(src, 0)]
        for i in range(k + 1):
            next_dMap = dMap.copy()
            next_q = []
            while q:
                cur, price = q.pop(0)
                if cur in fMap:
                    for r in fMap[cur]:
                        new_price = price + r[1]
                        if r[0] not in dMap or new_price < next_dMap[r[0]]:
                            next_dMap[r[0]] = new_price
                            next_q.append((r[0], new_price))
            
            dMap = next_dMap
            print(dMap)
            q = next_q

        if dst in dMap:
            return dMap[dst]
        else:
            return -1

