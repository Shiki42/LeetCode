class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        used = set()
        for i in range(len(s)):
            if not d.get(s[i]):
                if t[i] in used:
                    return False
                d[s[i]] = t[i]
                used.add(t[i])
            elif d[s[i]] != t[i]:
                return False


        return True