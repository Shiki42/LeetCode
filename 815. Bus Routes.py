from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
      if source == target:
        return 0
      q = [source]
      deep_map = {source:0}
      routes = list(map(set, routes))
      res = 501
      while q:
        cur = q.pop(0)
        depth = deep_map[cur]
        for bus in routes:
            if cur in bus:
                for st in bus:
                    if st == target:
                        res = min(depth + 1, res)
                    elif st not in deep_map or deep_map[st] > depth + 1:
                        deep_map[st] = depth + 1
                        q.append(st)
      if res == 501:
          return -1
      return res
