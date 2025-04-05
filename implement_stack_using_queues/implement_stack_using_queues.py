class MyStack(object):

    def __init__(self):
        """Initialises class with all it's attributes"""
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.items:
            return self.items.pop()
        else:
            raise IndexError()

    def top(self):
        """
        :rtype: int
        """
        if self.items:
            return self.items[-1]
        else:
            raise IndexError()

        

    def empty(self):
        """
        :rtype: bool
        """
        if self.items:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()