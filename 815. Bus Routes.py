from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
      if source == target:
        return 0
      q = []
      deep_map = {}
      routes = {i: route for i, route in enumerate(map(set, routes))}
      for bus in routes:
          if source in routes[bus]:
              deep_map[bus] = 1
              q.append(bus)

      res = 501

      while q:
        cur = q.pop(0)
        depth = deep_map[cur]
        if target in routes[cur]:
            return depth
        for bus in routes:
            for st in routes[cur]:
                if st in routes[bus] and bus not in deep_map:
                    deep_map[bus] = depth + 1
                    q.append(bus)
      if res == 501:
          return -1
      return res

