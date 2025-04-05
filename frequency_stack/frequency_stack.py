from collections import defaultdict, deque
class FreqStack(object):

    def __init__(self):
        """Initialises class with all it's attributes"""
        self.freq = defaultdict(int)
        self.group = defaultdict(deque)
        self.max_freq = 0 

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        self.group[f].append(val)
    
        

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()