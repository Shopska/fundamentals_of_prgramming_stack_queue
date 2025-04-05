class MyQueue(object):

    def __init__(self):
        """ Initialises class with all it's attributes"""
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
            return self.items.pop(0)
        else:
            raise IndexError("There are no elements in the queue") 

    def peek(self):
        """
        :rtype: int
        """
        if self.items:
            return self.items[0]
        else:
            raise IndexError("There are no elemnts in queue")

    def empty(self):
        """
        :rtype: bool
        """
        if self.items:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()