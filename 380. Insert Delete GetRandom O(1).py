class RandomizedSet(object):

    def __init__(self):
        self.idx2val, self.val2idx = {}, {}
        self.size = 0
        self.gap = []
        self.cul = 0
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val2idx:
            return False
        else:
            if self.gap:
                idx = self.gap.pop()
            else:
                idx = self.size
            self.idx2val[idx] = val
            self.val2idx[val] = idx
            self.size += 1
            if self.size > self.cul:
                self.cul = self.size
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val2idx:
            return False
        else:
            idx = self.val2idx[val]
            self.idx2val.pop(idx)
            self.val2idx.pop(val)
            if idx != self.size - 1:
                self.gap.append(idx)
            self.size -= 1
            return True

    def getRandom(self):
        """
        :rtype: int
        """

        while True:
            pick = random.randint(0,self.cul)
            if pick in self.idx2val:
                return self.idx2val[pick]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()